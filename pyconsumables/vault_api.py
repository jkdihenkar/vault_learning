"""
VaultAPI to easily interact with the vault's
 hvac lower level API
"""

from vault_confs import *
import hvac
import datetime
import json


class VaultAPI(object):
    """
    A little higher level vault API
    """
    def __init__(self):
        self.vault_cli = hvac.Client(
            url=VAULT_URL,
            token=VAULT_TOKEN_ROOT,
            verify=VAULT_VERIFY,
            timeout=VAULT_TIMEOUT,
            allow_redirects=VAULT_ALLOW_REDIRECTS
        )

    def get_seal_status(self) -> bool:
        return self.vault_cli.is_sealed()

    def attempt_unseal_old(self):
        self.vault_cli.unseal(key=VAULT_UNSEAL_KEYS[0])
        self.vault_cli.unseal(key=VAULT_UNSEAL_KEYS[1])
        self.vault_cli.unseal(key=VAULT_UNSEAL_KEYS[2])

    async def async_attempt_unseal(self):
        return await self.vault_cli.unseal_multi(VAULT_UNSEAL_KEYS)

    def attempt_unseal(self):
        return self.vault_cli.unseal_multi(VAULT_UNSEAL_KEYS)

    def write_secret(self, path: str, warp_ttl: int, kwargs: dict) -> dict:
        return self.vault_cli.write(
            path,
            wrap_ttl=80,
            **kwargs
        )

    def read_secret(self, path: str) -> dict:
        resp = self.vault_cli.read(
            path
        )
        return resp['data'] if resp else resp

    def rekey_vault(self):
        """
        Write the keys to a dump file
        """
        out = self.vault_cli.start_rekey(
            **VAULT_KEY_PROPS
        )

        dumpfile = VAULT_REKEYING_DUMP_FILE.format(date_time=datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))

        keys_out = self.vault_cli.rekey_multi(VAULT_UNSEAL_KEYS, out['nonce'])

        with open(dumpfile, 'w+') as dumpfile_fd:
            dumpfile_fd.write(json.dumps(keys_out))

        return keys_out

    def rekey_get_status(self):
        return self.vault_cli.rekey_status

    def is_rekey_ongoing(self):
        return self.vault_cli.rekey_status['started']

    def cancel_rekey(self):
        return self.vault_cli.cancel_rekey()

    def check_and_enable_approle(self):
        """
        Init approle backend
        STATELESS - can be called everytime without side effects
        """
        if VAULT_APPROLE_BACKEND_ENABLED and not self.check_auth_backend_mounted(VAULT_APPROLE_BACKEND_CHECK):
            self._enable_auth_role()
            return {'mounted': True, 'message': "Mount success" }
        else:
            return {'mounted': True, 'message': 'NoAction'}

    def _enable_auth_role(self):
        return self.vault_cli.enable_auth_backend(**VAULT_APPROLE_BACKEND)

    def _unmount_approle_backend(self, do_you_understand_what_it_does=False):
        """
        Masked for safety with 'do_you_understand_what_it_does' flag
        """
        if do_you_understand_what_it_does:
            self.vault_cli.disable_auth_backend('/auth/approle')
            return True
        else:
            return False

    def check_auth_backend_mounted(self, path):
        if path in self.vault_cli.list_auth_backends():
            return True
        else:
            return False

    def _enable_audit_file_backend(self, file=VAULT_AUDIT_LOG_FILE):
        return self.vault_cli.enable_audit_backend(
            'file',
            'Vault logs to file',
            {'file_path': file}
        )

    # Getting backup keys
    def get_backedup_keys(self):
        try:
            return self.vault_cli.get_backed_up_keys()
        except hvac.exceptions.InvalidRequest as e:
            return None
