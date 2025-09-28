import osmnx as ox
import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
import matplotlib.patheffects as pe

# 画像設定
fig_height = 3.8 # 82mm=3.22inch
fig_width = 5 # 105mm=4.13inch
dpi = 600

# 色設定
background_color = '#fefcf7'   # ミルキーホワイト（より明るく）
water_color          = '#5dbbe3'  # パステルブルー（鮮やかに）
road_color           = '#64c2a6'  # 明るいグリーン（白背景に映える）
railways_color       = '#2e2e2e'  # 鉄道：印刷で潰れないように濃いグレ
buildings_color      = '#d8a976'  # はっきりしたベージュオレンジ系
national_road_color = '#e6725b'  # 国道：明るめレンガ色

# 地図の設定
north = 44.97 #44.97
south = 44.87 #44.87
east = 141.88 # 141.9
west = 142.07 #142.07

# キャッシュの設定
ox.settings.use_cache = True
ox.settings.log_console = True

# 画像の設定
fig, ax = plt.subplots(figsize=(fig_width, fig_height)) # 図のサイズと背景色
plt.subplots_adjust(left=0, right=1, bottom=0, top=1) # 余白を極力狭くする　
ax.set_facecolor(background_color) # グラフエリア内の背景色

# データの取得と出力
print("川データ")
rivers = ox.features_from_bbox(bbox=[west, south, east, north], tags={'waterway': 'river'})
rivers.plot(ax=ax, color=water_color, linewidth=0.5)

print("水域データ")
water = ox.features_from_bbox(bbox=[west,south,east,north],tags={'natural': 'water'})
ox.plot_footprints(water, ax=ax, color=water_color, show=False, close=False)

print("車両道路データ")
road = ox.graph_from_bbox(bbox=[west,south,east,north],network_type='drive')
ox.plot_graph(road, ax=ax, node_size=0, edge_color=road_color, edge_linewidth=0.5, show=False, close=False)

print('県道データ')
secondary_road = ox.features_from_bbox(bbox=[west,south,east,north],tags={'highway': 'secondary'})
secondary_road.plot(ax=ax, color=road_color, linewidth=1)

print('国道データ')
trunk = ox.features_from_bbox(bbox=[west,south,east,north],tags={'highway': 'trunk'})
trunk.plot(ax=ax, color=national_road_color, linewidth=1.2, alpha=0.9)

print('鉄道データ')
railways = ox.features_from_bbox(bbox=[west,south,east,north],tags={'railway': 'rail'})
railways.plot(ax=ax, color=railways_color, linewidth=1, alpha=0.9)

print('建物データ')
buildings = ox.features_from_bbox(bbox=[west, south, east, north], tags={'building': True})
ox.plot_footprints(buildings, ax=ax, color=buildings_color, edge_color=buildings_color, edge_linewidth=0.3, show=True, close=True)

# ライセンスを表示
credit_text = "Map data from OpenStreetMap."

ax.text(
    0.03, 0.03,
    credit_text,
    transform=ax.transAxes,
    fontsize=6,
    color="black",
    ha="left", va="bottom",
    alpha=0.7,
    path_effects=[pe.withStroke(linewidth=0.5, foreground="black")]
)

# pngファイルで出力
fig.savefig("output/sample.png", dpi=dpi)
print("地図画像を出力しました: output/sample.png")