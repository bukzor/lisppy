.PHONY: all lint
all:
	false
lint:
	git ls-files '*.py' | xargs pylint
	git ls-files '*.py' | xargs flake8
