import sqlite3
import re
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']   # Matplotlib中文声明
plt.rcParams['axes.unicode_minus'] = False

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("SELECT music_name FROM music")
music_names = cursor.fetchall()
conn.close()

music_names = [name[0] for name in music_names]
truncated_names = [name[:80] + '...' if len(name) > 80 else name for name in music_names]
name_lengths = [len(name) for name in truncated_names] # 歌名长度

plt.figure(figsize=(10, 6))
plt.hist(name_lengths, bins=range(1, max(name_lengths) + 2), edgecolor='black', alpha=0.7)
plt.title('歌名字符长度分布')
plt.xlabel('长度')
plt.ylabel('频率')
plt.xticks(range(1, max(name_lengths) + 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() # name_length_character.png

cleaned_names = [re.sub(r'\(.*?\)|\[.*?\]', '', name) for name in music_names] # 去歌名修饰

def count_syllables(name): # 音节计数
    chinese_syllables = len(re.findall(r'[\u4e00-\u9fff]', name))
    english_words = re.findall(r'\b\w+\b', name)
    english_syllables = sum(len(word) // 2 + 1 for word in english_words if re.search(r'[a-zA-Z]', word))
    return chinese_syllables + english_syllables

# print(count_syllables("test"))
# print(count_syllables("sophisticated"))
# print(count_syllables("你好"))

syllable_counts = [count_syllables(name) for name in cleaned_names]

plt.figure(figsize=(10, 6))
plt.hist(syllable_counts, bins=range(1, max(syllable_counts) + 2), edgecolor='black', alpha=0.7)
plt.title('歌名音节数量分布')
plt.xlabel('音节数量')
plt.ylabel('频率')
plt.xticks(range(1, max(syllable_counts) + 1))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show() # name_length_syllable.png

less_equal_10 = [count for count in syllable_counts if count <= 10]
percentage = (len(less_equal_10) / len(syllable_counts)) * 100
print(f"{percentage:.2f}%") # 歌名音节≤10的总频率百分比