"""
======================================================================
Homework 4

Released: 2017-10-17
Due Date: 2017-10-24, EoD

They told me I could be anything...
...so I became void*.
======================================================================
"""

# is unique
def is_unique(word):
    arr = [0] * 26
    for i in range(0,len(word)):
        if (ord(word[i].lower()) - ord('a')) >= 0 and (ord(word[i].lower()) - ord('a')) < 26:
            arr[ord(word[i].lower()) - ord('a')] += 1
    for i in range(0,26):
        if arr[i] > 1:
            return False
    return True
    """
	Given a string, return true if the string's characters are unique.

	Args:
		(str) word: the input string.
	
	Returns:
		(bool) True if the string's characters are unique, False otherwise.
	"""
# Counting Anagrams
def count_anagrams(arr, uniq):
    count = 0
    uniq = "".join(sorted(uniq))
    for s in arr:
        s = "".join(sorted(s))
        if s.lower() == uniq.lower():
            count += 1
    return count
"""
	Given a list of strings, returns the exact anagrams of uniq in the list.
	
	Args:
		(List[str]) arr:  a list of strings.
		(str)       uniq: a string.
	
	Returns:
		(int) the number of anagrams of uniq in arr.
        """
# Anagram of Palindrome
def anagram_of_palindrome(word):
    count = 0
    a = [0] * 26
    for i in range(0,len(word)):
        if (ord(word[i].lower()) - ord('a')) >= 0 and (ord(word[i].lower()) - ord('a')) < 26:
            a[ord(word[i].lower()) - ord('a')] += 1
    for i in range(0,len(a)):
        if a[i] % 2 == 1:
            count += 1
    if count > 1:
        return False
    return True
"""
	Given a string, return true if the string is an anagram of a palindrome.

	Args:
		(str) word: the input string
	
	Returns:
		(bool) whether or not the input string is an anagram of a palindrome."""
# Reverse Dictionary
def reverse_dictionary(d):
    mydict = {}
    for key, value in d.items():
        mydict[value] = key
    return mydict
    """
	Given a dictionary d, reverse its keys and values.
	The values will all be unique.
	
	Args:
		(Dict[Any, Any]) d: the dictionary.

	Returns:
		(Dict[Any, Any]) a dictionary where the keys of d are its values and vice-versa. 
	"""
# Alphabet Finder
def alphabet_finder(sentence):
    Arr = []
    for i in range(0,26):
        Arr.append(0)
    for i in range(0,len(sentence)):
        if (ord(sentence[i].lower()) - ord('a')) >= 0 and (ord(sentence[i].lower()) - ord('a')) < 26:
            if Arr[ord(sentence[i].lower()) - ord('a')] == 0:
                Arr[ord(sentence[i].lower()) - ord('a')] = 1
        if sum(Arr) == 26:
            return sentence[:i+1]
    return None
    """
	Given a string, returns the shortest substring that:
		1. starts from the beginning of the string
		2. contains all the letters of the alphabet (case insensitive)
	If this is never true, return None.
	
	Args:
		(str) sentence: the input string

	Returns:
		(str) the shortest substring of sentence that satisfies both (1) and (2).
	"""
def happyCheck(n):
    #bool = False
    arr = [int(i) for i in str(n)]
    newNum = 0
    for i in range(0, len(arr)):
        newNum += arr[i]**2
    if newNum == 1:
        return True
    else:
        if newNum == 4:
            return False
        else:
            return happyCheck(newNum)
#return bool
# Happy Numbers
def happy_numbers(n):
    count = 0
    for j in range (1, n + 1):
        if (happyCheck(j)):
            count += 1
    return count
"""
	Given n, return the number of happy numbers between 1 and n (inclusive).
	https://en.wikipedia.org/wiki/Happy_number

	Args:
		(int) n: the upper bound.
	
	Returns:
		(int) the number of happy numbers from 1 to n.
	"""
