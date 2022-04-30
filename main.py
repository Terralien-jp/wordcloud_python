from unittest import result
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

text = open(r'test.txt', "r").read()
cut_text = jieba.cut(text)
result=" ".join(cut_text)
wc = WordCloud(
        # フォントを設定し、指定しない場合はスクランブルコードになる
        # バックグラウンドカラー
        background_color='white',
        # バックグラウンドの幅
        width=500,
        # バックグラウンドの高さ
        height=350,
        # 最大文字サイズ
        max_font_size=50,
        # 最小文字サイズ
        min_font_size=10,
        mode='RGBA'
        )
# wordcloudの出力
wc.generate(result)
# 画像保存
wc.to_file(r"wordcloud.png")
# 画像表示
plt.figure("jay")
plt.imshow(wc)
plt.axis("off")
plt.show()  