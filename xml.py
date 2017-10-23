from xml.etree.ElementTree import Element, SubElement, dump
from xml.etree.ElementTree import ElementTree
import datetime


def xml_func(Input):
    
    now = datetime.datetime.now()
    nowdate = now.strftime('%Y-%m-%d')
    nowTime = now.strftime('%H:%M:%S')
    #root 
    root = Element("Vulnerable_list ")
    root.attrib["Date"] = nowdate + " / "+nowTime
    #child
    if Input[0] is not None:
        for xx in range (0,len(Input[0][0])):
            
            Integrity = Element("Integrity")
            SubElement(Integrity, "I_child").text = Input[0][0][xx]
            root.append(Integrity)

            
    if Input[1] is not None:
        
        for xx1 in range (0,len(Input[1][0])):
            
            HardCoded = Element("HardCoded")
            SubElement(HardCoded,"H_child").text = Input[1][0][xx1]
            root.append(HardCoded)
        
    if Input[2] is not None:
        
        for xx2 in range (0,len(Input[2][0])):
            
            External_Library= Element("External_Library")
            SubElement(External_Library, "E_child").text =  Input[2][0][xx2]
            root.append(External_Library)


    #indent method
    def indent(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i
                

    ElementTree(root).write('plc.xml', xml_declaration=True, method='xml', encoding='UTF-8')
    

    indent(root)
    dump(root)







Input=[[["Project_name","File_name"]]
       ,[["B_name","N_name","#Line"]]
       ,[["EX"]]]


xml_func(Input)