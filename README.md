[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_G_SdF8U)
# python-refresher

I updated my_utils.py to include a get_column() function that reads a CSV file and retrieves values from a specified column (query_column) based on a matching condition in another column (query_value) and returns values from the result_column as a list. The result_column parameter can now be a string matching a column value, or an integer (the default is 1).

For context, my_utils accepts 4 parameters: file_name, query_column, query_value, and result_column.

file_name accepts the name/location of a file.
query_column accepts the index of the column you want to query.
query_value accepts the value that you're searching for in the query column.
result_column accepts the index OR name of the column that hold the results you're interested in.

As an example, get_column(file_name, query_column, query_value, result_column) could look like: get_column(file_name, country_column, country, fires_column), where the country_column is the index of the column that contains the country, country is name of the country you're interested in searching for in the country_column, and fires_column could contain the column index of the type of fire you're interested in. 

This could return a list containing the carbon emissions from forest fires in the US from each year available in the dataset.

print_fires.py uses get_column() to print the number of forest fires in the US.

run.sh runs the print_fires.py file.