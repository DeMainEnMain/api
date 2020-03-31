# Local settings that are environment dependent and 
# also things you do not want to see appearing in the repo like 
# keys
# This file is a template and has to be put in the settings directory of
# the django app, i.e. api/src/api/settings and should not be pushed on
# the repo

NETWORK_NAME = "eusko"
DATABASE_NAME = "api"
DATABASE_USER = "api"
DATABASE_PASSWORD = "api"
DATABASE_HOST = "localhost"

API_PUBLIC_URL = "http://sauvagnon.acacs.org/"
DOLIBARR_PUBLIC_URL = "http://sauvagnon.acacs.org/"
CYCLOS_PUBLIC_URL = 'http://sauvagnon.acacs.org:8080/cyclos/'
BDC_PUBLIC_URL = "http://cde.acacs.org"
GI_PUBLIC_URL = "http://gi.acacs.org"
CEL_PUBLIC_URL = ""

CYCLOS_CONSTANT_FILE = "/home/matthieu/api/etc/cyclos/cyclos_constants.yml"
CYCLOS_NAMES_FILE = "/home/matthieu/api/etc/cyclos/cyclos_constants_accounts.yml"
DOLIBARR_CONSTANT_FILE = "/home/matthieu/api/etc/dolibarr/dolibarr_constants.yml"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kci-=2)4_qh#a3+k#xt!0)_t838t9zjcjpl#&09(&2&kftskr('

