#!/usr/bin/python

import sys
import re
import csv
import fileinput
import pandas as pd

genome_data = 'Homo_sapiens.GRCh37.75.gtf'
ensg={}
for each_line_of_text in fileinput.input(genome_data):
    if each_line_of_text.startswith('#'):
        continue
    gene = re.findall(r'^.*?\t.*?\t(.*?)\t', each_line_of_text, re.I)
    ensem = re.findall(r'ENSG\d*', each_line_of_text, re.I)
    hugo = re.findall(r'gene_name "(.*?)"', each_line_of_text, re.I)
    
    if gene:
        ensg[ensem[0]] = hugo[0]
    
if sys.argv[1][:2] == '-f':
    columnnumber = sys.argv[1][2]
    geneset = sys.argv[2]
    column = int(columnnumber) - 1
    
else:
    column = 1
    geneset = sys.argv[1]

geneset = pd.read_csv(geneset)
geneset.iloc[:, column] = geneset.iloc[:, column].astype(str).str.replace(r'(\.\d*)', '')
geneset.iloc[:, column] = geneset.iloc[:, column].str.strip('"')
geneset.iloc[:, column] = geneset.iloc[:, column].replace(ensg)
print(geneset)
