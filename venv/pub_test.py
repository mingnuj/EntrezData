import glob
import xml.etree.ElementTree as ET
import os
import openpyxl
import xlsxwriter

data_path = "./data/"
file_name = "./keys_per_year/keyword_year.xlsx"
xml_list = os.listdir(data_path)

for i, xml_name in enumerate(xml_list):
    print(i, xml_name)
    doc = ET.parse(data_path + xml_name)
    file_num = int(xml_name[9:-4]) // 100
    print(file_num)
    wb = openpyxl.load_workbook("./keys_per_year/keyword_year{}.xlsx".format(file_num))
    page = wb.active
    for arti_num, article in enumerate(doc.findall('./PubmedArticle/MedlineCitation')):
        if (arti_num % 100) == 0:
            attrib = []

            # PMID
            attrib.append(article.find('./PMID').text)

            # 연도
            if article.find('./DateCompleted') is None:
                _year = article.find('./DateRevised/Year').text
            else:
                _year = article.find('./DateCompleted/Year').text
            attrib.append(_year)

            # MeshHeading
            if article.find('./MeshHeadingList') is None:
                print('mesh heading is noneType')
            else:
                for meshHeadings in article.find('./MeshHeadingList'):
                    for meshes in meshHeadings:
                        attrib.append(meshes.text)
            print(arti_num, attrib)
            # file_name = "./keys_per_year/" + _year + ".xlsx"
            page.append(attrib)
    print("./keys_per_year/keyword_year{}.xlsx".format(file_num))
    wb.save("./keys_per_year/keyword_year{}.xlsx".format(file_num))
