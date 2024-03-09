#!/bin/bash
read -p "Jaggu X=" x1
read -p "Jaggu Y=" y1
read -p "Police X=" x2
read -p "Police Y=" y2
read -p "H=" H
for (( i=1; i<=H; i++))
do
read -p "Police X=" x2
read -p "Police Y=" y2
x=$(bc <<< "$x2 - $x1")
y=$(bc <<< "$y2 - $y1")
dist=$(bc <<< "scale=2; sqrt($x * $x + $y * $y)")      
if (( $(bc <<< "$dist < 2") )); then
    echo "Location Reached"
elif (( $(bc <<< "$x2 > 0 && $y2 > 0") )); 
then
    echo " $dist NE"
elif (( $(bc <<< "$x2 < 0 && $y2 == 0") )); 
then
    echo "$dist W"
elif (( $(bc <<< "$x2 < 0 && $y2 > 0") )); then
    echo "$dist NW"
elif (( $(bc <<< "$x2 == 0 && $y2 < 0") )); 
then
    echo "$dist S"
elif (( $(bc <<< "$x2 == 0 && $y2 > 0") )); then
    echo "$dist N"
elif (( $(bc <<< "$x2 > 0 && $y2 == 0") )); 
then
    echo "$dist E"
elif (( $(bc <<< "$x2 > 0 && $y2 < 0") )); then
    echo "$dist SE"
elif (( $(bc <<< "$x2 < 0 && $y2 < 0") )); then
    echo "$dist SW"
fi
done 
if (( $(bc <<< "$dist >= 2") )); 
then
    echo "Time over"
fi
