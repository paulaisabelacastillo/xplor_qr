import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="XPLØR QR", page_icon="🌴")

# Estilos CSS modernos con texto blanco
st.markdown("""
<style>
.xplor-button {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #27ae60, #219653);
    color: white !important;
    padding: 15px;
    margin: 10px 0;
    border: none;
    border-radius: 25px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    text-decoration: none;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.xplor-button:hover {
    background: linear-gradient(135deg, #219653, #27ae60);
    transform: scale(1.05);
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

params = st.query_params if hasattr(st, 'query_params') else st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

if nombre and pais:
    st.markdown(f"""
        <div style='text-align:center; margin-top:60px;'>
            <h1 style='font-size:3em; color:#004225;'>🌟 ¡Hola {nombre.title()} de {pais.title()}!</h1>
            <p style='font-size:1.5em; color:#004225;'>¿En qué te puedo asistir?</p>
        </div>
    """, unsafe_allow_html=True)

    menu = st.selectbox("Elige una opción principal:", [
        "Lugares turísticos", "Hoteles", "Transporte", "Tienes una emergencia"
    ])

    if menu == "Lugares turísticos":
        sub = st.selectbox("¿Qué te interesa?", ["Museos", "Restaurantes", "Naturaleza", "Centros comerciales"])
        sugerencias = {
            "Museos": ["Biomuseo", "Museo del Canal", "Museo de Arte Contemporáneo"],
            "Restaurantes": ["Mercado del Marisco", "Tantalo", "Maito", "Fonda Lo Que Hay"],
            "Naturaleza": ["Parque Natural Metropolitano", "Isla Taboga", "San Blas", "Volcán Barú"],
            "Centros comerciales": ["Albrook Mall", "Multiplaza", "Metromall", "AltaPlaza"]
        }
    elif menu == "Hoteles":
        sugerencias = {
            "Hoteles": ["Hotel Sortis", "W Panama", "American Trade Hotel", "Selina Casco Viejo"]
        }
        sub = "Hoteles"
    elif menu == "Transporte":
        sugerencias = {
            "Transporte": ["MiBus", "Metro de Panamá", "Uber", "Cabify"]
        }
        sub = "Transporte"
    elif menu == "Tienes una emergencia":
        sugerencias = {
            "Emergencia": ["Policía: 104", "Ambulancia: 911", "Hospital Santo Tomás", "Hospital Nacional"]
        }
        sub = "Emergencia"

    st.subheader("Te recomendamos visitar:")
    for lugar in sugerencias.get(sub, []):
        query = urllib.parse.quote(lugar + " Panamá")
        url = f"https://www.google.com/search?q={query}"
        st.markdown(f"<a href='{url}' target='_blank' class='xplor-button'>{lugar}</a>", unsafe_allow_html=True)

else:
    st.title("📲 Generador de QR de Bienvenida\n**XPLØR**")
    nombre = st.text_input("🧑 Nombre")
    pais = st.text_input("🌐 País")

    if nombre and pais:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}"

        st.markdown("📌 Esta es la URL dentro del código QR:")
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption="🔲 Escanea este código QR", use_column_width=False)

        st.markdown(f"<a href='{local_url}' target='_blank' class='xplor-button'>🌍 Abrir bienvenida personalizada</a>", unsafe_allow_html=True)
