Role Name
========

This role installs the dingrod service to the target system. The dingrod service aids in monitoring an iRODS setup by providing an endpoint that can be pinged through an http GET request. 

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
