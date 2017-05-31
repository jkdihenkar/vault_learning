"""
ReKey Vault
"""
# TODO: Add docs in readme
# After fixing the bugin hvac this works

from vault_api import VaultAPI
import hvac

vault = VaultAPI()

# If true will check and cancel ongoing rekeying
CANCEL = False
DRY = True

if vault.is_rekey_ongoing():
    print("Detected ongoing rekeying ... Trying to get status")
    print(vault.rekey_get_status())
    if CANCEL:
        print("Detected CANCEL on rekeying, attempting to cancel...")
        if not DRY:
            print(vault.cancel_rekey())
else:
    print("No ongoing rekeying, trying to rekey VAULT...")
    if not DRY:
        print(vault.rekey_vault())

backup = vault.get_backedup_keys()
if backup:
    print(backup)
