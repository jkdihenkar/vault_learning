"""
Read creds from vault
"""
from vault_api import VaultAPI
import time

secret_keypath = 'test_password'

vault = VaultAPI()

# D: print(vault.get_seal_status())

if vault.get_seal_status():
    print(vault.attempt_unseal())
    time.sleep(1)


# Simple reading the secret
print("Reading password: ", vault.read_secret(secret_keypath))

# Exploring the key status
print("Key status: ", vault.vault_cli.key_status)