
triangleList=[]
for num in range (1,1000):
	triangleList.append((num*(num-1)/2))

count =0
with open("euler42.txt") as textFile:
	for word in textFile:
		word = word.strip('"')
		word= word.strip("\n")
		
		word = word[0:len(word)-1]
		#print word
		sum=0
		for character in word: 
			sum+= ord(character) - 64
			
		if sum in triangleList: 
			count+=1
			
print count