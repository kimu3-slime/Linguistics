import nltk
from nltk.book import *
from nltk.corpus import brown
import itertools

conj= ['after', 'although' ,'as', 'because', 'before' , 'if', 'since', 'so', 'than', 'though', 'unless', 'until', 'when', 'whenever', 'where', 'whereas', 'wherever',  'while']
text = brown.words()
tcon = [w.lower() for w in text if w.lower() in conj]
fdist_tcon = FreqDist(tcon)
Conj = fdist_tcon.keys()[:4]

def TCon(con):
    tcon = [w.lower() for w in text if w in Conj]
    fdist = FreqDist(bigrams(tcon))
    print fdist[con]
    return fdist[con]

def a(b,c):
    print 100.0*abs(b - c) / (b + c)

def d(bituple):
    a(TCon(bituple[0]),TCon(bituple[1]))

def bimake(tuple):
    return (tuple,tuple[::-1])

for v in  [w for w in itertools.combinations(Conj,2)]:
    print v,
    d(bimake(v))