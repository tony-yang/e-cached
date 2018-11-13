all: build-container test-py-cached

build-container:
	docker build -t e-cached .

test-py-cached:
	docker run --rm e-cached bash -c "cd py_cached && make test"
