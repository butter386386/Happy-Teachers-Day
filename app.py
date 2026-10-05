import streamlit as st
import time

# --- 1. PAGE CONFIGURATION (MUST BE FIRST) ---
st.set_page_config(
    page_title="Happy Teacher's Day!",
    page_icon="🍎",
    layout="centered"
)

# --- 2. BRIGHT & VIBRANT CUSTOM STYLING (CSS) ---
st.markdown("""
    <style>
    /* Ultra-bright neon shifting gradient background */
    .stApp {
        background: linear-gradient(135deg, #FF007F, #FF7F00, #7F00FF, #00F0FF);
        background-size: 300% 300%;
        animation: gradientBG 8s ease infinite;
        color: #FFFFFF;
        font-family: 'Comic Sans MS', 'Segoe UI', sans-serif;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Glassmorphism cards for readability over bright colors */
    .glass-card {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.4);
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        text-align: center;
    }

    /* Vibrant Glow Titles */
    .main-title {
        font-size: 3.5rem;
        font-weight: bold;
        color: #FFF;
        text-shadow: 0 0 10px #FF007F, 0 0 20px #FF007F, 0 0 40px #FF007F;
        margin-bottom: 10px;
    }

    .sub-title {
        font-size: 1.8rem;
        color: #FFFF00;
        text-shadow: 0 0 10px #FF7F00;
        margin-bottom: 20px;
    }

    /* Neon Terminal Box */
    .code-box {
        background-color: #121212;
        color: #39FF14; /* Cyber Neon Green */
        padding: 20px;
        border-radius: 12px;
        font-family: 'Courier New', monospace;
        font-size: 1.2rem;
        box-shadow: 0 0 20px #39FF14;
        display: inline-block;
        margin: 15px 0;
        text-align: left;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. HEADER SECTION ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">🌟 HAPPY TEACHER\'S DAY! 🌟</h1>', unsafe_allow_html=True)
# TODO: You can change "Dear Teacher" to her actual name below!
st.markdown('<h3 class="sub-title">To My Amazing Computer Science Teacher! 💻✨</h3>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. THE APOLOGY & APPRECIATION CARD ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.subheader("🎈 A Very Special Message Just For You 🎈")
st.write(
    "Dear Teacher, I am incredibly sorry that my message is reaching you late! "
    "You always keep our minds compiled, free of syntax errors, and fully optimized. "
    "To make up for missing the day, I built this custom web application just for you!"
)
st.write(
    "Thank you for being the ultimate compiler for my knowledge, debugging my mistakes, "
    "and always upgrading my programming skills. You are the best mentor anyone could ask for!"
)
st.markdown('</div>', unsafe_allow_html=True)

# --- 5. INTERACTIVE COMPUTER SCIENCE TRIBUTE ---
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.subheader("🖥️ Running Appreciation_Script.py...")

# Interactive compilation button
if st.button("👉 CLICK TO EXECUTE RESPECT_CODE 👈"):
    with st.spinner("Compiling admiration scripts..."):
        time.sleep(1)
        st.text("Loading libraries: gratitude, respect, inspiration...")
        time.sleep(1)
        st.text("Status: 0 Errors, 0 Warnings. Optimization Complete!")
    
    # Python-themed thank you card
    st.markdown("""
    <div class="code-box">
    <span style="color: #FF79C6;">while</span> True:<br>
    &nbsp;&nbsp;&nbsp;&nbsp;print(<span style="color: #F1FA8C;">"Thank you for being awesome! 🍎"</span>)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;print(<span style="color: #F1FA8C;">"Best Teacher Found in Database!"</span>)<br>
    &nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #FF79C6;">break</span> <span style="color: #6272A4;"># But my respect never ends!</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Triggers on-screen balloon animations
    st.balloons()
    st.success("🎉 Code executed seamlessly! Your teaching style is flawless! 🎉")
else:
    st.info("Click the button above to execute the program built for you!")

st.markdown('</div>', unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown(
    '<div style="text-align: center; margin-top: 50px; color: #FFF; font-size: 0.9rem; opacity: 0.9; text-shadow: 0 0 5px #000;">'
    'Made with 💻, ☕, and absolute respect | Better late than never! ❤️'
    '</div>', 
    unsafe_allow_html=True
)
