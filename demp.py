#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Copyright (c) 2024, Yehua Shang

  @Author :  Yehua Shang
  @Email  :  niceshang@outlook.com
  @Time   :  2024-12-03 17:03:51
  @Desc   :  
    解析XML文件 
    
'''

from xml.dom.minidom import parse, parseString

dom1 = parse('./demo1.xml')  # parse an XML file by name

