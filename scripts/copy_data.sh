#!/usr/bin/env bash

datafiles=("1920" "1819" "1718" "1617" "1516" "1415" "1314"
"1213" "1112" "1011" "0910" "0809" "0708" "0607"
"0506" "0405" "0304" "0203" "0102" "0001" "9900"
"9899" "9798" "9697" "9596" "9495" "9394" )


for val in ${datafiles[*]}; do
     `curl https://www.football-data.co.uk/mmz4281/$val/E0.csv > $val.csv`
done
