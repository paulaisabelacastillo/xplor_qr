# qr.py — XPLØR QR (Streamlit)
import streamlit as st
import urllib.parse
import random
import json
import base64

st.set_page_config(page_title="XPLØR QR", page_icon="", layout="centered")

# ====== Estilos ======
st.markdown("""
<style>
html, body, [class*="css"] {
  background: linear-gradient(135deg, #e0f7fa, #ffffff);
  font-family: 'Segoe UI', sans-serif; color: #2c3e50;
}
h1, h3 { text-align: center; color: #0a5f78; }
.xplor-button {
  display:block; width:100%;
  background: linear-gradient(135deg, #009688, #4db6ac);
  color:white !important; padding:16px; margin:12px 0;
  border:none; border-radius:30px; font-size:18px; font-weight:600;
  text-align:center; transition: all .3s ease; text-decoration:none;
  box-shadow: 0 6px 16px rgba(0,0,0,0.1);
}
.xplor-button:hover { background: linear-gradient(135deg, #00796b, #26a69a); transform: scale(1.07); cursor:pointer; }
.footer { text-align:center; margin-top:32px; opacity:.7; }
.badge { display:inline-block; background:#e0f2f1; color:#00695c; padding:6px 12px; border-radius:999px; margin:4px; font-size:14px; }
</style>
""", unsafe_allow_html=True)

# ====== Utilidad: decodificar ?data= (base64 url-safe) ======
def _decode_data_param(data_param: str):
    try:
        padding = '=' * (-len(data_param) % 4)  # completar padding si falta
        raw = base64.urlsafe_b64decode(data_param + padding).decode("utf-8")
        return json.loads(raw)
    except Exception:
        return None

# ====== Leer parámetros ======
params = st.experimental_get_query_params()
data_param = params.get("data", [None])[0]

# ====== Flujo directo con ?data= ======
if data_param:
    payload = _decode_data_param(data_param)
    if not payload:
        st.error("No pude leer los datos del QR. Pídele al robot que genere uno nuevo.")
        st.markdown("<div class='footer'>XPLØR © 2025</div>", unsafe_allow_html=True)
        st.stop()

    nombre       = payload.get("nombre", "")
    pais         = payload.get("pais", "")
    email        = payload.get("email", "")
    categoria    = payload.get("categoria", "")
    subcategoria = payload.get("subcategoria", "")
    sugerencias  = payload.get("sugerencias", [])

    # Encabezado
    if nombre or pais:
        st.markdown(f"<h1>¡Hola {nombre.title()} de {pais.title()}!</h1>", unsafe_allow_html=True)
    else:
        st.markdown("<h1>Tus recomendaciones XPLØR</h1>", unsafe_allow_html=True)
    if email:
        st.markdown(f"<h3>Email: {email}</h3>", unsafe_allow_html=True)

    # Chips
    chips = []
    if categoria: chips.append(f"<span class='badge'>Categoría: {categoria}</span>")
    if subcategoria: chips.append(f"<span class='badge'>Interés: {subcategoria}</span>")
    if chips:
        st.markdown(" ".join(chips), unsafe_allow_html=True)

    # Sugerencias
    if sugerencias:
        st.markdown("### Te recomendamos:")
        for lugar in sugerencias:
            q = urllib.parse.quote(lugar + " Panamá")
            st.markdown(
                f"<a class='xplor-button' href='https://www.google.com/search?q={q}' target='_blank'>{lugar}</a>",
                unsafe_allow_html=True
            )
    else:
        st.info("Aún no hay sugerencias. Pídele al robot que te recomiende 3–5 lugares.")

    st.markdown("<div class='footer'>XPLØR © 2025</div>", unsafe_allow_html=True)
    st.stop()

# ====== Fallback: tu flujo original (sin ?data=) ======
nombre = params.get("nombre", [None])[0]
pais   = params.get("pais", [None])[0]
email  = params.get("email", [None])[0]

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

else:
    st.markdown("<h1> Generador de QR de Bienvenida</h1>", unsafe_allow_html=True)
    st.markdown("###  ¡Completa los datos y comparte tu aventura!")
    nombre = st.text_input(" Tu nombre")
    pais   = st.text_input(" Tu país")
    email  = st.text_input(" Tu email")

    if nombre and pais and email:
        pagina_base = "https://xplor-qr.streamlit.app"
        local_url = f"{pagina_base}/?nombre={urllib.parse.quote(nombre)}&pais={urllib.parse.quote(pais)}&email={urllib.parse.quote(email)}"
        st.markdown("🔗 Esta es tu URL personalizada:")
        st.code(local_url)
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?data={urllib.parse.quote(local_url)}&size=200x200"
        st.image(qr_url, caption=" Escanea este código QR")
        st.markdown(f"<a class='xplor-button' href='{local_url}' target='_blank'> Ver tu bienvenida</a>", unsafe_allow_html=True)

st.markdown("<div class='footer'> XPLØR © 2025</div>", unsafe_allow_html=True)
