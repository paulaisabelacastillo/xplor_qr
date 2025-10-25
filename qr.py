import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="XPLØR QR", page_icon="🤖", layout="centered")

# 🌈 Modern Styles (Glass UI look)
st.markdown("""
<style>
html, body, [class*="css"] {
    background: linear-gradient(135deg, #E0F7FA, #FFFFFF);
    font-family: 'Segoe UI', sans-serif;
    color: #2C3E50;
}
h1, h3, h4 {
    text-align: center;
    color: #01579B;
}
div[data-testid="stSelectbox"] label {
    font-weight: 600;
}
.xplor-button {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #0288D1, #26C6DA);
    color: white !important;
    padding: 16px;
    margin: 12px 0;
    border: none;
    border-radius: 30px;
    font-size: 18px;
    font-weight: 600;
    text-align: center;
    transition: all 0.3s ease;
    text-decoration: none;
    box-shadow: 0 6px 16px rgba(0,0,0,0.15);
}
.xplor-button:hover {
    background: linear-gradient(135deg, #0277BD, #00BCD4);
    transform: scale(1.07);
    cursor: pointer;
}
.footer {
    text-align: center;
    color: #607D8B;
    margin-top: 30px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# 🚀 URL Parameters (either ?data=encoded_payload or ?nombre/pais/email)
params = st.experimental_get_query_params()

# === Allow both URL types ===
name = params.get("nombre", [None])[0]
country = params.get("pais", [None])[0]
email = params.get("email", [None])[0]
payload_data = params.get("data", [None])[0]

# === Decode payload from robot if exists ===
if payload_data:
    import json, base64
    try:
        padded = payload_data + "=" * (-len(payload_data) % 4)
        decoded = json.loads(base64.urlsafe_b64decode(padded.encode()).decode())
        category = decoded.get("category")
        subcategory = decoded.get("subcategory")
        suggestions = decoded.get("suggestions", [])
        name = decoded.get("name", "Visitor")
        country = decoded.get("country", "Unknown")
        email = decoded.get("email", "")
    except Exception as e:
        st.error("Invalid QR data format.")
        category = subcategory = None
        suggestions = []
else:
    category = subcategory = None
    suggestions = []

# 🗺️ SAME DATA AS ROBOT
categories = ["Tourist attractions", "Hotels", "Transportation", "Emergency services"]
subcategories = {
    "Tourist attractions": ["Museums", "Restaurants", "Nature", "Shopping malls"],
    "Hotels": ["Budget", "Luxury", "Downtown", "With pool"],
    "Transportation": ["Taxi", "Metro", "Car rental", "Ride-sharing apps"],
    "Emergency services": ["Hospital", "Police", "Embassy", "Pharmacy"],
}
recommendations = {
    "Museums": ["Biomuseum", "Canal Museum", "Museum of Contemporary Art"],
    "Restaurants": ["Seafood Market", "Tantalo", "Maito", "Fonda Lo Que Hay"],
    "Nature": ["Metropolitan Park", "Taboga Island", "Coiba National Park", "Boquete"],
    "Shopping malls": ["Multiplaza", "Albrook Mall", "Metromall", "Soho Mall"],
    "Budget": ["Hostel Loco Coco Loco", "Hotel Centroamericano", "Hotel Marparaiso"],
    "Luxury": ["Hotel Las Américas", "W Panama", "Trump Tower"],
    "Downtown": ["Hotel El Panamá", "Hotel Riu", "Hotel Marbella"],
    "With pool": ["Sortis Hotel", "Hotel Crowne Plaza", "Bristol Panama"],
    "Taxi": ["Uber", "Cabify", "Panamanian Taxis"],
    "Metro": ["Line 1", "Line 2", "MetroBus Recharges"],
    "Car rental": ["Thrifty", "Hertz", "Dollar Rent A Car"],
    "Ride-sharing apps": ["Uber", "InDrive", "Cabify"],
    "Hospital": ["Punta Pacífica Hospital", "National Hospital", "Santo Tomás Hospital"],
    "Police": ["National Police", "DIJ", "Emergency 104"],
    "Embassy": ["US Embassy", "French Embassy", "Colombian Embassy"],
    "Pharmacy": ["Arrocha", "Metro Plus", "El Javillo"]
}

# === If payload from robot ===
if payload_data:
    st.markdown(f"<h1>👋 Hello, {name.title()}!</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3>Welcome to Panama 🇵🇦</h3>", unsafe_allow_html=True)

    if category and subcategory:
        st.markdown(f"### You asked about **{subcategory}** in **{category}**.")
    else:
        st.markdown("### Here's what XPLØRBOT recommends for you:")

    st.markdown("#### 🌟 Recommended for you:")
    for place in suggestions:
        url = f"https://www.google.com/search?q={urllib.parse.quote(place + ' Panama')}"
        st.markdown(f"<a class='xplor-button' href='{url}' target='_blank'>{place}</a>", unsafe_allow_html=True)

# === Manual input mode (no payload) ===
elif name and country and email:
    st.markdown(f"<h1>👋 Welcome, {name.title()} from {country.title()}!</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3>📧 Email: {email}</h3>", unsafe_allow_html=True)
    st.markdown("<h4>How can I assist you today?</h4>", unsafe_allow_html=True)

    category = st.selectbox("Select a category:", categories)
    subcategory = st.selectbox("Select a subcategory:", subcategories[category])
    
    st.markdown("### 🌟 Recommended for you:")
    for place in recommendations[subcategory]:
        url = f"https://www.google.com/search?q={urllib.parse.quote(place + ' Panama')}"
        st.markdown(f"<a class='xplor-button' href='{url}' target='_blank'>{place}</a>", unsafe_allow_html=True)

# === Default QR Generator ===
else:
    st.markdown("<h1>🎯 Welcome QR Generator</h1>", unsafe_allow_html=True)
    st.markdown("### Create your personalized welcome link for XPLØRBOT!")

    name = st.text_input("Your name")
    country = st.text_input("Your country")
    email = st.text_input("Your email address")

    if name and country and email:
        base_page = "https://xplor-qr.streamlit.app"
        personal_url = f"{base_page}/?nombre={urllib.parse.quote(name)}&pais={urllib.parse.quote(country)}&email={urllib.parse.quote(email)}"

        st.markdown("🔗 Your personalized link:")
        st.code(personal_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(personal_url)}&size=200x200"
        st.image(qr_url, caption="📸 Scan this QR code to access your welcome page")

        st.markdown(f"<a class='xplor-button' href='{personal_url}' target='_blank'>Open your Welcome Page</a>", unsafe_allow_html=True)

# === Footer ===
st.markdown("<div class='footer'>🌍 XPLØR © 2025 – Made in Panama 🇵🇦 for the World Robot Olympiad (Singapore Edition)</div>", unsafe_allow_html=True)
