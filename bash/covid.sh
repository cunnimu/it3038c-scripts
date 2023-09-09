#!/bin/bash

#This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json) 
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATH=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalized')
POSINC=$(echo $DATA | jq '.[0].positiveIncrease')
NEGINC=$(echo $DATA | jq '.[0].negativeIncrease')
HOSINC=$(echo $DATA | jq '.[0].hospitalizedIncrease')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative tests, $DEATH deaths, and $HOSPITALIZED hospitalized."
echo "This is an increase of $POSINC positive tests, $NEGINC negative tests, and $HOSINC hospitalized."

