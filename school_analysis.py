import pandas as pd

# Исходные данные: оценки 10 учеников по 5 предметам (5-балльная система)
data = {
    'Ученик': ['Иван', 'Мария', 'Петр', 'Анна', 'Сергей', 'Елена', 'Дмитрий', 'Ольга', 'Алексей', 'Наталья'],
    'Математика': [5, 4, 3, 5, 4, 5, 3, 4, 5, 4],
    'Физика': [4, 5, 3, 4, 3, 5, 4, 5, 4, 3],
    'Химия': [3, 4, 4, 5, 5, 4, 3, 4, 5, 4],
    'Биология': [5, 3, 4, 4, 4, 5, 5, 3, 4, 5],
    'История': [4, 5, 5, 3, 4, 4, 4, 5, 3, 4]
}
df = pd.DataFrame(data).set_index('Ученик')

subjects = df.columns

print("="*40)
print("1. Первые строки DataFrame:")
print(df.head())

print("\n2. Средние оценки по каждому предмету:")
print(df.mean())

print("\n3. Медианные оценки по каждому предмету:")
print(df.median())

print("\n4. Квартильные значения и IQR по математике:")
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"Q1 (25%): {Q1_math}")
print(f"Q3 (75%): {Q3_math}")
print(f"IQR: {IQR_math}")

print("\n5. Стандартное отклонение по каждому предмету:")
print(df.std())

print("\n6. Лучший и худший ученик по каждому предмету:")
for subject in subjects:
    best = df[subject].idxmax()
    worst = df[subject].idxmin()
    print(f"{subject}: лучший — {best} ({df.loc[best, subject]}), худший — {worst} ({df.loc[worst, subject]})")

print("\n7. Средний балл каждого ученика и ранжирование:")
df['Средний_балл'] = df.mean(axis=1)
ranked = df['Средний_балл'].sort_values(ascending=False)
for i, (name, avg) in enumerate(ranked.items(), 1):
    print(f"{i}. {name}: {avg:.2f}")

print("\n8. Полная описательная статистика по предметам:")
print(df[subjects].describe())