import osmnx as ox
import matplotlib.pyplot as plt

"""
メモ
・キャッシュを使用したい
・範囲の指定をosmnx.features. features_from_bbox ( bbox , tags )などを使用して、緯度経度の枠で指定したい
・geojsonデータの読み込みとファイル画像の出力を行いたい
"""

# 地域の情報を取得（字雄興を例に）
latitude = 44.908699
longitude = 141.957398
dist = 8000 # km

print("featuresの取得")
water = ox.features_from_point(center_point=(latitude,longitude), dist=dist, tags={'natural': 'water'})
fig1, ax = ox.plot_footprints(water, figsize = (8, 8) , color = 'blue' , edge_color = 'none' , edge_linewidth = 0 , alpha = None , bgcolor = '#ffffff' , bbox = None , show = True , close = False , save = False , filepath = None , dpi = 600 ) 

print("道路データの取得")
road = ox.graph_from_point(center_point=(latitude,longitude), dist=dist,network_type='all')
fig2, ax = ox.plot_graph(road, ax = None , figsize = (8, 8) , bgcolor = '#ffffff' , node_color = 'w' , node_size = 0 , node_alpha = None , node_edgecolor = 'none' , node_zorder = 1 , edge_color = 'green' , edge_linewidth = 1 , edge_alpha = None , bbox = None , show = True , close = False , save = False , filepath = None , dpi = 300 ) 

# pngファイルで出力
fig2.savefig("output/sample.png", dpi=300)
print("地図画像を出力しました: output/sample.png")