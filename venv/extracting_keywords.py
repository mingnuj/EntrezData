import glob
import xml.etree.ElementTree as ET
import os

print("---Start extracting keywords---")

data_path = "./data/"

numKls = 0 # the number of key lists
numKs = 0  # the number of keys

xml_list = os.listdir(data_path)
print(xml_list)
# output = open("keywords.txt", "w", -1, "utf-8")

# xml 파일로부터 키워드를 뽑아낸다.
# 각각 파일 내의 키워드는 /로 구분하며, 파일은 new line으로 구분.
for i, xml_name in enumerate(xml_list):
    print(xml_name)
    key_list_quant = 0
    key_quant = 0
    doc = ET.parse(data_path + xml_name)
    root = doc.getroot()
    output = open("./keys/keyword{}.txt".format(i), "w", -1, "utf-8")
    for elem in root.iter("KeywordList"):
        for j, subElem in enumerate(elem):
            # print(subElem, subElem.text)
            output.write(str(subElem.text) + " ")
            if (j + 1) is not len(elem):
                output.write("/ ")
            else:
                key_quant = key_quant + j + 1
            numKs = numKs + 1
        output.write("\n")
        numKls = numKls + 1
        key_list_quant = key_list_quant + 1
    print(str(i + 1) + "  key lists: " + str(key_list_quant) + ", keys: " + str(key_quant) + "\n")
    output.close()

# output.close()
print("The number of keyword lists: "+ str(numKls) + "/ The number of keywords: " + str(numKs))
print("---Finish extracting keyLists---")