import streamlit as st

st.set_page_config(page_title="Happy Teacher's Day!", page_icon="💻", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    h1 { color: #2dd4bf !important; }
    .stButton>button { background-color: #0d9488 !important; color: white !important; border-radius: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("Happy Teacher's Day! ✨")
st.caption("Dedicated to the best Computer Science Teacher: **Mam Kiran Nabi**")

st.code("""
# apology_log.py
try:
    wish_teacher_on_time()
except Exception as e:
    print("Error 404: Timely Wish Not Found!")
    print("Compiling heartfelt apology module...")
""", language="python")

st.error("### 🙏 I Am So Sorry, Mam!")
st.write("I feel extremely guilty for missing the opportunity to wish you on time and needing your reminder. As your computer science student, forgetting feels like an unhandled bug in my system! Please forgive my delay—my respect and gratitude for you are always running 24/7.")

st.info("### To My Favorite Tech Mentor 👩‍💻")
st.write("Dear **Mam Kiran Nabi**,\n\nThank you for turning complex logic into simple understanding and making computer science so engaging. You don't just teach code; you inspire us to debug our mistakes and upgrade ourselves every day!")

if st.button("Click to Compile Wish 🚀"):
    st.success("🎉 System.out.println('Happy Teacher\\'s Day, Mam Kiran Nabi! You are legendary!'); 🎉")
