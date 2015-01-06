# coding: UTF-8
import nltk #言語処理の準備
from nltk.book import *
from nltk.corpus import brown
import itertools

conj= ['after', 'although' ,'as', 'because', 'before' , 'if', 'since', 'so', 'than', 'though', 'unless', 'until', 'when', 'whenever', 'where', 'whereas', 'wherever',  'while'] #抽出する接続詞の設定
text = brown.words() #Brownコーパスを使う
tcon = [w.lower() for w in text if w.lower() in conj] #Brownコーパスから接続詞だけを抽出
fdist_tcon = FreqDist(tcon)  #接続詞の度数分布
Conj = fdist_tcon.keys()[:4] #上位4つの接続詞とその頻度データ

def bimake(tuple): #接続詞組(B,C)があったときに、[[B,C],[C,B]]というデータをつくる
    return (tuple,tuple[::-1])

def TCon(con): #接続詞組のデータを度数に変換する
    tcon = [w.lower() for w in text if w in Conj]
    fdist = FreqDist(bigrams(tcon)) #接続詞組の度数分布
    print fdist[con] #度数の表示
    return fdist[con] #度数を返す

def a(b,c): #頻度b,cから計算できる、順序評価値a(b,c)の定義を与える
    print 100.0*abs(b - c) / (b + c)

def d(bituple): #[[B,C],[C,B]]というデータから頻度b,cを取り出し、順序評価値を計算させる
    a(TCon(bituple[0]),TCon(bituple[1]))

for v in  [w for w in itertools.combinations(Conj,2)]: #Conjから任意に接続詞組を取り出す
    print v, #接続詞組B,Cの表示
    d(bimake(v)) #[B,C]の頻度、[C,B]の頻度、接続組の順序評価値aの表示