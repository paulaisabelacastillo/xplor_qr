import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="XPLØR Panamá", page_icon="🌴")

st.markdown("""
    <style>
    .option-button {
        display: block;
        width: 80%;
        max-width: 300px;
        margin: 12px auto;
        padding: 16px;
        font-size: 18px;
        font-weight: bold;
        color: white;
        background: linear-gradient(135deg, #008CBA, #005f73);
        border-radius: 35px;
        text-align: center;
        text-decoration: none;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    .option-button:hover {
        background: linear-gradient(135deg, #00b4d8, #023e8a);
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

if nombre and pais:
    st.markdown(f"""
        <div style='text-align:center; margin-top:30px;'>
            <h1 style='font-size:2.5em; color:#004225;'>🎉 ¡Hola {nombre} de {pais}! 🌍</h1>
            <p style='font-size:1.3em;'>¿En qué puedo ayudarte hoy?</p>
        </div>
    """, unsafe_allow_html=True)

    opcion = st.radio("Te puedo asistir con:", [
        "Lugares turísticos",
        "Hoteles",
        "Transporte",
        "Tienes una emergencia"
    ])

    if opcion == "Lugares turísticos":
        interes = st.radio("¿Qué te interesa más?", [
            "Museos",
            "Restaurantes",
            "Naturaleza",
            "Centros Comerciales"
        ])

        lugares = {
            "Museos": ["Museo del Canal", "Biomuseo", "Museo de Arte Contemporáneo", "Museo Afroantillano"],
            "Restaurantes": ["Mercado del Marisco", "Tantalo", "Maito", "Fonda Lo Que Hay"],
            "Naturaleza": ["Parque Metropolitano", "Causeway de Amador", "Cerro Ancón", "Jardín Botánico"],
            "Centros Comerciales": ["Albrook Mall", "Multiplaza", "Metromall", "AltaPlaza"]
        }

        recomendaciones = random.sample(lugares[interes], 4)

        st.subheader("🌟 Te recomendamos visitar:")

        for lugar in recomendaciones:
            url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
            st.markdown(
                f"<a href='{url}' target='_blank' class='option-button'>{lugar}</a>",
                unsafe_allow_html=True
            )

    elif opcion == "Hoteles":
        hoteles = ["Hotel Central Panamá", "Sortis Hotel", "W Panamá", "Selina Casco Viejo"]
        recomendados = random.sample(hoteles, 3)

        st.subheader("🏨 Hoteles sugeridos:")
        for h in recomendados:
            url = f"https://www.google.com/search?q={urllib.parse.quote(h)}"
            st.markdown(
                f"<a href='{url}' target='_blank' class='option-button'>{h}</a>",
                unsafe_allow_html=True
            )

    elif opcion == "Transporte":
        st.subheader("🚌 Opciones de transporte recomendadas")
        transportes = [
            ("MiBus (MetroBus)", "https://www.mibus.com.pa"),
            ("Metro de Panamá", "https://www.elmetrodepanama.com"),
            ("Uber Panamá", "https://www.uber.com/pa/es/"),
            ("Cabify Panamá", "https://cabify.com/pa")
        ]
        for nombre, enlace in transportes:
            st.markdown(
                f"<a href='{enlace}' target='_blank' class='option-button'>{nombre}</a>",
                unsafe_allow_html=True
            )

    elif opcion == "Tienes una emergencia":
        st.subheader("📞 Números de emergencia en Panamá:")
        st.markdown("""
            <a href='tel:104' class='option-button' style='background:crimson;'>🚓 Policía Nacional (104)</a>
            <a href='tel:103' class='option-button' style='background:orangered;'>🚑 Ambulancia (103)</a>
            <a href='tel:911' class='option-button' style='background:#ff6600;'>📞 Emergencias (911)</a>
        """, unsafe_allow_html=True)

else:
    st.title("🔲 Generador de QR de Bienvenida")
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
