from posixpath import split
from gensim.models import word2vec
import numpy as np
import logging
import sys
import time
list = ["\n","。","、","(",")","「","」","?","!"]
a = "キモい"
percenta = 90
model = word2vec.Word2Vec.load(R"C:\Users\ichi\Desktop\working\Wikipedia\text\AA\wiki2\wikipedia20220720.model")

f = open(R"C:\Users\ichi\Desktop\working\Wikipedia\text\AA\wiki_wakati.txt", 'r', encoding='UTF-8') 
y = []
x = []
for line in f:
    for count in range(100):
        result= line.split(" ")
        print(result)
        for i in result:
          if a in model.wv and i in model.wv:
            if i not in list:
                w = model.wv.similarity(a, i)
                y.append(w)
                count = count + 1
            if count % 100 == 0 and count != 0:
                print("[info] 100 lines done.")
                print(y)
                num = np.percentile(y, q=[percenta])
                x.append(num)
                print("num is " + str(num))
                y = []
                time.sleep(1)
                count = 0
        else:
            print(" err ")

np.mean(x)
print("Result of "+str(percenta)+"% "+"is "+str(x))
input("Type to exit.")