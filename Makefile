install:
	pip install --upgrade pip &&\
		pip install setuptools &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py
	py.test --nbval *.ipynb

format:
	nbqa black *.ipynb &&\	
	black *.py && black test_*.py

lint:
	ruff check test_*.py && ruff check *.py
	nbqa ruff *.ipynb

generate_report:
	python main.py
		
all: install lint test format generate_report