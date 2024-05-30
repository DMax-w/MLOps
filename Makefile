# Запуск Практического задания №1
.PHONY: run_pt_1
run_pt_1:
	cd ./lab1; \
	./pipeline.sh

.PHONY: run_pt_3
run_pt_3:
	cd ./lab3; \
	make deps_model; \
	make model_preparing; \
	make docker_up;
