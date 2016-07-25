FROM seabass_icom 
COPY server.py       /.
COPY monitor.sh      /.
COPY initresp.sh     /.
COPY initsquare.sh   /.
COPY dingstart.sh    /.
CMD ["./dingstart.sh"]
