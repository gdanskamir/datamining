#!/usr/bin/env python
#-*- coding=utf-8 -*-

#@brief: 转移矩阵直接一次性计算完成；
#   此方法直观，但是不适合大规模运算，因为需要每一个元素PR值
#@auther: wangbo01
#@time: 2016.01.28

import json;
import sys;

reload(sys);
sys.setdefaultencoding('UTF-8')
S=[[0,0,0,0],[0.3333,0,0,1],[0.3333,0.5,0,0],[0.3333,0.5,1,0]]
init = 4
U=[[init,init,init,init],[init,init,init,init],[init,init,init,init],[init,init,init,init]]  #全部都为1的矩阵
f=[init,init,init,init]  #物征向量


alpha=0.85  # a 值 0-1之间的小数n=len(S) #网页数

'''
aS a权重值 由google决定值大小，0-1之间，S为原始矩阵 
'''
def multiGeneMatrix(gene,Matrix):
    mullist=[[0]*len(Matrix) for row in range(len(Matrix))] #定义新的矩阵大小，初始化为0
    for i in range(0,len(Matrix)):
        for j in range(0,len(Matrix)):
            mullist[i][j] += Matrix[i][j]*gene
    return mullist 

def multiGeneMatrixOne(gene, size):
    mullist=[[0]*size for row in range(size)] #定义新的矩阵大小，初始化为0
    for i in range(0, size):
        for j in range(0, size):
            mullist[i][j] += 1*gene
    return mullist 


'''
两个矩阵相加
'''
def addMatrix(Matrix1,Matrix2):
    if len(Matrix1[0])!=len(Matrix2):
        print "这两个矩阵无法相加..."
        return

    addlist=[[0]*len(Matrix1) for row in range(len(Matrix1))]    #定义新的矩阵大小
    for i in range(0,len(Matrix1)):
        for j in range(0,len(Matrix2)):
            addlist[i][j]=Matrix1[i][j]+Matrix2[i][j]
    return addlist
'''
矩阵与向量相乘,method1
'''
def multiMatrixVector(m,v):
    rv=range(len(v))
    for row in range(0,len(m)):
        temp=0
        for col in range(0,len(m[row])):
            temp += m[row][col]*v[col]
        rv[row]=temp
    return rv

###method2
f1=multiGeneMatrix(alpha,S)
f2=multiGeneMatrixOne((1-alpha)/len(U), len(U))
G=addMatrix(f1,f2)
print G;
#迭代过程
count=0
while(True):
    count=count + 1
    if count >= 200:
        break;
    pr_next=multiMatrixVector(G,f)
    print "第 %s 轮迭代" % count
    print str(round(pr_next[0],5)) +"\t" + str(round(pr_next[1],5)) + "\t" + str(round(pr_next[2],5)) + "\t" + str(round(pr_next[3],5))
    if round(f[0],5)==round(pr_next[0],5) and round(f[1],5)==round(pr_next[1],5) and round(f[2],5)==round(pr_next[2],5) and round(f[3],5)==round(pr_next[3],5):   #当前向量与上次向量值偏差不大后，停止迭
        break
    f=pr_next
#0.15    1.49296 0.827   1.52995
print "Page Rank值已计算完成"


