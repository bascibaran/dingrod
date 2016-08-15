FROM seabass_icom 
EXPOSE 20500
COPY server.py  /.
COPY dingpoker.py /.
COPY irods_environment.json /root/.irods/irods_environment.json
ENTRYPOINT ["python","./server.py"]
