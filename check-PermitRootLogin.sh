#!/bin/bash

sudo cat /etc/ssh/sshd_config | grep PermitRootLogin | grep -v "without-password"
