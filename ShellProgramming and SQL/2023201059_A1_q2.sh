#!/bin/bash
read -p "N=" N
echo "prices"
read -a prices
max=0
i=0
j=1
while (($j < $N))
do
 if [ ${prices[j]} -ge ${prices[i]} ]
 then
profit=$(( ${prices[j]} - ${prices[i]} ))
	if (($profit > $max)) then
	    max=$profit
	fi
j=$((j+1))
else
i=$j
j=$((j+1))
fi
done
echo "Maximum Profit: $max"


