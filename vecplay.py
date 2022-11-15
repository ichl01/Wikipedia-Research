from gensim.models import word2vec
import logging
import sys
"""a = input("1つ目の言葉を入力")
b = input("2つ目の言葉を入力")"""
model = word2vec.Word2Vec.load(R"C:\Users\ichi\Desktop\working\Wikipedia\text\AA\wiki2\wikipedia20220720.model")

def neighbor_word(posi, nega=[], n=500000):
    count = 1
    result = model.wv.most_similar(positive = posi, negative = nega, topn = n)
    for r in result:
        if r[1] > 0.42356288:#全体の8割よりキモい
            print(str(count)+" "+str(r[0])+" "+str(r[1]))
            count += 1


def calc(equation):
    if "+" not in equation or "-" not in equation:
        neighbor_word([equation])
    else:
        posi,nega = [],[]
        positives = equation.split("+")
        for positive in positives:
            negatives = positive.split("-")
            posi.append(negatives[0])
            nega = nega + negatives[1:]
        neighbor_word(posi = posi, nega = nega)

"""if a in model.wv and b in model.wv:
    w = model.similarity(a, b)
else:
    w = model.predict_output_word(a,topn=1)
    q = model.predict_output_word(b,topn=1)
print(w,q)"""
#print("類似度:", model.wv.similarity(a, b))
if __name__=="__main__":
    equation = sys.argv[1]
    calc(equation)
    