import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="XPLØR QR", page_icon="🌍", layout="centered")

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

# 🚀 URL Parameters
params = st.experimental_get_query_params()
name = params.get("nombre", [None])[0]
country = params.get("pais", [None])[0]
email = params.get("email", [None])[0]

# 🎉 Welcome Screen
if name and country and email:
    st.markdown(f"<h1>👋 Welcome, {name.title()} from {country.title()}!</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3>📧 Email: {email}</h3>", unsafe_allow_html=True)
    st.markdown("<h4>How can I assist you today?</h4>", unsafe_allow_html=True)

    category = st.selectbox("Select a category:", [
        "Tourist Attractions", "Hotels", "Transportation", "Emergency"
    ])

    subcategory = None
    if category == "Tourist Attractions":
        subcategory = st.selectbox("What type of place are you looking for?", 
                                   ["Museums", "Restaurants", "Nature", "Shopping Centers"])
    elif category == "Hotels":
        subcategory = st.selectbox("What kind of hotel do you prefer?", 
                                   ["Budget", "Luxury", "City Center", "With Pool"])
    elif category == "Transportation":
        subcategory = st.selectbox("What do you need?", 
                                   ["Taxi", "Metro", "Car Rental", "Ride Apps"])
    elif category == "Emergency":
        subcategory = st.selectbox("What kind of emergency?", 
                                   ["Hospital", "Police", "Embassy", "Pharmacy"])

    recommendations = {
        "Museums": ["Biomuseo", "Panama Canal Museum", "Museum of Contemporary Art"],
        "Restaurants": ["Mercado del Marisco", "Tantalo", "Maito", "Fonda Lo Que Hay"],
        "Nature": ["Metropolitan Park", "Taboga Island", "Coiba Park", "Boquete"],
        "Shopping Centers": ["Multiplaza", "Albrook Mall", "Metromall", "Soho Mall"],
        "Budget": ["Hostal Loco Coco Loco", "Hotel Centroamericano", "Hotel Marparaiso"],
        "Luxury": ["Las Américas Golden Tower", "W Panama", "JW Marriott Tower"],
        "City Center": ["Hotel El Panamá", "Riu Plaza", "Hotel Marbella"],
        "With Pool": ["Sortis Hotel", "Crowne Plaza", "The Bristol Panama"],
        "Taxi": ["Uber", "Cabify", "Panamanian Taxis"],
        "Metro": ["Line 1", "Line 2", "MetroBus Reloads"],
        "Car Rental": ["Thrifty", "Hertz", "Dollar Rent A Car"],
        "Ride Apps": ["Uber", "InDrive", "Cabify"],
        "Hospital": ["Punta Pacifica Hospital", "National Hospital", "Santo Tomás Hospital"],
        "Police": ["National Police", "DIJ", "Call 104"],
        "Embassy": ["U.S. Embassy", "French Embassy", "Colombian Embassy"],
        "Pharmacy": ["Arrocha", "Metro Plus", "El Javillo"]
    }

    if subcategory in recommendations:
        st.markdown("### 🌟 Recommended for you:")
        places = random.sample(recommendations[subcategory], k=min(4, len(recommendations[subcategory])))
        for place in places:
            url = f"https://www.google.com/search?q={urllib.parse.quote(place + ' Panama')}"
            st.markdown(f"<a class='xplor-button' href='{url}' target='_blank'>{place}</a>", unsafe_allow_html=True)

# 📲 QR Generator Screen
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

# Footer
st.markdown("<div class='footer'>🌍 XPLØR © 2025 – Made in Panama 🇵🇦 </div>", unsafe_allow_html=True)
