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
VAULT_TOKEN_ROOT = "cc5431f4-fa1e-6643-b66e-b0374d7ba170"

# Re-key params
VAULT_KEY_PROPS = {
    'secret_shares': 5,
    'secret_threshold': 2,
    'backup': True
}

# If you re-key vault you'll need to update this value
VAULT_UNSEAL_KEYS = [
    "Jh5JroURGXNPk1TPuPXGuVsccL76oar/wEB7OUTMyNth",
    "UDg4/5+5F1IygNebq/EQLyCr8LitpTSn2+U6OqLMmi0J",
    "P379cN17JY+uuGTub6nsUY0+Z2hP0TcPC+zXxq28YUpF"
]

