#!/bin/bash

# Separating out the params

prog="vault"

# User running the process
user="jd"
# Binary for running the process
exec="/home/jd/hashicorp/$prog"
# PID file
pidfile="/home/jd/hashicorp/$prog.pid"
# Log file
logfile="/home/jd/hashicorp/logs/${prog}.log"
# conf file
conffile="/home/jd/hashicorp/vault_conf.hcl"
# Loglevel for vault
# supported opts = "trace", "debug", "info", "warn", "err"
loglevel="info"