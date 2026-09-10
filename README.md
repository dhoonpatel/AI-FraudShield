# 🛡️ AI FraudShield

> **A Multi-Agent Autonomous Anti-Fraud Honeypot Framework**
> Powered by Strands Agents SDK, Groq Cloud Infrastructure, & Streamlit.

---

## 🚀 Overview
**AI FraudShield** is an innovative, active-defense solution designed to combat the rising wave of digital financial scams, phishing attacks, and social engineering frauds. Instead of just blocking scams, AI FraudShield actively neutralizes scammers using a **Multi-Agent Swarm Intelligence** architecture.

### 👥 The Agent Swarm
1. **Sniffer Agent 🔍**: Real-time evaluation of text inputs, calculating fraud vectors, threat types, and extraction of critical warning flags.
2. **Baiter Agent ("Dadaji") 👴**: An active conversational honeypot. If a threat is detected, this agent assumes the persona of a tech-illiterate, grandfatherly figure who types in broken Hinglish, tells long unrelated stories, and gives incorrect credentials—successfully wasting the scammer's operational time and keeping them away from actual victims.

---

## 📐 Architecture Diagram

![AI FraudShield Architecture](chart.png)

---

## 🛠️ Features
- **Instant Risk Scoring:** Immediate extraction of fraud patterns.
- **Active Honeypot Defense:** Automated counter-scam engagement scripts.
- **Blazing Fast Analytics:** Sub-second inference processing using Groq API tokens.
- **Clean Dashboard UI:** Beautifully structured modern UI built entirely using Streamlit.

---

## ⚙️ Setup & Installation Instructions

Follow these clear steps to clone, configure, and execute the project locally.

### 1. Prerequisites
Ensure you have **Python 3.9+** installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com
cd AI-FraudShield
```

### 3. Install Dependencies
Create a virtual environment and install the required modules:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install streamlit groq
```

### 4. Running the Application
Launch the application server with the following command:
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser to interact with the system.

---

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
