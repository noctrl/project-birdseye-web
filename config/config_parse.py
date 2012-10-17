import json
import os

__author__ = 'mjholler'

def config_parse():
    configs = None
    config_files = [item for item in os.listdir('.') if os.path.isfile(item) and item.endswith('.cfg')]

    for filename in files:
        f = open(filename, 'r')
        configs[filename] = json.loads(f.read())
        f.close()

    return configs

config = config_parse()

