import my_utils

# initialize inputs to get_column function
file_name = 'Agrofood_co2_emission.csv'
country_column = 0
country = 'United States of America'
fires_column = 'Forest fires'

# call get_column function to find forest fires in the United States
fires = my_utils.get_column(file_name, country_column, country, fires_column)
print(fires)