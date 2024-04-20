import streamlit as st
import pickle as pk
import pandas as pd
from streamlit_lottie import st_lottie

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    # Adjust the width of the image here to better fit the column width.
    st.image("pages/book.jpg", width=400)  # Adjust width as necessary
with col2:
    st.write(" ")  # This can remain as a spacer or be adjusted
with col3:
    styled_text = """
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    background-color: #f8f8f8;
                    color: #333;
                    line-height: 1.6;
                    margin: 1px;
                }
                h1 {
                    color: #FFFFFF;
                    margin-top: -30px;
                    text-shadow: 2px 2px 8px #76f5d6;
                }
            </style>
            <h1>Books Recommendation System</h1>
            <p>Unleash the magic of endless reading with our Book Recommendation System! Whether you're a seasoned bookworm or a curious newcomer, our system takes your current literary crush and connects you with your next page-turner. Just tell us the title of the book you're devouring, and we'll whisk you away on a new adventure with a perfectly matched recommendation. """

    st.markdown(styled_text, unsafe_allow_html=True)

# --------------------------------------------------------movie poster call---------------------------------------------------------


def recommend(book_name):

    try:
        # Find the index of the given book name in the dataframe
        book_index = book_list[book_list["Book_Title"] == book_name].index[0]
    except IndexError:
        st.error("Book not found in the database.")
        return [], []
    l = sorted((enumerate(similarity[book_index])), reverse=True, key=lambda x: x[1])[
        1:7
    ]

    recommended = []
    recommend_poster = []

    # Fetching book details for the recommended books
    for i in l:
        recommended_book = book_list.iloc[i[0]]
        recommend_poster.append(recommended_book.Image)
        recommended.append(recommended_book.Book_Title)

    return recommended, recommend_poster


book_lis = pk.load(open("pages/book.pkl", "rb"))
book_list = pd.DataFrame(book_lis)
similarity = pk.load(open("pages/book_similarity.pkl", "rb"))
selected = st.selectbox("Enter Book", (book_list["Book_Title"]))

if st.button("Recommend"):
    recommended, recommend_book_img = recommend(selected)
    recommend(selected)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended[0])
        st.image(recommend_book_img[0])
    with col2:
        st.text(recommended[1])
        st.image(recommend_book_img[1])
    with col3:
        st.text(recommended[2])
        st.image(recommend_book_img[2])
    with col4:
        st.text(recommended[3])
        st.image(recommend_book_img[3])
    with col5:
        st.text(recommended[4])
        st.image(recommend_book_img[4])
