#!/bin/bash
# This script bootstraps a virtualenv 
# environement for demos

# Starts
if [ ! -f ./vtenv/bin/python ]
then
    if [ ! -f ./virtualenv.py ]
    then
        echo "Please get a copy of virtualenv.py"
        exit 1
    fi
    python virtualenv.py vtenv
fi
vtenv/bin/pip install -r requirements.txt --download-cache=eggs
if [ ! -d ./vtenv/src/paramiko ];then
    vtenv/bin/pip install -e git://github.com/bearstech/paramiko.git#egg=paramiko || echo "Please install python-dev and retry"
else
    cd vtenv/src/paramiko
    git pull origin master
    cd ../../..
fi
if [ ! -d ./vtenv/src/fabric ];then
    vtenv/bin/pip install -e git://github.com/bearstech/fabric.git@ssh-agent#egg=fabric
else
    cd vtenv/src/fabric
    git pull origin ssh-agent
    cd ../../..
fi
if [ ! -f ./fab ];then
    echo " * Now you can type ./fab prepare to init your dir"
    ln -s vtenv/bin/fab fab
fi
echo " * Done"
exit

