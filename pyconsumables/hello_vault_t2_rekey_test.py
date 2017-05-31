"""
ReKey Vault
"""
# TODO: Make it work
# this doesn't work as of now

from vault_api import VaultAPI

vault = VaultAPI()

# If true will check and cancel ongoing rekeying
CANCEL = False

if vault.is_rekey_ongoing():
    print("Detected ongoing rekeying ... Trying to get status")
    print(vault.rekey_get_status())
    if CANCEL:
        print("Detected CANCEL on rekeying, attempting to cancel...")
        print(vault.cancel_rekey())
else:
    print("No ongoing rekeying, trying to rekey VAULT...")
    print(vault.rekey_vault())