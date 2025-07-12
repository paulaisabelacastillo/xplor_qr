import streamlit as st
import urllib.parse
import random

# Detectar parámetros de la URL
params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]

# 🖼️ Diseño de la página
st.set_page_config(page_title="XPLØR Bienvenida", page_icon="🌴")

# 💅 CSS personalizado para estilo increíble
estilo = """
<style>
body {
    background: linear-gradient(to right, #f4f8f3, #e4f0eb);
    font-family: 'Segoe UI', sans-serif;
    color: #004225;
}

h1 {
    font-size: 3.2rem;
    margin-bottom: 0.5em;
    color: #004225;
}

p {
    font-size: 1.3rem;
    margin-bottom: 1em;
}

.container {
    background-color: white;
    padding: 3em;
    margin-top: 4em;
    border-radius: 30px;
    box-shadow: 0 6px 20px rgba(0, 66, 37, 0.15);
    text-align: center;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
}

.button {
    display: inline-block;
    background: #50a47a;
    color: white;
    padding: 15px 30px;
    margin: 12px;
    border-radius: 30px;
    font-size: 1.1rem;
    text-decoration: none;
    transition: all 0.3s ease;
}

.button:hover {
    background-color: #387255;
    transform: scale(1.05);
}

.qr-container {
    text-align: center;
    margin-top: 2em;
}
</style>
"""
st.markdown(estilo, unsafe_allow_html=True)

# 🌴 Página de bienvenida personalizada
if nombre and pais:
    st.markdown(f"""
        <div class="container">
            <h1>🌴 ¡Bienvenido/a {nombre.title()} de {pais.title()}!</h1>
            <p>Explora, aprende y diviértete con <strong>XPLØR</strong>.</p>
            <p>Te recomendamos estos lugares mágicos en Panamá:</p>
    """, unsafe_allow_html=True)

    lugares = [
        "Canal de Panamá", "Casco Antiguo", "Isla Taboga", "Boquete",
        "Bocas del Toro", "Volcán Barú", "Parque Nacional Coiba",
        "San Blas", "Biomuseo", "Parque Natural Metropolitano"
    ]
    recomendaciones = random.sample(lugares, 4)
    for lugar in recomendaciones:
        url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
        st.markdown(f"<a href='{url}' class='button' target='_blank'>{lugar}</a>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# 📲 Generador de QR
else:
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.title("🔲 Generador de QR personalizado")
    st.write("Completa los datos para crear tu QR mágico ✨")

    nombre = st.text_input("Tu nombre")
    pais = st.text_input("Tu país")

    if nombre and pais:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}"

        st.markdown("<div class='qr-container'>", unsafe_allow_html=True)
        st.markdown("🔗 URL del QR:")
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption="📸 Escanea tu código QR", use_column_width=False)

        st.markdown(f"<a href='{local_url}' class='button' target='_blank'>🌐 Ir a tu bienvenida</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
