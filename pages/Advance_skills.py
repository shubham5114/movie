import pandas as pd
import streamlit as st


col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    # Adjust the width of the image here to better fit the column width.
    st.image("pages/advance_skill.jpg", width=350)  # Adjust width as necessary
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
                    margin-top: -20px;
                    text-shadow: 2px 2px 8px #76f5d6;
                }
            </style>
            <h1>Advance Skills Recommendation System</h1>
            <p>Dive into the future of your professional growth with our Advanced Skill Recommendation System.Explore your professional growth with our Advanced Skill Recommendation System. If you possess a foundational skill, our system is designed to guide you in advancing your expertise by recommending higher-level skills that align with your current abilities. This tool ensures a logical progression in your learning journey, helping you expand your knowledge and stand out in the competitive landscape. Start this exciting adventure to enhance your skills and achieve significant professional growth. """

    st.markdown(styled_text, unsafe_allow_html=True)


# Data
l = {
    "django": ["python", "HTML", "CSS", "Databases", "JavaScript"],
    "ReactJs": ["HTML", "CSS", "Javascript", "NodeJs", "MongoDb"],
    "HTML": ["CSS", "Javascript", "ReactJs", "NodeJs", "ExpressJs"],
    "CSS": ["Javascript", "ReactJs", "NodeJs", "ExpressJs", "Tailwind CSS"],
    "Javascript": ["ReactJs", "Angular", "VueJs", "NodeJs", "Databases"],
    "python": [
        "Machine Learning",
        "Streamlit",
        "Django",
        "Python Flask",
        "Deep Learning",
    ],
}

# Creating DataFrame
data = [(key, val) for key, val in l.items()]
df = pd.DataFrame(data, columns=["Skill", "Related_Technology"])
df["Image"] = [
    ["python.jpeg", "html.png", "css.jpeg", "dtabase.png", "javascript.png"],
    ["html.png", "css.jpeg", "javascript.png", "nodejs.jpeg", "mongodb.jpeg"],
    ["css.jpeg", "javascript.png", "reactjs.png", "nodejs.jpeg", "express.png"],
    ["javascript.png", "reactjs.png", "nodejs.jpeg", "express.png", "tailwind.jpeg"],
    ["reactjs.png", "angular.png", "vuejs.png", "nodejs.jpeg", "dtabase.png"],
    ["ml.jpeg", "streamlit.png", "django.jpeg", "flask.png", "dl.jpeg"],
]

# Custom CSS for image sizing
st.markdown(
    """
<style>
img {
    width: 100px;  # Set the width to your preference
    height: 100px; # Set the height to your preference
    object-fit: cover;  # Ensures the image covers the set area, may crop
}
</style>
""",
    unsafe_allow_html=True,
)


# Recommendation function
def recommend(skill):
    skill_index = df[df["Skill"] == skill].index[0]
    recommended_skills = df.iloc[skill_index]["Related_Technology"]
    recommended_images = df.iloc[skill_index]["Image"]

    return recommended_skills, recommended_images


# Streamlit UI
selected_skill = st.selectbox("Enter Skill", df["Skill"])
if st.button("Recommend"):
    recommended_skills, recommend_images = recommend(selected_skill)

    cols = st.columns(
        len(recommended_skills)
    )  # Dynamically create columns based on the number of recommendations

    for idx, col in enumerate(cols):
        with col:
            st.image(f"pages/{recommend_images[idx]}")  # Image size controlled by CSS
            st.write(recommended_skills[idx])
