FROM seabass_icom 
EXPOSE 20500
RUN yum install -y expect
COPY server.py  /.
COPY monitor.sh /.
COPY initspect  /.
COPY creds.sh   /.
COPY dingrod.sh /. 
ENTRYPOINT ["bash","./dingrod.sh"]
