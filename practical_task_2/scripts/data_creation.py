import os

import numpy as np
import pandas as pd


def generate_data(data_size, noise_power):
    # Генерируем данные по разным алгоритмам
    fields = [
        np.random.lognormal(1, 0.8, data_size),
        np.random.pareto(6, data_size),
        np.random.geometric(0.7, data_size),
        np.random.binomial(20, 0.9, data_size),
        np.random.exponential(3, data_size),
        np.random.normal(3, 4, data_size),
    ]

    # Генерируем целевой признак по функции
    target = (
            1.1 * fields[0]
            + 0.4 * fields[1] ** 2
            + 1.3 * np.exp(fields[2])
            + 0.6 * np.log(fields[3])
            + 0.4 * np.sqrt(fields[4])
            + fields[5] / 5
    )

    # Подмешиваем шум
    for index, feature in enumerate(fields):
        noises = np.random.randn(data_size) * noise_power
        fields[index] = feature + noises

    # Создаём дата сет вместе с целевой функцией
    fields.append(target)

    return np.stack(fields, axis=1)


def create_dirs(train_path, test_path):
    # Создаём папку train
    train_dir = os.path.dirname(train_path)
    if not os.path.isdir(train_dir):
        os.mkdir(train_dir)

    # Создаём папку test
    test_dir = os.path.dirname(test_path)
    if not os.path.isdir(test_dir):
        os.mkdir(test_dir)


def save_data(data, columns, train_path, test_path):
    # Создаём Pandas DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Разделим на тренировочные (80%) и тестовые (20%) данные
    split_idx = int(len(df) * 0.8)
    train = df[:split_idx]
    test = df[split_idx:]

    # Сохраним train.csv
    train.to_csv(train_path, index=False)

    # Сохраним test.csv
    test.to_csv(test_path, index=False)


# Наименование признаков и целевого признака - "Дневная температура".
columns = [
    "Feature_1",
    "Feature_2",
    "Feature_3",
    "Feature_4",
    "Feature_5",
    "Feature_6",
    "Daily_Temperature",
]

# Размер данных и сила шума.
data_size = 20000
noise_power = 0.07

train_path = os.environ["TRAIN_PATH"]
test_path = os.environ["TEST_PATH"]

data = generate_data(data_size, noise_power)
create_dirs(train_path, test_path)
save_data(data, columns, train_path, test_path)
