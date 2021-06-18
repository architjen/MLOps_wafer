import os
import argparse
import yaml
import logging

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_params(config_path)
    print(config)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    default_config_path = os.path.join('config', 'params.yaml')
    #contains all the things (default path, params, etc)
    args.add_argument('--config', default=default_config_path)
    #if we ever choose a diff datasourc, we ca pass it
    args.add_argument("--datasource", default=None)
    
    parsed_args = args.parse_args()
    main(config_path=parsed_args.config, datasource=parsed_args.datasource)
