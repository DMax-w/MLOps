# Практическое задание №3

__Выполнил:__ *Домченко Максим*

__Студент группы:__ *РИМ-130962*

## "Описание:"

### 1. Подготовлены скрипты для тренировки (`./src/model_preparing/`) и сохранения модели (`./src/model_dump/`)

### 2. Подготовлены скрипты интерфейса приложения (`./src/app/`) на `streamlit` для работы с моделью (`./src/model_dump/`)

### 3. В скриптах подготовки модели и приложения лежат разные файлы с зависимостями, чтобы не тянуть всё в контейнер с приложением

### 4. Разработан `Dockerfile`, в котором описан образ контейнера с необходимыми данными:

* Указан образ контейнера с версией `python`
* Установлены переменные окружения
* Скопированы и установлены зависимости приложения
* Скорироваан файлы приложения и модели
* Команда запуска приложения

### 5. Разработан файл `docker-compose.yml` в котором указан параметры запуска сервиса с моделью:
* Название сервиса
* Название собираемого образа и контейнера
* Прокинут порт, для взаимодействия
* Путь к `Dockerfile`

### 6. Для удобства локальной разработки и автоматизации сборки разработан `Makefile`

## Запуск приложения:
* Стянуть проект `git clone https://github.com/DMax-w/MLOps.git`
* Перейти в папку проекта `cd ./MLOps/`
* Выполнить команду `make run_pt_3`

## `make run_pt_3`:
* Перейдёт в папку с практической
* Выполнит подготовку среды с установкой необходимых зависимостей для подготовки модели (тренировка и сохранение)
* Запустит приложение в `docker` контейнере, к которому можно подключиться (http://localhost:7070/)
