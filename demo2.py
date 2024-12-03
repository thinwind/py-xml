#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'''
Copyright (c) 2024, Yehua Shang

  @Author :  Yehua Shang
  @Email  :  niceshang@outlook.com
  @Time   :  2024-12-03 17:17:23
  @Desc   :  
    XML修改Demo
    
'''

from xml.dom.minidom import parse


def replace_title_id(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        orign_id = title.getAttribute('id')
        new_id = orign_id.replace('A10', 'B10')
        title.setAttribute('id', new_id)
    return slides

if __name__ == '__main__':
    dom = parse('./demo1.xml') 
    slides = dom.getElementsByTagName("slide")
    slides = replace_title_id(slides)
    with open('./demo1_m.xml', 'w') as f:
        dom.writexml(f, addindent='', newl='', encoding='utf-8')
    print(dom.toxml())

