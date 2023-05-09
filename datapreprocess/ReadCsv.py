#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022/10/24:19:44
# @Author:  huxb
# @Email:   hxb_086@163.com

# 数据整体情况
import pandas as pd

def readCsvPosition(path='data/position.csv'):

    df = pd.read_csv(path)
    # df = df[['position_name', 'education', 'requirement', 'region_code', 'cutoff_time']]

    df.dropna(axis=1, how='all', inplace=True)
    df = df[df.columns.drop(list(df.filter(regex='Unnamed:')))]
    df["requirement"] = df["requirement"].astype("str")
    df["position_name"] = df["position_name"].astype("str")
    df.fillna({'requirement': '无'}, inplace=True)


    # 对区划的代码
    df.loc[df.region_code.str.contains(('[a-d]'), case=False), 'region_code'] = 900000000000
    df['region_code'] = df["region_code"].astype("float")

    df= df.rename(columns={'education': 'educationPosition'})
    # print(df.columns)
    return (df)


def readCsvPeople(path='data/people.csv'):
    dfPeople = pd.read_csv(path)

    # dfPeople_base = dfPeople[["resume_id", "user_name", "education", "sex", "current_residence"]]
    # 
    # dfPeople = dfPeople_base

    dfPeople.loc[dfPeople.education < 4, "educationPeople"] = 0.0
    dfPeople.loc[(dfPeople.education > 3) & (dfPeople.education < 6), "educationPeople"] = 1.0
    dfPeople.loc[dfPeople.education == 6, "educationPeople"] = 2.0
    dfPeople.loc[dfPeople.education > 6, "educationPeople"] = 3.0

    # dfPeople.education.unique()
    dfPeople= dfPeople.drop('education',axis=1)

    # print(dfPeople.columns)

    dfPeople.loc[
        dfPeople.current_residence.str.contains(('[a-d]'), case=False), 'current_residence'] = 100000000000

    dfPeople["current_residence"] = dfPeople["current_residence"].astype("float")

    # df_new['region_code'] = df_new["region_code"].astype("float")

    return (dfPeople)
