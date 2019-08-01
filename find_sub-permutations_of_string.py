def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
	
def permute_string(s):
    ''' Generate all permutations in lexicographic order of string `s`

        This algorithm, due to Narayana Pandita, is from
        https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

        To produce the next permutation in lexicographic order of sequence `a`

        1. Find the largest index j such that a[j] < a[j + 1]. If no such index exists, 
        the permutation is the last permutation.
        2. Find the largest index k greater than j such that a[j] < a[k].
        3. Swap the value of a[j] with that of a[k].
        4. Reverse the sequence from a[j + 1] up to and including the final element a[n].
    '''

    a = sorted(s)
    n = len(a) - 1
    while True:
        yield ''.join(a)

        #1. Find the largest index j such that a[j] < a[j + 1]
        for j in range(n-1, -1, -1):
            if a[j] < a[j + 1]:
                break
        else:
            return

        #2. Find the largest index k greater than j such that a[j] < a[k]
        v = a[j]
        for k in range(n, j, -1):
            if v < a[k]:
                break

        #3. Swap the value of a[j] with that of a[k].
        a[j], a[k] = a[k], a[j]

        #4. Reverse the tail of the sequence
        a[j+1:] = a[j+1:][::-1]
	
def substrings(string, min_length = 1):
	string = sortchars(string)
	strs = set()
	length = len(string)
	if length >= min_length:
	    strs = set(permute_string(string))
	if length <= min_length:
	    return strs
	for i in range(length):
		if i > 0 and str[i] == str[i-1]:
			continue
	    substr = string[:i] + string[i+1:]
	    strs = strs.union(substringsrec(substr, min_length))
	return strs

def substringsrec(string, min_length = 1):
	strs = set()
	length = len(string)
	if length >= min_length:
	    strs = set(permute_string(string))
	if length <= min_length:
	    return strs
	for i in range(length):
		if i > 0 and str[i] == str[i-1]:
			continue
	    substr = string[:i] + string[i+1:]
	    strs = strs.union(substringsrec(substr, min_length))
	return strs
	
def sortchars(s):
	chars = list()
	for c in s:
		chars.append(c)
	chars.sort()
	st = ""
	for c in chars:
		st += c
	return st

def sortstrings(strs, min_length = 0, max_length = 2_147_483_647)
	'''	Sorts a list of strings by length first (from shortest to longest), 
		then by lexicographic order.
		
		Essentially, this splits the original list into several lists, each containing strings of 
		a specific length, sorts those lists, and then recombines them into the original list from 
		shortest to longeat.
	'''
	min = max_length; max = min_length
	
	#find minimum and maximum string length
	for s in strs:
		if len(s) < min:
			min = len(s)
		elif len(s) > max:
			max = len(s)
	
	#This dictionary will contain the separated lists
	strdict = dict()
	
	#Initialize a new list for each length.
	for i in range(min, max+1):
		strdict[i] = list()
	
	#Adds each string in the list to the list corresponding to its length.
	for s in strs:
		strdict[len(s)].append(s)
	
	#Now that all of the strings in the list are stored elsewhere according to length, clear the list.
	strs.clear()
	
	for i in range(min, max+1):
		#Sort each sublist of string by lexicographic order (ascending).
		strdict[i].sort()
		#Move all the items in the sublist to the original list.
		strs.extend(strdict[i])
		del strdict[i]
	return
	
def getInt(s = "", errs = "Invalid input. Must input a valid number.", base = 10):
	'''	Tries to get a numeric input from the user, returning the result as an int.
		
		The input requested using the specified message, 
		then is converted to an int according to the specified base (10 by default).
		
		If the input contains characters invalid for the given base, prints the specified error message, 
		then asks for input again using the specified message.
	'''
	inS = input(s).strip()
	if base < 2:
		base = 10
	
	if base <= 10:
		if base == 10:
			while not inS.isdecimal():
				print(errs)
				inS = input(s).strip().replace(',', '')
		else:
			isValid = inS.isdecimal():
			for c in inS:
				if not isValid:
					break
				isValid = int(c) < base
			while not isValid:
				print(errs)
				inS = input(s).strip().replace(',', '')
				isValid = inS.isdecimal()
				for c in inS:
					if not isValid:
						break
					isValid = int(c) < base
	elif base <= 62:
		while not inS.isalnum():
			print(errs)
			inS = input(s).strip()
		if base <= 36:
			inS = inS.upper().strip()
			if base < 36:
				digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
				valid_digits = ''
				for i in range(base):
					valid_digits += digits[i]
				isValid = True
				for c in inS:
					if c not in valid_digits:
						isValid = False
						break
				while not isValid:
					print(errs)
					inS = input(s).upper().strip()
					isValid = inS.isalnum()
					for c in inS:
						if not isValid:
							break
						isValid = c in valid_digits
		elif base < 62:
			digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
			valid_digits = ''
			for i in range(base):
				valid_digits += digits[i]
			isValid = True
			for c in inS:
				if c not in valid_digits:
					isValid = False
					break
			while not isValid:
				print(errs)
				inS = input(s).strip()
				isValid = inS.isalnum()
				for c in inS:
					if isValid = False:
						break
					isValid = c in valid_digits
	
	return int(inS, base)


words = load_words()

while True:
	min_length = getInt("Enter minimum word length: ")

	while min_length < 1:
		print("Invalid number.")
		min_length = input("Enter minimum word length: ")
		
	s = input("Enter string to search: ").strip().lower().replace(' ','')
	if len(s) < min_length:
		print(s + " is too short.")
		continue
	if not s.isalpha():
		print("Invalid string. Must only contain letters a-z")
		continue
	slist = set(substrings(s, min_length))
	if len(slist) == 0:
		print("No results. List empty.")
	else:
		results = list(slist.intersection(words))
		if len(results) == 0:
			print("No results.")
		else:
			print(str(len(results)) + " results found.")
			sortstrings(results)
			for word in results:
				print(word)
		del slist
	
	print()
	repeat = input("Continue? (Y/N)").upper()
	if (repeat[0] != 'Y'):
		break
	print()

print("Program complete")
