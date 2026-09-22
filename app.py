if st.button("Scan for Threats"):
    if user_input.strip():
        # This spinner keeps the user informed while the model processes the text
        with st.spinner("🕵️ Analyzing text for scam indicators and calculating threat index... Please wait."):
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
                
                response = model.generate_content(prompt, stream=True)
                
                st.write("### Analysis Results:")
                message_placeholder = st.empty()
                full_response = ""
                
                for chunk in response:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                st.error(f"SYSTEM ERROR: {e}")
    else:
        st.warning("Please paste some text to scan.")
