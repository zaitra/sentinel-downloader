IMAGE := zaitra/sentinel-downloader

build: files/install-deps.yaml
	docker build --rm -t $(IMAGE) .

run-in-container: build
	docker run -it --rm -v /tmp/images:/tmp/images $(IMAGE) bash -c "sentinel-downloader download -c /src/files"
