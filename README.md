[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

my_utils.py includes a get_column() function that reads a CSV file and retrieves values from a specified column (query_column) based on a matching condition in another column (query_value) and returns values from the result_column as a list. my_utils.py also includes mean, median, and std_dev function to analyze
the information output from get_column().

For context, get_column() accepts 4 parameters: file_name, query_column, query_value, and result_column.

file_name accepts the name/location of a file.
query_column accepts the index of the column you want to query.
query_value accepts the value that you're searching for in the query column.
result_column accepts the index OR name of the column that hold the results you're interested in.

As an example, get_column(file_name, query_column, query_value, result_column) could look like: get_column(file_name, country_column, country, fires_column), where the country_column is the index of the column that contains the country, country is name of the country you're interested in searching for in the country_column, and fires_column could contain the column index of the type of fire you're interested in. 

This could return a list containing the carbon emissions from forest fires in the US from each year available in the dataset.

print_fires.py uses argparse to take command-line arguments for get_column() to print the CO2 emissions from a given source (like forest fires in the US), as well as an argument to specify what operation
(mean, median, std_dev) to perform on the output. If no operation is provided, the output from 
get_column() is returned. If an operation is provided, the output of print_fires.py is the result of
the operation.

run.sh runs 3 versions of print_fires.py, one that works and two that give errors.

The testing folder contains unit tests in test_my_utils.py, as well as function tests that use the
stupid simple bash testing fragmework in test_print_fires.sh. The unit tests specifically test the 
functions in my_utils.py, while the function tests confirm that print_fires.py is working properly.

To run the unit tests, a command like the following should suffice:
python3 test_my_utils.py

To run the function tests, a command like the following should suffice:
bash test/func/test_print_fires.sh

Note - provided a small sample file (test_file.csv) for testing.

To run basic, automated tests, I created a tests.yml file in .github/workflows. This file runs when any branch is pushed, and when a pull request is made from the main branch. It runs: unit tests (test_my_utils.py), functional tests (test_print_fires.sh), and style checks. To run style checks, I needed to create an environment.yml file to install pycodestyle.