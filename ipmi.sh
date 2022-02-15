#!/bin/bash
if grep -Eqi "CentOS" /etc/issue || grep -Eq "CentOS" /etc/*-release; then
	DISTRO='CentOS'
elif grep -Eqi "Red Hat Enterprise Linux Server" /etc/issue || grep -Eq "Red Hat Enterprise Linux Server" /etc/*-release; then
	DISTRO='RHEL'
elif grep  "Ubuntu" /etc/issue || grep -Eq "Ubuntu" /etc/*-release; then
	DISTRO='Ubuntu'
else
	echo "unknow"
fi

if [[ $DISTRO = "Ubuntu" ]]; then
	sudo apt install -y ipmitool
elif [[ $DISTRO = "CentOS" ]] || [[ $DISTRO = "RHEL" ]]; then
	sudo yum -y install ipmitool
fi
sudo modprobe ipmi_msghandler
sudo modprobe ipmi_devintf
sudo modprobe ipmi_si
sudo modprobe ipmi_poweroff
sudo modprobe ipmi_watchdog

sudo ipmitool user set password 2 ADMIN
or
#ipmitool user list 1
#ipmitool user set password 2 ADMIN
#ipmitool user enable 2
