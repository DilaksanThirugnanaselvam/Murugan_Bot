import os

import streamlit as st
from dotenv import load_dotenv

from agent import create_agent

# Load environment variables
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize agent
agent_executor = create_agent(groq_api_key)

# Streamlit UI Configuration
st.set_page_config(
    page_title="முருகன் Bot - Tamil AI Assistant",
    page_icon="🦚",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Enhanced Custom CSS for attractive Tamil UI
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Tamil:wght@300;400;500;600;700&display=swap');
    
    /* Main background with gold gradient */
    .stApp {
        background: linear-gradient(135deg, #ffd700 0%, #ffed4e 25%, #fff2a1 50%, #ffed4e 75%, #ffd700 100%);
        font-family: 'Noto Sans Tamil', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #b8860b, #daa520, #ffd700);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(184, 134, 11, 0.3);
        text-align: center;
        border: 3px solid #b8860b;
    }
    
    .main-header h1 {
        color: #8b4513;
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        color: #654321;
        font-size: 1.2rem;
        margin: 0.5rem 0 0 0;
        font-weight: 500;
    }
    
    /* Chat message styling */
    .stChatMessage {
        background: linear-gradient(145deg, #fff8dc, #fffacd);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(184, 134, 11, 0.2);
        border: 2px solid #daa520;
        font-family: 'Noto Sans Tamil', sans-serif;
    }
    
    .stChatMessage.user {
        background: linear-gradient(145deg, #e6f3ff, #cce7ff);
        border: 2px solid #4a90e2;
        margin-left: 2rem;
    }
    
    .stChatMessage.assistant {
        background: linear-gradient(145deg, #fff5ee, #ffe4d1);
        border: 2px solid #ff8c42;
        margin-right: 2rem;
    }
    
    /* Image container */
    .image-container {
        text-align: center;
        margin: 2rem 0;
        padding: 1rem;
        background: linear-gradient(145deg, #fff8dc, #fffacd);
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(184, 134, 11, 0.3);
        border: 3px solid #daa520;
    }
    
    /* Input styling */
    .stChatInput > div > div > input {
        background: linear-gradient(145deg, #fff8dc, #fffacd);
        border: 2px solid #daa520;
        border-radius: 25px;
        padding: 1rem 1.5rem;
        font-family: 'Noto Sans Tamil', sans-serif;
        font-size: 1.1rem;
        color: #8b4513;
    }
    
    .stChatInput > div > div > input:focus {
        border-color: #b8860b;
        box-shadow: 0 0 10px rgba(184, 134, 11, 0.5);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #ffd700, #ffed4e);
    }
    
    /* Spinner styling */
    .stSpinner {
        color: #b8860b !important;
    }
    
    /* Tamil text enhancement */
    .tamil-text {
        font-family: 'Noto Sans Tamil', sans-serif;
        font-weight: 500;
        line-height: 1.8;
        color: #654321;
    }
    
    /* Devotional quotes styling */
    .devotional-quote {
        background: linear-gradient(145deg, #ffe4b5, #ffd700);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #b8860b;
        margin: 1rem 0;
        font-style: italic;
        color: #8b4513;
        font-weight: 600;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(145deg, #daa520, #b8860b);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-family: 'Noto Sans Tamil', sans-serif;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(184, 134, 11, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(145deg, #b8860b, #daa520);
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(184, 134, 11, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Header
st.markdown(
    """
    <div class="main-header">
        <h1>🦚 முருகன் Bot</h1>
        <p class="tamil-text">தமிழ் கடவுள் முருகனைப் பற்றி கேளுங்கள் | Powered by AI</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Devotional Quote
st.markdown(
    """
    <div class="devotional-quote tamil-text">
        "வேலுண்டு வினையில்லை மயிலுண்டு பயமில்லை" 
    </div>
    """,
    unsafe_allow_html=True,
)
st.image(
    "murugan.jpg",
    caption="Lord Murugan – Divine Blessings",
    use_container_width=True,  # ✅ Recommended
)


# Sidebar with information
with st.sidebar:
    st.markdown("### 🕉️ முருகன் Bot Features")
    st.markdown("""
    - **தமிழ் மொழி ஆதரவு** (Tamil Language Support)
    - **வேகமான AI பதில்கள்** (Fast AI Responses)
    - **திருவிழாக்கள்** (Festivals Information)
    - **கோயில்கள்** (Temple Details)
    - **மந்திரங்கள்** (Sacred Mantras)
    - **கதைகள்** (Divine Stories)
    """)

    st.markdown("### 🙏 Sample Questions")
    st.markdown("""
    - தைப்பூசம் என்றால் என்ன?
    - What are Murugan's six abodes?
    - முருகன் மந்திரம் சொல்லுங்கள்
    - Tell me about Skanda Sashti
    """)

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(
            f'<div class="tamil-text">{message["content"]}</div>',
            unsafe_allow_html=True,
        )

# User Input
user_input = st.chat_input(
    "முருகன் பெருமானைப் பற்றி கேளுங்கள் (Ask about Lord Murugan in Tamil or English)"
)

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(
            f'<div class="tamil-text">{user_input}</div>', unsafe_allow_html=True
        )
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Generate response
    with st.spinner(
        "முருகன் பெருமான் அருளால் சிந்திக்கிறேன்... (Thinking with Lord Murugan's blessings...)"
    ):
        try:
            response = agent_executor.invoke(
                {
                    "input": user_input,
                    "chat_history": [
                        msg["content"]
                        for msg in st.session_state.chat_history
                        if msg["role"] == "assistant"
                    ],
                }
            )
            output = response["output"]
        except Exception as e:
            output = f"மன்னிக்கவும், தற்போது பதில் அளிக்க முடியவில்லை. (Sorry, unable to respond right now.) Error: {str(e)}"

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(f'<div class="tamil-text">{output}</div>', unsafe_allow_html=True)
    st.session_state.chat_history.append({"role": "assistant", "content": output})

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: linear-gradient(145deg, #fff8dc, #fffacd); border-radius: 15px; border: 2px solid #daa520;">
        <p class="tamil-text" style="color: #8b4513; font-weight: 600;">
            🕉️ யாமிருக்க பயமேன் ! 🕉️<br>
             by டிலக்சன் திருஞானசெல்வம் 🦚
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
