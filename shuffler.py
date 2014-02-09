#Developed by Leonardo Lee. 1/31/2014.
#The aim of this project was to practice python, but also look at deterministic shuffling techniques.
#My aim was to  create a fast and efficient program that utilized Python's features of lists to produce shuffled output.
#Since all output is inherently ordered in this case, I thought this would be a fun little practice session.

# Goals:
# 1. Create a shuffler that can shuffle any amount of stacks.
# 2. Create a program that determines the original list and the new list and figure out what
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

print shuffleList2 ( capList, 7 )
print shuffleList2 ( numList, 7 )
print shuffleList2 ( singleSuite, 9 )

######################################


#Shuffle any amount of cards
def shuffleN ( listToShuffle, numStack ):
	iteration = 1
	stackNum = 0

	stack = []
	while iteration <= numStack:
		stack.append( [] )
		iteration += 1

	while listToShuffle:
		pass
		#stack[stackNum].append(listToShuffle)
		#if stackNum <= numStack:
			#stackNum += 1

	listToShuffle.extend(stack)
	return listToShuffle

def shuffler( listToShuffle, repeat, numStack):
	timesShuffled = 0
	while timesShuffled <= repeat:
		#This is the code used to make the stacks shuffle.
		#shuffleN( listToShuffle, numStack)
		timesShuffled += 1

	return listToShuffle





