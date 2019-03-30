#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import re

str1 = 'Port-channel          192.168.189.254  YES     CONFIG   up                       u.p '

result = re.match(r'(.+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s*',str1).groups()
str2 = re.match(r'(\w+\:?\d+)\,?\s+(\w+\:?\d+)\,?\s+(\w+\:?\d+)\,?,\s+(\w+\:?\d+)',str).groups()

print ('%-15s%s'%('IP address:',result[1]))
print (result)
print (str2)