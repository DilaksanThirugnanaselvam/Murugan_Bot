முருகன் Bot 🤖🙏

A culturally inspired AI chatbot dedicated to Lord Murugan (முருகன்), the Tamil deity of war and youth, built with Retrieval-Augmented Generation (RAG), LangChain, and Streamlit.
An AI-powered journey into the world of Lord Murugan and Tamil diaspora worship.
🌟 About the Project
Murugan Bot is an interactive chatbot that answers queries about Lord Murugan, his mythology, temples (ஆறுபடை வீடு), festivals like Thaipusam (தைப்பூசம்), and worship practices among the Tamil diaspora, including Thamizh Muppattan (தமிழ் முப்பாட்டன்) in Mauritius and Eezham Thamizh Muruga Valipadu (ஈழத் தமிழ் முருக வழிபாடு) in Sri Lanka. By combining Retrieval-Augmented Generation (RAG) with real-time web search, the bot delivers accurate, culturally rich responses in English and Tamil.
Key Features

RAG-Powered Knowledge Base: Retrieves precise information from murugan_knowledge.txt using LangChain and FAISS with sentence-transformers/all-MiniLM-L6-v2 embeddings.
Real-Time Web Search: Integrates DuckDuckGo for up-to-date information beyond the knowledge base.
Interactive UI: Built with Streamlit for a user-friendly chat experience, supporting Tamil text (UTF-8 encoded).
Cultural Focus: Covers Murugan’s significance in Tamil culture, including festivals and diaspora traditions.
Robust AI: Powered by Grok’s llama3-70b-8192 model via the Groq API for fast, reliable responses.

🛠️ Tech Stack

Python: 3.10+ (tested with 3.13.2)
LangChain: For RAG and agent-based workflows
FAISS: Vector store for efficient document retrieval
HuggingFace: Embeddings via sentence-transformers
Streamlit: Interactive web interface
Groq: LLM backend for natural language processing
DuckDuckGo: Real-time web search
uv: Dependency management

🚀 Getting Started
Prerequisites

Python 3.10+: Ensure Python is installed (3.13.2 works, but 3.10 is recommended for compatibility).
uv: For dependency management (install via pip install uv).
Tamil Font: Install Noto Sans Tamil for proper rendering of Tamil text (e.g., முருகன்).
Groq API Key: Obtain from x.ai.

Installation

Clone the Repository:
git clone 
cd murugan_bot


Set Up Virtual Environment:
python -m venv .venv
.venv\Scripts\activate  # Windows
# or source .venv/bin/activate  # Linux/macOS


Install Dependencies:
uv sync

Or:
uv pip install .


Configure Environment:

Create a .env file in D:\murugan_bot:echo GROQ_API_KEY=your_groq_api_key_here > .env


Replace your_groq_api_key_here with your Groq API key.


Prepare Knowledge Base:

Ensure data/murugan_knowledge.txt exists with content about Lord Murugan:mkdir data
echo Lord Murugan (முருகன்) is a Hindu deity revered by Tamils worldwide... > data\murugan_knowledge.txt


Example content:Lord Murugan (முருகன்) is a Hindu deity revered by Tamils worldwide, known as the god of war and youth. His six primary temples, known as Arupadai Veedu (ஆறுபடை வீடு), include Tirupparankunram, Tiruchendur, Palani, Swamimalai, Thiruthani, and Pazhamudircholai. Thaipusam (தைப்பூசம்) is a major festival where devotees carry Kavadi (காவடி) to honor Murugan. Among Thamizh Muppattan (தமிழ் முப்பத்தான்) in Mauritius, Murugan worship includes vibrant processions at temples like Sockalingum Meenatchee Ammen Kovil. In Sri Lanka, Eezham Thamizh Muruga Valipadu (ஈழத் தமிழ் முருக வழிபாடு) centers around Nallur Kandaswamy Kovil, with festivals like Kanda Shasti.





Running the Bot

Test the Agent:
python agent.py


Expected output:Testing query: How do Eelam Tamils worship Murugan?
[Agent reasoning logs...]
Response: ஈழத் தமிழ் முருக வழிபாடு (Eezham Thamizh Muruga Valipadu) ஈழத் தமிழர்களிடையே ஆழமான பக்தியைக் குறிக்கிறது. யாழ்ப்பாணத்தில் உள்ள நல்லூர் கந்தசுவாமி கோவில் (Nallur Kandaswamy Kovil) முக்கியமான தலமாகும், அங்கு தைப்பூசம் மற்றும் கந்த சஷ்டி போன்ற பண்டிகைகள் பாரம்பரிய தமிழ் இசை மற்றும் நடனத்துடன் கொண்டாடப்படுகின்றன.




Run the Streamlit UI:
streamlit run app.py

Or:
uv run streamlit run app.py


Opens http://localhost:8501 for interactive chat.



Usage

Query Examples:
"What are Murugan’s temples?"
"தைப்பூசம் என்றால் என்ன?" (What is Thaipusam?)
"How do Eelam Tamils worship Murugan?"


Output Example:Among Thamizh Muppattan (தமிழ் முப்பத்தான்), the Tamil diaspora in Mauritius, Murugan worship is vibrant. Temples like the Sockalingum Meenatchee Ammen Kovil in Port Louis host grand Thaipusam (தைப்பூசம்) celebrations with Kavadi processions (காவடி ஆட்டம்) and cultural events, reflecting the community’s deep devotion to முருகன்.

📧 Contact

Author: Dilaksan Thirugnanaselvam
Email: thirudilak131@gmail.com

🙏 Acknowledgments

LangChain for powerful RAG and agent tools.
Grok and xAI for the fast llama3-70b-8192 model.
Streamlit for an intuitive UI.
The global Tamil community for preserving Murugan’s legacy.


Let’s celebrate Tamil culture through AI!Star ⭐ this repo if you find it useful, and share your feedback to make Murugan Bot even better!
