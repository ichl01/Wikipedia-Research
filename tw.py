# ライブラリのインポート
from datetime import datetime, timezone
from encodings import utf_8

import pandas
import pytz
import tweepy

# Twitterの認証
#Twitter情報。
#＊＊＊＊＊＊＊＊には自分自身のAPIキーなどを入力してください

consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

#Twitterの認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#　”wait_on_rate_limit = True”　利用制限にひっかかた時に必要時間待機する
api=tweepy.API(auth,wait_on_rate_limit=True)

# 検索条件の設定
search_word = input("search_word")
f = open("./"+search_word+'_tw_data.txt', 'x',encoding="utf_8")
#何件のツイートを取得するか
item_number = 1000
query = search_word+" since:2022-07-08_14:00:00_JST until:2022-07-08_15:00:00_JST"
#検索条件を元にツイートを抽出
tweets = tweepy.Cursor(api.search_tweets,q=search_word, tweet_mode='extended',result_type="mixed",lang='ja').items(item_number)

#関数:　UTCをJSTに変換する
def change_time_JST(u_time):
    #イギリスのtimezoneを設定するために再定義する
    utc_time = datetime(u_time.year, u_time.month,u_time.day, \
    u_time.hour,u_time.minute,u_time.second, tzinfo=timezone.utc)
    #タイムゾーンを日本時刻に変換
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    # 文字列で返す
    str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
    return str_time

#抽出したデータから必要な情報を取り出す
#取得したツイートを一つずつ取り出して必要な情報をtweet_dataに格納する
tw_data = []

for tweet in tweets:
    #ツイート時刻とユーザのアカウント作成時刻を日本時刻にする
    tweet_time = change_time_JST(tweet.created_at)
    create_account_time = change_time_JST(tweet.user.created_at)
    #tweet_dataの配列に取得したい情報を入れていく
    f.write(tweet.full_text)
   # tw_data.append([
    #    tweet.full_text,
     #                  ])
f.close
#取り出したデータをpandasのDataFrameに変換
#CSVファイルに出力するときの列の名前を定義
##   'ツイート本文',
  #  ]

#tw_dataのリストをpandasのDataFrameに変換
#df = pandas.DataFrame(tw_data,columns=labels)

#CSVファイルに出力する
#CSVファイルの名前を決める
#file_name=search_word+'_tw_data.csv'

#CSVファイルを出力する
#df.to_csv(file_name,encoding='utf-8-sig',index=False)
# Bearer Token AAAAAAAAAAAAAAAAAAAAALeBegEAAAAA0S2glPXi3%2FZ9DU8u3WmKkoQp6gI%3DHuoxPjuxP2y2Vo18MZeALJ8mGo7JbaJvT4ptjctNIBgMY80l4Z

import MeCab

f = open("./"+search_word+"_tw_data.txt", 'r', encoding='UTF-8') 
n = open("./"+search_word+"_tw_data_wakati.txt", 'x', encoding='UTF-8') 
tagger = MeCab.Tagger("-Owakati") #Taggerクラスのインスタンスを作成
for line in f:
    parse = tagger.parse(line) #parse(解析)をする
    n.write(parse + "\n")
    print(parse + "\n") #/nで改行して表示
n.close
f.close
print("End")