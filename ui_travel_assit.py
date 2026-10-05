import streamlit as st 
import base64
from google import genai
from dotenv import load_dotenv
from httpx import stream
import time
from PIL import Image
load_dotenv()

# Load your local stylish E image
favicon = Image.open("emoimage.png")

st.set_page_config(
    page_title="Emo Here",
    page_icon=favicon
)





# Load background image
with open("background.png", "rb") as image:
    background = base64.b64encode(image.read()).decode()

# Background only
st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/png;base64,{background}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stAppViewContainer"] {{
        background: transparent !important;
    }}

    [data-testid="stMain"] {{
        background: transparent !important;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    </style>
    """,
    unsafe_allow_html=True
)






st.markdown("""
<style>
.emo-header {
    position: fixed;
    top: 15px;
    left: 50%;
    transform: translateX(-50%);

    width: 92%;
    max-width: 1400px;
    height: 64px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 0 24px;

    background: rgba(255, 255, 255, 0.00);

    border: 1px solid rgba(255, 255, 255, 0.30);
    border-radius: 18px;

    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(12px);

    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);

    z-index: 999999;
}

.emo-logo {
    display: flex;
    align-items: center;
    gap: 10px;

    color: white;
    font-size: 23px;
    font-weight: 700;
    letter-spacing: 2px;
}

.emo-logo-icon {
    width: 32px;
    height: 32px;

    border-radius: 50%;

    background: rgba(255,255,255,0.18);

    border: 1px solid rgba(255,255,255,0.35);

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 16px;
}

.emo-nav {
    display: flex;
    align-items: center;
    gap: 30px;
    transform: translateY(-3px);
}

.emo-nav a {
    color: rgba(255,255,255,0.90);

    text-decoration: none;

    font-size: 14px;
    font-weight: 500;

    transition: 0.2s ease;
}

.emo-nav a:hover {
    color: white;
}

.emo-live {
    display: flex;
    align-items: center;
    gap: 8px;

    color: white;
    font-size: 13px;
}

.live-dot {
    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #62ff9b;

    box-shadow: 0 0 10px rgba(98,255,155,0.9);

    animation: livePulse 1.5s infinite;
}

@keyframes livePulse {
    0% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(1.35);
        opacity: 0.55;
    }

    100% {
        transform: scale(1);
        opacity: 1;
    }
}

@media (max-width: 700px) {
    .emo-header {
        width: 88%;
        padding: 0 15px;
    }

    .emo-nav {
        display: none;
    }

    .emo-logo {
        font-size: 20px;
    }
    .stButton > button {
    background: transparent !important;
    border: none !important;
    color: rgba(255,255,255,0.90) !important;
    box-shadow: none !important;
    font-size: 14px !important;
}

.stButton > button:hover {
    background: rgba(255,255,255,0.08) !important;
    color: white !important;
    border: none !important;
}
}
</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================
import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "Home"


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home"):
        st.session_state.page = "Home"

with col2:
    if st.button("Explore"):
        st.session_state.page = "Explore"
    
with col3:
    if st.button("My Trips"):
        st.session_state.page = "My Trips"

with col4:
    if st.button("About"):
        st.session_state.page = "About"


st.markdown("""
<div class="emo-header">

<div class="emo-logo">
<div class="emo-logo-icon">E</div>
EMO
</div>
<div class="emo-live">
<div class="live-dot"></div>
Live
</div>

</div>
""", unsafe_allow_html=True)
if st.session_state.page == "Home":

    st.title("Welcome to EMO")
    st.write("Your AI travel assistant.")
    
    client = genai.Client()
    location = st.text_input("Tell me your travel dream")
    days_nr = st.number_input("How many days of trip", min_value=1, max_value=30)
    budget = st.selectbox("Select Budget", ["Luxury", "Moderate", "Budgeted"])
    travel_type = st.radio("With whom you are travelling with", ["Family","Solo", "Friends"])
    prompt = f"""You are a Travel Planner, User is saying he/she wants to 
go to {location} and for {days_nr} days , he is on a budget of type {budget}
Travel Type is :  {travel_type}
Plan a tripo and share answer in bullet format"""

    if st.button("Plan Trip"):
         interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )

         with st.spinner("Wait for it...", show_time=True):
            time.sleep(3)

         st.success("And just like that…!! your journey begins!")
         st.write(interaction.output_text)
    
