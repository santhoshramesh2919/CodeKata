char=input()
vo=['a','e','i','o','u']
if char.isalpha():
	if char in vo:
		print("Vowel")
	else:
		print("Consonant")
else:
	print("invalid")
