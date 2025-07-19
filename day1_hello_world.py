# hello_world_app.py

import streamlit as st

# --------------------------
# Day 1: Streamlit Challenge
# --------------------------

st.set_page_config(page_title="Hello World", page_icon="👋")

# Title Section
st.title("👋 Hello World!")
st.caption("Kickstarting the #50Days Phython Chalange 🚀")

# Introduction
st.markdown("""
Welcome to **Day 1** of our coding adventure.

Let's explore the magic of Python and **Streamlit** by starting simple:

---

### 🎯 Goals for Today
- 🧱 Learn basic components
- 🖋️ Practice markdown formatting
- 🎉 Stay consistent and curious!

---

""")

# Highlight message
st.info("🌟 Pro Tip: Small progress every day adds up to big results!")

# Footer motivation
st.success("✅ Day 1 complete — onwards to greatness!")
