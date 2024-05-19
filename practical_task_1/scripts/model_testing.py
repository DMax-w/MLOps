import os
import pickle

import pandas as pd
from sklearn.metrics import r2_score


def load_model(model_path):
    # загрузим модель из дампа

    model = pickle.load(open(model_path, "rb"))

    return model


def test_model(model, test_prep_path):
    # Протестируем модель по метрике r2_score

    test_df = pd.read_csv(test_prep_path)

    X_test = test_df.drop(columns=["Daily_Temperature"])
    y_test = test_df["Daily_Temperature"]

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)

    return r2


# Достанем пути из переменных окружения
test_prep_path = os.environ["TEST_PREP_PATH"]
model_path = os.environ["MODEL_PATH"]

model = load_model(model_path)
r2 = test_model(model, test_prep_path)

print("=====================================")
print("Model R2 score =", r2)
print("ML pipeline complete.")
