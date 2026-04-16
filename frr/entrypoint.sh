#!/bin/sh

# Start FRR
/usr/lib/frr/docker-start &

# Start telnet server (No auth)
telnetd -F -l /usr/bin/vtysh
