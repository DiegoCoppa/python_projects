import xml.etree.ElementTree as ET

def parsexml(f,user):
    #with open('some/file/name.xml', 'wb+') as destination:
        #for chunk in f.chunks():
        #    destination.write(chunk)
    tree = ET.parse(f)
    root = tree.getroot()
    print(root)
    return
    