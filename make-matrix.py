f = open("words_alpha_5.txt", "r")
l=[{} for i in range(5)]
#dictionary['a'] of the dictionary at index 0, indictes the number of letter with a in 0th position
for line in f.readlines():
    word=line.strip()
    for i in range(len(word)):
        if(word[i] in l[i]):
            l[i][word[i]]+=1
        else:
            l[i][word[i]]=1
for j in range(5):
    for i in range(ord('a'), ord('z')+1):
        if chr(i) not in l[j].keys():
            l[j][chr(i)]=0
print(l)


