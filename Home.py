import streamlit as st

st.set_page_config(layout="wide")
# import pickle as pk
# import pandas as pd
import requests
from streamlit_lottie import st_lottie

# import pyttsx3
# import speech_recognition as sr
# import streamlit_scrollable_textbox as stx
from streamlit_option_menu import option_menu
import subprocess

# Set background color to dark gray
st.markdown(
    """
    <style>
    .css-17eq0hr {
        color: white;
        background-color: #1E1E1E;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

st.markdown(
    "<h1 style='text-align: center;color: #f8f8f8;text-shadow: 2px 2px 8px #37ad90;'>Recommendation System</h1>",
    unsafe_allow_html=True,
)

if selected == "Home":

    # --------------------------------------------------------hello animation---------------------------------------------------------
    c0, c1, c2 = st.columns([1, 2, 2])
    with c0:
        st.write("")
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

        # --------------------------------------------------------Domain call---------------------------------------------------------

        Domain_list = ["Choose Domain", "Movie", "Books", "Advanced Skills"]
    select = st.selectbox(
        "Enter Domain", Domain_list, index=0
    )  # Default selection is "Choose Domain"

    if select == "Choose Domain":
        st.write("Please select a domain to proceed.")
    elif select == "Movie":
        subprocess.Popen(["streamlit", "run", "pages/Movie.py"])

    elif select == "Books":
        subprocess.Popen(["streamlit", "run", "pages/Book.py"])

    elif select == "Advanced Skills":
        subprocess.Popen(["streamlit", "run", "pages/Advance_skills.py"])

    with c2:
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
                    margin-top: 40px;
                }
            </style>

            ## About Us

            Welcome to CineGenius, your ultimate gateway to personalized recommendations!

            Whether you're in the mood for an enthralling movie, an engaging book, or looking to acquire a new skill, CineGenius is designed to cater to your unique tastes. Dive into a world where your next favorite adventure, story, or learning opportunity is just a recommendation away. Explore, discover, and transform your leisure and learning experiences with CineGenius today!
            """

        st.markdown(styled_text, unsafe_allow_html=True)

# ------------------------------------------------About-------------------------------------------------------

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
        Unlock Your Next Favorite Adventure with CineGenius! Dive into a world where movies, books, and cutting-edge skills recommendations are perfectly tailored to your tastes.
        """
    # Movie Recommendation System with Live Chat
    about_text = """
        
        ### Key Features:
        - **Diverse Recommendations:** From blockbuster movies to must-read books and advanced learning skills, CineGenius covers all your entertainment and educational needs.
        - **Interactive Experience:** Engage in live chats with our intelligent system that listens, responds, and even speaks to you, making your interaction delightfully seamless.
        - **Live Chat Interaction:** Our unique live chat feature allows you to communicate with CineGenius:. Type your queries or speak, and CineGenius: responds in style.
        - **Audio Feedback:** CineGenius: not only writes responses but also speaks to you, making the interaction more immersive.
        
        ### How It Works:
        1. **Recommendation Engine:** Our powerful recommendation engine analyzes your watching history and preferences.
        2. **Live Chat:** Engage in real-time conversations with CineGenius:. Ask for recommendations, movie trivia, or just chat about films.
        3. **Audio Responses:** Enjoy the experience of CineGenius: responding to you with both written and spoken words.
        4. Simply enter your current interests, and CineGenius uses sophisticated algorithms to analyze your preferences and suggest content and skills that you are bound to love. 
        5. Whether you're in the mood for a gripping drama, an inspiring read, or a skill that boosts your career, CineGenius is here to guide you every step of the way.
        
        ### Experience CineGenius: Today!
            Step into the future of personalized recommendations with CineGenius. Start your journey through the pages and screens of new discoveries that are as unique as you are. 
            Explore CineGenius now and let your next favorite adventure find you!
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

# -------------------------------------------------------SideBar---------------------------------------------------------
st.sidebar.title("Live Chat")


# def write_to_sidebar(t):
#     with st.sidebar:
#         st.markdown(
#             f"""
#             <div style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; margin: 10px;">
#                 <span style="color: #3366cc; font-size: 18px; font-weight: bold;">{t}</span>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )


# -------------------------------------------------------------------------voice-------------------------------------------------------
# def speak(text):
#     engine = pyttsx3.init()
#     voices = engine.getProperty("voices")
#     ID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#     engine.setProperty("voice", ID)
#     write_to_sidebar("")
#     write_to_sidebar(f"Pillu:  {text}")
#     write_to_sidebar("")
#     if text == "stop":
#         return True  # Indicate to stop the program
#     engine.say(text=text)
#     engine.runAndWait()
#     return False  # Continue the program
# def speechrecognition():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         write_to_sidebar("Listening.....")
#         r.pause_threshold = 1
#         audio = r.listen(source, 0, 8)
#         try:
#             write_to_sidebar("Recognizing....")
#             query = r.recognize_google(audio, language="en")
#             write_to_sidebar("You:   " + query)
#             query = query.lower()
#             return query
#         except:
#             return ""
# def mainExexution(query):
#     Query = str(query).lower()
#     if "hello" in Query:
#         speak("Hello Sir, How can I help you?")
#     elif "stop" in Query:
#         speak("Nice to meet you sir")
#         return True  # Indicate to stop the program
#     return False  # Continue the program
# while True:
#     Query = speechrecognition()
#     if mainExexution(Query):
#         write_to_sidebar("Program stopped.")
#         break


# ----------------------------------------------------------------------chat--------------------------------------------------import streamlit as st
import streamlit as st


def write_to_sidebar():
    """Display all chat messages in the sidebar with styling."""
    for message in st.session_state.chat_history:
        st.sidebar.markdown(
            f"""
            <div style="background-color: #f4f4f4; padding: 10px; border-radius: 5px; margin: 10px;">
                <span style="color: #3366cc; font-size: 18px; font-weight: bold;">{message}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def main_execution(query):
    """Process user input and generate responses."""
    query = query.lower()
    if "hello" in query:
        response = "Hello! How can I help you today?"
    elif "stop" in query:
        response = "It was nice chatting with you! Have a great day!"
        st.session_state.chatting = False
    else:
        response = "Sorry, I didn't understand that. Can you please repeat?"
    st.session_state.chat_history.append(f"You: {query}")
    st.session_state.chat_history.append(f"Pillu: {response}")


if __name__ == "__main__":
    # Initialize session state variables if not already present
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
        st.session_state["chatting"] = True
        st.session_state["input_counter"] = 0

    write_to_sidebar()  # Display the chat history

    # Unique key for each input field
    unique_key = f"user_input_{st.session_state['input_counter']}"

    # Input field for user input
    user_input = st.sidebar.text_input("You:", key=unique_key)

    # Process input only if it is not empty
    if user_input:
        main_execution(user_input)
        # Increment the counter to ensure the next input widget has a new unique key
        st.session_state["input_counter"] += 1
        st.experimental_rerun()  # Rerun the app to update the chat log and reset the input box
