"""
String vault confs
"""

# Note: VAULT_VERIFY -- It should be a boolean in case we say it should be true of false saying we verify or not
#  and a string to CA bundle of we need to give a specific CA.
#  sessions.py => line #479

# Connect to vault
VAULT_URL = "https://localhost:9801"
VAULT_VERIFY = '/home/jd/hashicorp/ca.pem'
VAULT_TIMEOUT = 30
VAULT_ALLOW_REDIRECTS = True

# Root Token
VAULT_TOKEN_ROOT = "0891a60b-a132-b149-2ea2-2562316909b8"

# Re-key params
VAULT_KEY_PROPS = {
    'secret_shares': 5,
    'secret_threshold': 2,
    'pgp_keys': None,
    'backup': True
}

# If you re-key vault you'll need to update this value
VAULT_UNSEAL_KEYS = [
    "64N8/B4b7TQlXaJnWBlKkeDqwDBojeoohsm5wQGwvhAy",
    "EcVseyVYlCHbFXBrml3ODQmwlRz4x8ImYuCkMXOiVK4z",
    "+WeW5/MjUwKArQqlGivsqKUmcz2Tq1A8ahj6cHeMRjBZ",
    "lqB0Mo63XLNaecthOTsI3xnHZyYgqP4v9FA6uTi5y0+/",
    "12+E3uxLzXAn7AklC+r1qrm8SZkRI311H9yBnsBXet+w"
]

# Vault dump path after rekeying
VAULT_REKEYING_DUMP_FILE = '/home/jd/hashicorp/pyconsumables/rekey_{date_time}.json'

# Approle Backend Details
VAULT_APPROLE_BACKEND_ENABLED = True
VAULT_APPROLE_BACKEND_CHECK = 'auth/approle/'
VAULT_APPROLE_BACKEND = {
    'backend_type': 'approle',
    'description': 'Applications and Role Descriptions',
    'mount_point': '/auth/approle'
}

# Audit Backend
VAULT_AUDIT_LOG_FILE = '/home/jd/hashicorp/vault.m.log'


