#!/bin/bash
# Init
FILE="/tmp/out.$$"
GREP="/bin/grep"
REPO_HOME=/home/ctf-admin/lasactf/
# Make sure only root can run our script
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi
#Make temporary directories
mkdir $REPO_HOME/tmp
mkdir $REPO_HOME/tmpb
#Package and reinstall everything
shell_manager package -o $REPO_HOME/tmp $REPO_HOME/Problems
for f in $REPO_HOME/tmp/*
do
    echo "Installing $f..."
    dpkg -i $f
    apt-get install -fy
done
#Package and reinstall the bundle
shell_manager bundle -o $REPO_HOME/tmpb $REPO_HOME/Bundles/lasactf-problems.json
for f in $REPO_HOME/tmpb/*
do
    echo "Installing bundle: $f..."
    dpkg -i $f
    apt-get install -fy
done
#Redeploys all problems listed in the bundle
shell_manager undeploy -b lasactf-problems
shell_manager deploy -b lasactf-problems
rm -rf $REPO_HOME/tmp
rm -rf $REPO_HOME/tmpb
