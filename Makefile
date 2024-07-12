format-all:
	isort . --skip setup.py && black --exclude setup.py .

install-all:
	poetry install -E all --with dev --with test --with docs

update-all:
	poetry update && \
		poetry export --without-hashes -E all -f requirements.txt --output requirements.txt