"""
Dealing with Backends
"""
from vault_api import VaultAPI

vault = VaultAPI()

## Enabling auth backend as approle

# Check and enable auth approle backend
print(vault.check_and_enable_approle())

# Disable auth backend - check vault api for details
print(vault._unmount_approle_backend())

# Check auth backend loaded?
path = 'auth/approle/'
if vault.check_auth_backend_mounted(path):
    print("Auth backend is mounted at {}".format(path))
else:
    print("Not detected auth backend at {}".format(path))

## Enabling audit backend to file
print(vault._enable_audit_file_backend(vault.vault_conf.vault_audit_log_file))

# Getting details about backends
print("Audit: ", vault.vault_cli.list_audit_backends())
print("Auth: ", vault.vault_cli.list_auth_backends())
print("Polices: ", vault.vault_cli.list_policies())
# print("RoleSecrets: ", vault.vault_cli.list_role_secrets('root'))
print("TokenRoles: ", vault.vault_cli.list_token_roles())
print("SecretBackend: ", vault.vault_cli.list_secret_backends())
