# Подготовка виртуального окружения
.PHONY: venv
venv:
	(python3 -m venv ./.venv; . ./.venv/bin/activate;)

# Удаление виртуального окружения
.PHONY: del_deps
del_deps:
	rm -R ./.venv

# Установка пакетов приложения`
.PHONY: deps_app
deps_app: venv
	pip install -r ./src/app/requirements.txt;

# Установка пакетов подготовки модели
.PHONY: deps_model
deps_model: venv
	pip install -r ./src/model_preparing/requirements.txt;

# Переменные окружения для сохранения модели
export IRIS_SCALER := ./src/model_dump/iris_scaler.pkl
export IRIS_MODEL := ./src/model_dump/iris_model.pkl

# Запуск подготовки модели
.PHONY: model_preparing
model_preparing:
	(. ./.venv/bin/activate; python3 ./src/model_preparing/model_preparing.py)

# Запуск приложения с моделью в контейнере
.PHONY: docker_up
docker_up:
	docker compose down
	docker compose up -d --build
