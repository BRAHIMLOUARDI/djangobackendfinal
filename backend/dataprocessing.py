import os
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model


path_to_data = './fra.txt'

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


translation_file = open(path_to_data,"r", encoding='utf-8') 
raw_data = translation_file.read()
translation_file.close()


raw_data = raw_data.split('\n')
pairs = [sentence.split('\t') for sentence in  raw_data]
pairs=pairs[0:60000]

def clean_sentence(sentence):
    lower_case_sent = sentence.lower()
    string_punctuation = "?" + "¡" + '¿'+"."+"!"+'' 
    # # string_punctuation =string.punctuation.replace("'",'').replace("-",'')+ "¡" + '¿'

    clean_sentence = lower_case_sent.translate(str.maketrans('', '', string_punctuation))
   
    return clean_sentence
def tokenize(sentences):
    # Create tokenizer
    text_tokenizer = Tokenizer()
    # Fit texts
    text_tokenizer.fit_on_texts(sentences)
    return text_tokenizer.texts_to_sequences(sentences), text_tokenizer
english_sentences = [clean_sentence(pair[0]).replace("\u202f"," ").replace("\xa0"," ").replace("\u200b"," ").replace("«\u2009"," ").replace("\u2009"," ").replace("\xad","").rstrip().lstrip() for pair in pairs]

french_sentences = [clean_sentence(pair[1]).replace("\u202f"," ").replace("\xa0"," ").replace("\u200b"," ").replace("«\u2009"," ").replace("\u2009"," ").replace("\xad","").rstrip().lstrip() for pair in pairs]
# print(french_sentences[0])
# print("iweiofi")
# contant=str(french_sentences)
# print(contant[5])
# # file=open("backend/test.txt","w+")
# file.write(contant)
# file.close()
# print("iweiofi")
#print(french_sentences)
fra_text_tokenized, fra_text_tokenizer = tokenize(french_sentences)
eng_text_tokenized, eng_text_tokenizer = tokenize(english_sentences)





french_vocab = len(fra_text_tokenizer.word_index) + 1
# print(fra_text_tokenizer.word_index)
english_vocab = len(eng_text_tokenizer.word_index) + 1


max_french_len = int(len(max(fra_text_tokenized,key=len)))
max_english_len = int(len(max(eng_text_tokenized,key=len)))
print(max_french_len)
print(max_english_len)

fra_pad_sentence = pad_sequences(fra_text_tokenized,max_french_len, padding = "post")
eng_pad_sentence = pad_sequences(eng_text_tokenized,max_english_len, padding = "post")




fra_pad_sentence = fra_pad_sentence.reshape(*fra_pad_sentence.shape, 1)
eng_pad_sentence = eng_pad_sentence.reshape(*eng_pad_sentence.shape, 1)


print(max_french_len)
print(max_english_len)





def logits_to_sentence(model,sentence):

    x=[sentence]

    y=fra_text_tokenizer.texts_to_sequences(x)
    z=pad_sequences(y, max_french_len, padding = "post")
  
    z=np.reshape(z,(1,max_french_len,1))
    logits=model.predict(z)[0]
    index_to_words = {idx: word for word, idx in eng_text_tokenizer.word_index.items()}
    index_to_words[0] = '' 
    predict= ' '.join([index_to_words[prediction] for prediction in np.argmax(logits, 1)])
  
    return  predict
# x=[]           
# x.append(logits_to_sentence(model,"apprentissage profond est un type d'intelligence dérivé du apprentissage automatique"))
# print(x)

# /home/louardi/Downloads/my_model_v3.h5

# print("french vocabulary is of {} unique words".format(french_vocab))
# print("English vocabulary is of {} unique words".format(english_vocab))
#print(fra_text_tokenizer.word_index)
# contant3=str(fra_text_tokenized)

# file=open("/home/louardi/Documents/media/fra_text_tokenized192000.py","w+")
# file.write(contant3)
# file.close()
# contant4=str(eng_text_tokenized)

# file=open("/home/louardi/Documents/media/eng_text_tokenized192000.py","w+")
# file.write(contant4)
# file.close()

# contant5=str(fra_text_tokenizer.word_index)

# file=open("/home/louardi/Documents/media/fra_text_tokenizer.word_index192000.py","w+")
# file.write(contant5)
# file.close()
# contant6=str(eng_text_tokenizer.word_index)

# file=open("/home/louardi/Documents/media/eng_text_tokenizer.word_index192000.py","w+")
# file.write(contant6)
# file.close()


# contant1=str(french_sentences)

# file=open("/home/louardi/Documents/media/french_sentences192000.py","w+")
# file.write(contant1)
# file.close()
# contant2=str(english_sentences)

# file=open("/home/louardi/Documents/media/english_sentences192000.py","w+")
# file.write(contant2)
# file.close()


