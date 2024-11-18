import sqlite3
import jieba
from jieba import analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import re

plt.rcParams['font.sans-serif'] = ['SimHei']   # Matplotlib中文声明
plt.rcParams['axes.unicode_minus'] = False

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT lyrics_pure FROM music")
lyrics_data = cursor.fetchall()
conn.close()

excluded_phrases = [
    "作词", "作曲", "编曲", "制作人", "出品", "人声编辑", "录音", "总监", "原唱", "设计", "监制", "钢琴", "音频编辑", "统筹", "企划", "合音", "发行", "封面", "推广", "营销",
    "音乐统筹", "混音", "母带", "营销推广", "项目总监", "音乐总监", "合声", "键盘", "吉他", "和音", "贝斯", "打击乐", "长号", "萨克斯", "小号", "弦乐", "大提琴", "小提琴", "录音", "混音", "作词", "作曲"
]

lyrics_text = "\n".join([item[0] for item in lyrics_data])
lyrics_lines = lyrics_text.split('\n')
filtered_lines = [line for line in lyrics_lines if not any(phrase in line for phrase in excluded_phrases)] # 去非歌词行
cleaned_lines = [re.sub(r'\[.*?\]', '', line) for line in filtered_lines] # 去时间戳
cleaned_text = " ".join(cleaned_lines)
cleaned_text = re.sub(r'[^\w\s]', '', cleaned_text) # 去标点

keywords = analyse.extract_tags(cleaned_text, topK=1000, withWeight=False) # 关键词

wordcloud = WordCloud(width=800, height=400, background_color='white', font_path='simhei.ttf').generate(' '.join(keywords))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('全歌词词云图') # lyrics_cloud_all.png
plt.show()

words_count = Counter(cleaned_text.split())
keywords_frequency = {word: count for word, count in words_count.items() if word in keywords} # 词频统计
sorted_keywords_frequency = sorted(keywords_frequency.items(), key=lambda x: x[1], reverse=True) # 按次数排序
# print(sorted_keywords_frequency)

words, frequencies = zip(*sorted_keywords_frequency)

plt.figure(figsize=(20, 10))
plt.bar(words[:20], frequencies[:20])
plt.xticks(rotation=45)
plt.xlabel('关键词')
plt.ylabel('频率')
plt.title('全关键词频率柱状图')
plt.show() # lyrics_statistics_all.png



chinese_text = re.sub(r'[a-zA-Z]', '', cleaned_text) # 去英文单独分析中文
chinese_text = re.sub(r'\s+', ' ', chinese_text)

keywords_cn = analyse.extract_tags(chinese_text, topK=1000, withWeight=False)

wordcloud_cn = WordCloud(width=800, height=400, background_color='white', font_path='simhei.ttf').generate(' '.join(keywords_cn))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_cn, interpolation='bilinear')
plt.axis('off')
plt.title('中文歌词词云图')
plt.show() # lyrics_cloud_chinese.png

words_count_cn = Counter(chinese_text.split())
keywords_frequency_cn = {word: count for word, count in words_count_cn.items() if word in keywords}
sorted_keywords_frequency_cn = sorted(keywords_frequency_cn.items(), key=lambda x: x[1], reverse=True)

words_cn, frequencies_cn = zip(*sorted_keywords_frequency_cn)

plt.figure(figsize=(20, 10))
plt.bar(words_cn[:20], frequencies_cn[:20])
plt.xticks(rotation=45)
plt.xlabel('关键词')
plt.ylabel('频率')
plt.title('中文关键词频率柱状图')
plt.show() # lyrics_statistics_chinese.png