all: clean processdata 
	echo 'Done running all commands'
processdata:
	python transform_data.py 
clean: 
	rm output/converted-data.csv
