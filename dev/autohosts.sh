#!/bin/bash
#License: GPLv2
wget -q http://smartladder.googlecode.com/svn/hosts/pc/hosts
a=`cat /etc/hosts | grep '#update'`
b=`cat hosts |grep '#update'`
if [ "$a" != "$b" ]; then
	sudo rm /etc/hosts
	sudo mv hosts /etc/
	rm hosts
	echo 'hosts文件已更新'
else
	echo 'hosts文件已是最新'
fi
