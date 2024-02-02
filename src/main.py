import sys
import io
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from dotenv import load_dotenv
load_dotenv()
from utils.handle_url import api

# Análise Temporal 
## Anual
df = api.get_historical_data(city='London')

## Limpeza dos dados 
df = df.fillna(0)

df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].dt.year
media_por_ano = df.groupby('date')[['pm2.5', 'pm10', 'o3', 'no2', 'so2', 'co']].mean()

plt.figure(figsize=(7,7))
sns.heatmap(media_por_ano, cmap=sns.color_palette("YlOrBr", as_cmap=False), fmt=".5f", linecolor="white", linewidths=1, annot=True)
plt.show()

## O  monitor de qualidade do ar usa sensores de partículas a laser para medir em tempo real a poluição por partículas PM2.5 e 
## PM10, que é um dos poluentes atmosféricos mais prejudiciais.

## Coordenadas para o Brasil 
# LEFT, BOTTOM, RIGHT, TOP = (
  # -73.9872354804,
  # -33.7683777809,
  # -34.7299934555,
  # 5.24448639569
# )
# df = api.get_range_coordinates_air((TOP, LEFT), (BOTTOM, RIGHT))
# df[df['station'].str.contains('Brazil')]