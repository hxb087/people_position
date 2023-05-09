#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022/10/25:14:49
# @Author:  huxb
# @Email:   hxb_086@163.com

import pandas as pd


def matching(dfPeople, dfPosition):
    list_all = []

    for fn in range(len(dfPeople)):
        if (fn % 300 == 0):
            print(fn)

        dfPeopleList = list(dfPeople.values[fn])
        dfPosition['diff'] = abs(dfPosition['region_code'] - (dfPeople['current_residence'].values[fn]))

        dfPositionList = list(
            dfPosition.loc[(dfPosition.educationPosition == dfPeople['educationPeople'].values[fn])].sort_values(
                by="diff",
                ascending=True).head(
                10).values)

        for fnn in range(len(dfPositionList)):
            PeoplePositionList = dfPeopleList.copy()
            PeoplePositionList.extend(dfPositionList[fnn])
            list_all.append(PeoplePositionList)

    columns = dfPeople.columns.append(dfPosition.columns)
    df = pd.DataFrame(list_all)
    df.columns = columns
    df = df.drop('diff', axis=1)
    # df.columns = ['resume_id', 'user_name', 'education', 'sex', 'current_residence', 'position_name', 'education1',
    #               'requirement', 'region_code',
    #               'cutoff_time', 'diff']

    # df = df.drop(['education1','diff'],axis=1)
    # df.to_csv('people_position.csv', index=None)

    return (df)
