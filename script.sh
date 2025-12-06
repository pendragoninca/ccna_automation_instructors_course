#! /bin/bash
file='out.txt'
while read line;
do
 echo $line
done < $file