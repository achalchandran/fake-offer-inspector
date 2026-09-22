# fake-offer-inspector

# 🕵️ Fake Offer Letter & Phishing Inspector

An AI-powered security scanner built for the **PromptWars** hackathon. This application helps job seekers detect recruitment fraud, payment scams, and high-pressure phishing tactics by analyzing suspicious job offer text in real-time and calculating a dynamic **Scam Threat Index**.

---

## 🚀 Live Demo & Links
* **Live Application:** [Access Deployed App](https://fake-offer-inspector-pvzckyqxbkcrmpiqnfvkcy.streamlit.app)
* **GitHub Repository:** [View Source Code](https://github.com/achalchandran/fake-offer-inspector)

---

## 🛠️ Tech Stack & Architecture
* **Frontend & Backend:** Python, Streamlit
* **AI Model:** Google Gemini API (`gemini-3.6-flash`) via Google AI Studio
* **Deployment Platform:** Streamlit Community Cloud
* **Security:** Secure environment variable configuration using Streamlit Secrets.

---

## ✨ Key Features
1. **Real-Time Threat Analysis:** Pasted job descriptions or emails are instantly analyzed for hidden red flags.
2. **Dynamic Scam Threat Index:** Computes a risk percentage (0–100%) to visually quantify the likelihood of a scam.
3. **Structured Breakdown:** Generates a concise summary, bulleted red flags (e.g., equipment deposit traps, sketchy payment demands), and safety recommendations.
4. **Streaming Output:** Provides live typing feedback using Gemini's streaming capabilities for a fast, responsive user experience.

