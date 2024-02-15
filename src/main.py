import sys
import io
import numpy as np
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from dotenv import load_dotenv
load_dotenv()
from utils.handle_url import api

# Análise Temporal 
## Anual

temporal_analysis_df = api.get_historical_data(city='Brazil')

temporal_analysis_df['date'] = pd.to_datetime(temporal_analysis_df['date'])
temporal_analysis_df['date'] = temporal_analysis_df['date'].dt.year
mean_per_year = temporal_analysis_df.groupby('date')[['pm2.5', 'pm10', 'o3', 'no2', 'so2', 'co']].mean()

cmap_graph_map = sns.color_palette("YlOrBr", as_cmap=False)
plt.figure(figsize=(7,7))
sns.heatmap(mean_per_year, cmap=cmap_graph_map, fmt=".5f", linecolor="white", linewidths=1, annot=True)
plt.show()

## O  monitor de qualidade do ar usa sensores de partículas a laser para medir em tempo real a poluição por partículas PM2.5 e
## PM10, que é um dos poluentes atmosféricos mais prejudiciais.
## Além das substâncias o3, no2, so2 e co. Anualmente no Brasil, as partículas prejudiciais obteve um ...

#-------------------------------------------------------------------------------------------------------------------------------------------

# Análise Geográfica
## América do Sul

geographic_analysis_df = api.get_multiple_city_air(['Brazil', 'Argentina', 'Uruguai', 'Paraguai', 'Chile', 'Bolivia', 'Equador', 'Guiana Francesa', 'Venezuela', 
                                                    'Peru', 'Colômbia', 'Suriname', 'Guiana']) 

shapefile_south_america = 'map_south_america/AMERICA_SUL.shp'
map_south_america = gpd.read_file(shapefile_south_america)
print(map_south_america)

merged_map_shapefile_with_dataframe = map_south_america.merge(geographic_analysis_df, left_on='country', right_on='city')

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
merged_map_shapefile_with_dataframe.plot(column='dominant_pollutant', ax= ax, legend=True, cmap=cmap_graph_map)

ax.set_axis_off()
plt.show()