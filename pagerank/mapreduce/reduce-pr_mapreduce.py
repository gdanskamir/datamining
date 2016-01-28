#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys,json

reload(sys);
sys.setdefaultencoding('UTF-8');

alpha = 0.8

link_matrix = {};
pr_matrix = {}
for line in sys.stdin:
    token_list = line.strip('\n').split('\t');
    if token_list[0].strip() == "":
        continue;
    if token_list[1] == "link_data":
        link_matrix[token_list[0]] = token_list[2];
    else:
        if token_list[0] not in pr_matrix:
            pr_matrix[token_list[0]] = 0.0
        pr_matrix[token_list[0]] = pr_matrix[token_list[0]] + float(token_list[2]);


for k,v in link_matrix.items():
    pr = pr_matrix.get(k, 0.0);
    pr = pr*alpha + (1-alpha);
    print k + "\t" + str(pr) + "\t" + v;


#for k, v in pr_matrix.items():
#    pr = v*alpha + (1-alpha);
#    print k + "\t" + str(pr) + "\t" + link_matrix.get(token_list[0], "");
