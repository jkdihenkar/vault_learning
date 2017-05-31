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
        return self.vault_cli.seal_status['sealed']

    def attempt_unseal(self):
        self.vault_cli.unseal(key="Jh5JroURGXNPk1TPuPXGuVsccL76oar/wEB7OUTMyNth")
        self.vault_cli.unseal(key="UDg4/5+5F1IygNebq/EQLyCr8LitpTSn2+U6OqLMmi0J")
        self.vault_cli.unseal(key="P379cN17JY+uuGTub6nsUY0+Z2hP0TcPC+zXxq28YUpF")

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
