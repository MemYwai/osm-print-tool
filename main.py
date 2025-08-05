import osmnx as ox
import matplotlib.pyplot as plt

"""
メモ
・余白がいい感じになるようにサイズを調整（現時点ではH3.5*W5が良さそう）
・geojsonデータの読み込みとファイル画像の出力を行いたい
"""

# 画像設定
fig_height = 3.8 # 82mm=3.22inch
fig_width = 5 # 105mm=4.13inch
dpi = 600

# 色設定
background_color = '#fefcf7'   # ミルキーホワイト（より明るく）
water_color          = '#5dbbe3'  # パステルブルー（鮮やかに）
road_color           = '#64c2a6'  # 明るいグリーン（白背景に映える）
railways_color       = '#2e2e2e'  # 鉄道：印刷で潰れないように濃いグレー　→主張が強いのでもう少し優しい色
buildings_color      = '#d8a976'  # はっきりしたベージュオレンジ系　→もう少しオレンジを強くしたい
station_color        = '#f06b72'  # コーラルピンク（駅として目立つ） →要検討
national_road_color  = '#e94d3d'  # 赤系レンガ色（国道の主張を強めに）　→要検討
park_color           = '#6dcf7b'  # 明るいミントグリーン（自然エリア）　→要検討
border_color         = '#7a7a7a'  # グレーを少し抑えて明瞭に　→要検討
"""
station_color = '#f09ca2'      # ピンクレッド系（駅として認識されやすい）
national_road_color = '#e6725b'  # 国道：明るめレンガ色
park_color = '#a9d5a2'         # グリーン系（少し鮮やかに）
border_color = '#8c8c8c'       # グレー（彩度を少しだけ上げて見やすく）
"""

# 地図の設定
north = 44.97 #44.97
south = 44.87 #44.87
east = 141.88 # 141.9
west = 142.07 #142.07

# キャッシュの設定
ox.settings.use_cache = True
ox.settings.log_console = True

# 画像の設定
fig, ax = plt.subplots(figsize=(fig_width, fig_height), facecolor=background_color) # 図のサイズと背景色
plt.subplots_adjust(left=0, right=1, bottom=0, top=1) # 余白を極力狭くする　
ax.set_facecolor(background_color) # グラフエリア内の背景色

# データの取得と出力
print("川データ")
rivers = ox.features_from_bbox(bbox=[west, south, east, north], tags={'waterway': 'river'})
rivers.plot(ax=ax, color=water_color, linewidth=0.7)

print("水域データ")
water = ox.features_from_bbox(bbox=[west,south,east,north],tags={'natural': 'water'})
ox.plot_footprints(water, ax=ax, color=water_color, show=False, close=False)

print("全道路データ")
road = ox.graph_from_bbox(bbox=[west,south,east,north],network_type='all')
ox.plot_graph(road, ax=ax, node_size=0, edge_color=road_color, edge_linewidth=0.3, edge_alpha=0.5, show=False, close=False)

print("車両道路データ")
road = ox.graph_from_bbox(bbox=[west,south,east,north],network_type='drive')
ox.plot_graph(road, ax=ax, node_size=0, edge_color=road_color, edge_linewidth=0.5, show=False, close=False)

print('県道データ')
secondary_road = ox.graph_from_bbox(bbox=[west, south, east, north], truncate_by_edge=True, custom_filter='["highway"~"secondary"]')
ox.plot_graph(secondary_road, ax=ax, node_size=0, edge_color=road_color, edge_linewidth=1, show=False, close=False)

print('国道データ')
trunk = ox.features_from_bbox(bbox=[west,south,east,north],tags={'highway': 'trunk'})
trunk.plot(ax=ax, color=national_road_color, linewidth=1.2)


print('鉄道データ')
railways = ox.graph_from_bbox(bbox=[west, south, east, north], truncate_by_edge=True, custom_filter='["railway"~"rail"]')
ox.plot_graph(railways, ax=ax, node_size=0, edge_color=railways_color, edge_linewidth=0.7, show=False, close=False)

print('建物データ')
buildings = ox.features_from_bbox(bbox=[west, south, east, north], tags={'building': True})
ox.plot_footprints(buildings, ax=ax, color=buildings_color, edge_color=buildings_color, edge_linewidth=0.3, show=True, close=True)


print('駅データの取得')

# pngファイルで出力
fig.savefig("output/sample.png", dpi=dpi)
print("地図画像を出力しました: output/sample.png")