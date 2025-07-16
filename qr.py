import streamlit as st
import urllib.parse
import random

# 🌐 Configuración de la página
st.set_page_config(page_title="XPLØR QR", page_icon="📲")

# 🎨 Estilos personalizados
st.markdown("""
<style>
h1, h2, h3 {
    text-align: center;
    color: #1d3557;
}
.xplor-button {
    display: block;
    width: 100%;
    background: linear-gradient(135deg, #28a745, #218838);
    color: white !important;
    padding: 15px;
    margin: 10px 0;
    border: none;
    border-radius: 25px;
    font-size: 18px;
    font-weight: bold;
    text-align: center;
    transition: all 0.3s ease;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.xplor-button:hover {
    background: linear-gradient(135deg, #218838, #28a745);
    transform: scale(1.05);
    color: white !important;
}
.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

# 🧭 Obtener parámetros desde la URL
params = st.experimental_get_query_params()
nombre = params.get("nombre", [None])[0]
pais = params.get("pais", [None])[0]
email = params.get("email", [None])[0]

# 🎉 Si vienen datos en la URL, mostramos la bienvenida
if nombre and pais and email:
    st.markdown(f"<h1>🌟 ¡Hola {nombre.title()} de {pais.title()}!</h1>", unsafe_allow_html=True)
    st.markdown(f"<h3>📧 Email: {email}</h3>", unsafe_allow_html=True)
    st.markdown("<h3>¿En qué te puedo asistir?</h3>", unsafe_allow_html=True)

    categoria = st.selectbox("🔍 Elige una opción principal:", [
        "Lugares turísticos", "Hoteles", "Transporte", "Tienes una emergencia"
    ])

    subcategoria = None
    if categoria == "Lugares turísticos":
        subcategoria = st.selectbox("🌴 ¿Qué te interesa?", ["Museos", "Restaurantes", "Naturaleza", "Centros comerciales"])
    elif categoria == "Hoteles":
        subcategoria = st.selectbox("🏨 ¿Qué buscas?", ["Económicos", "Lujo", "Cerca del centro", "Con piscina"])
    elif categoria == "Transporte":
        subcategoria = st.selectbox("🚕 ¿Qué necesitas?", ["Taxi", "Metro", "Renta de auto", "App de transporte"])
    elif categoria == "Tienes una emergencia":
        subcategoria = st.selectbox("🚨 ¿Cuál es tu situación?", ["Hospital", "Policía", "Embajada", "Farmacia"])

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
        st.markdown("### ⭐ Te recomendamos:")
        lugares = random.sample(sugerencias[subcategoria], k=min(4, len(sugerencias[subcategoria])))
        for lugar in lugares:
            url = f"https://www.google.com/search?q={urllib.parse.quote(lugar + ' Panamá')}"
            st.markdown(f"<a class='xplor-button' href='{url}' target='_blank'>{lugar}</a>", unsafe_allow_html=True)

# 🧩 Formulario para generar QR
else:
    st.markdown("<h1>📲 Generador de QR de Bienvenida</h1>", unsafe_allow_html=True)
    st.markdown("### ✨ ¡Completa los datos y comparte tu aventura!")

    nombre = st.text_input("🐣 Nombre")
    pais = st.text_input("🌍 País")
    email = st.text_input("📧 Email")

    if nombre and pais and email:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}&email={urllib.parse.quote(email)}"

        st.markdown("🔗 Esta es la URL para tu bienvenida:")
        st.code(local_url)

        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption="🔲 Escanea tu código QR")

        st.markdown(f"<a class='xplor-button' href='{local_url}' target='_blank'>🌐 Ver Bienvenida</a>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>© 2025 XPLØR - PTY 🌎</div>", unsafe_allow_html=True)
