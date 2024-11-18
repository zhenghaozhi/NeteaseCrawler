import sqlite3
import re
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from collections import Counter

plt.rcParams['font.sans-serif'] = ['SimHei']   # Matplotlib中文声明
plt.rcParams['axes.unicode_minus'] = False

label_mapping = {
    '1 star': '非常负面',
    '2 stars': '负面',
    '3 stars': '中性',
    '4 stars': '正面',
    '5 stars': '非常正面'
}
expected_order = ['非常正面', '正面', '中性', '负面', '非常负面']

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT lyrics FROM music")
lyrics_data = cursor.fetchall()
conn.close()

lyrics = [lyric[0] for lyric in lyrics_data]

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\u4e00-\u9fff\s]', '', text)  # 保留字母和中文
    text = re.sub(r'\s+', ' ', text).strip()
    return text

preprocessed_lyrics = [preprocess_text(lyric) for lyric in lyrics]

model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, truncation=True)
predictions = classifier(preprocessed_lyrics) # 情感分类

predicted_labels = [pred['label'] for pred in predictions]
mapped_labels = [label_mapping[label] for label in predicted_labels]
label_counts = Counter(mapped_labels)
sorted_counts = [label_counts[label] if label in label_counts else 0 for label in expected_order]

plt.figure(figsize=(10, 6))
plt.bar(expected_order, sorted_counts)
plt.title('歌曲情感分布')
plt.xlabel('情感')
plt.ylabel('数量')
plt.xticks(rotation=45)
plt.show() # music_emotion.png