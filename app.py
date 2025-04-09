import streamlit as st

st.set_page_config(page_title="Growth Mindset Project", page_icon="🧠")
st.title("🧠Growth Mindset Challenge: Web App with Streamlit")

st.header("📈 Welcome to Your Growth Journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 🌟")

# Quote Section
st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill")

# Challenge Input
st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You are facing: {user_input}. Keep pushing forward towards your goal! 🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection Section
st.header("✨ Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"🔆 Great insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experiences helps you grow! Share your thoughts.")

# Achievement Section
st.header("🏆 Celebrate Your Wins!")
achivement = st.text_input("Share something you've recently accomplished:")

if achivement:
    st.success(f"🌠 Amazing! You achieved: {achivement}")
else:
    st.info("Big or small, every achievement counts! Share one now 🤩")

# Footer
st.write("---")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! ⭐")
st.write("**⛔ Created by Mizna Moin**")
