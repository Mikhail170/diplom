import numpy as np
import seaborn as sns
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ СТОЛБЧАТЫХ ГРАФИКОВ (MATPLOTLIB)
# Данные о продажах
продукты = ['Продукт A', 'Продукт B', 'Продукт C', 'Продукт D']
продажи = [1500, 2300, 1800, 2200]
цвета = ['blue', 'orange', 'green', 'red']

# Создание столбчатого графика
plt.bar(продукты, продажи, color=цвета)
plt.title('Продажи продуктов за месяц')
plt.xlabel('Продукты')
plt.ylabel('Продажи (в рублях)')
# Показ процентов на каждом столбце
for i in range(len(продажи)):
    plt.text(i, продажи[i] + 50, f'{(продажи[i] / sum(продажи)) * 100:.1f}%', ha='center')
plt.show()



# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ГИСТОГРАММ (MATPLOTLIB)
# Генерация случайных оценок студентов (среднее 70, стандартное отклонение 10)
оценки = np.random.normal(70, 10, 100)

# Создание гистограммы
n, bins, patches = plt.hist(оценки, bins=10, edgecolor='black', alpha=0.7)

# Применение цветовой карты к каждому столбцу
for i in range(len(patches)):
    patches[i].set_facecolor(plt.cm.viridis(i / len(patches)))

plt.title('Распределение оценок на экзамене')
plt.xlabel('Оценки')
plt.ylabel('Количество студентов')
plt.grid(axis='y', alpha=0.75)  # Сетка по оси Y для лучшей читабельности
plt.show()



# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ КРУГОВЫХ ДИАГРАММ (MATPLOTLIB)
# Данные о расходах
категории = ['Продукты', 'Транспорт', 'Жилище', 'Развлечения', 'Здоровье']
расходы = [400, 150, 600, 200, 100]
цвета = ['gold', 'lightcoral', 'lightskyblue', 'mediumseagreen', 'plum']

# Создание круговой диаграммы
plt.pie(расходы, labels=категории, autopct='%1.1f%%', startangle=90, colors=цвета)
plt.title('Распределение расходов по категориям')
plt.axis('equal')  # Равный аспект для круга
plt.show()



# ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ГРАФИКОВ ПАР (SEABORN)
#Загрузка набора данных Iris
iris = sns.load_dataset('iris')
# График пар (Pair Plot)
sns.pairplot(iris, hue='species', markers=['o', 's', 'D'])
plt.title('Графики пар в наборе данных Iris')
plt.show()



#ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ МНОГОУРОВНЕВЫХ ГРАФИКОВ (SEABORN)
#Загрузка набора данных о ценах на алмазы
tips = sns.load_dataset('diamonds')
# FacetGrid: многоуровневый график цикла по категориям
g = sns.FacetGrid(tips, col='cut', hue='color', margin_titles=True)
g.map(sns.scatterplot, 'carat', 'price', alpha=0.7)
g.add_legend()
plt.subplots_adjust(top=0.9)
g.fig.suptitle('Цены на алмазы по категории и цвету')
plt.show()



#ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ГРАФИКОВ С НЕСКОЛЬКИМИ ОСЯМИ (SEABORN)
#Dummy data: расходы и доходы
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'expenses': [500, 600, 700, 800, 900, 700, 950, 800, 1100, 900, 1000, 1200],
    'income': [800, 950, 1000, 1100, 1200, 1150, 1300, 1400, 1350, 1600, 1500, 1800]
}
df = pd.DataFrame(data)
# Создание графиков с несколькими осями
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
sns.lineplot(data=df, x='month', y='expenses', ax=ax1, color='r', marker='o', label='Расходы')
sns.lineplot(data=df, x='month', y='income', ax=ax2, color='g', marker='s', label='Доходы')
# Настройка осей и легенд
ax1.set_ylabel('Расходы', color='r')
ax2.set_ylabel('Доходы', color='g')
ax1.set_title('Сравнение расходов и доходов по месяцам')
ax1.set_xticks(range(len(df['month'])))
ax1.set_xticklabels(df['month'])
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()



#ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ИНТЕРАКТИВНОГО ГРАФИКА РАССЕЯНИЯ (PLOTLY)
#Загрузка данных о цветах Iris
iris = px.data.iris()
# Создание графика рассеяния
fig = px.scatter(iris, x='sepal_width', y='sepal_length', color='species',
                 title='График рассеяния для цветов Iris')
fig.show()



#ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ КРУГОВОЙ ДИАГРАММЫ (PLOTLY)
# Данные о расходах по категориям
categories = ['Продукты', 'Транспорт', 'Жилище', 'Развлечения', 'Здоровье']
values = [400, 150, 600, 200, 100]
df = pd.DataFrame({
    'categories': categories,
    'values': values
})
# Создание круговой диаграммы
fig = px.pie(df, values='values', names='categories', title='Распределение расходов')
fig.show()
# Создание данных
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
expenses = [500, 600, 700, 800, 900, 700, 950, 800, 1100, 900, 1000, 1200]
income = [800, 950, 1000, 1100, 1200, 1150, 1300, 1400, 1350, 1600, 1500, 1800]
df = pd.DataFrame({
    'months': months,
    'expenses': expenses,
    'income': income
})



#ПРИМЕР ВИЗУАЛИЗАЦИИ ДАННЫХ ПРИ ПОМОЩИ ГРАФИКА С НЕСКОЛЬКИМИ ОСЯМИ (PLOTLY)
# Создание графика с несколькими осями
fig = go.Figure()
# Добавление графика расходов
fig.add_trace(go.Scatter(x=df['months'], y=df['expenses'], mode='lines+markers', name='Расходы', line=dict(color='red')))
# Добавление графика доходов
fig.add_trace(go.Scatter(x=df['months'], y=df['income'], mode='lines+markers', name='Доходы', line=dict(color='green')))
# Настройка меток осей и заголовка
fig.update_layout(title='Сравнение расходов и доходов по месяцам', yaxis_title='Сумма (в $)')
fig.show()
