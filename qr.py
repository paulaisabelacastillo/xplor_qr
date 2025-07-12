import streamlit as st
import urllib.parse
import random

# Detectar parámetros de la URL
params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

if nombre and pais:
    st.set_page_config(page_title="Bienvenida", page_icon="🌴")
    st.markdown("""
        <style>
            .reco-boton {
                display: inline-block;
                padding: 15px 30px;
                margin: 15px auto;
                background: linear-gradient(135deg, #FF7F50, #FF6347);
                color: white;
                text-align: center;
                border-radius: 30px;
                font-size: 18px;
                text-decoration: none;
                font-weight: bold;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
            }
            .reco-boton:hover {
                background: linear-gradient(135deg, #ff3c2e, #d81b00);
                transform: scale(1.05);
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style='text-align:center; margin-top:100px;'>
            <h1 style='font-size:3em; color:#004225;'>🎉 ¡Bienvenido/a {nombre} de {pais}! 🌴</h1>
            <p style='font-size:1.5em; color:#004225;'>Explora, aprende y diviértete con XPLØR.</p>
        </div>
    """, unsafe_allow_html=True)

    menu_principal = st.selectbox("👉 ¿En qué puedo asistirte hoy?", [
        "Selecciona una opción",
        "Lugares turísticos",
        "Hoteles",
        "Transporte",
        "Tienes una emergencia"
    ])

    if menu_principal == "Lugares turísticos":
        interes = st.selectbox("¿Qué tipo de lugar te interesa?", [
            "Selecciona una categoría",
            "Museos",
            "Restaurantes",
            "Naturaleza",
            "Centros comerciales"
        ])

        lugares = {
            "Museos": ["Biomuseo", "Museo del Canal Interoceánico", "Museo de Arte Contemporáneo"],
            "Restaurantes": ["Mercado del Marisco", "Tantalo", "Maito", "Fonda Lo Que Hay"],
            "Naturaleza": ["Parque Natural Metropolitano", "Isla Taboga", "Volcán Barú"],
            "Centros comerciales": ["Albrook Mall", "Multiplaza", "Metromall"]
        }

        if interes in lugares:
            st.subheader("🌟 Te recomendamos visitar:")
            for lugar in random.sample(lugares[interes], min(4, len(lugares[interes]))):
                url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
                st.markdown(f"<a href='{url}' target='_blank' class='reco-boton'>{lugar}</a>", unsafe_allow_html=True)

    elif menu_principal == "Hoteles":
        hoteles = ["Hotel Central Panamá", "W Panama", "Hilton Panama", "Sortis Hotel"]
        st.subheader("🏨 Sugerencias de alojamiento:")
        for hotel in hoteles:
            url = f"https://www.google.com/search?q={urllib.parse.quote(hotel + ' Panamá')}"
            st.markdown(f"<a href='{url}' target='_blank' class='reco-boton'>{hotel}</a>", unsafe_allow_html=True)

    elif menu_principal == "Transporte":
        opciones = ["Uber Panamá", "MiBus Panamá", "Metro de Panamá", "Alquiler de autos"]
        st.subheader("🚌 Opciones de transporte:")
        for opcion in opciones:
            url = f"https://www.google.com/search?q={urllib.parse.quote(opcion)}"
            st.markdown(f"<a href='{url}' target='_blank' class='reco-boton'>{opcion}</a>", unsafe_allow_html=True)

    elif menu_principal == "Tienes una emergencia":
        st.subheader("🚨 Contactos de emergencia")
        st.markdown("""
            <p><strong>📞 Contacta inmediatamente a:</strong></p>
            <a href='tel:104' class='reco-boton' style='background:#d9534f;'>🚓 Policía Nacional (104)</a>
            <a href='tel:103' class='reco-boton' style='background:#f0ad4e;'>🚑 Ambulancia (103)</a>
            <a href='tel:911' class='reco-boton' style='background:#5bc0de;'>📞 Emergencias (911)</a>
        """, unsafe_allow_html=True)

else:
    st.set_page_config(page_title="Generador QR", page_icon="📲")
    st.title("🔲 Generador de QR personalizado")
    nombre = st.text_input("Nombre")
    pais = st.text_input("País")

    if nombre and pais:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}"

        st.markdown("📌 Esta es la URL dentro del código QR:")
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption="🔲 Escanea este código QR", use_column_width=False)

        st.markdown(f"[🌐 Abrir bienvenida personalizada]({local_url})", unsafe_allow_html=True)
