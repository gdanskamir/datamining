#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import re;
import json;
import sys;


lemmid_dict = {};
name_to_id = {};
for line in open("/home/disk0/wangbo01/import-data/baike-data/baike-data-merge"):
    token_list = line.strip().split('\t');
    lemmid_dict[token_list[0]] = "";
    if token_list[1] in name_to_id:
        name_to_id[token_list[1]] = -1;
    else:
        name_to_id[token_list[1]] = token_list[0];

redict_dict = {};
for line in open("Baike-Synonym.txt"):
    token_list = line.strip().split('\t')
    redict_dict[token_list[0]] = token_list[4];

main_dict = {};
for line in open("/home/disk0/wangbo01/import-data/baike-data/data/Baike-AllInfo.txt"):
    token_list = line.strip().split('\t');
    if token_list[11] == "1":
        main_dict[token_list[1]] = token_list[0];

def get_redict_id(link_id):
    if link_id in redict_dict:
        return redict_dict[link_id]
    else:
        return link_id;


def get_link_id(link_id, link_name):
    if link_id in lemmid_dict:
        return get_redict_id(link_id)
    else:
        if link_name in name_to_id and name_to_id[link_name] != -1: 
            return get_redict_id(name_to_id[link_name]);
        else:
            if link_name in main_dict:
                return main_dict[link_name]
            else:
                return "";

            

link_data = {};
current_id = "";
current_list = [];
for line in open("/home/disk0/wangbo01/kg/baike/baike_struct/features/rela/get_link_rela.v1"):
    token_list = line.strip().split('\t');
    new_id = token_list[2];
    if new_id != current_id:
        if current_id != "":
            print current_id + "\t" + ",".join(current_list);
        current_id = new_id;
        del current_list[:]
    link_id = token_list[4]; 
    link_name = token_list[5];
    
    link_id_new = get_link_id(link_id, link_name);
    if link_id_new != "":
        current_list.append(link_id_new);
print current_id + "\t" + ",".join(current_list);
