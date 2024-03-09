#!/bin/bash
set -f
file="$1"
if [ ! -f "$file" ]; then
    echo "Input file Does Not found."
    exit 1
fi
while IFS= read -r line;
 do
words=($line)
num=${#words[@]}
i=0
j=$((num - 1))
while [ $i -le $j ]; 
do
if [ "${words[i]}" == '#' ] || [ "${words[i]}" == '$' ] || [ "${words[i]}" == '@' ] || [ "${words[i]}" == '*' ]; 
then
     ((i++))
elif [ "${words[j]}" == '#' ] || [ "${words[j]}" == '$' ] || [ "${words[j]}" == '@' ] || [ "${words[j]}" == '*' ]; 
then
    ((j--))
else
	temp="${words[i]}"
	words[i]="${words[j]}"
	words[j]="$temp"
	((i++))
	((j--))
fi
done
echo "${words[@]}"
done < "$file"

