#!/bin/bash

python3 -m venv ./.venv;
. ./.venv/bin/activate;
pip install -r requirements.txt
flake8 ./scripts --count --select=E9,F63,F7,F82 --show-source --statistics;
flake8 ./scripts --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics;

# Необходимые для ML пайплайна переменные окружения.
export TRAIN_PATH="${PWD}/train/train.csv"
export TRAIN_PREP_PATH="${PWD}/train/train_prep.csv"

export TEST_PATH="${PWD}/test/test.csv"
export TEST_PREP_PATH="${PWD}/test/test_prep.csv"

export MODEL_PATH="${PWD}/model/model.pkl"

# Запуск ML пайплайна.
python3 ./scripts/data_creation.py
python3 ./scripts/model_preprocessing.py
python3 ./scripts/model_preparation.py
python3 ./scripts/model_testing.py
