#!/bin/bash
# This script bootstraps a virtualenv 
# environement for demos
set -e
# Starts
if [ ! -f ./vtenv/bin/python ]
then
    python virtualenv.py vtenv
    rm virtualenv.pyc
fi
vtenv/bin/pip install -r requirements.txt --download-cache=eggs
# Activate virtualenv compat on our project
echo " * Activate virtualenv on project"
sed -i "s/# activate_this =/activate_this =/g" sample_project/manage.py sample_project/deploy/deploy.wsgi
sed -i "s/# execfile/execfile/g" sample_project/manage.py sample_project/deploy/deploy.wsgi
echo " * Done"
exit

