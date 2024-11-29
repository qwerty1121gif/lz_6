import pandas as pd
import matplotlib.pyplot as plt

file_path = 'titanic.parquet'
df = pd.read_parquet(file_path)
df.to_csv('titanic.csv', index=False, encoding='utf-8')
print(f'Файл сохранен как: titanic.csv')

df = pd.read_csv('titanic.csv')

survival_percentage = df.groupby('Pclass')['Survived'].value_counts(normalize=True).mul(100).unstack().rename(columns={0: 'Не выжили', 1: 'Выжили'})

survival_percentage.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'], figsize=(10,6))
plt.title('Выживаемость пассажиров Титаника')
plt.xlabel('Класс билета')
plt.xticks(rotation=0)
plt.ylabel('Процент')
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f'{x:.0f}%'))
plt.ylim(0,100)
plt.tight_layout()
plt.show()

