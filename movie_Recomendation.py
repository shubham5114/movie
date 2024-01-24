#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pickle as pk
# import matplotlib.pyplot as mlt
import ast  # use to convert a string of list to list
from nltk.stem.porter import PorterStemmer
import streamlit as st
import pickle as pk
import pandas as pd
import requests
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pyttsx3
import speech_recognition as sr
import streamlit_scrollable_textbox as stx
from streamlit_option_menu import option_menu
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# In[2]:


df_credit = pd.read_csv("tmdb_5000_credits.csv")
# df_credit.head()


# In[3]:


df_movie = pd.read_csv("tmdb_5000_movies.csv")
# df_movie.head(2)


# ## Merging both the datasets

# In[4]:


df_movie = df_movie.merge(df_credit, on="title")
# df_movie.info()


# ## Selecting the required Columns

# In[5]:


movie = df_movie[["id", "genres", "title", "overview", "keywords", "cast", "crew"]]
# movie


#  ## finding the missing values in data

# In[6]:


movie.isnull().sum()


# ## removing the missing data movies

# In[7]:


movie.dropna(inplace=True)


#  ## checking for any duplicate data of movies (2 or more same rows)

# In[8]:


movie.duplicated().sum()


# In[9]:


# movie.genres.iloc[0]


# ## Converting the columns into more refined form (more understandable & omitting the unnecessary things)

# In[10]:


# ## Proper formatting and extracting the required values

# In[11]:


def convert(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i["name"])
    return l


# In[12]:


movie["genres"] = movie["genres"].apply(convert)
# movie


# In[13]:


movie["keywords"] = movie["keywords"].apply(convert)
# movie


# ## Extracting the top 3 cast values

# In[14]:


def convert3(obj):
    l = []
    cnt = 0
    for i in ast.literal_eval(obj):
        if cnt != 3:
            l.append(i["name"])
            cnt += 1
        else:
            break
    return l


# In[15]:


movie["cast"] = movie["cast"].apply(convert3)
# movie


# ## Extracting the director's name

# In[16]:


def convert_dir(obj):
    l = []
    for i in ast.literal_eval(obj):
        if i["job"] == "Director":
            l.append(i["name"])
            break
    return l


# In[17]:


movie["crew"] = movie["crew"].apply(convert_dir)
# movie


# ## converting overview column into list of string

# In[18]:


movie["overview"] = movie["overview"].apply(lambda x: x.split())
# movie


# ## Removing the spaces b/w the words for making it easy to search for a word

# In[19]:


movie["genres"] = movie["genres"].apply(lambda x: [i.replace(" ", "") for i in x])
movie["keywords"] = movie["keywords"].apply(lambda x: [i.replace(" ", "") for i in x])
movie["cast"] = movie["cast"].apply(lambda x: [i.replace(" ", "") for i in x])
movie["crew"] = movie["crew"].apply(lambda x: [i.replace(" ", "") for i in x])
# movie


# ## Combining many columns

# In[20]:


movie["tag"] = (
    movie["overview"]
    + movie["genres"]
    + movie["keywords"]
    + movie["cast"]
    + movie["crew"]
)


# ## Making new dataFrame

# In[21]:


new_movie = movie[["id", "title", "tag"]]
# new_movie


# ## Combining all words in tag column

# In[22]:


new_movie["tag"] = new_movie["tag"].apply(lambda x: " ".join(x))
# new_movie


# ## Stemming

# In[23]:


ps = PorterStemmer()


# In[24]:


def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return y


# In[25]:


new_movie["tag"].apply(stem)


# In[ ]:


# ## Converting every letter to lower case

# In[26]:


new_movie["tag"] = new_movie["tag"].apply(lambda x: x.lower())
# new_movie


# In[27]:


# new_movie.iloc[0]


# # Vectorization of Words

# -> Find the freq. of all the words occurs in whole tag columns
# -> Then we can extract the no. of required words for prediction

# In[28]:


