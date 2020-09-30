Input = input("Enter a phrase: ").upper()	#Converting lowercases in input into uppercases.

l = list(Input)	#making list

l.sort()	#just use the sort method

for i in l:	#looping thru the list

	print(i, end = "")	#printing the letters in a single line.

print()	