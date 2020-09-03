.PHONY: init
init:
	python -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt

.PHONY: run
run:
	uvicorn fast:app --reload