elif st.session_state.page == "Explore":

    st.title("🌍 Explore the World")
    st.write("""Discover places worth adding to your next journey.

### 🇯🇵 Japan

**Tradition meets the future.**
Explore Tokyo's energy, Kyoto's temples, cherry blossoms, incredible food, and peaceful mountain landscapes.

### 🇮🇹 Italy

**Art, history & unforgettable food.**
Wander through Rome, Venice, Florence and the Amalfi Coast while experiencing centuries of art, architecture and Italian cuisine.

### 🇫🇷 France

**Romance, culture & timeless beauty.**
See Paris, the French Riviera, historic towns and world-famous museums while enjoying French food and café culture.

### 🇨🇭 Switzerland

**Alpine beauty at its finest.**
Experience dramatic mountains, crystal-clear lakes, charming villages and scenic train journeys through the Alps.

### 🇹🇭 Thailand

**Tropical escapes & vibrant culture.**
From Bangkok's energy to Phuket's beaches and Chiang Mai's culture, Thailand offers food, beaches, temples and adventure.

### 🇮🇩 Indonesia

**Islands, nature & rich traditions.**
Discover Bali, volcanic landscapes, tropical beaches, ancient temples and diverse local cultures across thousands of islands.

### 🇦🇺 Australia

**Wild nature meets modern cities.**
Explore Sydney, the Great Barrier Reef, beaches, unique wildlife and vast landscapes made for adventure.

### 🇺🇸 United States

**A country of endless possibilities.**
Experience New York's skyline, California's coast, national parks, iconic cities and landscapes that change dramatically from state to state.

### 🇪🇸 Spain

**Sun, culture & unforgettable experiences.**
Enjoy Barcelona's architecture, Madrid's energy, Mediterranean beaches, historic cities and world-famous Spanish cuisine.

### 🇬🇷 Greece

**Ancient history & island escapes.**
Discover Athens, whitewashed island villages, turquoise waters, ancient ruins and spectacular Mediterranean sunsets.

### 🇦🇪 United Arab Emirates

**Futuristic cities & desert adventures.**
Experience Dubai and Abu Dhabi's modern architecture, luxury attractions, desert landscapes and vibrant city life.

### 🇳🇿 New Zealand

**Pure nature & adventure.**
Explore dramatic mountains, peaceful lakes, green landscapes and spectacular outdoor experiences across both islands.

### 🇸🇬 Singapore

**Small country, big experiences.**
Discover futuristic architecture, incredible food, clean cityscapes, Gardens by the Bay and a fascinating mix of cultures.

### 🇹🇷 Türkiye

**Where continents and cultures meet.**
Explore Istanbul's historic streets, Cappadocia's unique landscapes, Mediterranean coastlines and centuries of history.

### 🇿🇦 South Africa

**Wildlife, landscapes & adventure.**
Go beyond Cape Town to discover dramatic coastlines, mountains, national parks and unforgettable wildlife experiences.
""")

elif st.session_state.page == "My Trips":

    st.title("My Trips")
    st.write("Your saved trips will appear here.")

elif st.session_state.page == "About":

    st.title("About EMO")
    st.write("""## ✈️ About Travel Assist

### Your Journey. Simplified.

Travel Assist is your personal AI-powered travel companion, built to make trip planning simpler, smarter, and more enjoyable.

Instead of spending hours searching through different websites, Travel Assist helps you discover destinations, plan trips, explore places, and get practical travel suggestions — all in one place.

### 🌍 What We Do

**🧭 Discover**
Explore destinations around the world and find places that match your interests.

**🗺️ Plan**
Get practical travel ideas, itineraries, activities, and suggestions for your journey.

**🤖 Ask AI**
Chat with your travel assistant and get simple, personalized answers to your travel questions.

**💡 Travel Smarter**
Make better decisions with useful information tailored to your preferences, time, and travel style.

### ❤️ Our Vision

We believe travel planning shouldn't feel complicated.

Our goal is to make discovering the world easier for everyone — whether you're planning your first trip, a weekend escape, or your next big adventure.

**Dream a destination.
Plan the journey.
Make the memories. 🌎**
.""")
    st.title("Please share your valuable Feedback")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    selected = st.feedback("stars")
###################################################################################


