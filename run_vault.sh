./vault server  --config=vault_conf.hcl -log-level info &
./vault server  --config=vault_conf.hcl.s1 -log-level info &

wait
