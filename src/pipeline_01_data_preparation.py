import os
import argparse
import yaml
import logging


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    #contains all the things (default path, params, etc)
    args.add_argument('--config', default=None)
    #if we ever choose a diff datasourc, we ca pass it
    args.add_argument("--datasource", default=None)
    
    parsed_args = args.parse_args()
    print(parsed_args.config, parsed_args.datasource)