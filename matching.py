import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

stopWords = set(stopwords.words('english'))

punctuation = ["/'", ",", ".", "!", "?", ";"]

# desc = "Shaka is an online platform that helps companies keep their employees engaged whether they are working in the office or at home."
offering = "I am in need of mentors with a background in HR or Organizational Psychology. I sell into this market but it is not my background so mentors who could\
 help me better reach my future clientele via strategic outreach and messaging would be very valuable. If there are mentors with a legal background, that\
 would be huge for Shaka. I am not sure that the documents I created are sufficient for client agreements at scale. I would love to network with angels and\
 venture capitalists, I do not have a strong network of connections in this space and I fear it will hinder me during fundraising. Lastly, the office space will\
 help me attract more serious team members onto our founding team and give us a productive, professional space to work."

tokenDesc = word_tokenize(offering)
filteredDesc = []

for w in tokenDesc:
    if w.lower() not in stopWords and w not in punctuation:
        filteredDesc.append(w)

nlp = spacy.load("en_core_web_sm")
doc = nlp(offering)

print(doc.ents)
chunk = [chunk.text for chunk in doc.noun_chunks if chunk.text.lower() not in stopWords]

print("Noun phrases:", chunk)


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
industry = "Business Productivity"

