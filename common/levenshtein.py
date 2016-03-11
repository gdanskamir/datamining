#!/usr/bin/env python
#-*- coding:UTF-8 -*-

#################################################
# 编辑距离
# Author : gdanskamir
# Date   : 2016-02-18
# HomePage : http://www.cnblogs.com/gdanskamir
#################################################

def levenshtein(vec_A, vec_B):
    len_A = len(vec_A) + 1;
    len_B = len(vec_B) + 1;

    ##判断空字符串
    if len_A == 1:
        return len_B -1
    if len_B == 1:
        return len_A -1

    matrix = [range(len_A) for x in range(len_B)]

    for i in range(1,len_B):
        matrix[i][0] = i
    for i in range(1,len_B):
        for j in range(1,len_A):
            deletion = matrix[i-1][j]+1
            insertion = matrix[i][j-1]+1
            substitution = matrix[i-1][j-1]
            if vec_B[i-1] != vec_A[j-1]:
                substitution += 1
            matrix[i][j] = min(deletion,insertion,substitution)
    return matrix[len_B-1][len_A-1]

