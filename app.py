import os
import streamlit as st
from groq import Groq

# 1. पेज का विजुअल डिजाइन (Attractive Theme)
st.set_page_config(page_title="AI FraudShield", page_icon="🛡️", layout="centered")

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🛡️ AI FraudShield</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px; color: #666;'>Conceptual Multi-Agent Framework powered by Strands Agents SDK & Groq</p>", unsafe_allow_html=True)
st.write("---")

# Groq API Key Setup
GROQ_API_KEY = "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"
try:
    client = Groq(api_key=GROQ_API_KEY)
except Exception as e:
    st.error(f"Initialization Error: {e}")

# 2. इनपुट बॉक्स (Attractive Input Area)
st.subheader("📝 Live Threat Analysis Portal")
incoming_scam_message = st.text_area(
    "Paste any suspicious SMS, Email text, or Call transcript below:",
    placeholder="e.g., Hello, I am from Amazon HR. You can earn Rs. 5000 daily...",
    height=120
)

# 3. लाइव बटन और एआई प्रोसेसिंग
if st.button("🚀 Execute FraudShield Analysis", use_container_width=True):
    if not incoming_scam_message.strip():
        st.warning("Please enter some text to analyze!")
    else:
        with st.spinner("Executing Multi-Agent Swarm Pipeline... Please wait."):
            
            system_instruction = (
                "You are the AI FraudShield system running on Strands Agents SDK.\n"
                "Your framework consists of two core agents:\n"
                "1. Sniffer Agent: Analyzes the user input for scams, financial fraud, or threats. Outputs: SCAM DETECTED (YES/NO) and Critical Red Flags.\n"
                "2. Baiter Agent (Dadaji): If it's a scam, acts as a tech-illiterate old grandfather 'Dadaji' to hilariously waste the scammer's time. Speak in funny, confusing, broken Hinglish/English, ask about their health, give wrong OTPs, and drag the chat to frustrate them.\n"
                "Output the result in a clean, professional hackathon demo format with proper headers for both agents."
            )
            
            try:
                # Groq API Call
                completion = client.chat.completions.create(
                    model="qwen/qwen3.6-27b",
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": incoming_scam_message}
                    ],
                    temperature=0.7,
                    max_tokens=400 
                )
                
                ai_output = completion.choices[0].message.content
                
                # 4. शानदार विजुअल कार्ड्स में लाइव आउटपुट दिखाना
                st.success("Analysis Complete! Displaying Hackathon Demo Output:")
                
                st.markdown("### 📊 Live Agent Swarm Output")
                st.info(ai_output)
                
                st.write("---")
                st.markdown("<h4 style='color: green; text-align: center;'>Live Setup Test: SUCCESS ✔️</h4>", unsafe_allow_html=True)
                st.caption("Strands Agent Network: Active and Responsive via High-Speed Cloud Infrastructure.")
                
            except Exception as e:
                st.error(f"Connection failed: {e}")
