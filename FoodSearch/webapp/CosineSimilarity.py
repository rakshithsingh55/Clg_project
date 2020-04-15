from .CountWords2 import CountWords2
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer

import sys
import math

# create English stop words list
class CosineSimilarity:

    def process(st1, st2):
        #print(st1)
        #print('--------')
        #print(st2)
        st1=st1.lower()
        st2=st2.lower()
        test_tup = (st1,st2) 

        #print("The original tuple is : " + str(test_tup)) 
        res = ", ".join(sorted(set(test_tup[0].split()) & set(test_tup[1].split()) )) 
        print('res===',res)

        up=0;
        d1=1
        d2=1
        for key in res.split(','):

            a = CosineSimilarity.tf(st1, key)
            b = CosineSimilarity.tf(st2, key)

            up=up+(a*b)
            d1=d1*a
            d2=d2*b


        down=math.sqrt(d1)*math.sqrt(d2)
        #print(up,down)
        r=0
        try:
            r=up/down
        except:
            pass
        #print(r)




        return r


    def tf(st, key):
        key=key.strip()
        st=st.strip()
        #print(st,key)
        d = 0
        try:

            l = len(st)
            tot = 0
            
            
                ##print('>>>>>>>>>>>>',w)
            c = CountWords2.countOccurences(st, key)
            #print('CCCCCCCCCCCCCCCCC',c)
            

            tf = c / l
            d = tf
            #print('tf=',d)



        except Exception as e:
            #print("trY3")
            #print(e.args[0])
            tb = sys.exc_info()[2]
            #print(tb.tb_lineno)
        #print(d)
        return d


if __name__ == "__main__":
    r = CosineSimilarity.process("bjp modi",'modi bjp')
    #print(r)
