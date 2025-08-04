import osmnx as ox
import matplotlib.pyplot as plt
import pandas as pd

"""
メモ
・キャッシュを使用したい
・geojsonデータの読み込みとファイル画像の出力を行いたい
"""

dpi = 600

north = 44.97
south = 44.87
east = 141.9
west = 142.07

print("featuresの取得")
water = ox.features_from_bbox(bbox=[west,south,east,north],tags={'natural': 'water'})

print("道路データの取得")
road = ox.graph_from_bbox(bbox=[west,south,east,north],network_type='all')

print('鉄道データの取得')
railways = ox.graph_from_bbox(bbox=[west, south, east, north], network_type='all', simplify=True, retain_all=True, truncate_by_edge=True, custom_filter='["railway"~"rail"]')

print('建物データの取得')
buildings = ox.features_from_bbox(bbox=[west, south, east, north], tags={'building': True})

# 共通のFigureとAxesを作成
print('プロット処理')
fig, ax = plt.subplots(figsize=(10, 8)) # 横：縦

# 道路を描画
ox.plot_graph(road, ax=ax, show=False, close=False, bgcolor='#ffffff', edge_color='green', node_size=0)

# 水域を重ねて描画
ox.plot_footprints(water, ax=ax, show=True, close=True, color='blue', edge_color='none')

# add the railway
ox.plot_graph(railways, ax=ax, show=True, close=True, edge_color='black', edge_linewidth=0.5, node_size=0)

ox.plot_footprints(buildings, ax=ax, show=True, close=True, color='orange', edge_color='none')

# pngファイルで出力
fig.savefig("output/sample.png", dpi=dpi)
print("地図画像を出力しました: output/sample.png")

"""
# 使用した関数についてのメモ
features_from_bbox ( bbox , tags )
    bbox ( tuple[ float, float, float, float] ) – 境界ボックスは(left, bottom, right, top)で表されます。座標は非投影の緯度経度度 (EPSG:4326) で指定します。
    tags ( dict[ str, bool| str| list[ str]] ) – 選択したエリア内の要素を検索するためのタグ
graph_from_bbox ( bbox , * , network_type = 'all' , simplify = True , retain_all = False , truncate_by_edge = False , custom_filter = None )
    bbox ( tuple[ float, float, float, float] ) – 境界ボックスは(left, bottom, right, top)で表されます。座標は非投影の緯度経度度 (EPSG:4326) で指定します。
    network_type ( ) – {“all”, “all_public”, “bike”, “drive”, “drive_service”, “walk”} custom_filterstrがNoneの場合に取得する道路ネットワークの種類。
    simplify ( ) – Trueの場合、 simpliify_graphbool関数を使用してグラフトポロジを簡素化します。
    その他もろもろ
"""