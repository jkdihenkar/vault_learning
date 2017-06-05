"""
String vault confs
"""

# Note: VAULT_VERIFY -- It should be a boolean in case we say it should be true of false saying we verify or not
#  and a string to CA bundle of we need to give a specific CA.
#  sessions.py => line #479

# Python namespaces - Use more of it.


class VaultConfig(object):

    def __init__(self):
        # Connect to vault
        self.vault_url = "https://localhost:9801"
        self.vault_verify = '/home/jd/hashicorp/ca.pem'
        self.vault_timeout = 30
        self.vault_allow_redirects = True

        # Root Token
        self.vault_token_root = "0891a60b-a132-b149-2ea2-2562316909b8"

        # Re-key params
        self.vault_key_props = {
            'secret_shares': 5,
            'secret_threshold': 2,
            'pgp_keys': None,
            'backup': True
        }

        # If you re-key vault you'll need to update this value
        self.vault_unseal_keys = [
            "64N8/B4b7TQlXaJnWBlKkeDqwDBojeoohsm5wQGwvhAy",
            "EcVseyVYlCHbFXBrml3ODQmwlRz4x8ImYuCkMXOiVK4z",
            "+WeW5/MjUwKArQqlGivsqKUmcz2Tq1A8ahj6cHeMRjBZ",
            "lqB0Mo63XLNaecthOTsI3xnHZyYgqP4v9FA6uTi5y0+/",
            "12+E3uxLzXAn7AklC+r1qrm8SZkRI311H9yBnsBXet+w"
        ]

        # Vault dump path after rekeying
        self.vault_rekeying_dump_file = '/home/jd/hashicorp/pyconsumables/rekey_{date_time}.json'

        # Approle Backend Details
        self.vault_approle_backend_enabled = True
        self.vault_approle_backend_check = 'auth/approle/'
        self.vault_approle_backend = {
            'backend_type': 'approle',
            'description': 'Applications and Role Descriptions',
            'mount_point': '/auth/approle'
        }

        # Audit Backend
        self.vault_audit_log_file = '/home/jd/hashicorp/vault.m.log'

