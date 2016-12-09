# dingrod:  iRODS monitoring service for CentOS 6
This service is intended to make it easier to monitor iRODS using pingdom. 
Currently, dingrod just parses the information from the icommand imiscsvrinfo into a JSON object. 
The actual probing mechanisms live in dingpoker.py so it is pretty straightforward to augment what dingrod probes/parses. 

## HOW TO INSTALL/RUN DINGROD. 


### INSTALL
Get the payload directory. 

The payload directory contains all the files necessary to install/run dingrod. However, you must first edit the irods_environment.json.template to create an irods_environment.json file that points to your iRODS installation. 
Do not change the iRODS user in the environment JSON, as we want dingrod's actions to be associated w/ the dingrod system user. 

So , once you have your environment JSON all set up, run the script, install.sh. 
this installs the service, and the iCommands that the service uses to probe your iRODS installation. 

You must now source your .bashrc file! This is easily done with the command `. ~/.bashrc`

### RUN
dingrod is administrated by `service dingrod`. 
`service dingrod start` starts dingrod
`service dingrod stop`  stops  dingrod
`service dingrod status` tells you whether dingrod is currently online. 

once dingrod is running, you can now ping it using http GET requests! 
curl -X GET dingrodhost:8080
8080 is the default dingrod port, but you can change it easily enough by modifying $DAEMONARGS in `payload/dingrod`

Happy dinging!
