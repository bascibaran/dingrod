dingrod
========

This role installs the dingrod service to the target system. The dingrod service aids in monitoring an iRODS setup by providing an endpoint that can be pinged through an http GET request. 
This service is intended to make it easier to monitor iRODS using pingdom. 
Currently, dingrod just parses the information from the icommand imiscsvrinfo into a JSON object. 
The actual probing mechanisms live in dingpoker.py so it is pretty straightforward to augment what dingrod probes/parses. 

Requirements
------------

Currently , the dingrod role only supports CentOS 6 systems. When you run this role, it runs under the assumption that it's setting dingrod up on a cent 6 box. 


Role Variables
------------
the role variables you can set are:
dingrod_irods_host: the host where the iRODS system to monitor lives. (default = localhost) 
dingrod_irods_port: the port of your target iRODS system (default = 1247 )
dingrod_irods_zone: the iRODS zone that dingrod is to monitor (default = tempZone)
dingrod_port: NOT TO BE CONFUSED WITH dingrod_irods_port! the port on which dingrod listens for http GET requests. (default = 8080)


Dependencies
------------

This role depends on the CyVerse-Ansible.irods-icommands role from Ansible Galaxy. 

Example Playbook
-------------------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: dingrod
      roles:
         - role: dingrod
	   dingrod_irods_host: irods.yourirods.org
	   dingrod_irods_port: 1247
	   dingrod_irods_zone: tempZone
	   dingrod_poert: 8080

License
-------

BSD

Author Information
------------------
Baran Balkan (bascibaran)
github.com/bascibaran




# dingrod:  iRODS monitoring service for CentOS 6
### INSTALL
Dingrod is packaged as an ansible role. An example playbook using this role is present in this repo, named `playbook.yml`
As you can see in the example playbook, you need root access to your target machine to install dingrod. 
If you don't want to use ansible, you can just grab the contents of the `roles/dingrod/files` directory onto your target machine and  just run the `install.sh` script. 
 However, you must first edit the `roles/dingrod/files/irods_environment.json.template` to create an `irods_environment.json` file that points to your iRODS installation. 
Do not change the iRODS user in the environment JSON, as we want dingrod's actions to be associated w/ the dingrod system user. 

### RUN
dingrod is administrated by `service dingrod`. 
`service dingrod start` starts dingrod
`service dingrod stop`  stops  dingrod
`service dingrod status` tells you whether dingrod is currently online. 

once dingrod is running, you can now ping it using http GET requests! 
curl -X GET dingrodhost:8080
8080 is the default dingrod port, but you can change it easily enough by modifying $DAEMONARGS in `roles/dingrod/files/dingrod`

Happy dinging!
