import os, sys

# Getting a api settings from apiconfig
homepath = os.path.expanduser("~")
setting_file = homepath + "\\.config\\rescale\\apiconfig"
try:
    f = open(setting_file, 'r', encoding='UTF8')
    lines = f.readlines()
    f.close()
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

API_baseurl = lines[1].split('=')[1].rstrip('\n').lstrip().replace("'", "")
API_key = lines[2].split('=')[1].rstrip('\n').lstrip().replace("'", "")
API_token = 'Token ' + apikey
