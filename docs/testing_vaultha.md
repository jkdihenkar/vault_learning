# Vault HA Scanerio Test

**Actual setup**

node1 => :9801
node2 => :9802

status output:
```
# Primary vault
[jd@jaypc hashicorp]$ ./vault status -address=https://localhost:9801
Sealed: false
Key Shares: 5
Key Threshold: 2
Unseal Progress: 0
Unseal Nonce:
Version: 0.7.2
Cluster Name: vault-cluster-0ddf7bf1
Cluster ID: 30dbbe17-5ee5-4a91-4df6-8a9bf141eb3b

High-Availability Enabled: true
	Mode: active
	Leader: https://127.0.0.1:9801

# Standby vault
[jd@jaypc hashicorp]$ ./vault status -address=https://localhost:9802
Sealed: false
Key Shares: 5
Key Threshold: 2
Unseal Progress: 0
Unseal Nonce:
Version: 0.7.2
Cluster Name: vault-cluster-0ddf7bf1
Cluster ID: 30dbbe17-5ee5-4a91-4df6-8a9bf141eb3b

High-Availability Enabled: true
	Mode: standby
	Leader: https://127.0.0.1:9801
```

**Failover scanerio**

shutting down 1 vault on `:9801` which is leader

```
# :9802
[jd@jaypc hashicorp]$ ./vault status -address=https://localhost:9802
Sealed: false
Key Shares: 5
Key Threshold: 2
Unseal Progress: 0
Unseal Nonce:
Version: 0.7.2
Cluster Name: vault-cluster-0ddf7bf1
Cluster ID: 30dbbe17-5ee5-4a91-4df6-8a9bf141eb3b

High-Availability Enabled: true
	Mode: active
	Leader: https://127.0.0.1:9802

# :9801
[jd@jaypc hashicorp]$ ./vault status -address=https://localhost:9801
Error checking seal status: Get https://localhost:9801/v1/sys/seal-status: dial tcp [::1]:9801: getsockopt: connection refused

```
