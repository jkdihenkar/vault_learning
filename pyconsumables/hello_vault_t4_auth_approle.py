from vault_api import VaultAPI

# describe/view a policy

vault = VaultAPI()

# print(vault.vault_cli._get('/v1/sys/policy').json())

for policy in vault.vault_cli.list_policies():
    try:
        print(vault.vault_cli.get_policy(policy, parse=True))
    except Exception as e:
        print("Failed for {}".format(policy))
        print(vault.vault_cli.get_policy(policy, parse=False))

# defining roles

# defining policies controlling roles