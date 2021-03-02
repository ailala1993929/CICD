#!/bin/bash
#注意区分$ "" '' `` $()
echo `date +"%Y-%m-%d %H:%M:%S"`
echo `who | wc -l`
echo $(who | wc -l)

sum=0
sum1=0
for j in {1..100};do
  sum1=$[$sum1+$j]
done
echo $sum1


for i in {1..100};do
  if [[ $i -lt 100 ]]; then
      printf $i+
  else
      printf $i=
  fi
  sum=$[sum+$i]
done
echo $sum
