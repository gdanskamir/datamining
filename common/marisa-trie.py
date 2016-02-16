#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import marisa_trie
import sys;
import re;
import time;
if __name__ == "__main__":
    #trie = [[]]
    data_list = [];
    data_dict = {};
    data_size = 0;
    for line in open("/home/disk0/wangbo01/kg/spo/rule/query-recall/wise/us-da/all_law_list"):
        #insert_key(line.strip().decode('UTF-8', 'ignore'), True, trie);
        data_size = data_size + 1;
        data_list.append(line.strip().decode('UTF-8', 'ignore'));
        data_dict[line.strip().decode('UTF-8', 'ignore')] = 0;
    trie = marisa_trie.Trie(data_list);
    data_set = set(data_list);
    find_list_tmp = [];
    for line in open("/home/disk0/wangbo01/kg/spo/rule/query-recall/wise/ubs/law.0118.uniq.ok.clean_pat.label"):
        find_list_tmp.append(line.strip().split('\t')[0].decode('UTF-8', 'ignore'));
    find_list = [];
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_list.extend(find_list_tmp);
    find_key = len(find_list);
    print "data_size: " + str(data_size);
    print "find list size: " + str(find_key);
    print "############marisa-trie###############"
    start = time.clock()
    find_iter = 0;
    for i in find_list:
        if i in trie:
            find_iter = find_iter + 1;
    end = time.clock()
    print end-start
    print "total find: " + str(find_iter);


