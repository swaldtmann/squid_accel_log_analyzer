#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

log_data  = open('./data/access.log', 'r')
fields = ['ts', 'elapsed', 'remhost', 'status', 'bytes',
          'method', 'url', 'rfc931', 'peerstatus', 'type']
split_list = list()


for line in log_data:
    ls = line.split()
    l_type = ls[9]
    l_url = ls[6]
    #  if l.type == "text/html":
    if l_type == "application/vnd.apple.mpegurl":
        # Group by Time Interval
        file = (l_url).split("/")[-1]
        if file == "playlist.m3u8":
            # split_list.append(line.split())
            split_list.append([ls[0], ls[2], ls[6], file])

df = pd.DataFrame(split_list, columns=['ts', 'remhost', 'url', 'file'])
df.ts = pd.to_datetime(df.ts, unit='s')
print(df.dtypes)
print(df)


df_final = df.groupby(pd.Grouper(key='ts',freq='15min')).count()

#df_final = df_grouped.sort_values('url', ascending=False)
print(df_final)
#df_final.to_csv (r'./export_dataframe.csv', index = True, header=True)
with pd.ExcelWriter('./date/export_dataframe.xlsx') as writer:
    df_final.to_excel(writer)