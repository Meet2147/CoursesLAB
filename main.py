import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Learn Apply Build - AI & Python Projects", layout="wide")

# Header Section
st.title("Learn Apply Build - AI & Python Projects")
st.subheader("Master real-world AI applications with our hands-on projects")

# Project Display Section
projects = [
    {
        "title": "Mask Detection - Python Teachable Machine",
        "description": "Develop a mask detection system using Python and Google's Teachable Machine.",
        # "image": "path/to/mask_detection_image.jpg"  # Replace with actual image path
    },
    {
        "title": "Telegram GenAI Chatbot - Telegram, Google Gemini",
        "description": "Build an advanced chatbot integrated with Google Gemini on Telegram.",
        # "image": "path/to/telegram_genai_image.jpg"  # Replace with actual image path
    },
    {
        "title": "ChatGPT Clone - Streamlit Python",
        "description": "Create your own version of ChatGPT using Streamlit and Python.",
        # "image": "path/to/chatgpt_clone_image.jpg"  # Replace with actual image path
    },
    {
        "title": "Measurement App - Python",
        "description": "Build a versatile measurement app in Python for practical applications.",
        # "image": "path/to/measurement_app_image.jpg"  # Replace with actual image path
    },
    {
        "title": "Transcription and Summarization GenAI - Python OpenAI",
        "description": "Learn to transcribe and summarize audio using Python and OpenAI.",
        # "image": "path/to/transcription_summarization_image.jpg"  # Replace with actual image path
    },
    {
        "title": "PPT Generation APP Gen AI - Python OpenAI",
        "description": "Automate the creation of presentations with Python and OpenAI.",
        # "image": "path/to/ppt_generation_image.jpg"  # Replace with actual image path
    },
    {
        "title": "FaceRecognition Attendance - Python, MySQL",
        "description": "Develop a face recognition-based attendance system using Python and MySQL.",
        # "image": "path/to/facerecognition_attendance_image.jpg"  # Replace with actual image path
    },
    {
        "title": "ChatGPT Telegram Bot - Python, Telegram",
        "description": "Build a ChatGPT-powered bot for Telegram using Python.",
        # "image": "path/to/chatgpt_telegram_bot_image.jpg"  # Replace with actual image path
    }
]

# Display projects in a grid layout
cols = st.columns(2)
for i, project in enumerate(projects):
    with cols[i % 2]:
        # st.image(project["image"], caption=project["title"], use_column_width=True)
        st.write(f"**{project['title']}**")
        st.write(project["description"])
        st.write(f"**Fees:** {project['fees']}")
        st.button("Learn More", key=i)

# Footer Section
st.markdown("---")
st.markdown("**Contact Us**: info@learnapplybuild.com | **Follow Us**: [LinkedIn](https://linkedin.com/company/learnapplybuild)")
