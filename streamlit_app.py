import streamlit as st
import joblib

# Load model and vectorizer
model = joblib.load("scam_classifier_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Streamlit UI
st.title("Craigslist Mobile Ad Scam Detector")
st.write("Paste your ad title and description to check the scam probability.")

title = st.text_input("Ad Title")
description = st.text_area("Ad Description")

if st.button("Analyze"):
    if not title and not description:
        st.warning("Please provide ad title or description.")
    else:
        input_text = title + " " + description
        X_input = vectorizer.transform([input_text])
        prob = model.predict_proba(X_input)[0][1]
        st.metric("Scam Probability", f"{prob:.2%}")
        if prob > 0.7:
            st.error("⚠️ High risk of scam.")
        elif prob > 0.6:
            st.warning("⚠️ Might be suspicious.")
        else:
            st.success("✅ Likely legitimate.")
