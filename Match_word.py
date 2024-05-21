import numpy as np


filename = "FrenchWordDb.txt"
Db = np.loadtxt(filename,dtype=str,delimiter=',')
final_tab=[]
i=0
while i<len(Db):
    final_tab.append(str(Db[i]))
    i+=1
    

def split_word(word):
    length=len(word)
    word_splitten=[]
    i=0
    while i<length:
        word_splitten.append(word[i])
        i+=1
    return word_splitten

def matching_words(wordsDb,letters_sequence:list):
    matching_words_list=[]

    for word in wordsDb:
        word_splitten=split_word(word)
        length=len(word_splitten)
        i=0
        while i<length:
            if word_splitten[i] in letters_sequence:
                match=True
                i+=1
            else:
                match=False
                break
        if  match==True:
            matching_words_list.append(word)
            
    if matching_words_list==[]:
        return "sorrry ,but no words is corresponding"
    return matching_words_list

def words(number:int,letters_sequence:list):
    result=[]
    words_db=matching_words(Db,letters_sequence)
    for word in words_db:
        if len(word)==number:
            result.append(word)
    return result

