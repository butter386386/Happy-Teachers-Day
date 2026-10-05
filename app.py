import streamlit as st
import datetime

# 1. Page Settings with Clean Theme
st.set_page_config(
    page_title="For My Computer Teacher",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium Light Mode CSS Styling
st.markdown(
    """
    <style>
    /* Clean, ultra-bright executive light background */
    .stApp {
        background-color: #FAFAFA;
    }
    
    /* Elegant typography */
    .hero-title {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 3.2rem;
        font-weight: 700;
        color: #1E293B;
        text-align: center;
        margin-bottom: 5px;
    }
    .hero-subtitle {
        font-family: 'Courier New', Courier, monospace;
        font-size: 1.2rem;
        color: #64748B;
        text-align: center;
        margin-bottom: 35px;
    }

    /* Beautiful, clean white cards with crisp borders */
    .premium-card {
        background-color: #FFFFFF;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        border: 1px solid #E2E8F0;
        margin-bottom: 25px;
    }
    
    .card-heading {
        font-size: 1.4rem;
        font-weight: 600;
        color: #0F172A;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* Styling adjustments for a polished finish */
    div.stButton > button {
        background-color: #4F46E5 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Fire Initial Wave of Balloons Immediately
st.balloons()

# 4. Beautiful Header Section
st.markdown("<h1 class='hero-title'>Happy Teacher's Day! 🎈</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='hero-subtitle'>// A Heartfelt Apology & Smart China Toolkit</h3>", unsafe_allow_html=True)

# 5. The Heartfelt Apology Card
st.markdown(
    """
    <div class='premium-card'>
        <div class='card-heading'>✉️ Sincerest Apologies</div>
        <p style='color: #334155; font-size: 1.1rem; line-height: 1.7; margin: 0;'>
            <b>Dear Teacher,</b><br><br>
            I am incredibly sorry that I forgot to wish you on Teacher's Day and required a reminder. 
            As my computer teacher, you spend so much time helping us debug our syntax errors and understand complex logic. 
            I feel terribly sorry about my oversight. To make it up to you, I built this pristine workspace to serve as a handy, 
            everyday companion during your time in China.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# 6. Grid Layout for the Everyday Tools
col1, col2 = st.columns(2, gap="large")

with col1:
    # TOOL 1: Instant RMB Price Converter
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-heading'>💱 China Shopping Converter</div>", unsafe_allow_html=True)
    st.write("Instantly convert Chinese Yuan (RMB / ¥) to check grocery or store prices:")
    
    rmb_amount = st.number_input("Enter Amount in Yuan (¥):", min_value=0.0, value=100.0, step=10.0)
    exchange_rate = st.slider("Set Current Exchange Rate (e.g., 1 USD to CNY):", min_value=5.0, max_value=10.0, value=7.25, step=0.01)
    
    usd_value = rmb_amount / exchange_rate
    st.markdown(f"### 💵 Converted Value: **${usd_value:.2f} USD**")
    st.markdown("</div>", unsafe_allow_html=True)

    # TOOL 2: Dual Clock
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-heading'>🕒 Dual Time-Zone Sync</div>", unsafe_allow_html=True)
    st.write("Stay perfectly synchronized with family and classes back home.")
    
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    china_time = utc_now + datetime.timedelta(hours=8)
    home_time = utc_now + datetime.timedelta(hours=5, minutes=30) # Defaulting to common standard timezone
    
    clk1, clk2 = st.columns(2)
    with clk1:
        st.metric(label="🇨🇳 China Standard (CST)", value=china_time.strftime("%I:%M %p"))
    with clk2:
        st.metric(label="🏠 Home Local Time", value=home_time.strftime("%I:%M %p"))
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # TOOL 3: Everyday Expat Phrasebook
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-heading'>🗣️ Daily Life Survival Phrases</div>", unsafe_allow_html=True)
    st.write("Essential phrases she can read or point to while navigating locally:")
    
    category = st.selectbox("Choose a Scenario:", ["🚕 Taking a Taxi", "🍲 Ordering Food", "🛍️ Shopping & Payments"])
    
    if "Taxi" in category:
        st.info("**Take me to this address, please:**\n\n请带我去这个地址 (Qǐng dài wǒ qù zhège dìzhǐ)")
        st.info("**Please stop here:**\n\n请在这里停车 (Qǐng zài zhèlǐ tíngchē)")
    elif "Food" in category:
        st.success("**I would like to order this:**\n\n我要点这个 (Wǒ yào diǎn zhège)")
        st.success("**Not too spicy, please:**\n\n请不要太辣 (Qǐng bùyào tài là)")
    elif "Shopping" in category:
        st.warning("**How much is this?**\n\n这个多少钱？ (Zhège duōshǎo qián?)")
        st.warning("**Can I pay with WeChat Pay?**\n\n可以用微信支付吗？ (Kěyǐ yòng Wēixìn zhīfù ma?)")
    st.markdown("</div>", unsafe_allow_html=True)

    # TOOL 4: Massive Balloon Blast Center
    st.markdown("<div class='premium-card'>", unsafe_allow_html=True)
    st.markdown("<div class='card-heading'>🎈 Balloon Blast Control</div>", unsafe_allow_html=True)
    st.write("Whenever things get busy, click below for an immediate celebration overlay:")
    
    if st.button("🚀 LAUNCH BALLOONS 🚀", use_container_width=True):
        st.balloons()
        
    st.write("")
    accepted = st.checkbox("Teacher, please check this box to officially accept my apology! 🥺")
    if accepted:
        st.balloons()
        st.success("Apology Accepted! Thank you for being the most amazing teacher! 💖")
    st.markdown("</div>", unsafe_allow_html=True)

# 7. Minimalist Professional Footer
st.write("---")
st.markdown(
    "<p style='text-align: center; color: #94A3B8; font-family: monospace; font-size: 0.85rem;'>// Crafted using Python & Streamlit | Dedicated to a phenomenal educator.</p>",
    unsafe_allow_html=True
)
