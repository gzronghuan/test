#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import re

str = '衣服:300, 平板:2999, 手机:5288, 电脑:9888'

str_count = str.count('手机')

#if str_count != 0:
#    for a = str_count:

i = str.find('手机')
j = str.find(',',i)
#x = str.index('手g',17,25)

str_result1 = str[i:j]
str_result2 = str.split(', ')

print(str_result1)
print(str_result2[2])
print(str_count)

net_card = '''en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	ether 60:03:08:99:ef:b4 
	inet6 fe80::1c1c:7cab:b1dc:81c7%en0 prefixlen 64 secured scopeid 0x5 
	inet 192.168.31.245 netmask 0xffffff00 broadcast 192.168.31.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
'''
a = 'ether\s+([0-9a-fA-F]{1,2}\:[0-9a-fA-F]{1,2}\:[0-9a-fA-F]{1,2}\:[0-9a-fA-F]{1,2}\:[0-9a-fA-F]{1,2}\:[0-9a-fA-F]{1,2})'
ipaddr = re.search(r'inet\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',net_card)
macaddr = re.search(a,net_card)

print('{:10}{:<10}'.format('IP地址：',ipaddr.group(1)))
print('{0:10}{1:<10}'.format('MAC地址：',macaddr.group(1)))