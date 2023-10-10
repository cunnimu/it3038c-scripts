#uncomment for demo
#create files
#touch {a..e}.txt
#show files
#ls *.txt

#for every text file:

for file in *.txt;
do
	filename=${1}
	newname="${filename}$((++i)).txt"
	#Rename files
	printf '%s-->%s\n' ${file} ${newname}
	mv "$file" "$newname"
	
done

#uncomment to show results
#ls *.txt
