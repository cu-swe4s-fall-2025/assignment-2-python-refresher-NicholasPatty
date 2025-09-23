import my_utils
import argparse


# Print CO2 emissions from fires in a given country
def print_fires():
    """
    Print CO2 emissions from forest fires in a given country.
    Uses argparse to get user inputs for file name, country column index,
    country name, and fires column name.
    Calls get_column function from my_utils module to retrieve and print
    the emissions data.
    """
    parser = argparse.ArgumentParser(description='Print CO2 emissions from '
                                     'forest fires in the US.',
                                     prog=my_utils)
    parser.add_argument('--file_name', type=str,
                        help='CSV file name',
                        required=True)
    parser.add_argument('--country_column', type=int,
                        help='Column index for country name of interest',
                        required=True)
    parser.add_argument('--country', type=str,
                        help='Country name of interest',
                        required=True)
    parser.add_argument('--fires_column', type=str,
                        help='Column name for fire type of interest',
                        required=True)

    args = parser.parse_args()
    fires = my_utils.get_column(args.file_name, args.country_column,
                                args.country, args.fires_column)

    return (print(fires))


def main():
    print_fires()


if __name__ == "__main__":
    main()

# initialize inputs to get_column function if not using argparse
# file_name = 'Agrofood_co2_emission.csv'
# country_column = 0
# country = 'United States of America'
# fires_column = 'Forest fires'

# call get_column function to find emissions from forest fires in the US
# fires = my_utils.get_column(file_name, country_column, country, fires_column)
# print(fires)
