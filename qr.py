import streamlit as st
import urllib.parse
import random

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="XPLØR Panamá", page_icon="🌴", layout="centered")

# --- PARÁMETROS DE URL ---
params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

# --- DATOS ---
lugares_turisticos = {
    "museos": ["Museo del Canal Interoceánico", "Biomuseo", "Museo de Arte Contemporáneo"],
    "restaurantes": ["Mercado del Marisco", "Tántalo", "Maito", "Fonda Lo Que Hay"],
    "naturaleza": ["Parque Natural Metropolitano", "Cerro Ancón", "Isla Taboga"],
    "centros comerciales": ["Albrook Mall", "Multiplaza", "Altaplaza"]
}

hoteles = ["Hotel Central Panamá", "W Panamá", "Hilton Panamá", "Selina Casco Viejo"]
transportes = ["Uber Panamá", "Metro de Panamá", "MiBus Panamá"]
emergencia = ["📞 911 - Emergencias", "🚑 Hospital Santo Tomás", "🚓 Policía Nacional"]

# --- INTERFAZ PERSONALIZADA ---
if nombre and pais:
    st.markdown(f"""
    <div style='text-align:center; margin-top:60px;'>
        <h1 style='font-size:3em; color:#004225;'>🎉 ¡Bienvenido/a {nombre} de {pais}! 🌎</h1>
        <p style='font-size:1.4em; color:#444;'>¿Cómo puedo asistirte hoy?</p>
    </div>
    """, unsafe_allow_html=True)

    opcion = st.selectbox("Selecciona una categoría:",
                          ["---", "Lugares turísticos", "Hoteles", "Transporte", "Tienes una emergencia"])

    if opcion == "Lugares turísticos":
        interes = st.radio("¿Qué te interesa explorar?", ["Museos", "Restaurantes", "Naturaleza", "Centros comerciales"])
        if interes:
            categoria = interes.lower()
            recomendaciones = random.sample(lugares_turisticos[categoria], 3)
            st.markdown("<h3 style='text-align:center;'>🌟 Te recomendamos visitar:</h3>", unsafe_allow_html=True)
            for lugar in recomendaciones:
                url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
                st.markdown(f"""
                    <div style='text-align:center;'>
                        <a href='{url}' target='_blank' style='display:inline-block; padding:14px 24px; margin:10px; background:#008080; color:white; border-radius:30px; text-decoration:none; font-size:16px; font-weight:bold; transition:0.3s;'>
                            {lugar}
                        </a>
                    </div>
                """, unsafe_allow_html=True)

    elif opcion == "Hoteles":
        st.markdown("<h3 style='text-align:center;'>🏨 Recomendaciones de hospedaje:</h3>", unsafe_allow_html=True)
        for hotel in random.sample(hoteles, 3):
            url = f"https://www.google.com/search?q={urllib.parse.quote(hotel + ' Panamá')}"
            st.markdown(f"""
                <div style='text-align:center;'>
                    <a href='{url}' target='_blank' style='display:inline-block; padding:14px 24px; margin:10px; background:#336699; color:white; border-radius:30px; text-decoration:none; font-size:16px; font-weight:bold;'>
                        {hotel}
                    </a>
                </div>
            """, unsafe_allow_html=True)

    elif opcion == "Transporte":
        st.markdown("<h3 style='text-align:center;'>🚗 Opciones de transporte:</h3>", unsafe_allow_html=True)
        for medio in transportes:
            url = f"https://www.google.com/search?q={urllib.parse.quote(medio)}"
            st.markdown(f"""
                <div style='text-align:center;'>
                    <a href='{url}' target='_blank' style='display:inline-block; padding:14px 24px; margin:10px; background:#cc6600; color:white; border-radius:30px; text-decoration:none; font-size:16px; font-weight:bold;'>
                        {medio}
                    </a>
                </div>
            """, unsafe_allow_html=True)

    elif opcion == "Tienes una emergencia":
        st.markdown("<h3 style='text-align:center; color:red;'>🚨 Información de emergencia</h3>", unsafe_allow_html=True)
        for e in emergencia:
            st.markdown(f"<p style='text-align:center; font-size:20px; color:#B22222;'>{e}</p>", unsafe_allow_html=True)

else:
    # PÁGINA DE INICIO PARA GENERAR QR
    st.title("🔲 Generador de QR de Bienvenida")
    nombre = st.text_input("Nombre")
    pais = st.text_input("País")

    if nombre and pais:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}"

        st.markdown("📌 Esta es la URL dentro del código QR:")
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption="🔲 Escanea este código QR")

        st.markdown(f"[🌐 Abrir bienvenida personalizada]({local_url})", unsafe_allow_html=True)
