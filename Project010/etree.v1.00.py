# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:37:44 2021

@author: Diego
"""
from lxml import etree as ET
from io import StringIO, BytesIO

tree = ET.parse('calibracion.xml')


root = tree.getroot()
print("root tag:", root.tag)
print("root att:", root.attrib)
"""
for child in root:
    print(child.tag, child.attrib)
"""
print ("child roots: ")
for child in root:
    print({x.tag for x in root.findall( child.tag +"/*")})



#print(root[0][1].text)
"""
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
#print(root[0][1].text)
"""