cv = CountVectorizer(
    max_features=5000, stop_words="english"
)  # we need 5000 freq. for prediction and we r removing the stop words of english lang.


# In[29]:


vector = cv.fit_transform(new_movie["tag"]).toarray()
# vector


# In[30]:


cv.get_feature_names_out()


# ## Distance calculation of 1 movie to another - using Cosine distance(calculation angle b/w 2 movies)

# ##### Eucledian distance give incorrect o/p for large values

# In[31]:


# In[32]:


similarity = cosine_similarity(vector)


# In[33]:


# similarity[0]


# ## using enumerate for pairing index with similarity values

# #### Reverse sorting on based on the values

# In[34]:


# sorted(enumerate(similarity[0]), reverse=True, key=lambda x: x[1])[1:6]


# In[35]:


# def recommend(movie_name):
#     movie_index = new_movie[new_movie["title"] == movie_name].index[0]
#     l = sorted(enumerate(similarity[movie_index]), reverse=True, key=lambda x: x[1])[
#         1:6
#     ]
#     for i in l:
#         print(new_movie.iloc[i[0]].title)


# In[36]:


# --------------------------------------------------------Nav Bar---------------------------------------------------------

selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Contact Me"],
    icons=["house", "question-circle-fill", "person-lines-fill"],
    menu_icon="cast",
    orientation="horizontal",
    styles={
        "container": {"padding": "10"},
        # "icon": {"color": "orange", "font-size": "25px"},
        # "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#37ad90"},
    },
)

if selected == "Home":
    st.title("Recommendation System")

    # --------------------------------------------------------hello animation---------------------------------------------------------
    c1, c2 = st.columns([6, 3])
    with c1:
        url = requests.get(
            "https://lottie.host/fd53e292-06c0-4390-953c-1a9251cadb88/UBuRn7TaTu.json"
        )
        url_json = dict()
        if url.status_code == 200:
            url_json = url.json()
        else:
            st.write("Error in URL")

        st_lottie(
            url_json,
            # change the direction of our animation
            reverse=True,
            # height and width of animation
            height=400,
            width=400,
            # speed of animation
            speed=1,
            # means the animation will run forever like a gif, and not as a still image
            loop=True,
            # quality of elements used in the animation, other values are "low" and "medium"
            quality="high",
            # THis is just to uniquely identify the animation
            key="Hello",
        )

        # --------------------------------------------------------movie poster call---------------------------------------------------------

        def poster(movie_id):
            response = requests.get(
                "https://api.themoviedb.org/3/movie/{}?api_key=e38b1e7fe3ec597dfcb5bb86217e9e94&language=en-US".format(
                    movie_id
                )
            )
            data = response.json()
            return "http://image.tmdb.org/t/p/w500/" + data["poster_path"]

        def recommend(movie_name):
            movie_index = movie_list[movie_list["title"] == movie_name].index[0]
            l = sorted(
                (enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1]
            )[1:6]
            recommended = []
            recommend_poster = []
            for i in l:
                movie_id = movie_list.iloc[i[0]].id
                # fetch poster from API

                recommend_poster.append(poster(movie_id))
                recommended.append(movie_list.iloc[i[0]].title)
                # print(recommend_movies_poster)
            return recommended, recommend_poster

        # movie_list = pk.load(open("movie.pkl", "rb"))
        # movie_list = pd.DataFrame(movie_list)

        # similarity = pk.load(open("similarity.pkl", "rb"))
        movie_list = pd.DataFrame(new_movie)
        selected = st.selectbox("Enter Movie", (movie_list["title"]))

        if st.button("Recommend"):
            recommend_movies_name, recommend_movies_poster = recommend(selected)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(recommend_movies_name[0])
                st.image(recommend_movies_poster[0])
            with col2:
                st.text(recommend_movies_name[1])
                st.image(recommend_movies_poster[1])
            with col3:
                st.text(recommend_movies_name[2])
                st.image(recommend_movies_poster[2])
            with col4:
                st.text(recommend_movies_name[3])
                st.image(recommend_movies_poster[3])
            with col5:
                st.text(recommend_movies_name[4])
                st.image(recommend_movies_poster[4])

    with c2:
        # st.subheader("ABOUT ME")

        # Styled static text using st.markdown
        styled_text = """
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background-color: #f8f8f8;
                color: #333;
                line-height: 1.6;
                margin: 20px;
            }

            h2 {
                color: #76f5d6;
            }

            p {
                font-size: 16px;
                margin-bottom: 15px;
            }
        </style>

        ## About Us

        Welcome to our Recommendation System Avatar! 

        Today,we understand that finding the right recommendations can greatly enhance your experience. Our Recommendation System Avatar is here to assist you in discovering personalized recommendations tailored just for you.

        """

        st.markdown(styled_text, unsafe_allow_html=True)

