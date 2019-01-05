import os
import gensim
import psycopg2
connection = psycopg2.connect( host= 'localhost', user='scrapeuser', database='scraped_news', password='simple')
cursor = connection.cursor()
connection.set_session(autocommit=True)
cursor.execute("""SELECT content from news_table""")
documents = cursor.fetchall()
documents = str(documents)
stoplist = set('for a of the and to in'.split()) # Useless, could have relationship with anything.
# remove common words and tokenize
for document in documents:
    texts = [word for word in document.lower().split() if word not in stoplist]

for sent in corpus:
    tok_corp = nltk.word_tokenize(str(sent))
model = gensim.models.Word2Vec(tok_corp, min_count=1, size = 40)

#model.save('testmodel')
#model = gensim.models.Word2Vec.load('test_model')
#model.most_similar('word')
#model.most_similar([vector])
