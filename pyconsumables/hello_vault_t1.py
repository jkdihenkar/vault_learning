"""
Read creds from vault
"""

from vault_confs import *
import time
import hvac

vault_cli = hvac.Client(
    url=VAULT_URL,
    token=VAULT_TOKEN_ROOT,
    verify=VAULT_VERIFY,
    timeout=VAULT_TIMEOUT,
    allow_redirects=VAULT_ALLOW_REDIRECTS
)

# print(vault_cli.list('sys/'))

# if vault is sealed unseal it
if vault_cli.seal_status['sealed']:
    vault_cli.unseal(key="Jh5JroURGXNPk1TPuPXGuVsccL76oar/wEB7OUTMyNth")
    vault_cli.unseal(key="UDg4/5+5F1IygNebq/EQLyCr8LitpTSn2+U6OqLMmi0J")
    vault_cli.unseal(key="P379cN17JY+uuGTub6nsUY0+Z2hP0TcPC+zXxq28YUpF")

    time.sleep(1)

    # test successfully unsealed
    if vault_cli.seal_status['sealed']:
        print("Successfully able to unseal vault!")
    else:
        print("Python HVAC API not able to unseal vault.")

else:
    tkey = '/secret/password'
    tval = {'key': 'hello123'}
    if vault_cli.read(tkey) is None:
        print("No key found for {}".format(tkey))

        # creating the key
        resp = vault_cli.write(tkey, wrap_ttl=80, hello='world')
        print("Response after write is : {}".format(resp))