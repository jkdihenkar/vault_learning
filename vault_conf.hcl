listener "tcp" {
  address= "localhost:9801"
  cluster_address= "localhost:9851"
  tls_cert_file= "l.pem"
  tls_key_file= "l.key"
  tls_min_version= "tls12"
}

storage "consul" {
  address= "localhost:9901"
  path= "vault"
  check_timeout= "5s"
  consistency_mode= "default"
  max_parallel= "128"
  path= "vault/"
  scheme= "https"
  service= "vault"
  service_tags= "vault-service"
  tls_ca_file= "ca.pem"
  tls_min_version= "tls12"
  token= "devtesting"
//  tls_skip_verify=true
}
