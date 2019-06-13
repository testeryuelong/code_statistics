# -*-coding:utf-8 -*-
# @Author : Zhigang

import os

def func_file(path):
    """统计文件中的代码行数"""
    lineNum=0
    Flag=True
    with open(path,"r",encoding="utf-8",errors='ignore') as fp:
        for line in fp:
            line=line.strip()
            if not line:
                continue
            elif  line.startswith("# -*-coding:utf-8 -*-") or line.startswith("# encoding:utf-8")\
                or line.startswith("# coding=utf-8"):
                lineNum+=1
                continue
            elif line.startswith("#"):
                continue

            if line=="'''" and Flag==True:
                Flag=False
                continue
            elif line=="'''"  and  Flag==False:
                Flag = True
                continue
            elif line=='"""' and Flag==True:
                Flag=False
                continue
            elif line=='"""' and Flag==False:
                Flag = True
                continue

            if line.startswith("'''") and line.endswith("'''"):
                continue
            elif line.startswith('"""') and line.endswith('"""'):
                continue
            elif line.startswith("'''") and Flag==True:
                Flag=False
                continue
            elif line.startswith('"""') and Flag==True:
                Flag=False
                continue
            elif line.endswith("'''") and Flag==False:
                Flag=True
                continue
            elif line.endswith('"""') and Flag==False:
                Flag=True
                continue
            if Flag==True:
                lineNum+=1
    return lineNum


def func_dir(path):
    """遍历目录"""
    fileNum=0
    allLineNum=0
    result_dict={}
    for root,dirs,files in os.walk(path):
        for file in files:
            file_path=os.path.join(root,file)
            if os.path.splitext(file_path)[1] in [".py"]:
                fileNum+=1
                lineNum=func_file(file_path)
                # print("文件名为:{0},代码行数为:{1}".format(file_path,lineNum))
                result_dict[file_path]=lineNum
                allLineNum+=lineNum
    return result_dict


def judge(path):
    """对输入的路径进行判断"""
    if not path:
        return
    if not os.path.exists(path):
        return '输入的路径不存在'
    if not os.path.abspath(path):
        return '请输入绝对路径'
    if os.path.isfile(path):
        lineNum=func_file(path)
        return '{0}文件的代码行数为{1}行'.format(path,lineNum)
    elif os.path.isdir(path):
        result_dict=func_dir(path)
        return result_dict
        # return '{0}路径下的文件有{1}个，总计代码行数为{2}行'.format(path,fileNum,lineNum)

if __name__=="__main__":
    print (judge("D:\PythonTest\count_code"))
    print (judge("D:\PythonTest\count_code\zhigangtest.py"))