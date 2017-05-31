"""
String vault confs
"""

# Note: VAULT_VERIFY -- It should be a boolean in case we say it should be true of false saying we verify or not
#  and a string to CA bundle of we need to give a specific CA.
#  sessions.py => line #479

VAULT_URL = "https://localhost:9801"
VAULT_TOKEN_ROOT = "cc5431f4-fa1e-6643-b66e-b0374d7ba170"
VAULT_VERIFY = '/home/jd/hashicorp/ca.pem'
VAULT_TIMEOUT = 30
VAULT_ALLOW_REDIRECTS = True
