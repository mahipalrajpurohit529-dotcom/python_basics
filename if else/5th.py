# Q5 Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.

letter = str(input("Enter your letter:"))
letter = letter.lower()

if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
    print("Vowel")
else : print("consonant")
