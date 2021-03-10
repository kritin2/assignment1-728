import xml.etree.ElementTree as ET

def readXml(filename):

    tree = ET.parse(filename)
    root = tree.getroot()
    preposition = root.attrib['item']
    # print(preposition)

    for i,instance in enumerate(root):
        validInstance = True
        instanceId = instance.attrib['id']
        for child in instance:
            if child.tag == "answer":
                senseId = child.attrib['senseid']
            elif child.tag == "context":
                leftContext = child.text
                prepositionValue = child[0].text
                if prepositionValue == None:
                    validInstance = False
                    continue
                rightContext = child[0].tail
                print(leftContext)
                print(rightContext)
                print(prepositionValue)

if __name__ == '__main__' :
    readXml("data_assn1/data_assn1/Train/Source/pp-about.sents.trng.xml")

    

