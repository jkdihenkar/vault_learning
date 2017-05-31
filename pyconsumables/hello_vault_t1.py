"""
Read creds from vault
"""
from vault_api import VaultAPI

secret_path = '/secret/password'

vault = VaultAPI()

# D: print(vault.get_seal_status())

if vault.get_seal_status():
    print(vault.attempt_unseal())

# Simple reading the secret
print("Reading password: ", vault.read_secret(secret_path))

# Exploring the key status
print("Key status: ", vault.vault_cli.key_status)