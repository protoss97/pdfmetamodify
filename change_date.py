# -*- coding:utf-8 -*-
# Author:Liu Hongliang

from PyPDF4 import PdfFileReader,PdfFileWriter


source_file=open("f:\\c1.pdf","rb")
fin=PdfFileReader(source_file)
info=dict(fin.getDocumentInfo())
info['/ModDate']=info['/CreationDate']
print(info)
dest_file=open("f:\\c2.pdf","wb")
fout=PdfFileWriter()
fout.addMetadata(info)
fout.appendPagesFromReader(fin)
fout.write(dest_file)
source_file.close()
dest_file.close()