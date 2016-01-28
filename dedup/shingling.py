#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys
import re
import json
import re;
import logging;

reload(sys);
sys.setdefaultencoding('UTF-8');
from common_func import *

replace_pat=re.compile("^((第|\(|（)?(零|一|二|三|四|五|六|七|八|九|十|百|千|万|0|1|2|3|4|5|6|7|8|9|０|１|２|３|４|５|６|８|７|９){1,6}(、|\.| |\)|）|章|节|编|篇|章|条|项|目))");


k_shingle=7


def compute_jaccard_sim(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return 0;
    else:
        return len(set_1 & set_2) * 1.0 / len(set_1 | set_2)

def k_shingle_seg(text_format):
    idx = 0;
    ret_all = [];
    idx_end = idx + k_shingle;


    #if idx_end <= len(text_format):
    #    ret_all.append(text_format[len(text_format) - k_shingle : len(text_format)]);
    #    ret_all.append(text_format[0:k_shingle]);
    #    return ret_all;
    #else:
    #    return [];

    ###
    while idx_end <= len(text_format):
        ret_all.append(text_format[idx:idx_end]);
        idx = idx + 1;
        idx_end = idx + k_shingle;
    return ret_all;


all_shingle_list = [];
pair_list_t = [];
for line in open("all_case.shingling.v4.filter"):
    token_list = line.strip('\n').split('\t');
    all_shingle_list.append(token_list[0])
    all_shingle_list.append(token_list[2]);
    pair_list_t.append((token_list[0], token_list[2]))
pair_list = set(pair_list_t)

all_data_list = []
law_idx = 0;
for law_info in sys.stdin:
    data_arr = json.loads(law_info.strip(), strict=False,  encoding="UTF-8");
    
    seq_list = data_arr.get("sequenceRegulation", []);
    name = data_arr.get('normalRegulationName', "");
    id = data_arr["@id"];
    if id not in all_shingle_list:
        continue;
    data_set = [];
    clause_idx = 0;
    for item in data_arr["regulationClause"]:
        text = item["clauseBody"];
        text_format = re.sub(replace_pat, "", text.encode('UTF-8', 'ignore')).strip().decode('UTF-8', 'ignore');
        get_data_set = k_shingle_seg(text_format);
        data_set.extend(get_data_set);
        clause_idx = clause_idx + 1;
    law_idx = law_idx + 1;
    if law_idx % 100 == 0:
        print >>sys.stderr, "load law ", law_idx;

    all_data_dict = {};
    all_data_dict["name"] = name;
    all_data_dict["id"] = id;
    all_data_dict["shingle"] = set(data_set);
    all_data_dict["sequenceRegulation"] = seq_list;
    #print ";".join(all_data_dict["shingle"]).encode('UTF-8', 'ignore');
    all_data_list.append(all_data_dict);





idx = 0;
while idx < len(all_data_list):
    idx_inner = idx + 1;
    while idx_inner < len(all_data_list):
        if (all_data_list[idx]["id"], all_data_list[idx_inner]["id"]) not in pair_list and \
                (all_data_list[idx_inner]["id"], all_data_list[idx]["id"]) not in pair_list:
            idx_inner = idx_inner + 1;
            continue;
        if all_data_list[idx]["id"] not in all_data_list[idx_inner]["sequenceRegulation"]:
            rate = compute_jaccard_sim(all_data_list[idx]["shingle"], all_data_list[idx_inner]["shingle"]);
            if rate >= 0.75:
                print "\t".join([all_data_list[idx]["id"], all_data_list[idx]["name"], all_data_list[idx_inner]["id"], all_data_list[idx_inner]["name"], str(rate)]).encode('UTF-8', 'ignore');
        idx_inner = idx_inner + 1;
    idx = idx + 1;

    if idx % 100 == 0:
        print >> sys.stderr, "process: ", idx;
