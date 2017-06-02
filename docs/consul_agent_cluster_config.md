# Consul

Consul agent supports two modes server and client. Server mode takes additional responsibility and are somewhat resourse extensive and hence are suggested to be run on their own dedicated servers, while clients are lightweight processed and connects to cluster.

Ref: https://www.consul.io/docs/agent/basics.html

## Configurations

Explaining the params in the config file of consul.

```
{
// Name of data center
  "datacenter": "ha_dc_segment1",
// Where should consul server store data?
  "data_dir": "/data/consul",
// Loglevel 
  "log_level": "INFO",
  "node_name": "consul_node_1",
  "node_id": "c6411be5-304a-4372-9c05-93578b9cf696",
// running in server mode
  "server": true,
// node is allowed to bootstrap and start a cluster
  "bootstrap": true,
// encryption key for node - node communication
  "encrypt": "oLfrB/k2hECb6XDMzTZ2xA==",
// following described in details here: [https://www.consul.io/docs/agent/options.html]
  "advertise_addr": "127.0.0.1",
  "addresses": {
    "https": "127.0.0.1"
  },
  "ports": {
    "https": 9901,
    "dns": 9051,
    "http": -1,
    "server": 9951,
    "serf_lan": 8311,
    "serf_wan": 8321
  },
  "key_file": "l.key",
  "cert_file": "l.pem",
  "ca_file": "ca.pem",
  "watches": [

  ]
}
```

And a sample agent config file:

```
{
  "datacenter": "ha_dc_segment1",
  "data_dir": "/data/consul5",
  "log_level": "DEBUG",
  "node_name": "consul_node_5",
  "node_id": "1b5ede5b-7343-4458-97f7-e05c0918e5be",
  "server": false,
  "bootstrap": false,
  "encrypt": "oLfrB/k2hECb6XDMzTZ2xA==",
  "start_join": [ "127.0.0.1:8311" ],
  "advertise_addr": "127.0.0.1",
  "addresses": {
    "https": "127.0.0.1"
  },
  "ports": {
    "https": 9909,
    "dns": -1,
    "http": -1,
    "server": 9959,
    "serf_lan": 8319,
    "serf_wan": 8329
  },
  "key_file": "l.key",
  "cert_file": "l.pem",
  "ca_file": "ca.pem",
  "watches": [

  ],
  // agent supports a UI mode and gives GUI
  "ui": true
}
```