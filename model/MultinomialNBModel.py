#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022/10/25:14:36
# @Author:  huxb
# @Email:   hxb_086@163.com

from jieba import lcut
import pandas as pd


# 对于学历进行文本分类   0代表研究生以上  1代表本科  2专科  3高中及以下


def MultinomialNBModel(df):
    df_train = df.loc[~(df.educationPosition.isnull())]
    df_test = df.loc[(df.educationPosition.isnull())]
    data = df_train[["educationPosition", "requirement"]].values

    X, Y = [' '.join(lcut(i[1])) for i in data], [i[0] for i in data]

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer

    # 将文本中的词语转换为词频矩阵
    vectorizer = CountVectorizer()

    # 计算个词语出现的次数
    vec = vectorizer.fit(X)
    X_data = vec.transform(X)

    # 获取词袋中所有文本关键词
    # word = vectorizer.get_feature_names()

    # print('【查看单词】')

    # for w in word:
    #     print(w, end=" ")
    # else:
    #     print("\n")

    # 将词频矩阵X统计成TF-IDF值
    transformer = TfidfTransformer()

    tf = transformer.fit(X_data)
    tfidf = tf.transform(X_data)

    # 查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
    weight = tfidf.toarray()
    # print(weight)

    # --------------------------------------数据分析------------------------------------
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import classification_report
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(weight, Y)
    # print(len(X_train), len(X_test))
    # print(len(y_train), len(y_test))
    # print(X_train)

    # 调用MultinomialNB分类器
    clf = MultinomialNB().fit(X_train, y_train)
    pre = clf.predict(X_test)
    # print("预测结果:", pre)
    # print("真实结果:", y_test)
    # print(classification_report(y_test, pre))

    # 对于测试数据

    df_test_use = df_test[["educationPosition", "requirement"]]
    data_test = df_test_use.values
    X_test1 = [' '.join(lcut(i[1])) for i in data_test]
    X_test1 = vec.transform(X_test1)
    # tfidf1 = tf.transform(X_test1)

    # 查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
    # weight1 = tfidf1.toarray()
    # print(weight1)

    pre1 = clf.predict(X_test1)
    # print("预测结果:", pre1)

    df_test['educationPosition'] = pre1

    # df_pre = df.loc[df.education.isnull()]
    # # df.loc[df.education.isnull()]['predict'] = pre1

    # df_pre['education'] = pre1
    # df_test.to_csv("bb3.csv")

    df_position = pd.concat([df_train, df_test])

    return (df_position)
