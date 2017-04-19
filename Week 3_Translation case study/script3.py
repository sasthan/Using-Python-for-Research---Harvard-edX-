from collections import Counter
import numpy as np

def count_words_fast(text):
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

def word_count_distribution(text):
    word_counts = count_words_fast(text)
    count_distribution = {}
    for keys, values in word_counts.items():
        if values in count_distribution:
            count_distribution[values]+=1
        else:
            count_distribution[values]=1
    return count_distribution

distribution = word_count_distribution("you are what you eat wherever you get time now because you are")


def more_frequent(distribution):
    b={}
    cumsum = 0
    print(distribution)
    b = np.cumsum(distribution)
    
       
      #   b.insert(0, {'keys':keys, 'values':cumsum})
        
   # np.cumsum(distribution[::-1])[::-1]
    print(b)


more_frequent(distribution)      
