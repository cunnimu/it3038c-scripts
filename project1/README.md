# Project 1
This is a simple script to rename a group of related files with the same name plus a sequential number. I sometimes have files that are sequential but have the same name. Renaming them individually takes time and that could be automated instead. It is a simple demonstration and could be edited or expanded on for more interesting file renaming.
## Use
```
./rename.sh [NewFileName]
```
Call the script with the desired new file name.
```
for file in *.txt;

do

    filename=${1}

    newname="${filename}$((++i)).txt"

    #Rename files

    printf '%s-->%s\n' ${file} ${newname}

    mv "$file" "$newname"

done
```
Script can be changed for other formats or specific files by editing:
```
for file in [SpecificFileName]*.csv
```
And then change the output:
```
newname = "${filename}$((++i))".csv
```
## Demo
```
#uncomment for demo

#create files

#touch {a..e}.txt

#show files

#ls *.txt
```
Included is a test/demonstration of the script. When uncommented, this creates 5 text files. It then renames the files. The purpose of this is to demonstrate the renaming with the sequential numbers. Comment out/remove the indicated lines to use the script without this demo.
