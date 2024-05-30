class Iris:
    CLASSES = ("setosa", "versicolor", "virginica")

    # Если не сможем привести к числу с плавающей точкой - обработаем ошибку выше
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width):
        self.sepal_length = float(sepal_length)
        self.sepal_width = float(sepal_width)
        self.petal_length = float(petal_length)
        self.petal_width = float(petal_width)

    def get_params(self):
        return (
            self.sepal_length,
            self.sepal_width,
            self.petal_length,
            self.petal_width,
        )
