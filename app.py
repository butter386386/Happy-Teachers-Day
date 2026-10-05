import streamlit as st

# Set up page configurations
st.set_page_config(
    page_title="Happy Teacher's Day!",
    page_icon="🍎",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling the application beautifully
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f9fc;
    }
    .header-text {
        color: #2E4053;
        font-family: 'Georgia', serif;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-text {
        color: #5D6D7E;
        font-family: 'Arial', sans-serif;
        text-align: center;
        font-size: 18px;
        margin-bottom: 25px;
    }
    .card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 5px solid #3498DB;
        margin-bottom: 20px;
    }
    .card-title {
        color: #2980B9;
        font-family: 'Arial', sans-serif;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .card-body {
        color: #34495E;
        font-size: 16px;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        color: #95A5A6;
        font-size: 14px;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_attributes_allowed=True,
)

# Header Section
st.markdown("<h1 class='header-text'>🎒 Happy Teacher's Day! 🍎</h1>", unsafe_attributes_allowed=True)
st.markdown("<p class='sub-text'>Better late than never, to the best Computer Teacher!</p>", unsafe_attributes_allowed=True)

# Visual element: Trigger balloons right away to make it celebratory
st.balloons()

# The Heartfelt Apology Card
st.markdown(
    """
    <div class='card'>
        <div class='card-title'>Dear Teacher, 💻✨</div>
        <div class='card-body'>
            I am incredibly sorry that I missed wishing you on Teacher's Day. 
            You had to remind me, and I have been feeling completely terrible about it ever since! 
            Please accept my sincerest apologies. You truly deserve to be celebrated every day for the patience and wisdom you bring to the classroom.
        </div>
    </div>
    """,
    unsafe_attributes_allowed=True,
)

# The Appreciation Card
st.markdown(
    """
    <div class='card' style='border-left: 5px solid #2ECC71;'>
        <div class='card-title'>Why You Are Awesome! 🚀</div>
        <div class='card-body'>
            Thank you for making complex code simple, for debugging our errors with a smile, 
            and for inspiring us to build amazing things. Your impact goes way beyond the computer lab!
        </div>
    </div>
    """,
    unsafe_attributes_allowed=True,
)

# Interactive Features
st.write("---")
st.markdown("### 🌟 Interaction Zone")

# Button to let her trigger more animations
if st.button("Click here for a surprise! 🎉"):
    st.balloons()
    st.confetti()  # Works automatically if streamlit elements update
    st.success("You are the best teacher ever! 🙌")

# A small card where you can change the status
accepted = st.checkbox("Teacher, have you accepted my apology? 🥺👉👈")
if accepted:
    st.balloons()
    st.markdown(
        "<div style='background-color:#D4EFDF; padding:15px; border-radius:10px; color:#196F3D; font-weight:bold; text-align:center;'>Yay! Thank you so much for being so forgiving! You're the best! 💖</div>", 
        unsafe_attributes_allowed=True
    )

# Footer
st.write("---")
st.markdown("<p class='footer'>Made with Python, Streamlit, and a whole lot of respect.</p>", unsafe_attributes_allowed=True)
