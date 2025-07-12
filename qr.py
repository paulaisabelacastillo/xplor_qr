import streamlit as st
import urllib.parse
import random

# Detectar parámetros de la URL
params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

st.set_page_config(page_title="XPLØR - Bienvenida", page_icon="🌴")

fondo_css = """
<style>
body {
    background-color: #f4f8f3;
    font-family: 'Segoe UI', sans-serif;
    color: #004225;
}
.block-container {
    padding: 2em 3em;
    background-color: #ffffff;
    border-radius: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-top: 50px;
}
h1 {
    font-size: 3em;
    margin-bottom: 0.3em;
}
p {
    font-size: 1.5em;
}
a.button {
    display: block;
    background: #50a47a;
    color: white;
    text-align: center;
    padding: 15px;
    margin: 15px 0;
    border-radius: 25px;
    text-decoration: none;
    font-size: 1.2em;
    transition: background 0.3s;
}
a.button:hover {
    background: #387255;
}
</style>
"""

st.markdown(fondo_css, unsafe_allow_html=True)

if nombre and pais:
    st.markdown(f"""
        <div style='text-align:center;'>
            <h1>🎉 ¡Bienvenido/a {nombre.title()} de {pais.title()}! 🌴</h1>
            <p>Explora, aprende y diviértete con <strong>XPLØR</strong>.</p>
            <p>Te recomendamos estos lugares increíbles para visitar en Panamá:</p>
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
        st.markdown(f"<a href='{url}' target='_blank' class='button'>{lugar}</a>", unsafe_allow_html=True)

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
