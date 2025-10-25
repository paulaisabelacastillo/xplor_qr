import streamlit as st
import urllib.parse
import json, base64

st.set_page_config(page_title="XPLØR QR", page_icon="🤖", layout="centered")

# 🌈 Modern Glass-UI Style
st.markdown("""
<style>
html, body, [class*="css"] {
    background: linear-gradient(135deg, #e0f7fa, #ffffff);
    font-family: 'Segoe UI', sans-serif;
    color: #2c3e50;
}
h1, h3, h4 {
    text-align: center;
    color: #01579B;
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
    margin-top: 40px;
    font-size: 14px;
}
.robot-image {
    display: block;
    margin: 0 auto 20px auto;
    width: 160px;
}
</style>
""", unsafe_allow_html=True)

# 🧩 Get parameters from URL
params = st.experimental_get_query_params()
payload_data = params.get("data", [None])[0]

# 🧠 Same dictionary as robot
SUGGESTIONS = {
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

# 🚀 Decode robot payload
if payload_data:
    try:
        padded = payload_data + "=" * (-len(payload_data) % 4)
        decoded = json.loads(base64.urlsafe_b64decode(padded.encode()).decode())
        category = decoded.get("category", "Tourist attractions")
        subcategory = decoded.get("subcategory", "")
        suggestions = decoded.get("suggestions", [])
        name = decoded.get("name", "Visitor")
        country = decoded.get("country", "Traveler")
    except Exception as e:
        st.error("⚠️ Invalid or corrupted QR data. Please scan again.")
        st.stop()
else:
    st.warning("⚠️ This page only works when opened from the robot’s QR code.")
    st.stop()

# 🤖 Header
st.image("https://raw.githubusercontent.com/marisollinero/xplor-assets/main/xplorbot_head.png", 
         use_column_width=False, 
         output_format="PNG", 
         caption="", 
         width=160)

st.markdown(f"<h1>👋 Hello, {name.title()}!</h1>", unsafe_allow_html=True)
st.markdown(f"<h3>Welcome to Panama 🇵🇦</h3>", unsafe_allow_html=True)

if category and subcategory:
    st.markdown(f"<h4>Exploring: <b>{subcategory}</b> ({category})</h4>", unsafe_allow_html=True)
else:
    st.markdown("<h4>Here are your personalized recommendations:</h4>", unsafe_allow_html=True)

# 🌟 Show Recommendations
if suggestions:
    st.markdown("### 🌟 XPLØRBOT recommends:")
    for place in suggestions:
        url = f"https://www.google.com/search?q={urllib.parse.quote(place + ' Panama')}"
        st.markdown(f"<a class='xplor-button' href='{url}' target='_blank'>{place}</a>", unsafe_allow_html=True)
else:
    # fallback if the robot sends only category/subcategory
    fallback = SUGGESTIONS.get(subcategory, [])
    if fallback:
        st.markdown("### 🌟 XPLØRBOT recommends:")
        for place in fallback:
            url = f"https://www.google.com/search?q={urllib.parse.quote(place + ' Panama')}"
            st.markdown(f"<a class='xplor-button' href='{url}' target='_blank'>{place}</a>", unsafe_allow_html=True)
    else:
        st.info("No recommendations available. Please rescan your QR.")

# Footer
st.markdown("<div class='footer'>🌍 XPLØR © 2025 – Made in Panama 🇵🇦</div>", unsafe_allow_html=True)
