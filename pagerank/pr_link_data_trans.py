#!/usr/bin/env python
#-*- coding=utf-8 -*-

import json;
import sys;

reload(sys);
sys.setdefaultencoding('UTF-8')


size = 0;

##newID -->  idx转化
id_list = {};
##idx到new_ID --> 转化
id_list_revert = [];
link_data = {}; ##边关系数据
idx = 0;
for line in open("/home/disk0/wangbo01/import-data/baike-data/baike-data-merge"):
    token_list = line.strip('\n').split('\t');
    id_list[token_list[0]] = [idx, 0];
    #id_list_revert.append(token_list[0])
    idx = idx + 1;

for line in open("./link_matrix"):
    token_list = line.strip('\n').split('\t');
    if token_list[0] not in id_list:
        id_list[token_list[0]] = [idx, 0];
        #id_list_revert.append(token_list[0])
        idx = idx + 1;
    if token_list[0] not in link_data:
        link_data[token_list[0]] = [];
    arr_list = token_list[1].split(',');
    link_data[token_list[0]].extend(arr_list);
    
for k, v in link_data.items():
    print str(k) + "\t1\t" + ",".join(v);
    id_list[k][1] = 1;

for k,v in id_list.items():
    if v[1] == 0:
        print k + "\t1\t"

print >> sys.stderr, "load all data ok, matrix_len", idx

matrix_size = idx; ##矩阵长度
exit(0)
trans_org = [[0 for col in range(matrix_size)] for row in range(matrix_size)]
#init_pr = [1 for col in range(matrix_size)];
alpha=0.85 # a 值 0-1之间的小数


###get_trans
for k, value_list in link_data:
    to_other = 1.0/len(value_list);
    if k in id_list:
        col_no = id_list[k];
        for item in value_list:
            if item in id_list:
                row_no = id_list[item];
                
                if col_no != row_no:
                    trans_org[row_no][col_no] = trans_org[row_no][col_no] + to_other;

print >> sys.stderr, "prepare init trans ok";
'''
矩阵与向量相乘
'''
def multiMatrixVector(m,v):
    rv=range(len(v))
    for row in range(0,len(m)):
        temp=0
        for col in range(0,len(m[row])):
            temp+=m[row][col]*v[col]
        rv[row]=temp
    return rv 


#公式
for i in range(0,matrix_len):
    for j in range(0, matrix_len):
        trans_org[i][j] += trans_org[i][j]*alpha

alpha_else = (1-alpha)/len(matrix_size);
for i in range(0,matrix_len):
    for j in range(0, matrix_len):
        trans_org[i][j] += 1*alpha_else;


print >>sys.stderr, "trans matrix dump"
print "trans: " + json.dumps(trans_org)  #trans matrix

exit(0);

def check_exit(pr_next, f):
    idx = 0;
    error = 0;
    while idx < matrix_len:
        error = error + abs(round(f[idx],5) - round(pr_next[idx],5))
        idx = idx + 1;
    print >> sys.stderr, "current error ", str(error);
    if error < 0.001:
        return True;
    else:
        return False;
#迭代过程
count=0
while(True):
    count=count + 1
    pr_next=multiMatrixVector(trans_org, init_pr)
    print >>sys.stderr,  "第 %s 轮迭代" % count
    print "iter_" + str(count) + ": " + json.dumps(pr_next);
    if check_exit(pr_next, init_pr) == True:
        break;
    init_pr=pr_next

print >>sys.stderr, "Page Rank值已计算完成"
idx = 0;
for i in init_pr:
    print i + "\t"+id_list_revert[idx] + "\t" + str(round(init_pr[idx],5));
    idx = idx + 1;
