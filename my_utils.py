def get_column(file_name, query_column, query_value, result_column=1):
    # open file and process it line by line
    get_column_array = []
    with open(file_name, 'r') as file:

        # check file header to determine index of result_column if it is a string
        header = file.readline().strip().split(',')
        # if result_column is an integer, use it directly as the index
        if isinstance(result_column, str):
            result_index = header.index(result_column)
        else:
            result_index = result_column 
        file.seek(0) # reset file pointer to the beginning of the file   
        
        # for each line, split the line into an array
        for line in file:
            columns = line.strip().split(',')
            # check to see if the query_column position matches the query_value
            # when the above condition is met, add the value in the result_column position into the array
            if columns[query_column] == query_value:
                get_column_array.append(columns[result_index])
    
    # return the array storing the column values
    return get_column_array

#index = 'Forest fires'
#print(get_column('Agrofood_co2_emission.csv', 0, 'Afghanistan', index))