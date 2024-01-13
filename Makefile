ifeq ($(OS), Windows_NT)
run:
	python src/__main__.py

build: setup.py
	python setup.py build bdist_wheel

clean:
	if exist "./build" rd /s /q build
	if exist "./dist" rd /s /q dist
	if exist "./pdf_merger.egg-info" rd /s /q pdf_merger.egg-info
else
run:
	python3 src/__main__.py

build: setup.py
	python3 setup.py build bdist_wheel

clean:
	rm -rf build
	rm -rf dist
	rm -rf pdf_merger.egg-info
endif