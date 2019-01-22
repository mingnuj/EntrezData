import ftplib
import ftputil
import io
import gzip
from xml.dom.minidom import parse, parseString
import shutil
import sys
import socket
import os

# ftp 서버로부터 pubmed 데이터를 가져온다.
ftp = ftplib.FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()
ftp.cwd('/pubmed/baseline')
file_mapper = {}

for file in ftp.nlst():
    print(file)
    # md5파일은 생략한다.
    if len(file.split('.xml.gz.md5')) > 1: continue
    # 압축 파일만 받아서 compressed data 파일에 쓴다.
    if len(file.split('.xml.gz')) > 1:
        f = open('./compressed_data/'+file, 'wb+').write
        file_mapper[file] = ftp.retrbinary('RETR '+ file, f)

# 기존에 있는 파일을 가져다가 사용하는 경우
# files = os.listdir(path = "./compressed_data")
count = 0
# for key in files:
# xml 파일 압축 해제
for key in file_mapper:
    print("{} 압축해제중: ".format(count) + key)
    with open('./data/' + key[:-3], 'w', encoding='UTF8') as xml_file:
        with gzip.open('./compressed_data/'+key, "rb+") as origin:
            for lines in origin:
                # print(lines)
                xml_file.writelines(lines.decode('UTF8'))
        origin.close()
    xml_file.close()
    count+=1

