"""
VaultAPI to easily interact with the vault's
 hvac lower level API
"""

from vault_confs import *
import hvac


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
        return self.vault_cli.read(
            path
        )['data']
