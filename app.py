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
        try:
            model = genai.GenerativeModel('gemini-3.6-flash')
            prompt = f"""
            Analyze the following job offer text for a security scan.
            1. Identify payment demand red flags (e.g., pay-for-equipment, deposit traps).
            2. Check for unusual urgency or unprofessional language.
            3. Calculate a dynamic Scam Threat Index from 0 to 100%.
            
            Provide a concise summary, list the red flags as bullet points, and display the final Scam Threat Index in bold at the top.
            
            Job Offer: {user_input}
            """
            
            # Request a streaming response from the AI
            response = model.generate_content(prompt, stream=True)
            
            st.write("### Analysis Results:")
            
            # Create an empty container to hold the typing text
            message_placeholder = st.empty()
            full_response = ""
            
            # Update the text live as the AI generates it
            for chunk in response:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
            
            # Remove the cursor block when finished
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"SYSTEM ERROR: {e}")
    else:
        st.warning("Please paste some text to scan.")
