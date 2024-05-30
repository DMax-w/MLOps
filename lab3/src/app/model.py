import os
import pickle

from iris import Iris
from sklearn.preprocessing import StandardScaler


def load_model():
    iris_scaler_path = os.environ["IRIS_SCALER"]
    iris_model_path = os.environ["IRIS_MODEL"]

    scaler = pickle.load(open(iris_scaler_path, "rb"))
    model = pickle.load(open(iris_model_path, "rb"))

    def predict_iris(iris: Iris):
        iris_params = iris.get_params()
        iris_prepared_params = scaler.transform([iris_params])

        iris_label = model.predict(iris_prepared_params)[0]
        iris_class = Iris.CLASSES[iris_label]

        return iris_class

    return predict_iris
