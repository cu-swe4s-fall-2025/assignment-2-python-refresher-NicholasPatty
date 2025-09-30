#!/bin/bash

echo "running print_fires.py"

python_script=print_fires.py
file_name="Agrofood_co2_emission.csv"
country_column=0
country="United States of America"
fires_column="Forest fires"

echo "-----------------------------------"
echo "example 1 (successful execution expected):"

python3 "$python_script" \
--file_name "$file_name" \
--country_column $country_column \
--country "$country" \
--fires_column "$fires_column"

echo "-----------------------------------"
echo "example 2 (error expected):" 
file_name='fake.csv'

python3 "$python_script" \
--file_name "$file_name" \
--country_column $country_column \
--country "$country" \
--fires_column "$fires_column"

echo "-----------------------------------"
echo "example 3 (error expected):"
file_name="Agrofood_co2_emission.csv"
fires_column="oil fire"

python3 "$python_script" \
--file_name "$file_name" \
--country_column $country_column \
--country "$country" \
--fires_column "$fires_column"

echo "done"

chmod -x run.sh