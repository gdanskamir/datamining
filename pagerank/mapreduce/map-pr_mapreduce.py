#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import sys,json,time
import random

all_node_no = 5025717
ID_RANDOM=50000;
reload(sys);
sys.setdefaultencoding('UTF-8');

all_merge_pr_trans = {};
idx = 0;
ISOTIMEFORMAT='%Y-%m-%d %X'
time_str = time.strftime(ISOTIMEFORMAT, time.localtime());

print >> sys.stderr, "[", time_str, "] begin to load dict";
id_list = [];
for line in open('all_id_list'):
    all_merge_pr_trans[line.strip()] = 0.0;
    id_list.append(line.strip())
    idx = idx + 1;
    if idx % 1000000 == 0:
        time_str = time.strftime(ISOTIMEFORMAT, time.localtime());
        print >> sys.stderr, "[", time_str, "] load dict lineno:", idx;


time_str = time.strftime(ISOTIMEFORMAT, time.localtime());
print >> sys.stderr, "[", time_str, "] load dict ok"

idx=0;
for line in sys.stdin:
    token_list = line.strip('\n').split('\t');

    idx = idx + 1;
    if idx % 5000 == 0:
        time_str = time.strftime(ISOTIMEFORMAT, time.localtime());
        print >> sys.stderr, "[", time_str, "] process lineno:", idx;

    pr = float(token_list[1]);
    if token_list[0].strip() == "":
        print >> sys.stderr, "token_list 0 is null", line.strip();
        continue;
    print token_list[0] + "\tlink_data\t" + token_list[2];
    
    link_to_list = token_list[2].split(",");
    link_to_degree = len(link_to_list)
    if token_list[2].strip() == "" or link_to_degree == 0:
        pr_trans = pr/ID_RANDOM;
        #for k, v in all_merge_pr_trans.items():
        #    all_merge_pr_trans[k] += pr_trans;
        random_list = random.sample(id_list, ID_RANDOM);
        for k in random_list:
            all_merge_pr_trans[k] += pr_trans;
    else:
        pr_trans = pr/link_to_degree;
        for item in link_to_list:
            all_merge_pr_trans[item] += pr_trans

time_str = time.strftime(ISOTIMEFORMAT, time.localtime());
print >> sys.stderr, "[", time_str, "] process over!";
for k, v in all_merge_pr_trans.items():
    print k + '\tpr_trans\t' + str(v)
