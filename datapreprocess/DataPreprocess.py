#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2022/10/25:9:43
# @Author:  huxb
# @Email:   hxb_086@163.com

import pandas as pd

def dataPreprocess(df):

    #数据打标签

    # print(df.columns)

    df.loc[(df['requirement'].str.contains('犯罪|纹身|学历不限', case=False)), ['educationPosition']] = 3.0

    df.loc[df.requirement.str.len() < 6, ['educationPosition']] = 3.0

    df.loc[(df['position_name'].str.endswith(("干部", "储干", "主任", "医生", "医师", "老师", "药师", "教师"))), ['educationPosition']] = 2.0
    df.loc[(df['position_name'].str.contains('导师|博士|教授|院长', case=False)), ['educationPosition']] = 0.0
    df.loc[(df['position_name'].str.contains('设计|总监|系统|教务|财会|管理|运营|运行|技术|特助|出纳|财务|主任|主管|助理|秘书|幼师|研发|开发', case=False)), [
        'educationPosition']] = 2.0
    df.loc[(df['position_name'].str.contains('教练|学徒|技师', case=False)), ['educationPosition']] = 3.0

    df.loc[(df['position_name'].str.contains('文员|会计|教官|技术员|行政', case=False)), ['educationPosition']] = 2.0

    df.loc[(df['position_name'].str.contains('设计师|校长|工程师', case=False)), ['educationPosition']] = 1.0

    df.loc[(df['position_name'].str.endswith(("员", "工", "岗"))), ['educationPosition']] = 3.0
    df.loc[(df['position_name'].str.endswith(("专员", "经理", "顾问"))), ['educationPosition']] = 2.0

    df.loc[(df['position_name'].str.contains(
        '焊|床|卫生巾|导购|辅警|保卫|操作工|理货员|安全|业务|面点|业务员|清雪工|修理|机械|军事|普工|驾|营业员|快递|仓|维修|采购|海员|仓库|骑手|物流|库|材料员|收派员|质检|拉丝|大堂|机修|电工|清洁|理发|保管|采购|焊工|服务|标兵|木工|钳工',
        case=False)), ['educationPosition']] = 3.0
    df.loc[(df['position_name'].str.contains(
        '保安|保洁|工人|销售|焊工|安保|司机|开车|铆工|客服|维护|护士|导游|推销|洗车|打磨|收银|装卸|起重|手工|万能|地暖|管工|司炉|技工|生产|装配|加油|温泉|磨床|水泥|厨师',
        case=False)), ['educationPosition']] = 3.0

    df.loc[(df['requirement'].str.contains('博士|硕士|研究生', case=False)), ['educationPosition']] = 0.0
    df.loc[(df['requirement'].str.contains('本科', case=False)), ['educationPosition']] = 1.0
    df.loc[(df['requirement'].str.contains('大专|专科', case=False)), ['educationPosition']] = 2.0
    df.loc[(df['requirement'].str.contains('高中|初中|中专', case=False)), ['educationPosition']] = 3.0

    return (df)

