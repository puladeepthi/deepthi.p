l = input("Input a letter of the alphabet: ")

if l in ('a', 'e', 'i', 'o', 'u'):
	print("%s is a vowel." % l)
elif l == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
elif('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'):
	print("%s is a consonant." % l) 
else:
    print("invalid")	
