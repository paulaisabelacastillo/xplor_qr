# qr.py — XPLØR QR (modo kiosco: SOLO muestra datos recibidos por ?data=)
import streamlit as st
import urllib.parse
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
.cta-link { text-align:center; margin-top: 24px; }
.cta-link a { color:#00695c; font-weight:600; text-decoration:underline; }
</style>
""", unsafe_allow_html=True)

# ====== Utilidad: decodificar ?data= (base64 url-safe) ======
def _decode_data_param(data_param: str):
    try:
        padding = "=" * (-len(data_param) % 4)  # completar padding si falta
        raw = base64.urlsafe_b64decode(data_param + padding).decode("utf-8")
        return json.loads(raw)
    except Exception:
        return None

# ====== Leer parámetros ======
params = st.query_params  # API nueva de Streamlit
data_param = params.get("data")  # str | None

# ====== Bloque reutilizable: CTA a sitio web ======
def render_cta_web():
    st.markdown(
        "<div class='cta-link'>Para más información ingresar a la página de "
        "<a href='http://www.xplorandplay.com/' target='_blank' rel='noopener noreferrer'>http://www.xplorandplay.com/</a>"
        "</div>",
        unsafe_allow_html=True
    )
    # Botón grande opcional
    st.markdown(
        "<a class='xplor-button' href='http://www.xplorandplay.com/' target='_blank' rel='noopener noreferrer'>Ir a xplorandplay.com</a>",
        unsafe_allow_html=True
    )

# ====== Flujo directo con ?data= ======
if data_param:
    payload = _decode_data_param(data_param)
    if not payload:
        st.error("No pude leer los datos del QR. Pídele al robot que genere uno nuevo.")
        render_cta_web()
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

    # === NUEVO: CTA al sitio ===
    render_cta_web()

    st.markdown("<div class='footer'>XPLØR © 2025</div>", unsafe_allow_html=True)
    st.stop()

# ====== Modo kiosco: si NO llega ?data=, no hay formulario ======
st.markdown("<h1>Escanea el QR del robot</h1>", unsafe_allow_html=True)
st.write("Abre esta página desde el código QR generado por XPLØRBot para ver tus recomendaciones.")
render_cta_web()
st.markdown("<div class='footer'>XPLØR © 2025</div>", unsafe_allow_html=True)
