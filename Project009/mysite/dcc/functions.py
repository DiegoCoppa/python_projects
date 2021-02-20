
from lxml import etree as ET


def parsexml(f):
    print(f)
    tree = ET.parse(f)
    root = tree.getroot()
    print(root.tag)
    print(root.attrib)
    for child in root:
        print({x.tag for x in root.findall(child.tag+"/*")})




    #with open('some/file/name.xml', 'wb+') as destination:
        #for chunk in f.chunks():
        #    destination.write(chunk)
#    tree = ET.parse(f)
#    root = tree.getroot()
#    print(root)