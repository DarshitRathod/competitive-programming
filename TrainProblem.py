#how many minimum platforms required to serve given time table


arrival = [900,940,950,1100,1500,1800]
departure = [910,1120,1130,1200,1900,2000]


arrival.sort()
departure.sort()

max_paltform = 1
needed_paltform = 1


i = 1
j = 0

while( i != int(len(arrival)-1) and j != int(len(departure)-1) ):
	if arrival[i] < departure[j]:
		max_paltform =  max_paltform + 1
		i+=1
	else:
		max_paltform =  max_paltform - 1
		j+=1
	if max_paltform > needed_paltform:
		needed_paltform = max_paltform
	
print(needed_paltform)
	