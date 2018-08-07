# Example Repo

This repo contains the following files:

- `some-analysis.ipynb` - A sample Jupyter Notebook.
- `raw_python_file.py` - An example python file which scores a 10/10 via pylint. 
- `transform_data.py` - A python file which transforms the data in the `/data` folder and places it in the `/output` folder.
- `Makefile` - This Makefile can be used to transform the data using 1 shell command. Run `make` while in this directory to produce the output csv file.

In order to lint the python file, run the following command `pylint *.py`