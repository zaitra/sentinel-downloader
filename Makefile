IMAGE := docker.io/zaitra/sentinel-downloader
TEST_IMAGE := docker.io/zaitra/sentinel-downloader-tests
TEST_TARGET := ./tests/unit ./tests/integration/

build: files/install-deps.yaml
	docker build --rm -t $(IMAGE) .

run-in-container: build
	docker run -it --rm -v /tmp/images:/tmp/images $(IMAGE) bash -c "sentinel-downloader download -c /src/.sd.yaml"

test-image: build
	docker build --rm -t $(TEST_IMAGE) -f Dockerfile.tests .

check:
	find . -name "*.pyc" -exec rm {} \;
	PYTHONPATH=$(CURDIR) PYTHONDONTWRITEBYTECODE=1 python3 -m pytest --color=yes --verbose --showlocals --cov=sentinel_downloader --cov-report=term-missing $(TEST_TARGET)

check-in-container: test-image
	docker run --rm \
	-v $(CURDIR):/src \
	-w /src \
	--security-opt label=disable \
	$(TEST_IMAGE) make check
