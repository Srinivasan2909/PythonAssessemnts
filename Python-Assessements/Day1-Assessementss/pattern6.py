word=input("Enter the word")
for i in range(0,len(word)):
    print(" "*(len(word)-i),word[0:i+1])
