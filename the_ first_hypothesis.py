# Минимально необходимые библиотеки
import pandas as pd
import matplotlib.pyplot as plt

# 1. Загрузка данных
df = pd.read_parquet('/content/transaction_fraud_data.parquet')
print("Данные загружены. Столбцы:", list(df.columns))

# 2. Основной расчет
fraud_rates = df.groupby('is_outside_home_country')['is_fraud'].mean() * 100
print("\nПроцент мошенничества:")
print(fraud_rates)

# 3. Дополнительная статистика
print("\nДополнительно:")
print("Всего транзакций:", len(df))
print("За границей:", df['is_outside_home_country'].sum())

# 4. Простой график
plt.figure(figsize=(7, 4))
fraud_rates.plot(kind='bar', color=['green', 'red'])
plt.title('Уровень мошенничества по локациям')
plt.ylabel('Процент мошенничества')
plt.xticks([0, 1], ['В своей стране', 'За границей'], rotation=0)
plt.show()
