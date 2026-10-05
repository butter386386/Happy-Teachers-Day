import streamlit as np
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Happy Teacher's Day!",
    page_icon="🍎",
    layout="centered"
)

# --- BRIGHT & VIBRANT CUSTOM STYLING (CSS) ---
st.markdown("""
    <style>
    /* Vibrant gradient background and universal font styling */
    .stApp {
        background: linear-gradient(135deg, #FF007F, #FF7F00, #7F00FF, #00F0FF);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        color: #FFFFFF;
        font-family: 'Comic Sans MS', 'Segoe UI', sans-serif;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Card styling for readability over bright colors */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.25);
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        text-align: center;
    }

    /* Neon neon headers */
    .main-title {
        font-size: 3.5rem;
        font-weight: bold;
        color: #FFF;
        text-shadow: 0 0 10px #FF007F, 0 0 20px #FF007F, 0 0 30px #FF007F;
        margin-bottom: 10px;
    }

    .sub-title {
        font-size: 1.8rem;
        color: #FFFF00;
        text-shadow: 0 0 8px #FF7F00;
        margin-bottom: 20px;
    }

    /* Pulse animation for code elements */
    .code-box {
        background-color: #1E1E1E;
        color: #39FF14; /* Neon Green */
        padding: 15px;
        border-radius: 10px;
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        box-shadow: 0 0 15px #39FF14;
        display: inline-block;
        margin: 15px 0;
    }
    </style>
""", unsafe_gradient=True)

# --- AUDIO CAPABILITY (OPTIONAL) ---
# If you have a celebratory music track, you can un-comment the lines below:
# st.audio("celebration_music.mp3", format="audio/mp3", start_time=0)

# --- HEADER SECTION ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">🌟 HAPPY TEACHER\'S DAY! 🌟</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="sub-title">To the Best Computer Science Teacher Ever! 💻✨</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- THE APOLOGY & APPRECIATION CARD ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.subheader("🎈 A Very Special Message Just For You 🎈")
st.write(
    "Dear Teacher, I am incredibly sorry that I missed wishing you on the exact day! "
    "You always keep our minds compiled, free of syntax errors, and fully optimized. "
    "To make up for my late wish, I built this custom app entirely for you!"
)
st.write(
    "Thank you for being the ultimate compiler for my knowledge, debugging my mistakes, "
    "and always upgrading my programming skills. You are truly irreplaceable!"
)
st.markdown('</div>', unsafe_allow_html=True)

# --- INTERACTIVE COMPUTER SCIENCE TRIBUTE ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.subheader("🖥️ Running Teacher_App.py...")

# Interactive button to run the code
if st.button("👉 CLICK TO EXECUTE APPRECIATION CODE 👈"):
    # Simulated loading logs for a techy feel
    with st.spinner("Compiling admiration scripts..."):
        time.sleep(1)
        st.text("Loading libraries: gratitude, respect, inspiration...")
        time.sleep(1)
        st.text("Status: 0 Errors, 0 Warnings. Success!")
    
    # Beautiful Python syntax themed block
    st.markdown("""
    <div class="code-box">
    <span style="color: #FF79C6;">while</span> True:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;print(<span style="color: #F1FA8C;">"Thank you for being amazing! 🍎"</span>)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;print(<span style="color: #F1FA8C;">"Best Teacher Found in Database!"</span>)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #FF79C6;">break</span> <span style="color: #6272A4;"># But our respect never ends!</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Celebratory balloons!
    st.balloons()
    st.success("🎉 Code executed successfully! Your teaching style is flawless! 🎉")
else:
    st.info("Click the button above to run the special program built for you!")

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(
    '<div style="text-align: center; margin-top: 50px; color: #FFF; font-size: 0.9rem; opacity: 0.8;">'
    'Made with 💻, ☕, and lots of respect | Better late than never! ❤️'
    '</div>', 
    unsafe_allow_html=True
)
