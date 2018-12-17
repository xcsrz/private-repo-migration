

run:
	python run.py

config:
	pip install -r requirements.txt

clean:
	rm -rf repos/*
	touch repos/.gitkeep
