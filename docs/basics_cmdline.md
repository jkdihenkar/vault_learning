# Taking to vault via cmdline

1. `auth` with token

```
[jay@data2 ~]$ vault auth -address=https://kingkong.jdpc.com:9801 
Token (will be hidden): 
Successfully authenticated! You are now logged in.
token: 790a1a26-7691-dd1e-d720-a7d2e8657e4c
token_duration: 0
token_policies: [root]
```

2. `write` secret to vault

```
[jay@data2 ~]$ vault write -address=https://kingkong.jdpc.com:9801 /secret/test_password uname=helloworld 
Success! Data written to: secret/test_password
```

3. `read` secret from vault

```
[jay@data2 ~]$ vault read -address=https://kingkong.jdpc.com:9801 /secret/test_password
Key             	Value
---             	-----
refresh_interval	768h0m0s
uname           	helloworld
```