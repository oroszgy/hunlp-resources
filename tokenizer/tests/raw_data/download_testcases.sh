#!/usr/bin/env bash

wget https://github.com/dlt-rilmta/quntoken/archive/master.zip
unzip master.zip
mv ./quntoken-master/test/test_*.txt ./
rm -rf master.zip
rm -rf quntoken-master
