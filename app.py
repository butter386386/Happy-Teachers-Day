import streamlit as st
import datetime

# 1. Page Configuration
st.set_page_config(
    page_title="Teacher's Daily Companion & Apology Workspace",
    page_icon="🇨🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Ultra-Bright, Professional Pastel Theme Styling
st.markdown(
    """
    <style>
    /* Clean, ultra-bright gradient background */
    .stApp {
        background: linear-gradient(135deg, #f0f4f8 0%, #e6fffa 50%, #fff5f5 100%);
    }
    
    /* Vibrant, elegant title font styling */
    .bright-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(to right, #ff4b4b, #ff7675, #6c5ce7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2px;
    }
    .bright-sub {
        color: #2d3436;
        text-align: center;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 30px;
    }

    /* Premium bright, highly visible custom containers */
    .utility-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .utility-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #2d3436;
        margin-bottom: 15px;
        border-left: 5px solid #ff4b4b;
        padding-left: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Automatic Opening Balloon Welcome
st.balloons()

# 4. Bright Header Setup
st.markdown("<h1 class='bright-title'>🎈 Welcome to Your Daily Expat Toolkit! 🇨🇳</h1>", unsafe_allow_html=True)
st.markdown("<p class='bright-sub'>A Heartfelt Apology Turned into Something Useful Every Day</p>", unsafe_allow_html=True)

# 5. The Core Apology Statement (Highly visible on white panel)
with st.container(border=True):
    st.markdown(
        """
        ### 👋 Dear Teacher,
        I am so incredibly sorry for missing your Teacher's Day wish and requiring a reminder! 
        Since you are currently exploring and working in **China**, I wanted to build you a live workspace that 
        isn't just an apology, but a **practical tool you can use every single day** to navigate your environment!
        """
    )

st.write("")

# 6. Functional Two-Column Desktop Layout
col1, col2 = st.columns(2, gap="large")

with col1:
    # FUNCTION 1: Live Local Currency Converter
    st.markdown("<div class='utility-card'>", unsafe_allow_html=True)
    st.markdown("<div class='utility-title'>💱 Real-Time CNY Shopping Converter</div>", unsafe_allow_html=True)
    st.write("Quickly convert Chinese Yuan (RMB) to keep track of store prices:")
    
    cny_amount = st.number_input("Enter Amount in Chinese Yuan (¥):", min_value=0.0, value=10.0, step=1.0)
    
    # Custom rate configuration slider (so she can adjust it easily without redeploying)
    conversion_rate = st.slider("Current Exchange Rate (e.g., 1 USD to CNY):", min_value=1.0, max_value=100.0, value=7.25, step=0.01)
    converted_val = cny_amount / conversion_rate
    
    st.subheader(f"💵 Approx. Foreign Currency value: ${converted_val:.2f}")
    st.markdown("</div>", unsafe_allow_html=True)

    # FUNCTION 2: Global Dual Time Clock Matrix
    st.markdown("<div class='utility-card'>", unsafe_allow_html=True)
    st.markdown("<div class='utility-title'>🕒 Dual Time-Zone Synchronizer</div>", unsafe_allow_html=True)
    st.write("Never mix up hours when scheduling calls or classes back home.")
    
    # Generate time calculations based on system time offsets
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    china_time = utc_now + datetime.timedelta(hours=8)
    
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.metric(label="🇨🇳 China Standard Time", value=china_time.strftime("%I:%M %p"))
    with t_col2:
        # Easy drop-down for her to sync to her home time zone offset
        home_offset = st.selectbox("Select Your Home Timezone Offset (UTC):", options=list(range(-12, 15)), index=17) # Default index to typical home offset
        home_time = utc_now + datetime.timedelta(hours=home_offset)
        st.metric(label="🏠 Home Local Time", value=home_time.strftime("%I:%M %p"))
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    # FUNCTION 3: Survival Phrasebook (Highly functional for a new expat!)
    st.markdown("<div class='utility-card'>", unsafe_allow_html=True)
    st.markdown("<div class='utility-title'>🗣️ Daily Expat Survival Phrasebook</div>", unsafe_allow_html=True)
    st.write("Quickly copy-paste or read important phrases to locals while traveling:")
    
    phrase_category = st.radio("Select Situation Matrix:", ["🚕 Taking a Taxi", "🍲 Ordering Food", "🛍️ Shopping & Payments"], horizontal=True)
    
    if "Taxi" in phrase_category:
        st.info("**Please take me to this address:**\n\n请带我去这个地址 (Qǐng dài wǒ qù zhège dìzhǐ)")
        st.info("**Stop here, thank you:**\n\n请在这里停车，谢谢 (Qǐng zài zhèlǐ tíngchē, xièxiè)")
    elif "Food" in phrase_category:
        st.success("**I would like to order this:**\n\n我要点这个 (Wǒ yào diǎn zhège)")
        st.success("**Not too spicy, please:**\n\n请不要太辣 (Qǐng bùyào tài là)")
    elif "Shopping" in phrase_category:
        st.warning("**How much is this?**\n\n这个多少钱？ (Zhège duōshǎo qián?)")
        st.warning("**Can I pay with WeChat Pay?**\n\n可以用微信支付吗？ (Kěyǐ yòng Wēixìn zhīfù ma?)")
    st.markdown("</div>", unsafe_allow_html=True)

    # FUNCTION 4: The Ultimate Interactive Balloon Triggers
    st.markdown("<div class='utility-card'>", unsafe_allow_html=True)
    st.markdown("<div class='utility-title'>🎈 The Stress-Relief Balloon Spam Zone</div>", unsafe_allow_html=True)
    st.write("Click these custom buttons to trigger massive balloon cascades whenever class gets stressful!")
    
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("🔴 Fire Red Waves", use_container_width=True, type="primary"):
            st.balloons()
    with b2:
        if st.button("🔵 Fire Blue Waves", use_container_width=True):
            st.balloons()
    with b3:
        if st.button("🟢 Fire Green Waves", use_container_width=True):
            st.balloons()
            
    # Checkbox closure confirmation
    accepted = st.checkbox("Teacher, check this box if you accept my apology! 🤝")
    if accepted:
        st.balloons()
        st.toast("Success! Apology logged successfully.", icon="💖")
        st.success("Thank you so much! Wishing you an incredible journey ahead in China! 🏔️✨")
    st.markdown("</div>", unsafe_allow_html=True)

# 7. Bright, Minimalist Professional Footer
st.write("---")
st.markdown(
    "<p style='text-align:center; color:#7f8c8d; font-family:sans-serif; font-size:13px;'>Built exclusively for a wonderful Computer Science Teacher. Have a safe and amazing stay in China!</p>",
    unsafe_allow_html=True
)
