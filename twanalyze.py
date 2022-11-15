search_word = input("search_word")
from posixpath import split

import numpy as np
from gensim.models import word2vec

a = "悪口"
b = "キモい"
c = "死ね"
model = word2vec.Word2Vec.load(R"C:\Users\ichi\Desktop\working\Wikipedia\text\AA\wiki2\wikipedia20220720.model")
f = open("./"+search_word+"_tw_data_wakati.txt", 'r', encoding='UTF-8') 
x = []
bb = []
cc = []
for line in f:
    result= line.split(" ")
    print(result)
    for i in result:
      if i in model.wv:
        y = model.wv.similarity(a, i)
        bb.append(model.wv.similarity(b, i))
        cc.append(model.wv.similarity(c, i))
        x.append(y)
      else:
        print(" err ")

x90 = np.percentile(x, q=[99])
x80 = np.percentile(x, q=[90])
x70 = np.percentile(bb, q=[99])
x60 = np.percentile(bb, q=[90])
x50 = np.percentile(cc, q=[99])
x40 = np.percentile(cc, q=[90])
print((x90+x70+x50)/3,(x80+x60+x40)/3)
input("Type to exit.")