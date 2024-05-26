import os

import pandas as pd
from sklearn.preprocessing import PowerTransformer, StandardScaler


def preprocess_data(train_path, test_path):
    # Пред обработка данных
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)

    scaler = StandardScaler()
    power = PowerTransformer()

    scaler_features = [
        "Feature_1",
        "Feature_4",
        "Feature_6",
    ]

    power_features = [
        "Feature_2",
        "Feature_3",
        "Feature_5",
        "Daily_Temperature",
    ]

    train[scaler_features] = scaler.fit_transform(train[scaler_features])
    test[scaler_features] = scaler.fit_transform(test[scaler_features])

    train[power_features] = power.fit_transform(train[power_features])
    test[power_features] = power.fit_transform(test[power_features])

    return train, test


def save_prep_data(train, test, train_prep_path, test_prep_path):
    # Сохраним train_prep.csv
    train.to_csv(train_prep_path, index=False)

    # Сохраним test_prep.csv
    test.to_csv(test_prep_path, index=False)


# Достанем пути из переменных окружения
train_path = os.environ["TRAIN_PATH"]
train_prep_path = os.environ["TRAIN_PREP_PATH"]

test_path = os.environ["TEST_PATH"]
test_prep_path = os.environ["TEST_PREP_PATH"]

train, test = preprocess_data(train_path, test_path)
save_prep_data(train, test, train_prep_path, test_prep_path)
