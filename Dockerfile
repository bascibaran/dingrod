FROM seabass_icom 
COPY server.py /.
COPY monitor.sh /.
COPY initresp.sh /.
COPY initsquare.sh /.
RUN /bin/bash -c "./initsquare.sh"
CMD ["python","./server.py"]
