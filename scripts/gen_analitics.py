import argparse
from os import path

import pandas as pd

import utils

SOURCE_DATA_NAME = "source_data"
AIRBNB_FILE_NAME = "listings.csv"
ZILLOW_FILE_NAME = "Zip_Zhvi_2bedroom.csv"


def parse_args():
    parser = argparse.ArgumentParser(description='Process real estate data')
    parser.add_argument("--airbnb-file-loc",
                        type=argparse.FileType('r'),
                        help="file location for airbnd data csv")
    parser.add_argument("--zillow-file-loc",
                        type=argparse.FileType('r'),
                        help="file location for zillow data csv")

    return parser.parse_args()


def main():
    dir_path = path.dirname(path.realpath(__file__))
    if args.airbnb_file_loc:
        airbnb_df = pd.read_csv(args.airbnb_file_loc, encoding='latin-1')
    else:
        airbnb_df = pd.read_csv(
            path.join(dir_path, '..', SOURCE_DATA_NAME, AIRBNB_FILE_NAME),
            encoding='latin-1')

    if args.zillow_file_loc:
        zillow_df = pd.read_csv(args.zillow_file_loc, encoding='latin-1')
    else:
        zillow_df = pd.read_csv(
            path.join(dir_path, '..', SOURCE_DATA_NAME, ZILLOW_FILE_NAME),
            encoding='latin-1'
        )
    utils.create_plots(airbnb_df, zillow_df)
    # ax = airbnb_df.plot.barh(x="bedrooms", y="price")


if __name__ == '__main__':
    args = parse_args()
    main()
