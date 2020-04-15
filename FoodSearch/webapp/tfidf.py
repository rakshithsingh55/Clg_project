from .CountWords import CountWords
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

import sys
import math

# create English stop words list
en_stop = get_stop_words('en')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()

tokenizer = RegexpTokenizer(r'\w+')

class TFIDF:

    def process(ing, kwd):
        tokens = tokenizer.tokenize(kwd)
        stopped_tokens = [i for i in tokens if not i in en_stop]
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        keytokens = stemmed_tokens
        tokens = tokenizer.tokenize(ing)
        stopped_tokens = [i for i in tokens if not i in en_stop]
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        ingtokens = stemmed_tokens

        
        
        d = TFIDF.main(ingtokens, keytokens)

        return d


    def main(ing, keys):
        d = 0
        try:

            l = len(ing)
            tot = 0
            for w in keys:
                #print('>>>>>>>>>>>>',w)
                c = CountWords.countOccurences(ing, w)
                #print('CCCCCCCCCCCCCCCCC',c)
                tot = tot + c

            tf = tot / l
            idf = math.log(l/tot)
            d = tf * idf



        except Exception as e:
            print("trY3")
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        print(d)
        return d


if __name__ == "__main__":
    r = TFIDF.process("bjp-modi",'modi')
    print(r)
