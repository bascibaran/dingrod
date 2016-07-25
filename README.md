# dingrod:  pingrod as docker service
service to aid iRODS monitoring with pingdom


this service is intended to make it ease to monitor iRODS using pingdom 
without cluttering iRODS' logs with the undigestable GET requests sent by pingdom. 

pingrod should be running on a machine that has icommands set up and the iinit set up
to direct the icommands toward the iRODS set up that you intend to monitor. 

pingrod listens on port 20500 and returns status 200 if iRODS is up, and 503 if iRODS is down. 




