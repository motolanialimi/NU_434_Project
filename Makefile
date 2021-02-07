setup:
	# You may want to do this
	virtualenv --python $(which python3) ~/.hellovenv
	# afterward then source
	# source ~/.hellovenv/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py


lint:
	pylint --disable=R,C main.py

All: install lint test
