.PHONY: all lint test
all:
	@echo "There's nothing to build."

.PHONY: CI test lint
CI: lint test
test:
	py.test
lint:
	git ls-files '*.py' | xargs pylint
	git ls-files '*.py' | xargs flake8
