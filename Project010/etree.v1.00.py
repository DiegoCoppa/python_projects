# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:37:44 2021

@author: Diego
"""
import xml.etree.ElementTree as ET


tree = ET.parse('C:/43Python/01.RepositorioGithub/python_projects/Project010/calibracion.xml')

#root = fromstring(xml_text)
"""

root = tree.getroot()
print(root.tag)
print(root.attrib)
for child in root:
    print(child.tag, child.attrib)
print(root[0][1].text)
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
#print(root[0][1].text)

"""