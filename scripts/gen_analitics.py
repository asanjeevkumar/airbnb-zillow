import argparse
from os import path

import pandas as pd

SOURCE_DATA_NAME = "source_data"
AIRBNB_FILE_NAME = "listing.csv"
ZILLOW_FILE_NAME = "Zip_Zhvi_2bedroom.csv"


def get_file_wrapper():
    pass


def main(args):
    airbnb_df = pd.read_csv(args.airbnb_file_loc)
    zillow_df = pd.read_csv(args.zillow_file_loc)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process real estate data')
    parser.add_argument("--airbnb-file-loc",
                        type=argparse.FileType('r'),
                        help="file location for airbnd data csv")
    parser.add_argument("--zillow-file-loc",
                        type=argparse.FileType('r'),
                        help="file location for airbnd data csv")
    main(parser.parse_args())
