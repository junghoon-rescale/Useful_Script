import os
import sys

# Getting a api settings from apiconfig
HOME = os.path.expanduser("~")
PATH_APICONFIG = HOME + "\\.config\\rescale\\apiconfig"
try:
    f = open(PATH_APICONFIG, 'r', encoding='UTF8')
    lines = f.readlines()
    f.close()
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

API_baseurl = lines[1].split('=')[1].rstrip('\n').lstrip().replace("'", "")
API_key = lines[2].split('=')[1].rstrip('\n').lstrip().replace("'", "")
API_token = 'Token ' + API_key
