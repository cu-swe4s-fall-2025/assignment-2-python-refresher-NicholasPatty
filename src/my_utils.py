import sys


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
    # open file and process it line by line -- handle file not found error
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        sys.exit(1)

    # initialize empty array to hold results
    get_column_array = []
    with f:
        header = f.readline().strip().split(',')
        # handle case of result_column not being a valid input
        try:
            if header.index(result_column):
                pass
        except ValueError:
            print(f"Error: The column '{result_column}' is not a valid option "
                  f"for result_column.")
            sys.exit(1)
        # check header to determine index of result_column if it is a string
        if isinstance(result_column, str):
            result_index = header.index(result_column)
        else:
            result_index = result_column
        # build array of results where query_column matches query_value
        for line in f:
            columns = line.strip().split(',')
            # handle case where query_column index is out of range
            if query_column >= len(columns):
                print(f"Error: The query_column index '{query_column}' "
                      f"is out of range.")
                sys.exit(1)
            # if a match is found, process the result_column value
            if columns[query_column] == query_value:
                # append integer value to results, handle non-numeric values
                try:
                    int_value = int(float(columns[result_index]))
                    get_column_array.append(int_value)
                except ValueError:
                    print(f"Warning: Non-numeric value \
                          '{columns[result_index]}' found. Exiting.")
                    sys.exit(1)
    return get_column_array


def mean(values):
    """
    This function calculates the mean of a list of numeric values.

    Parameters:
    ------------
    values (list): A list of numeric values.

    Returns:
    ------------
    float: The mean of the input values.
    """
    if not values:
        return None
    return sum(values) / len(values)


def median(values):
    """
    This function calculates the median of a list of numeric values.

    Parameters:
    ------------
    values (list): A list of numeric values.

    Returns:
    ------------
    float: The median of the input values.
    """
    if not values:
        return None
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return float(sorted_values[mid])


def std_dev(values):
    """
    This function calculates the standard deviation of a list of
    numeric values.

    Parameters:
    ------------
    values (list): A list of numeric values.

    Returns:
    ------------
    float: The standard deviation of the input values.
    """
    if not values:
        return None
    mean_value = mean(values)
    variance = sum((x - mean_value) ** 2 for x in values) / len(values)
    return variance ** 0.5


# main function to test functionality
def main():
    file_name = 'Agrofood_co2_emission.csv'
    country_column = 0
    country = 'Canada'
    fires_column = 'Forest fires'
    fires = get_column(file_name, country_column, country, fires_column)
    mean_fires = mean(fires)
    median_fires = median(fires)
    std_dev_fires = std_dev(fires)

    print(f"CO2 emissions from {fires_column} in {country}: {fires}")
    print(f"Mean: {mean_fires}")
    print(f"Median: {median_fires}")
    print(f"Standard Deviation: {std_dev_fires}")
    print('Test of get_column function complete.')


if __name__ == "__main__":
    main()
