import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data = {
#     "набор А" : [85, 90, 95, 100, 105],
#     "набор Б" : [70, 80, 95, 110, 120],
# }
#
# df = pd.DataFrame(data)
# stdA = df["набор А"].std()
# stdB = df["набор Б"].std()
#
# print(f"стандартное отклонение набор А - {stdA}")
# print(f"стандартное отклонение набор Б - {stdB}")

# data = {
#     "Возраст" : [23, 22, 21, 25, 25, 26, 27, 29, 30, 28],
#     "Зарплата" : [54000, 50000, 57000, 60000, 59000, 58000, 49000, 53000, 55000, 62000],
# }
#
# df = pd.DataFrame(data)
# print(df.describe())
# print(f"Средний возраст - {df["Возраст"].mean()}")
# print(f"Медианный возраст - {df["Возраст"].median()}")
# print(f"Стандарное отклонение возраста - {df["Возраст"].std()}")
#
# print(f"Средняя зарплата - {df["Зарплата"].mean()}")
# print(f"Медианная зарплата - {df["Зарплата"].median()}")
# print(f"Стандарное отклонение зарплаты - {df["Зарплата"].std()}")

# dates = pd.date_range(start="2024-07-26", periods=10, freq="D")
# values = np.random.rand(10)
# df = pd.DataFrame({"Date": dates, "Value": values})
# df.set_index("Date", inplace=True)
# print(df)
# month = df.resample("M").mean()
# print(month)

# data = {"value" : [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
# df = pd.DataFrame(data)
#
# # df["value"].hist()
# df.boxplot(column="value")
# plt.show()
# # print(df.describe())
# Q1 = df["value"].quantile(0.25)
# Q3 = df["value"].quantile(0.75)
# IQR = Q3 - Q1
# downside = Q1 - 1.5 * IQR
# upside = Q3 + 1.5 * IQR
# df_new = df[(df["value"] >= downside)&(df["value"] <= upside)]
# df_new.boxplot(column="value")
# plt.show()

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)

df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')
print(df['gender'].cat.categories)
print(df['department'].cat.categories)
print(df['department'].cat.codes)

df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df)