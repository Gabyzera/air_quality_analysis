import os 
import io
import sys
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
## Anual no Brasil

# temporal_analysis_df = api.get_historical_data(city='Brazil')

# temporal_analysis_df['date'] = pd.to_datetime(temporal_analysis_df['date'])
# temporal_analysis_df['date'] = temporal_analysis_df['date'].dt.year
# mean_per_year = temporal_analysis_df.groupby('date')[['pm2.5', 'pm10', 'o3', 'no2', 'so2', 'co']].mean()

# cmap_graph_map = sns.color_palette("YlOrBr", as_cmap=False)
# plt.figure(figsize=(7,7))
# sns.heatmap(mean_per_year, cmap=cmap_graph_map, fmt=".5f", linecolor="white", linewidths=1, annot=True)
# plt.show()

# '''O  monitor de qualidade do ar usa sensores de partículas a laser para medir em tempo real a poluição por partículas PM2.5 e PM10, que é um dos poluentes 
# atmosféricos mais prejudiciais.Além das substâncias o3, no2, so2 e co. Anualmente no Brasil, as partículas prejudiciais obteve um ...'''

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Análise de poluentes (AQI, PM2.5, PM10, NO2, SO2, O3, CO)
## No Brasil

# pollutants_analysis_df = api.get_city_air('Brazil')
# mean_values = pollutants_analysis_df[['aqi', 'pm2.5', 'pm10', 'o3', 'co', 'no2','so2']].mean()

# new_df_for_barplot = pd.DataFrame({
#     'Pollutants': mean_values.index,
#     'Mean Values': mean_values.values
# })

# df_sorted = new_df_for_barplot.sort_values(by='Mean Values')
# palette = sns.color_palette("YlOrBr", len(df_sorted))
# colors = palette.as_hex()

# df_sorted.plot.bar(x='Pollutants', y='Mean Values', color=colors, legend=False)
# plt.show()

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Análise Geográfica
## América do Sul

geographic_analysis_df = api.get_multiple_city_air(['Brazil', 'Argentina', 'Uruguai', 'Paraguai', 'Chile', 'Bolivia', 'Equador', 'Guiana Francesa', 'Venezuela', 
                                                    'Peru', 'Colômbia', 'Suriname', 'Guiana']) 

current_dir = os.path.dirname(__file__) 
shapefile_path_south_america = os.path.join(current_dir, 'map_south_america', 'AMERICA_SUL.shp')
map_south_america = gpd.read_file(shapefile_path_south_america)

merged_map_shapefile_with_dataframe = map_south_america.merge(geographic_analysis_df, left_on='NOME', right_on='city')

merged_map_shapefile_with_dataframe['pm2.5_log'] = np.log1p(merged_map_shapefile_with_dataframe['pm2.5'].fillna(0))
fig, ax = plt.subplots(1, 1, figsize=(6, 5))
merged_map_shapefile_with_dataframe.plot(column='pm2.5_log', ax=ax, legend=True, cmap='YlOrBr')

ax.set_axis_off()
plt.show()