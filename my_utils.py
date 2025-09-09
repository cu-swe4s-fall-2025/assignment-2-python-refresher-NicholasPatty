def get_column(file_name, query_column, query_value, result_column):
    # open file and process it line by line
    get_column_array = []
    with open(file_name, 'r') as file:
        # for each line, split the line into an array
        for line in file:
            columns = line.strip().split(',')
            # check to see if the query_column position matches the query_value
            # when the above condition is met, add the value in the result_column position into the array
            if columns[query_column] == query_value:
                get_column_array.append(columns[result_column])
    # return the array storing the column values
    return get_column_array

#print(get_column('Agrofood_co2_emission.csv', 0, 'Afghanistan', 3))