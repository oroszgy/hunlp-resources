#!/bin/bash

for i in `seq 0 9`; do wget ftp://ftp.mokk.bme.hu/Language/Hungarian/Crawl/Web2/web2-4p-$i.tar.gz; done

for i in `seq 0 9`; do tar -xvf web2-4p-$i.tar.gz; done
