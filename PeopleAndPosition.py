#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022/10/24:19:34
# @Author:  huxb
# @Email:   hxb_086@163.com

import os
from datapreprocess.ReadCsv import readCsvPosition, readCsvPeople
from datapreprocess.DataPreprocess import dataPreprocess
from model.MultinomialNBModel import MultinomialNBModel
from model.Matching import  matching
import argparse

import warnings
warnings.filterwarnings("ignore", category=Warning)



parser = argparse.ArgumentParser()
parser.add_argument('--DATAPOSITION', help='inner batch size', default="data/position.csv", type=str)
parser.add_argument('--DATAPEOPLE', help='inner batch size', default="data/people.csv", type=str)
parser.add_argument('--OUTPATH', help='inner batch size', default="out/People_Position.csv", type=str)
# parser.add_argument('--EPOCH', help='inner batch size', default=1000, type=int)
# parser.add_argument('--BATCH_SIZE', help='inner batch size', default=16, type=int)
args = parser.parse_args()

if __name__ == '__main__':
    # pathPosition = os.path.join(os.getcwd(), 'data', 'position.csv')
    pathPosition = args.DATAPOSITION
    pathPeople =  args.DATAPEOPLE
    pathOutpath = args.OUTPATH

    dfPosition = readCsvPosition(pathPosition)
    dfPreprocess = dataPreprocess(dfPosition)
    dfClassification = MultinomialNBModel(dfPreprocess)
    # print(dfClassification.columns)
    # print(dfClassification.head(2).values)

    # pathPeople = os.path.join(os.getcwd(), 'data', 'people.csv')
    dfPeople = readCsvPeople(pathPeople)
    # print(dfPosition.head(2).values)
    # print(dfPosition.columns)

    # print(dfPeople.columns,dfClassification.columns)
    dfRef = matching(dfPeople,dfClassification)
    dfRef.to_csv(pathOutpath, index=None)
    # print(dfRef.columns)
    pass
