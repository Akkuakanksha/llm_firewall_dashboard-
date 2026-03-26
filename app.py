import streamlit as st
import pandas as pd
from classifier import classify_prompt

# 🔹 Page config
st.set_page_config(page_title="LLM Firewall", layout="centered")

# 🔹 Custom CSS (UI MAGIC)
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #00ADB5;
}
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #00ADB5;
    font-weight: 600;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #1c1f26;
    margin-bottom: 20px;
}
.safe {
    color: #00FFAB;
    font-weight: bold;
}
.unsafe {
    color: #FF4C4C;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 🔹 Keyword filter
def keyword_filter(text):
    keywords = ["hack", "attack", "kill", "bypass", "violence", "hate", "password", "bank", "data"]
    for word in keywords:
        if word in text.lower():
            return "unsafe"
    return "safe"

# 🔹 Title
st.markdown('<div class="title">🔐 LLM Firewall Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Guardrails for Prompt Safety</div>', unsafe_allow_html=True)

st.write("")

# 🔹 Input Card
st.markdown('<div class="card">', unsafe_allow_html=True)

threshold = st.slider("⚙️ Set Strictness Threshold", 0.1, 1.0, 0.6)

user_input = st.text_area("✍️ Enter Prompt")

analyze = st.button("🚀 Analyze")

st.markdown('</div>', unsafe_allow_html=True)

# 🔹 Result Card
if analyze:

    result = classify_prompt(user_input)
    keyword_result = keyword_filter(user_input)

    if keyword_result == "unsafe" or result["confidence"] > threshold:
        verdict = "unsafe"
        verdict_class = "unsafe"
    else:
        verdict = "safe"
        verdict_class = "safe"

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🔍 Result")

    st.markdown(f"### Verdict: <span class='{verdict_class}'>{verdict.upper()}</span>", unsafe_allow_html=True)
    st.write(f"📂 Category: {result['category']}")
    st.write(f"📊 Confidence: {round(result['confidence'], 2)}")
    st.write(f"🧠 Keyword Filter: {keyword_result}")

    st.markdown('</div>', unsafe_allow_html=True)

# 🔹 Evaluation Section
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📊 Evaluation Metrics")

try:
    df = pd.read_csv("results.csv")

    total = len(df)
    correct = sum(df["true"] == df["model"])
    accuracy = correct / total

    false_pos = len(df[(df["model"] == "unsafe") & (df["true"] == "safe")])
    false_neg = len(df[(df["model"] == "safe") & (df["true"] == "unsafe")])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total", total)
    col2.metric("Accuracy", round(accuracy, 2))
    col3.metric("False Positives", false_pos)
    col4.metric("False Negatives", false_neg)

    st.write("")
    st.dataframe(df)

except:
    st.write("Run evaluation.py first")

st.markdown('</div>', unsafe_allow_html=True)