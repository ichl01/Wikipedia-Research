from gensim.models import word2vec
import logging
import sys
"""a = input("1つ目の言葉を入力")
b = input("2つ目の言葉を入力")"""
model = word2vec.Word2Vec.load(R"C:\Users\ichi\Desktop\working\Wikipedia\text\AA\wiki2\wikipedia20220720.model")
def neighbor_word(posi, nega=[], n=100):
   print(model.wv.most_similar(positive = posi, negative = nega, topn = n))
neighbor_word("キモい")