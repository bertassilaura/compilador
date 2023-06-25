# A versão do python utilizada foi 3.8.10
	
.PHONY: run clean
setup:
	pip3 install -r requirements.txt

clean:
	rm -rf __pycache__

run:
	python3 main.py


