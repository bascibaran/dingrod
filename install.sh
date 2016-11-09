#!/bin/bash

# this script installs dingrod. 
echo "+++++++++++++++++++++\n+INSTALLING DINGROD!+\n+++++++++++++++++++++\n"

echo  "> creating dingrod habitat @ /var/lib/dingrod\n" 
mkdir /var/lib/dingrod
echo  "> creating dingrod system user\n"
adduser --system --home /var/lib/dingrod dingrod
chown  -R dingrod /var/lib/dingrod 
echo  "> moving payload to habitat\n"
cp dingrod.py   /var/lib/dingrod/. 
cp dingpoker.py /var/lib/dingrod/.

if [[ -e irods_environment.json ]]
then
  echo "> moving irods environment .json file\n"
  mkdir /var/lib/dingrod/.irods
  cp irods_environment.json /var/lib/dingrod/.irods/.
else
  echo "> irods_environment.json does not exist!\nUse the template!\n"
  exit 1
fi


echo "> changing ownership of dingrod materials to the system user.\n"

chown dingrod /var/lib/dingrod/*

echo "> placing service script in /etc/init.d\n"
cp dingrod /etc/init.d/.
chkconfig --add dingrod

echo "> installing iCommands in dingrod user space.\n"

mv irods-icommands-4.1.9-centos-6.installer /var/lib/dingrod/icommands
su - dingrod << 'EOF'
yes "" | sh icommands 
. ~/.bashrc
exit
'EOF'
