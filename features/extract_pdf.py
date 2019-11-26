word_dictionary={}
def tester(inp,ind):
    
    for text in inp.split():
        if text not in word_dictionary.keys():
            word_dictionary[text]={"paragraph":[ind],"frequency":[1]}
        elif index not in word_dictionary[text]["paragraph"]:
            word_dictionary[text]["paragraph"].append(ind)
            word_dictionary[text]["frequency"].append(1)
        else:
            word_dictionary[text]["frequency"][index-1]+=1

    
    
f = open("D://tap chief/features/test-input.txt", "r")
inputtext=f.read().split("\n\n\n")
index=1
for i in inputtext:
    #print(i)
    
    tester(i,index)
    index+=1
#print(inputtext)
print(word_dictionary)

