# 1. Импортируем нужные библиотеки
import pandas as pd
import matplotlib.pyplot as plt

# 2. Загружаем данные
df = pd.read_parquet('/content/transaction_fraud_data.parquet')

# 3. Проверяем тип данных в столбце
print("Тип данных в last_hour_activity:", type(df['last_hour_activity'].iloc[0]))

# 4. Если данные уже словари - работаем напрямую
df['many_transactions'] = df['last_hour_activity'].apply(lambda x: x['num_transactions'] > 10)
df['big_amount'] = df['last_hour_activity'].apply(lambda x: x['total_amount'] > 5000)

# 5. Считаем процент мошенничества
result = df.groupby(['many_transactions', 'big_amount'])['is_fraud'].mean() * 100
print("\nПроцент мошенничества:")
print(result)

# 6. Простая визуализация
result.unstack().plot(kind='bar', color=['lightblue', 'orange'])
plt.title('Риск мошенничества по активности')
plt.ylabel('Процент мошенничества')
plt.xlabel('Много транзакций (>10)')
plt.xticks([0, 1], ['Нет', 'Да'], rotation=0)
plt.legend(['Сумма ≤5000', 'Сумма >5000'])
plt.show()