if selected == "About":
    # import streamlit as st

    # Styling for the About Section
    styled_about_text = """
        <style>
            h1 {
                color: #f8f8f8;
                text-shadow: 2px 2px 8px #37ad90;
            }
            p {
                color: #f8f8f8;
                font-size: 16px;
            }
        </style>

        # About CineGenius:

        CineGenius: is not just a movie recommendation system; it's your personalized movie companion. Our system goes beyond algorithms and engages with you in a dynamic and conversational way.
    """

    # Movie Recommendation System with Live Chat
    about_text = """

        ### Key Features:
        - **Intelligent Recommendations:** CineGenius:s employs advanced algorithms to understand your preferences and suggests movies tailored just for you.
        - **Live Chat Interaction:** Our unique live chat feature allows you to communicate with CineGenius:. Type your queries or speak, and CineGenius: responds in style.
        - **Audio Feedback:** CineGenius: not only writes responses but also speaks to you, making the interaction more immersive.

        ### How It Works:
        1. **Recommendation Engine:** Our powerful recommendation engine analyzes your watching history and preferences.
        2. **Live Chat:** Engage in real-time conversations with CineGenius:. Ask for recommendations, movie trivia, or just chat about films.
        3. **Audio Responses:** Enjoy the experience of CineGenius: responding to you with both written and spoken words.

        ### Experience CineGenius: Today!
            Dive into the world of movies with CineGenius:. Whether you're a film enthusiast or looking for something new, CineGenius: is here to make your movie-watching experience exceptional.
            _Lights, Camera, Action!_

    """

    # Render the styled about section
    # Render the about text

    st.markdown(styled_about_text, unsafe_allow_html=True)
    st.markdown(about_text, unsafe_allow_html=True)

# ----------------------------------------------------contact me-----------------------------------------------------

