from collections import Counter

def firstRepeated(str):
	
	words = str.split(" ")
	print(words)
	
	dictt = Counter(words)
	print(dictt)
	
	for key in words:
		if(dictt[key]>1):
			print(key)
			break

if __name__ == "__main__":
	str = "Ravi had been saying that he had been there"
	firstRepeated(str)
	
#Core Logic	
"""
def fun(str):
	words = str.split(" ")
	print(words)
	
	for i in range(len(words)):
		for j in range(i+1,len(words)):
			if words[i] == words[j]:
				print(words[i])
				return
		
if __name__ == "__main__":
	str = "Ravi had been saying that he had been there"
	fun(str)"""