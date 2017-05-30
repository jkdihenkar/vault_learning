# Steps for running the Vault/Consul on Local

s1: `sh run_consul.sh`
s2: `sh run_consul_agent.sh`
s3: `sh run_vault.sh`
s4: unseal vault

`./vault unseal -address=https://localhost:9801`

```
[jd@jaypc hashicorp]$ ./vault init -address=https://localhost:9801
Unseal Key 1: Jh5JroURGXNPk1TPuPXGuVsccL76oar/wEB7OUTMyNth
Unseal Key 2: UDg4/5+5F1IygNebq/EQLyCr8LitpTSn2+U6OqLMmi0J
Unseal Key 3: P379cN17JY+uuGTub6nsUY0+Z2hP0TcPC+zXxq28YUpF
Unseal Key 4: ECX0q/W1iEIFSE9G6b+oAFoC6p28iIznSeph1jqnDVpr
Unseal Key 5: tjZYK3EWsIey2z9U9oCc7r0H6ILKqEzwmgVGHFce6veB
Initial Root Token: cc5431f4-fa1e-6643-b66e-b0374d7ba170

Vault initialized with 5 keys and a key threshold of 3. Please
securely distribute the above keys. When the vault is re-sealed,
restarted, or stopped, you must provide at least 3 of these keys
to unseal it again.

Vault does not store the master key. Without at least 3 keys,
your vault will remain permanently sealed.

```

s5: cmdline interface with root token

`./vault auth -address=https://localhost:9801 cc5431f4-fa1e-6643-b66e-b0374d7ba170`

`./vault list -address=https://localhost:9801 secret/password`
