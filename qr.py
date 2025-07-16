import streamlit as st
import urllib.parse
import random

st.set_page_config(page_title="XPLØR QR", page_icon="", layout="centered")

# 🌈 Paleta y estilos modernos
st.markdown("""
<style>
/* Fondo claro con color suave */
html, body, [class*="css"] {
    background: linear-gradient(135deg, #e0f7fa, #ffffff);
    font-family: 'Segoe UI', sans-serif;
    color: #2c3e50;
}

/* Encabezados centrados */
h1, h3 {
    text-align: center;
    color: #0a5f78;
}

/* Botones */
.xplor-button {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #009688, #4db6ac);
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
    box-shadow: 0 6px 16px rgba(0,0,0,0.1);
}
.xplor-button:hover {
    background: linear-gradient(135deg, #00796b, #26a69a);
    transform: scale(1.07);
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# 🚀 Parámetros desde URL
params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]
email = params.get("email", [None])[0]

# 🎉 Pantalla de bienvenida
if nombre and pais and email:
    st.markdown(f"<h1> ¡Hola {nombre.title()} de {pais.title()}!</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3> Email: {email}</h3>", unsafe_allow_html=True)
    st.markdown("<h3>¿En qué te puedo asistir?</h3>", unsafe_allow_html=True)

    categoria = st.selectbox("Selecciona una categoría:", [
        "Lugares turísticos", "Hoteles", "Transporte", "Tienes una emergencia"
    ])

    subcategoria = None
    if categoria == "Lugares turísticos":
        subcategoria = st.selectbox("¿Qué te interesa?", ["Museos", "Restaurantes", "Naturaleza", "Centros comerciales"])
    elif categoria == "Hoteles":
        subcategoria = st.selectbox("¿Qué buscas?", ["Económicos", "Lujo", "Cerca del centro", "Con piscina"])
    elif categoria == "Transporte":
        subcategoria = st.selectbox("¿Qué necesitas?", ["Taxi", "Metro", "Renta de auto", "App de transporte"])
    elif categoria == "Tienes una emergencia":
        subcategoria = st.selectbox("¿Cuál es tu situación?", ["Hospital", "Policía", "Embajada", "Farmacia"])

    sugerencias = {
        "Museos": ["Biomuseo", "Museo del Canal", "Museo de Arte Contemporáneo"],
        "Restaurantes": ["Mercado del Marisco", "Tantalo", "Maito", "Fonda Lo Que Hay"],
        "Naturaleza": ["Parque Metropolitano", "Isla Taboga", "Parque Coiba", "Boquete"],
        "Centros comerciales": ["Multiplaza", "Albrook Mall", "Metromall", "Soho Mall"],
        "Económicos": ["Hostal Loco Coco Loco", "Hotel Centroamericano", "Hotel Marparaiso"],
        "Lujo": ["Hotel Las Américas", "W Panama", "Trump Tower"],
        "Cerca del centro": ["Hotel El Panamá", "Hotel Riu", "Hotel Marbella"],
        "Con piscina": ["Sortis Hotel", "Hotel Crowne Plaza", "Bristol Panama"],
        "Taxi": ["Uber", "Cabify", "Taxis Panameños"],
        "Metro": ["Línea 1", "Línea 2", "MetroBus Recargas"],
        "Renta de auto": ["Thrifty", "Hertz", "Dollar Rent A Car"],
        "App de transporte": ["Uber", "InDrive", "Cabify"],
        "Hospital": ["Hospital Punta Pacífica", "Hospital Nacional", "Hospital Santo Tomás"],
        "Policía": ["Policía Nacional", "DIJ", "Servicio 104"],
        "Embajada": ["Embajada de EE.UU.", "Embajada de Francia", "Embajada de Colombia"],
        "Farmacia": ["Arrocha", "Metro Plus", "El Javillo"]
    }

    if subcategoria in sugerencias:
        st.markdown("###  Te recomendamos:")
        lugares = random.sample(sugerencias[subcategoria], k=min(4, len(sugerencias[subcategoria])))
        for lugar in lugares:
            url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
            st.markdown(f"<a class='xplor-button' href='{url}' target='_blank'>{lugar}</a>", unsafe_allow_html=True)

# 📲 Formulario de QR
else:
    st.markdown("<h1> Generador de QR de Bienvenida</h1>", unsafe_allow_html=True)
    st.markdown("###  ¡Completa los datos y comparte tu aventura!")

    nombre = st.text_input(" Tu nombre")
    pais = st.text_input(" Tu país")
    email = st.text_input(" Tu email")

    if nombre and pais and email:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}&email={urllib.parse.quote(email)}"

        st.markdown("🔗 Esta es tu URL personalizada:")
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption=" Escanea este código QR")

        st.markdown(f"<a class='xplor-button' href='{local_url}' target='_blank'> Ver tu bienvenida</a>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'> XPLØR © 2025</div>", unsafe_allow_html=True)
