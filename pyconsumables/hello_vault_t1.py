"""
Read creds from vault
"""

import time
from vault_api import VaultAPI

secret_path = '/secret/password'

vault = VaultAPI()

if not vault.get_seal_status():
    vault.attempt_unseal()

print("Reading password: " , vault.read_secret(secret_path))