#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from sqlalchemy import create_engine

df_zones = pd.read_csv('taxi+_zone_lookup.csv')

engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
engine.connect()


df_zones.head(n=0).to_sql(name='zones', con=engine, if_exists='replace')
df_zones.to_sql(name='zones', con=engine, if_exists='append')

print('inserted zones data')








