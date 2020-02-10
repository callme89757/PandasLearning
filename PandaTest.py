# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 17:16:35 2020

@author: c_young
"""
import pandas as pd
f=open("D:/python/myprogram/PandaLearning/task_1_zhaopin_data.csv",encoding='utf-8')
df=pd.read_table(f,sep=',')
df1=pd.DataFrame(df)
print(df1.head())
print(df1.tail())
print(df1.head(3))
print(df1.iloc[2])
print(df1[['学历要求','工作经验','是否全职']])
df2=df1.set_index("公司名")
df3=df2.drop(["其他备注"],axis=1)
df4=df3.drop(["上海蜗兴科技有限公司"])
df4.to_csv('D:/python/myprogram/PandaLearning/task_1_zhaopin_data_update.csv')
print("ok")
f.close

