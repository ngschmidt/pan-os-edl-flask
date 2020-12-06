#!/usr/bin/python3
# Execution for PAN EDL Flask
# Nicholas Schmidt
# 06 Dec 2020

# Command line parsing imports
import argparse

# Import IronStrataLiburatt
from IronStrataLiburatt import IronStrataLiburatt

# Arguments Parsing
parser = argparse.ArgumentParser(description='Process YAML Inputs')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Output Verbosity')
parser.add_argument('--ip', action='store_true', default=False, help='Make the output an IP EDL')
parser.add_argument('--fqdn', action='store_true', default=False, help='Make the output a FQDN EDL')
parser.add_argument('--url', action='store_true', default=False, help='Make the output a URL EDL')
parser.add_argument('url', help='Data Source URL')
args = parser.parse_args()

pan_edl = IronStrataLiburatt(args.url, args.verbosity)
