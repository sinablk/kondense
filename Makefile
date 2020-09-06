MODULE := kondense
BLUE='\033[0;34m'
NC='033[0m' # no color


test:
	@pytest

lint:
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8

clean:
	rm -rf .pytest_cache .coverage coverage.xml *.egg-info __pycache__