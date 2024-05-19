import os
import pickle

import pandas as pd
from sklearn.svm import SVR


def train_model(train_prep_path):
    # Тренируем модель

    train_df = pd.read_csv(train_prep_path)

    X_train = train_df.drop(columns=["Daily_Temperature"])
    y_train = train_df["Daily_Temperature"]

    model = SVR()
    model.fit(X_train, y_train)

    return model


def create_directory(model_path):
    # Создадим папку для сохранения модели

    model_dir = os.path.dirname(model_path)
    if not os.path.isdir(model_dir):
        os.mkdir(model_dir)


def save_model(model, model_path):
    # Сохраним модель
    pickle.dump(model, open(model_path, "wb"))


# Читаем пути из переменных окружения
train_prep_path = os.environ["TRAIN_PREP_PATH"]
model_path = os.environ["MODEL_PATH"]

model = train_model(train_prep_path)
create_directory(model_path)
save_model(model, model_path)
