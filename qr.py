import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="XPLØR Panamá", page_icon="🌴")

# Estilos CSS modernos
st.markdown("""
<style>
body {
    background-color: #f0fdf9;
}
h1, h2, h3 {
    color: #013220;
}
.xplor-button {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #28a745, #218838);  /* Fondo verde */
    color: white;  /* Texto blanco */
    padding: 15px;
    margin: 10px 0;
    border: none;
    border-radius: 25px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    transition: all 0.3s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.xplor-button:hover {
    background: linear-gradient(135deg, #218838, #1e7e34);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# Extraer parámetros de URL
params = st.query_params if hasattr(st, "query_params") else st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

# PÁGINA DE BIENVENIDA
if nombre and pais:
    st.markdown(f"<h1 style='text-align:center;'>🌴 ¡Bienvenido/a {nombre} de {pais}!</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align:center;'>¿En qué puedo ayudarte?</h3>", unsafe_allow_html=True)

    categoria = st.selectbox("Selecciona una categoría:", ["Lugares turísticos", "Hoteles", "Transporte", "Tienes una emergencia"])

    if categoria == "Lugares turísticos":
        interes = st.selectbox("¿Qué tipo de lugares te interesan?", ["Museos", "Restaurantes", "Naturaleza", "Centros comerciales"])
        if interes == "Museos":
            lugares = ["Biomuseo", "Museo del Canal", "Museo de Historia"]
        elif interes == "Restaurantes":
            lugares = ["Mercado del Marisco", "Tantalo", "Maito", "Fonda Lo Que Hay"]
        elif interes == "Naturaleza":
            lugares = ["Isla Taboga", "Parque Natural Metropolitano", "Parque Nacional Soberanía"]
        else:
            lugares = ["Albrook Mall", "Multiplaza", "Metromall"]

        st.subheader("Te recomendamos visitar:")
        for lugar in lugares:
            url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
            st.markdown(f"<a href='{url}' target='_blank' class='xplor-button'>{lugar}</a>", unsafe_allow_html=True)

    elif categoria == "Hoteles":
        hoteles = ["Sortis Hotel", "Waldorf Astoria", "Hotel Central", "Hard Rock Hotel"]
        st.subheader("Hoteles recomendados:")
        for hotel in hoteles:
            url = f"https://www.google.com/search?q={urllib.parse.quote(hotel + ' Panamá')}"
            st.markdown(f"<a href='{url}' target='_blank' class='xplor-button'>{hotel}</a>", unsafe_allow_html=True)

    elif categoria == "Transporte":
        opciones = ["Uber", "Metro de Panamá", "MiBus", "Taxis Amarillos"]
        st.subheader("Opciones de transporte:")
        for op in opciones:
            url = f"https://www.google.com/search?q={urllib.parse.quote(op + ' Panamá')}"
            st.markdown(f"<a href='{url}' target='_blank' class='xplor-button'>{op}</a>", unsafe_allow_html=True)

    elif categoria == "Tienes una emergencia":
        st.subheader("Líneas de emergencia:")
        st.markdown("<a class='xplor-button' href='tel:911'>🚨 Llamar al 911</a>", unsafe_allow_html=True)
        st.markdown("<a class='xplor-button' href='https://maps.app.goo.gl/NZzyvLgbB4zjCwS49' target='_blank'>🏥 Hospital más cercano</a>", unsafe_allow_html=True)

# GENERADOR QR (página de inicio)
else:
    st.markdown("<h1 style='text-align:center;'>📲 Generador de QR de Bienvenida <br><span style='color:#013220;'>XPLØR</span></h1>", unsafe_allow_html=True)
    nombre = st.text_input("🥸 Nombre")
    pais = st.text_input("🌍 País")

    if nombre and pais:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}"

        st.markdown("<div style='text-align:center;'>📌 URL del QR:</div>", unsafe_allow_html=True)
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption="🔲 Escanea este código QR", use_column_width=False)

        st.markdown(f"<div style='text-align:center;'><a href='{local_url}' target='_blank' class='xplor-button'>🌐 Abrir bienvenida personalizada</a></div>", unsafe_allow_html=True)
