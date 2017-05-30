./vault server  --config=vault_conf.hcl -log-level debug &
./vault server  --config=vault_conf.hcl.s1 -log-level debug &

wait
