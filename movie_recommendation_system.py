import pandas as pd
import tkinter as tk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(title):
	return df[df.title == title]["index"].values[0]

df = pd.read_csv("movie_dataset.csv")       #TO READ THE CSV FILE

features = ['keywords','cast','genres','director']

for feature in features:
	df[feature] = df[feature].fillna('')    #Create a column in DF which combines all selected features

def combine_features(row):
	try:
		return row['keywords'] +" "+row['cast']+" "+row["genres"]+" "+row["director"]
	except:
		print ("Error:", row)


df["combined_features"] = df.apply(combine_features,axis=1)



cv = CountVectorizer()              #Create count matrix from this new combined column


count_matrix = cv.fit_transform(df["combined_features"])


cosine_sim = cosine_similarity(count_matrix)    #Compute the Cosine Similarity based on the count_matrix

def recommend(movie):
	movie_user_likes = movie     #The user input

	movie_index = get_index_from_title(movie_user_likes)            #Get index of this movie from its title

	similar_movies =  list(enumerate(cosine_sim[movie_index]))

	sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)   #Get a list of similar movies in descending order of similarity score

	x = []
	i=0
	for element in sorted_similar_movies:               #Print titles of first 20 movies
		x.append(get_title_from_index(element[0]))
		i=i+1
		if i>21:
			break
	return x[1]+'\n'+x[2]+'\n'+x[3]+'\n'+x[4]+'\n'+x[5]+'\n'+x[6]+'\n'+x[7]+'\n'+x[8]+'\n'+x[9]+'\n'+x[10]\
		   +x[11]+'\n'+x[12]+'\n'+x[13]+'\n'+x[14]+'\n'+x[15]+'\n'+x[16]+'\n'+x[17]+'\n'+x[18]+'\n'+x[19]+'\n'+x[20]+'\n'+x[21]



def result(movie):
	label['text']=(recommend(movie))


root = tk.Tk()

HEIGHT = 500
WIDTH = 600


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_label = tk.Label(root, bg='#D1D0CE')
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Recommend Me!", command=lambda: result(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.7, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()

