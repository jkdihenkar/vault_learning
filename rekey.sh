curl \
    --header "X-Vault-Token: cc5431f4-fa1e-6643-b66e-b0374d7ba170" \
    --request PUT \
    --data @rekey_payload.json \
    https://localhost:9801/v1/sys/rekey/init
