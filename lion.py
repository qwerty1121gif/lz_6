import docx
import re
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'lion.docx'
doc = docx.Document(file_path)
text = ' '.join([paragraph.text for paragraph in doc.paragraphs]).lower()

words = pd.Series(re.findall(r'\b\w+\b', text))
total_words = len(words)
word_counts = words.value_counts()
df_words = word_counts.rename_axis('Слово').reset_index(name='Частота')
df_words['Процент'] = (df_words['Частота'] / total_words) * 100

print(df_words)
df_words.to_csv('word_frequency.csv', index=False, encoding='utf-8')
print(f'Результаты частоты слов сохранены в файл: word_frequency.csv')

letters = pd.Series(re.findall(r'[а-яА-ЯёЁ]', text)).value_counts()
df_letters = letters.rename_axis('Буква').reset_index(name='Частота')
df_letters['Процент'] = (df_letters['Частота'] / len(letters)) * 100

plt.figure(figsize=(10, 6))
plt.bar(df_letters['Буква'], df_letters['Частота'], color='green') #Изменено цвет
plt.title('Частота встречаемости букв')
plt.xlabel('Буквы')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
