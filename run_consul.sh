consuls=("consul.hcl.master" "consul.hcl.s1" "consul.hcl.s2" "consul.hcl.s3")
for consul in ${consuls[@]} ; do
  CONSUL_ID="${consul}"
  echo ./consul agent -pid-file="${CONSUL_ID}.pid" -config-file="${CONSUL_ID}"
  ./consul agent -pid-file="${CONSUL_ID}.pid" -config-file="${CONSUL_ID}" &
  sleep 10
  done

wait
echo "All consuls died... :("
