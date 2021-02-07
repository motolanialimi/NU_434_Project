setup:
	# You may want to do this
	virtualenv --python $(which python3) ~/.hellovenv
	# afterward then source
	# source ~/.hellovenv/bin/activate

test:
	python -m pytest -vv test_hello.py

format:
	black *.py


lint:
	pylint --disable=R,C hello.py

All: install lint test