if selected == "Contact Me":
    import streamlit as st
    import requests
    from streamlit_lottie import st_lottie

    c1, c2 = st.columns([1, 1])
    with c1:
        styled_text = """
            <style>
                h1 {
                    color: #f8f8f8;
                    padding-left: 10px;
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>
            # Contact Me
        
            
            """
        st.markdown(styled_text, unsafe_allow_html=True)
    with c2:
        url = requests.get(
            "https://lottie.host/f4d597d4-dcb2-4192-a6ac-4eed6d41b422/YKnPIo8ExR.json"
        )
        url_json = dict()
        if url.status_code == 200:
            url_json = url.json()
        else:
            st.write("Error in URL")
        st_lottie(
            url_json,
            # change the direction of our animation
            reverse=True,
            # height and width of animation
            height=200,
            width=400,
            # speed of animation
            speed=1,
            # means the animation will run forever like a gif, and not as a still image
            loop=True,
            # quality of elements used in the animation, other values are "low" and "medium"
            quality="high",
            # THis is just to uniquely identify the animation
            key="contact",
        )

    form_text = """
            <style>

                h3 {
                    color: #f8f8f8;
                    padding-left: 10px;
                    padding-top: 100px;
                    text-shadow: 2px 2px 8px #CE4BC2;
                }

            </style>

            ### Contact Form
            
            """
    st.markdown(form_text, unsafe_allow_html=True)

    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/shubhampaliitr@email.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Details of your problem"></textarea>
        <button type="submit">Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style.css")

    styled_text = """
            <style>
                h3 {
                    color: #f8f8f8;
                    padding-left: 10px;
                    text-shadow: 2px 2px 8px #CE4BC2;
                }
            </style>

            ### Social Media Links
            """

    def social_media_icons():
        icons = {
            "LinkedIn": "https://www.linkedin.com/in/shubham-kumar-78058924b/",
            "GitHub": "https://github.com/shubham5114",
            "Twitter": "https://twitter.com/your-twitter-profile",
            "Instagram": "https://www.instagram.com/shubham.5114/",
            "Facebook": "https://facebook.com/your-facebook-profile",
            "Discord": "https://discord.com/channels/@me",
            # Add more social media icons and links as needed
        }

        icons_html = []
        for platform, link in icons.items():
            icon_html = f"""
                <a href="{link}" target="_blank" class="social-icon">
                    <i class="fab fa-{platform.lower()}"></i>
                </a>
            """
            icons_html.append(icon_html)

        return " ".join(icons_html)

    # Additional Contact Information
    contact_info = """
            <style>
                .contact-info {
                    font-size: 18px;
                    color: #f8f8f8;
                    text-shadow: 2px 2px 8px #CE4BC2;
                    # margin-top: 20px;
                }
            </style>

            ### Contact Information
            - **Name:** Shubham Pal
            - **Email:** shubhampaliitr@gmail.com
            - **Phone:** +91- 7988192771
            """
    # st.markdown(contact_info, unsafe_allow_html=True)

    # Copyright Section
    copyright_text = """
            <style>
                .copyright {
                    font-size: 16px;
                    color: #f8f8f8;
                    text-shadow: 2px 2px 8px #CE4BC2;
                    margin-top: 20px;
                }
            </style>

            ### Copyright © 2023 Shubham pal. All Rights Reserved.
            """
    # st.markdown(copyright_text, unsafe_allow_html=True)

    # Styled footer with social media links, contact information, and copyright
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
            .social-icon {
                font-size: 30px;
                color: #3498db; /* Icon color */
                margin: 0 10px; /* Adjust spacing between icons */
                transition: color 0.3s; /* Add smooth transition effect on hover */
                text-decoration: none;
            }

            .social-icon:hover {
                color: #e74c3c; /* Change color on hover */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display social media icons and contact information in columns
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown(styled_text, unsafe_allow_html=True)
        st.markdown(social_media_icons(), unsafe_allow_html=True)

    with col2:
        st.markdown(contact_info, unsafe_allow_html=True)
    st.markdown(copyright_text, unsafe_allow_html=True)

# --------------------------------------------------------SideBar---------------------------------------------------------

st.sidebar.title("Live Chat")


def write_to_sidebar(t):
    with st.sidebar:
        st.markdown(
            f"""
            <div style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; margin: 10px;">
                <span style="color: #3366cc; font-size: 18px; font-weight: bold;">{t}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", ID)
    write_to_sidebar("")
    write_to_sidebar(f"Pillu:  {text}")
    write_to_sidebar("")
    if text == "stop":
        return True  # Indicate to stop the program
    engine.say(text=text)
    engine.runAndWait()
    return False  # Continue the program


def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        write_to_sidebar("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

        try:
            write_to_sidebar("Recognizing....")
            query = r.recognize_google(audio, language="en")
            write_to_sidebar("You:   " + query)
            query = query.lower()
            return query

        except:
            return ""


def mainExexution(query):
    Query = str(query).lower()
    if "hello" in Query:
        speak("Hello Sir, How can I help you?")
    elif "stop" in Query:
        speak("Nice to meet you sir")
        return True  # Indicate to stop the program
    return False  # Continue the program


while True:
    Query = speechrecognition()
    if mainExexution(Query):
        write_to_sidebar("Program stopped.")
        break
