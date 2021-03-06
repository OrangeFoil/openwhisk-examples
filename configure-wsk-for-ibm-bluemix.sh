#!/bin/bash
# copy the credentials for IBM Cloud Functions to the regular OpenWhisk CLI
set -e

APIHOST=$(bluemix cloud-functions property get --apihost | cut -f 3)
AUTH=$(bluemix cloud-functions property get --auth | cut -f 3)

wsk property set --apihost $APIHOST
wsk property set --auth $AUTH
