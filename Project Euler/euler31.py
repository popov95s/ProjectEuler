
sum=1
for onePound in range(0,2):
	for fiftyP in range (0,4):
		for twentyP in range(0,10):
			for tenP in range (0,20):
				for fiveP in range (0,40):
					for twoP in range (0,100):
						for oneP in range (0,200):
							if (onePound*100 + fiftyP*50 + twentyP*20 + tenP*10 + fiveP*5+twoP*2+oneP) == 200:
								sum+=1
								
print sum