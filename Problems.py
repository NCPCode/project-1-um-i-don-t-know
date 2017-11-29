def addAll(n):
	sum = n*(n+1)/2;
	return sum

def exclaim(string):
	return (string + "!")

def sentencesInAString(string):
	charBegin = 0
	charEnd = 1
	sentences = 0
	while True:
		try:
			char = string[charBegin]
		except:
			return sentences
			exit()
		if (char == "." or char == "!" or char == "?"):
			sentences += 1
		charBegin += 1
		charEnd += 1

def frame(stringList):
	maxLength = 0
	for string in stringList:
		if len(string) > maxLength:
			maxLength = len(string)
	for x in range(maxLength + 2):
		print("*", end="")
	print()
	for string in stringList:
		print("*", end="")
		print(string, end="")
		for space in range(maxLength - len(string)):
			print(" ", end="")
		print("*")
	for x in range(maxLength + 2):
		print("*", end="")

def caesarCypher(string, n):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	stringAsNums = []
	for char in range(len(string)):
		try:
			stringAsNums.append(index(string[char]))
		except:
			stringAsNums.append(string[char])
	location = 0
	for char in stringAsNums:
		try:
			char = int(char)
		except:
			char = str(char)
		if char.isdigit():
			stringAsNums[location] += n
			if stringAsNums[location] > 25:
				stringAsNums[location] -= 26
		location += 1
	finalString = []
	for char in stringAsNums:
		try:
			char = int(char)
		except:
			char = str(char)
		if char.isdigit():
			finalString.append(alphabet[char])
		else:
			finalString.append(char)

	return ("".join(finalString))


num = input("Input number >> ")
string = input("Input string >> ")
print(caesarCypher(string, num))




#arrayLength = int(input("How many words? >> "))
#stringArray = []
#for x in range(arrayLength):
#	string = input("Input word >> ")
#	stringArray.append(string)
#frame(stringArray)

#num = input("Input number >> ")
#print(addAll(int(num)))
#exclaim = input("Input string >> ")
#print(exclaim(exclaim))
#stringinput
#print(sentencesInAString("Hello World! My name is Umair. How are you?"))