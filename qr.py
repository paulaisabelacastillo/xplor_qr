import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="XPLØR Asistente Turístico", page_icon="🌴")

# Estilos modernos y llamativos
st.markdown("""
    <style>
    .xplor-button {
        display: block;
        width: 100%;
        background: linear-gradient(to right, #00C9FF, #92FE9D);
        color: black;
        padding: 15px;
        margin: 10px 0;
        border: none;
        border-radius: 25px;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        transition: all 0.3s ease;
        text-decoration: none;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
    .xplor-button:hover {
        background: linear-gradient(to right, #43e97b, #38f9d7);
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]
opcion = params.get("opcion", [None])[0]
subopcion = params.get("subopcion", [None])[0]

# Si ya escaneó el QR con parámetros: página de bienvenida y opciones
if nombre and pais and opcion:
    st.title(f"🌟 ¡Bienvenido/a {nombre.title()} de {pais.title()}!")

    if opcion == "Lugares turísticos" and subopcion:
        st.subheader(f"Te interesan lugares de tipo: {subopcion}")
        lugares = {
            "Museos": ["Biomuseo", "Museo Afroantillano", "Museo del Canal"],
            "Restaurantes": ["Mercado del Marisco", "Tántalo", "Maito", "Fonda Lo Que Hay"],
            "Naturaleza": ["Parque Natural Metropolitano", "Cerro Ancón", "Isla Taboga"],
            "Centros comerciales": ["Albrook Mall", "Multiplaza", "AltaPlaza"]
        }
        for lugar in lugares.get(subopcion, []):
            url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
            st.markdown(f"<a href='{url}' target='_blank' class='xplor-button'>{lugar}</a>", unsafe_allow_html=True)

    elif opcion == "Hoteles":
        hoteles = ["Central Hotel Panamá", "Hotel Sortis", "W Panamá", "Selina Casco Viejo"]
        for hotel in hoteles:
            url = f"https://www.google.com/search?q={urllib.parse.quote(hotel)}"
            st.markdown(f"<a href='{url}' target='_blank' class='xplor-button'>{hotel}</a>", unsafe_allow_html=True)

    elif opcion == "Transporte":
        transportes = ["MiBus Panamá", "Metro de Panamá", "Uber Panamá", "DiDi Panamá"]
        for t in transportes:
            url = f"https://www.google.com/search?q={urllib.parse.quote(t)}"
            st.markdown(f"<a href='{url}' target='_blank' class='xplor-button'>{t}</a>", unsafe_allow_html=True)

    elif opcion == "Tienes una emergencia":
        st.markdown("""
        <a href='tel:104' class='xplor-button' style='background: #ff4d4d;'>🚨 Policía Nacional</a>
        <a href='tel:911' class='xplor-button' style='background: #ff9900;'>🚑 Ambulancia</a>
        <a href='tel:103' class='xplor-button' style='background: #1e90ff;'>🔥 Bomberos</a>
        """, unsafe_allow_html=True)

# Si no hay parámetros: generador de QR solamente
else:
    st.title("📲 Generador de QR de Bienvenida XPLØR")
    nombre = st.text_input("🧑 Nombre")
    pais = st.text_input("🌍 País")
    categoria = st.selectbox("Selecciona una categoría", ["Lugares turísticos", "Hoteles", "Transporte", "Tienes una emergencia"])
    subcategoria = ""
    if categoria == "Lugares turísticos":
        subcategoria = st.selectbox("¿Qué te interesa?", ["Museos", "Restaurantes", "Naturaleza", "Centros comerciales"])

    if nombre and pais and categoria:
        base_url = "https://xplor-qr.streamlit.app"
        url = f"{base_url}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}&opcion={urllib.parse.quote(categoria)}"
        if subcategoria:
            url += f"&subopcion={urllib.parse.quote(subcategoria)}"

        st.markdown("📌 Esta es la URL dentro del código QR:")
        st.code(url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(url)}&size=200x200"
        st.image(qr_url, caption="🔲 Escanea este código QR", use_column_width=False)

        st.markdown(f"[🌐 Abrir bienvenida personalizada]({url})", unsafe_allow_html=True)
