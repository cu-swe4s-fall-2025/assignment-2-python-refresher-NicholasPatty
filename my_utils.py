def get_column(file_name, query_column, query_value, result_column=1):
    """
    This function reads a CSV file and retrieves values from a specified column
    (query_column) based on a matching condition in another column
    (query_value) and returns values from the result_column.

    Parameters:
    ------------
    file_name (str): The name of the CSV file to read.
    query_column (int): The index of the column to search for the query_value.
    query_value (str): The value to search for in the query_column.
    result_column (int or str): The index or name of the column from which to
    retrieve values when a match is found. Defaults to 1.

    Returns:
    ------------
    list: A list of values from the result_column where the query_column
    matches the query_value.
    """
    import sys

    get_column_array = []

    # open file and process it line by line -- handle file not found error
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)

    with f:

        header = f.readline().strip().split(',')
        # check file header to determine index of result_column is a string
        # if result_column is an integer, use it directly as the index
        if isinstance(result_column, str):
            result_index = header.index(result_column)
        else:
            result_index = result_column

        # f.seek(0) # reset file pointer to the beginning of the file

        # for each line, split the line into an array
        for line in f:
            columns = line.strip().split(',')
            # check to see if the query_column position matches the query_value
            # when the above condition is met, add the value in the
            # result_column position into the array
            if columns[query_column] == query_value:
                get_column_array.append(columns[result_index])

    # return the array storing the column values
    return get_column_array

# uncomment below to test the function directly

# file_name = 'Agrofood_co2_emissions.csv'
# country_column = 0
# country = 'United States of America'
# fires_column = 'Forest fires'

# print(get_column(file_name, country_column, country, fires_column))
