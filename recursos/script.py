#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

comando = "pip install pandas"
os.system(comando)

import pandas as pd 

archivo = "UniversityData.csv"
df = pd.read_csv(archivo, usecols=["University",  "lat", "lon"], dtype={'University': 'str',  'lat': 'float64', 'lon': 'float64'})
df = df.dropna(subset=['lat','lon'])
df.to_csv(archivo) 