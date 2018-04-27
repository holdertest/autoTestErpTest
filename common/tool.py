#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
# @Time    : 2018-04-26 10:45  
# @Author  : Baimo  
# @Site    :   
# @File    : tool.py</span>

import json;
import hashlib;
from common import const;
import  random;

def convert(string):
    str=json.loads(json.dumps( string, ensure_ascii=False, encoding='UTF-8'))
    jsonSigned = sign(str, const.UNSIGN_KEY) + "$" + str;
    return  jsonSigned;

def sign(str,key):
    str=str.lower()
    str=str + "&key=" + key;
    return getmd5hash(str)

def  getmd5hash(str):
    m1 = hashlib.md5()
    m1.update(str.encode(encoding='utf-8'))
    return m1.hexdigest()

def get_str(min,max):
    s1 = tuple(("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w","x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
         "T","U", "V", "W", "X", "Y", "Z"));
    str=""
    num=random.randint(0,max)%(max-min+1)+min
    for index in  range(num):
        num1=random.randint(0,len(s1))%(len(s1) - 1)
        str=str+s1[num1]

    return str