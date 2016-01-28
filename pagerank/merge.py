#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import re;
import json;
import sys;

link_data = {};
for line in sys.stdin:
    token_list = line.strip('\n').split('\t');
    if token_list[0] not in link_data:
        link_data[token_list[0]] = [];
    link_data[token_list[0]].extend(token_list[2].split(','))


for k,v in link_data.items():
    print str(k) + "\t1\t" + ",".join(v);
