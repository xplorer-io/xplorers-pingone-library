
SHELL = /bin/bash
SHELLFLAGS = -ex

help:  ## Get help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.PHONY: help

test:  ## Run Python unit tests from src/tests/ directory
	$(info [+] Running Python unit tests...)
	@pipenv run nosetests -v xplorers_pingone/tests
.PHONY: test

test-coverage:  ## Check unit test coverage
	@LOGLEVEL=INFO pipenv run nosetests -v --with-coverage --cover-erase --cover-package=. xplorers_pingone/tests
.PHONY: test-coverage

install: ## run pipenv install
	$(info [+] Running pipenv install...)
	@pipenv install --dev
