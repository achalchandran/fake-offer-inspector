import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Phishing Inspector", page_icon="🕵️")

st.title("Fake Offer Letter & Phishing Inspector")
st.write("Paste a suspicious job offer below to calculate its Scam Threat Index.")

# Configure API key securely using Streamlit Secrets
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

user_input = st.text_area("Job Offer Text:", height=200)

if st.button("Scan for Threats"):
    if user_input.strip():
        with st.spinner("Analyzing text for red flags..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"""
                Analyze the following job offer text for a security scan.
                1. Identify payment demand red flags (e.g., pay-for-equipment, deposit traps).
                2. Check for unusual urgency or unprofessional language.
                3. Calculate a dynamic Scam Threat Index from 0 to 100%.
                
                Provide a concise summary, list the red flags as bullet points, and display the final Scam Threat Index in bold at the top.
                
                Job Offer: {user_input}
                """
                response = model.generate_content(prompt)
                st.markdown(response.text)
            except Exception as e:
                # This will now show us the REAL error message!
                st.error(f"SYSTEM ERROR: {e}")
    else:
        st.warning("Please paste some text to scan.")
