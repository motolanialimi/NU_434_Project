setup:
	# You may want to do this
	virtualenv --python $(which python3) ~/.hellovenv
	# afterward then source
	# source ~/.hellovenv/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv hello_test.py

format:
	black *.py


lint:
	pylint --disable=R,C hello.py

All: install lint test
