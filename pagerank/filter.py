#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys;
import re;
import json;



##过滤空的node, 目标IDlist
id_list = [];
for line in open("pr_init.merge"):
    id_list.append(line.strip().split('\t')[0]);

id_set = set(id_list);
print >> sys.stderr, "load id_set ok";
###获取出链入链list
link_dict = {};
for line in open("pr_init.merge"):
    token_list = line.strip('\n').split('\t');
    if token_list[2].strip() == "":
        continue;
    link_to_list = token_list[2].strip().split(',');
    is_null = True;
    for i in link_to_list:
        item = i.strip();
        if item != "" and item in id_set:
            link_dict[item] = "";
            is_null = False;
    if not is_null:
        link_dict[token_list[0].strip()] = "";

print >>sys.stderr, "load link_dict ok!";

##根据出入链接IDlist过滤行；并根据id_set过滤linktolist
for line in open("pr_init.merge"):
    token_list = line.strip('\n').split('\t');
    id = token_list[0];
    link_to_list = token_list[2].split(',');
    if token_list[0] in link_dict:
        link_to_output = [];
        for item in link_to_list:
            item = item.strip();
            if item != "" and item in id_set:
                link_to_output.append(item);
        print token_list[0] + "\t1\t" + ",".join(link_to_output);
