import streamlit as st
from iris import Iris
from model import load_model

# Загрузка и кэширование модели
@st.cache_resource()
def load_cache_model():
    return load_model()


predict = load_cache_model()

# Заголовки
st.title("Определение вида Ириса по параметрам!")
st.text("Введите размеры околоцветников Ириса:")

# Ввод параметров Ириса
sepal_length = st.number_input("Длина наружной доли околоцветника (sepal length)")
sepal_width = st.number_input("Ширина наружной доли околоцветника (sepal width)")
petal_length = st.number_input("Длина внутренней доли околоцветника (petal length)")
petal_width = st.number_input("Ширина внутренней доли околоцветника (petal width)")

# Если заполнили все поля
if sepal_length and sepal_width and petal_length and petal_width:
    # Валидация
    try:
        iris = Iris(sepal_length, sepal_width, petal_length, petal_width)
    except ValueError:
        st.warning("Введены некорректные значения. Пожалуйста введите числа.")

    # Предсказание
    try:
        iris_class = predict(iris)
        st.success(iris_class)
    except:
        st.error("Ошибка модели.")
