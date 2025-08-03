import osmnx as ox
import matplotlib.pyplot as plt

"""
# 対象地域の情報を取得
# place = "Tokyo Station, Tokyo, Japan"
# place = "Nakamuraku,Nagoya,Aichi,Japan"
#place = "Toikanbetsu,Horonobe,Hokkaido,Japan"
#graph = ox.graph_from_place(place, network_type="drive")


fig, ax = ox.plot_graph(graph, show=False, close=True)
fig.savefig("output/sample.png", dpi=300)
print("地図画像を出力しました: output/tokyo_station.png")

"""
# 地域の情報を取得（字雄興を例に）
latitude = 44.908699
longitude = 141.957398
dist = 8000 # km

# キャッシュを使う
#ox.config(use_cache=True, log_console=True)

"""
graph = ox.graph_from_point(center_point=(latitude,longitude),
                            network_type='drive',
                           simplify=True,
                           retain_all=True,
                           dist=dist,
                           custom_filter='["highway"~"secondary|secondary_link|primary|primary_link|trunk|trunk_link"]["lanes"=2]')
"""

#osmnx.features. features_from_bbox ( bbox , tags )  でもいいかも、緯度軽度の枠で指定？


print("featuresの取得")
water = ox.features_from_point(center_point=(latitude,longitude), dist=dist, tags={'natural': 'water'})
fig1, ax = ox.plot_footprints(water, figsize = (8, 8) , color = 'blue' , edge_color = 'none' , edge_linewidth = 0 , alpha = None , bgcolor = '#aaaaaa' , bbox = None , show = True , close = False , save = False , filepath = None , dpi = 600 ) 


print("道路データを取得します")
road = ox.graph_from_point(center_point=(latitude,longitude), dist=dist,network_type='all')
#nodes, edges = ox.graph_to_gdfs(G)
print("道路データの取得が完了しました")
fig2, ax = ox.plot_graph(road, ax = None , figsize = (8, 8) , bgcolor = '#aaaaaa' , node_color = 'w' , node_size = 0 , node_alpha = None , node_edgecolor = 'none' , node_zorder = 1 , edge_color = 'red' , edge_linewidth = 1 , edge_alpha = None , bbox = None , show = True , close = False , save = False , filepath = None , dpi = 300 ) 
"""
road = ox.features_from_point(center_point=(latitude,longitude), dist=dist, tags={'natural': 'drive'})
fig3, ax = ox.plot_footprints(road, figsize = (8, 8) , color = 'blue' , edge_color = 'none' , edge_linewidth = 0 , alpha = None , bgcolor = '#aaaaaa' , bbox = None , show = True , close = False , save = False , filepath = None , dpi = 600 ) 
"""
print(type(fig1))
print(type(fig2))

# 複数の<class 'matplotlib.figure.Figure'>をどう組み合わせるか悩み中
fig, ax = plt.subplots(figsize=(12, 12))
fig.patch.set_facecolor('green')
ax.set_facecolor('green')

fig2.plot(ax=ax, color='red', linewidth=1)

# 現状ここの変数をfig1か2にすればそれぞれのデータは出力される
fig.savefig("output/sample.png", dpi=300)
print("地図画像を出力しました: output/sample.png")

# 追加項目　geojsonデータを読み込んで重ねたい