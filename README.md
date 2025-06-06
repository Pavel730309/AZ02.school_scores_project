# Исследование оценок учеников

## Описание задачи

Дан набор данных — таблица с оценками 10 учеников по 5 предметам (Математика, Физика, Химия, Биология, История).  
Задача — провести базовый анализ этого набора, используя Python и библиотеку Pandas.

### Требуется:

1. Создать DataFrame с оценками.
2. Вывести первые строки таблицы для визуальной проверки.
3. Рассчитать среднюю и медианную оценку по каждому предмету.
4. Найти первый (Q1) и третий (Q3) квартили, а также межквартильный размах (IQR) для оценок по математике.
5. Вычислить стандартное отклонение по каждому предмету.
6. Для каждого предмета определить лучшего и худшего ученика.
7. Рассчитать средний балл каждого ученика и отсортировать учеников по этому баллу (ранжирование).
8. Вывести полную описательную статистику (`describe()`) по всем предметам.

---

## Краткие выводы анализа

- **Средние и медианные оценки** по предметам позволяют оценить общую успеваемость класса и разброс результатов.
- **Q1, Q3 и IQR по математике** показывают, насколько равномерно распределены оценки и есть ли выбросы.
- **Стандартное отклонение** помогает увидеть, в каких предметах оценки более разбросаны.
- **Лучший и худший ученик по предметам** — быстрая идентификация сильных и слабых учеников.
- **Средний балл и ранжирование** — позволяет выявить общих отличников и отстающих в классе.
- **Описательная статистика** даёт детальное представление о распределении оценок (минимум, максимум, среднее, медиана, квартиль, стандартное отклонение).

---

## Использование

1. Откройте или скопируйте файл `school_analysis.py`.
2. Запустите код в Python 3.x (необходима библиотека `pandas`).
3. Результаты анализа выводятся в консоль построчно.
4. Для изменения данных достаточно заменить словарь `data` в начале файла.

---

## Пример вывода

