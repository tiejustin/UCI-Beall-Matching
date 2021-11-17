import nltk
import spacy
import gensim.downloader as api
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from gensim.models import Word2Vec
from gensim.models import Phrases


# desc = "Shaka is an online platform that helps companies keep their employees engaged whether they are working in the office or at home."
offering = "I am in need of mentors with a background in HR or Organizational Psychology. I sell into this market but it is not my background so mentors who could\
 help me better reach my future clientele via strategic outreach and messaging would be very valuable. If there are mentors with a legal background, that\
 would be huge for Shaka. I am not sure that the documents I created are sufficient for client agreements at scale. I would love to network with angels and\
 venture capitalists, I do not have a strong network of connections in this space and I fear it will hinder me during fundraising. Lastly, the office space will\
 help me attract more serious team members onto our founding team and give us a productive, professional space to work."

tokenDesc = word_tokenize(offering)
#get noun phrases from tokenized string
nlp = spacy.load("en_core_web_sm")
doc = nlp(offering)

print(doc.ents)
chunk = [chunk.text for chunk in doc.noun_chunks]

print("Noun phrases:", chunk)

filteredChunks = []

for nouns in chunk:
    splitNouns = nouns.split()
    splitNouns = pos_tag(splitNouns)
    temp = []
    for wd in splitNouns:
        if "JJ" in wd[1] or "NN" in wd[1]:
            temp.append(wd[0])
    if temp:
        filteredChunks.append(" ".join(temp))

print(filteredChunks)       

#initiliaze data for Word2Vec
dataset = api.load("text8")
data = [d for d in dataset]
#train a bigram detector
bigram_transformer = Phrases(data)
#apply bigrams to train Word2Vec
model = Word2Vec(bigram_transformer[data], min_count = 1)
#save the model for later
model.save("newmodel")

#still need to implement finding similarities between words
#thoughts on how to implement:
#call model.similarity(words in filteredChunks, words in Industries/Skillsets)
#find the highest similarity and determine if it is a high enough ratio to accept as being synonmyous to the word
#interpret that the words are the same if they are similar enough
#refine and return list of mentors that have such words on their insightly profile.

# print(filteredDesc)

# # #Example code for finding Synonyms
# # #Plan to iterate through noun phrases and find synonyms with possible skillsets/industries
# synonyms = []

# input_word = "ecommerce"
# for syn in wordnet.synsets(input_word):
#     for lm in syn.lemmas():
#         synonyms.append(lm.name())

# print(set(synonyms))

# Shaka "Best category that fits their startup"
# Business productivity == productivity (in insightly)
# The contacts below only has 'productivity':
# Hemantha Wickramasinghe; John Nall (x2); Liam Bucci; Michael Green; 
# Nikil Dutt; Vartkess Apkarian; Philip Duncan; Lorenzo Valdevit; J. Michael McCarthy 
# industry = "Business Productivity"

