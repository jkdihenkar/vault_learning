#!/bin/bash

# Separating out the params

prog="consul"

# User running the process
user="jd"
# Binary for running the process
exec="/home/jd/hashicorp/$prog"
# PID file
pidfile="/home/jd/hashicorp/$prog.pid"
# Log file
logfile="/home/jd/hashicorp/logs/${prog}.log"
# conf file
conffile="/home/jd/hashicorp/consul.hcl.master"
# Reading more confs from conf.d
confdir="/home/jd/hashicorp/consul.d"