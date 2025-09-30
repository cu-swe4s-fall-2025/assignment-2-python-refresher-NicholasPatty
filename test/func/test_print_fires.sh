# test print fires using Stupid Simple Bash Testing framework

test -e ssshtest || curl -s -O https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

file_name="test/func/test_file.csv"
country_column=0
country="United States of America"
fires_column="Forest fires"
operation="mean"

# test 1: test print_fires mean
run test_my_utils_1 python3 src/print_fires.py \
--file_name "$file_name" \
--country_column "$country_column" \
--country "$country" \
--fires_column "$fires_column" \
--operation "$operation"
assert_in_stdout 1925.8666
assert_exit_code 0

# test 2: test print_fires std_dev
operation="std_dev"
run test_my_utils_2 python3 src/print_fires.py \
--file_name "$file_name" \
--country_column "$country_column" \
--country "$country" \
--fires_column "$fires_column" \
--operation "$operation"
assert_in_stdout 1024.27
assert_exit_code 0

# test 3: test print_fires invalid operation
operation="invalid_op"
run test_my_utils_3 python3 src/print_fires.py \
--file_name "$file_name" \
--country_column "$country_column" \
--country "$country" \
--fires_column "$fires_column" \
--operation "$operation"
assert_in_stderr "invalid choice"
assert_exit_code 2

# test 4: test print_fires non-existent file
file_name="non_existent_file.csv"
operation="mean"
run test_my_utils_4 python3 src/print_fires.py \
--file_name "$file_name" \
--country_column "$country_column" \
--country "$country" \
--fires_column "$fires_column" \
--operation "$operation"
assert_in_stdout "The file '$file_name' was not found."
assert_exit_code 1

# test 5: test print_fires median
file_name="test/func/test_file.csv"
operation="median"
run test_my_utils_5 python3 src/print_fires.py \
--file_name "$file_name" \
--country_column "$country_column" \
--country "$country" \
--fires_column "$fires_column" \
--operation "$operation"
assert_in_stdout 1555
assert_exit_code 0

# test 6: test print_fires with invalid result_column
fires_column="Invalid Column"
operation="mean"
run test_my_utils_6 python3 src/print_fires.py \
--file_name "$file_name" \
--country_column "$country_column" \
--country "$country" \
--fires_column "$fires_column" \
--operation "$operation"
assert_in_stdout "Error: The column '$fires_column' is not a valid option"
assert_exit_code 1

# test 7: test print_fires with invalid country value
fires_column="Forest fires"
country="NonExistentCountry"
operation="mean"
run test_my_utils_7 python3 src/print_fires.py \
--file_name "$file_name" \
--country_column "$country_column" \
--country "$country" \
--fires_column "$fires_column" \
--operation "$operation"
assert_in_stdout "None"
assert_exit_code 0