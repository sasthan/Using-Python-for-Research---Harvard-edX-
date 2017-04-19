text="This is my test text. we are keeping this text short"

def count_word(text):
    text=text.lower()
    skips=[".",",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")

    
    word_counts={}
    for word in text.split(" "):
        #known word
        if word in word_counts:
            word_counts[word]+=1
        #unknown word
        else:
            word_counts[word]=1
    return word_counts

from collections import Counter 

def count_word_fast(text):
    text=text.lower()
    skips=[".",",",";",":","'",'"']
    for ch in skips:
        text = text.replace(ch,"")
    
    word_counts=Counter(text.split(" "))
    return word_counts

 
def read_book(title_path):
    with open(title_path, "r", encoding="utf8") as current_file:
        text=current_file.read()
        text = text.replace("\n","").replace("\r","")
    return text
        
def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return(num_unique, counts)
"""
import os
book_dir="./Books"

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + author):
            inputfile = book_dir+ "/" + author + "/" + title
            print(inputfile)
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
"""
import pandas as pd

table = pd.DataFrame(columns=("name","age"))
table.loc[1]="James",22
table.loc[2]="Jess",32

            
