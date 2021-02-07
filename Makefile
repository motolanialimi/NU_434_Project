setup:
	# You may want to do this
	virtualenv --python $(which python3) ~/.hellovenv
	# afterward then source
	# source ~/.hellovenv/bin/activate

install:
	pip install -r requirements.txt

lint:
	pylint --disable=R,C main.py
    # C conventional related checks
	# R refactoring related checks
	# W various warnings
	# E errors, for probable bugs in the code
	# F fatal, if an error occured which prevented pylint
