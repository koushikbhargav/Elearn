# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:36:50 2018

@author: sajan kumar
"""

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import Algorithmia
from googlesearch import search

import PyPDF2
 

pdfFileObj = open('handbook.pdf', 'rb')
def  hack(pdfFileObj):
    import Algorithmia
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print(pdfReader.numPages)
    pageObj = pdfReader.getPage(55)
    print(pageObj.extractText())
    
    inp = pageObj.extractText()
    
    client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
    algo = client.algo('nlp/Summarizer/0.1.6')
    print(algo.pipe(inp).result)
    
    stopWords = set(stopwords.words('english'))
    wordtokens = word_tokenize(inp)
    fil_sent = [w for w in wordtokens if not w in stopWords]
    f = {}
    for word in fil_sent:
        if word not in f:
            f[word]  = 1 
        else:
            f[word] += 1
    client = Algorithmia.client('simeIg+RX6DGJbO8d0NmbFy2aAL1')
    algo = client.algo('cindyxiaoxiaoli/KeywordExtraction/0.3.0')
    key = algo.pipe(inp).result
    for i in  key:
        print(i)
        
        for url in search(i, stop = 5):
            print(url)
            
    pdfFileObj.close()
hack(pdfFileObj)