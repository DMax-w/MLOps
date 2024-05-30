import os
import pickle

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Загрузка датасета Iris
iris_data = load_iris()

# Независимые переменные и зависимый целевой параметр
X = iris_data.data
y = iris_data.target

# Стандартизация данных
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Разделение данных на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=39
)

# Обучение модели
model = LogisticRegression()
model.fit(X_train, y_train)

# Проверка модели на тестовой выборке
y_pred = model.predict(X_test)

# Отчёт по метрикам классификации
report = classification_report(y_test, y_pred, target_names=iris_data.target_names)
print("Classification report:", report, sep="\n", end="\n\n")

# Сохранение модели и предобработчика данных
iris_scaler_file = os.environ["IRIS_SCALER"]
iris_model_file = os.environ["IRIS_MODEL"]
iris_model_dir = os.path.dirname(iris_model_file)

os.makedirs(iris_model_dir, exist_ok=True)

with open(iris_scaler_file, "wb") as f:
    pickle.dump(scaler, f)

with open(iris_model_file, "wb") as f:
    pickle.dump(model, f)
