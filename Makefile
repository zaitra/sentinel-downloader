IMAGE := zaitra/sentinel-downloader

build: files/install-deps.yaml
	docker build --rm -t $(IMAGE) .

run-in-container: build
	docker run -it --rm $(IMAGE) -v /tmp/images:/tmp/images bash -c "sentinel-downloader download"
