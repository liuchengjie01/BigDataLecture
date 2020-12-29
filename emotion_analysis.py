# -*- coding: utf-8 -*-
import snownlp as sn
import happybase as hb
import requests

text = u"我今天很难过，我今天很愤怒"


def testNLP():
    s = sn.SnowNLP(text)
    for sentence in s.sentences:
        print(sentence)
        s1 = sn.SnowNLP(sentence)
        print(s1.sentiments)


def open_table():
    conn = hb.Connection("localhost", protocol="compact", transport="framed")
    return conn


def main(conn):
    conn.open()
    content = conn.table("content")
    # row = content.row('123', columns=['cf1:content'])
    rows = content.scan(row_start=None, row_stop=None, row_prefix=None, columns=[b'cf1:content'])
    for key, value in rows:
#        print(key.decode("utf-8"))
        sentence = value[b'cf1:content'].decode("utf-8")
#        print(sentence)
#    print(type(rows))
        res = sn.SnowNLP(sentence)
        if(res.sentiments >= 0.5):
            print("positive")
        else:
            print("negative")


if __name__ == '__main__':
    print("nlp analysis")
    main(open_table())

