from fastapi import FastAPI

from Match_word import  words,split_word
app = FastAPI()



@app.get("/")
def result(word_length:int,letters_provided:str):

    letters_sequence=split_word(letters_provided)
    return words(word_length,letters_sequence)