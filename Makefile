.PHONY: all
all:
	@echo "There's nothing to build."


venv: requirements.txt
	virtualenv -p python3.5 venv --prompt '(lispy) '
	./venv/bin/pip install -r requirements.txt


.PHONY: CI test lint
CI: lint test
test: venv
	./venv/bin/py.test $(ARGS)
lint: venv
	git ls-files '*.py' | xargs ./venv/bin/flake8
	git ls-files '*.py' | xargs ./venv/bin/pylint
