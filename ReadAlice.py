# This program will find the word that appears the most in Alice A I Wonderland.
import os
import datetime
path_to_output_file="resualts.txt"
path_to_alice = "alice_in_wunderland.txt"


def main_count_Alice():
    alice_text = read_Alice_text(path_to_alice)

    alice_clean = clean_Alice(alice_text)

    words = word_split(alice_clean)
    
    words = remove_singal_chars(words)

    word_count = count_words_in_Alice(words)

    sorted_words = sort_words(word_count)
    print(sorted_words)
    
    check_if_excist_and_rename(path_to_output_file)
    put_words_into_file(path_to_output_file, sorted_words)
    




def read_Alice_text(filepath):
    alice_raw_text = open(filepath, mode='r', encoding='utf-8-sig')
    alice_lower = alice_raw_text.read().lower()
    return (alice_lower)

def clean_Alice(alicetxt):

    alicecleantxt = ""
    for _ in alicetxt:
        if _ in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
           alicecleantxt += _
        else:
            alicecleantxt += " "

    print('alicecleantxt \n', alicecleantxt)
    return(alicecleantxt)
    
    # Did not work, find out why?
    """ alicetxt = alicetxt.translate(str.maketrans(string.punctuation, ' '*len(string.punctuation))).lower()   
    alicetxt = alicetxt.replace('\n', ' ')
    alicetxt = alicetxt.replace('\ufeff', '') """
     
    


def word_split(text_to_split):
    return(text_to_split.split())

def remove_singal_chars(words_to_clean):
    clean_words=[]
    for word in words_to_clean:
        if len(word) > 1:
            clean_words.append(word)
        elif word == 'a':
            clean_words.append(word)
          

    return(clean_words)
        
    
def count_words_in_Alice(words):
    
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = words.count(word)
        
            
    return(word_count)
    print('count Alice')
                
def sort_words(word_count):    
    sorted_words_by_numbers ={}
    max_val_key = None
    second_best_key = None
    #round = 0
    while len(sorted_words_by_numbers) != len(word_count):
        for key in word_count:
            if key not in sorted_words_by_numbers:
                #round += 1
                second_best_key = key
                max_val_key = key
                for key_to_comper in word_count:                   
                    if key_to_comper not in sorted_words_by_numbers:
                        if word_count[key] < word_count[key_to_comper] and  word_count[key_to_comper] > word_count[max_val_key]:
                            second_best_key = max_val_key
                            max_val_key = key_to_comper
                        elif word_count[key_to_comper] > word_count[second_best_key] or max_val_key == second_best_key:
                            second_best_key = key_to_comper
                            
            sorted_words_by_numbers[max_val_key] = word_count[max_val_key]
            sorted_words_by_numbers[second_best_key] = word_count[second_best_key]
        
    return sorted_words_by_numbers
      
def check_if_excist_and_rename(file):
    x = datetime.datetime.now()
    ref = x.strftime("%f")
    if os.path.exists(file):
        new_file_name = file + ref
        os.rename(file, new_file_name)

def put_words_into_file(file, words):
    f = open(file, mode='w', encoding='utf-8-sig')
    for key in words:
        text = key + ':' + str(words[key]) + '\n'
        f.write(text)
    f.close
    

    
    
    
    


main_count_Alice()
