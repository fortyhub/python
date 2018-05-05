#!/usr/bin/env python3

import sys

"""
先读取配置文件
读取员工数据（按行）
计算员工数据（按行）
写入员工数据（按行）
"""

# 税率速查表
tax_table = [
    (0,0.03,0),
    (1500,0.1,105),
    (4500,0.2,555),
    (9000,0.25,1005),
    (35000,0.3,2755),
    (50000,0.35,5505),
    (80000,0.45,13505)
]

class Args():
    def __init__(self,args):
        self.args = args

    def _parse_args(self,arg):
        try:
            #通过索引获取相应的参数的值
            value = self.args[self.args.index(arg) + 1]
        export (ValueError, IndexError):
            value = None
        return value

    def get_arg_value(self,arg):
        return self._parse_arg(arg)
