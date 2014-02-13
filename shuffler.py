#Developed by Leonardo Lee. 1/31/2014.
#The aim of this project was to practice python, but also look at deterministic shuffling techniques.
#My aim was to  create a fast and efficient program that utilized Python's features of lists to produce shuffled output.
#Since all output is inherently ordered in this case, I thought this would be a fun little practice session.

# Goals:
# 1. Create a shuffler that can shuffle any amount of stacks. **Complete**
# 1.a. Human Error, account for human error that can influence the outcome.
# 2. Create a program that determines the original list and the new list and figure out what.
# 3. Create a program that can store this information and put it in a .js data visualization tool.

#Variables. An empty list and test lists.
capList = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
lowList = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
numList = [1,2,3,4,5,6,7,8,9,0]
deckOfCards = ['AoH', '2oH', '3oH', '4oH', '5oH','6oH','7oH','8oH','9oH','10oH','JoH','QoH','KoH','AoS', '2oS', '3oS', '4oS', '5oS','6oS','7oS','8oS','9oS','10oS','JoS','QoS','KoS','AoD', '2oD', '3oD', '4oD', '5oD','6oD','7oD','8oD','9oD','10oD','JoD','QoD','KoD','AoC', '2oC', '3oC', '4oC', '5oC','6oC','7oC','8oC','9oC','10oC','JoC','QoC','KoC']
singleSuite = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
listToShuffle = []

######################################
#A fast implementation of a shuffler that shuffles with 2 stacks. 1/31/2014
def shuffleTwice ( listToShuffle ):
	iteration = 1
	stackA = []
	stackB = []

	while listToShuffle:
		if iteration % 2 == 0:
			stackB.append( listToShuffle.pop() )
		else :
			stackA.append( listToShuffle.pop() )

		iteration += 1

	listToShuffle = stackA + stackB
	return listToShuffle

#Shuffles two stacks only.
def shuffleList2 ( listToShuffle, repeat ):
	timesShuffled = 0
	while timesShuffled <= repeat:
		listToShuffle = shuffleTwice ( listToShuffle )
		timesShuffled += 1

	return listToShuffle

######################################
######################################

#Shuffle any amount of cards Finished 2-10-14
def shuffleN ( listToShuffle, stackCount ):
	iteration = 1
	stack = []

	#Generates Stacks to the about in stackCount.
	while iteration <= stackCount:
		stack.append( [] )
		iteration += 1

	#Pops from listToShuffle and populates the subStacks.
	while listToShuffle:
		for subStack in stack:
			if listToShuffle:
				subStack.append( listToShuffle.pop() )

	#Concatenates from the subStacks back to listToShuffle to return the shuffled list.
	for subStack in stack:
		listToShuffle += subStack

	return listToShuffle

#Takes the inputs of how many times the shuffler repeats the process and such.
def shuffler( listToShuffle, repeat, stackCount ):
	timesShuffled = 0
	while timesShuffled <= repeat:
		#shuffleN is the code used to make the stacks shuffle.
		shuffleN( listToShuffle, stackCount )
		timesShuffled += 1

	return listToShuffle


########################################
########################################
#Human Touch: This part of the code is to add human error and to add randomization in how stacks are shuffled. This should try to use the code from above to give it a human element.
#Taking ideas from exchange shuffle, the best way to approach this would be to 'pretend' to add another card to a stack that we just placed a card in. In human randomness terms I believe this would be the best formulation.
#Obviously this formulation is arbitrary as human error is not as clean as this suggests, but I hope that this would represent abstractly the chance of an error occuring in the shuffle of a deck.

def shuffleError(stackCount):
	errorChance = random.randint(0, stackCount + 1)

	if stackCount == errorChance:
		stackCount -= 1

	return stackCount




########################################
########################################
#Compares lists.
#I am designing this so that you would have to assign listToShuffle where the 

def compareChange():
	pass
	#Counts Differences.
	#Gives a list of the elements that are different than the original list.


########################################
#Testing area
#print "Original Shuffler program"
#print shuffleList2 ( capList, 7 )

print "New shuffler program"
print shuffler( capList, 9, 3 )


#print shuffleN( capList, 2)







