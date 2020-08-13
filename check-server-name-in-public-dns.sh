#!/bin/bash

#declare -a arr=()
declare -a arr=("api.mycompany.ru")


for i in "${arr[@]}"
do
   echo "-------------------------------------"
   echo "$i"
   nslookup "$i" 8.8.8.8
   echo "-------------------------------------"
done
