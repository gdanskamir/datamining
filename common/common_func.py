#!/usr/bin/env python
#-*- coding:UTF-8 -*-
import re;
import sys;
import json;
import time;
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(filename)s %(funcName)s:%(lineno)d] %(levelname)s %(message)s',
                                            datefmt='%Y-%m-%d %H:%M:%S');

reload(sys)
sys.setdefaultencoding('UTF-8');

#@brief: 输入为unicode 全角转半角
def strQ2B(ustring):
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += unichr(inside_code)  
    return rstring

#@brief: 去掉末尾的特殊字符
def replace_trim_token(str, token_list):
    for token in token_list:
        if str.endswith(token):
            str = str[0:-len(token)];
    return str;


#@brief: 计算jaccard相似度
def compute_jaccard_sim(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return 0;
    else:
        return len(set_1 & set_2) * 1.0 / len(set_1 | set_2)

