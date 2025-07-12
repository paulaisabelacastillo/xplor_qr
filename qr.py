import streamlit as st
import urllib.parse
import random

# Detectar parámetros de la URL
params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

if nombre and pais:
    st.set_page_config(page_title="Bienvenida", page_icon="🌴")
    st.markdown(f"""
        <div style='text-align:center; margin-top:100px;'>
            <h1 style='font-size:3em; color:#004225;'>🎉 ¡Bienvenido/a {nombre} de {pais}! 🌴</h1>
            <p style='font-size:1.5em; color:#004225;'>Explora, aprende y diviértete con XPLØR.</p>
        </div>
    """, unsafe_allow_html=True)

    lugares = [
        "Canal de Panamá", "Casco Antiguo", "Isla Taboga", "Boquete",
        "Bocas del Toro", "Volcán Barú", "Parque Nacional Coiba",
        "San Blas", "Biomuseo", "Parque Natural Metropolitano"
    ]

    recomendaciones = random.sample(lugares, 4)
    for lugar in recomendaciones:
        url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
        st.markdown(f"<a href='{url}' target='_blank' style='display:block; background:#50a47a; color:white; text-align:center; padding:12px; margin:10px 0; border-radius:25px; text-decoration:none;'>{lugar}</a>", unsafe_allow_html=True)

else:
    st.set_page_config(page_title="Generador QR", page_icon="📲")
    st.title("🔲 Generador de QR de Bienvenida")
    nombre = st.text_input("Nombre")
    pais = st.text_input("País")

    if nombre and pais:
        # 👇 CAMBIA esta URL por la de tu app real (la sabrás en el Paso 6)
        pagina_base = "https://xplor-qr.streamlit.app"  # 👈 tu nueva URL real
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}"

        st.markdown("📌 Esta es la URL dentro del código QR:")
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption="🔲 Escanea este código QR", use_column_width=False)

        st.markdown(f"[🌐 Abrir bienvenida personalizada]({local_url})", unsafe_allow_html=True)
        
