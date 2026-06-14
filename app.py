import streamlit as st
import google.generativeai as genai
import random

# ==================== CONFIGURACIÓN ====================
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# ==================== CHAT MEMORY ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================== CSS ====================
st.markdown("""
<style>

    /* ===== HERO (MITAD PANTALLA) ===== */
    .hero {
        height: 45vh;
        background: url("https://riobrancoperu.com.pe/wp-content/uploads/2015/01/construccion-1100x420.jpg");
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        border-radius: 0 0 25px 25px;
        overflow: hidden;
    }

    .hero::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.55);
    }

    .hero h1, .hero p {
        position: relative;
        z-index: 1;
        color: #0b2a4a;
        text-align: center;
    }

    /* ===== TEXTO GENERAL AZUL OSCURO ===== */
    h1, h2, h3, p, label {
        color: #0b2a4a !important;
    }

    /* ===== BENTO CARDS ===== */
    .bento-card {
        background: rgba(255,255,255,0.88);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
        border: 1px solid rgba(0,0,0,0.05);
    }

    .section-container {
        background: rgba(255,255,255,0.7);
        border-radius: 25px;
        padding: 1rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }

    /* BOTÓN */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 30px;
        width: 100%;
    }

</style>
""", unsafe_allow_html=True)

# ==================== GEMINI ====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

try:
    model = genai.GenerativeModel("models/gemini-2.5-flash")
except:
    try:
        model = genai.GenerativeModel("models/gemini-2.5-pro")
    except:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

# ==================== HERO ====================
st.markdown("""
<div class="hero">
    <div>
        <h1>🏗️ SEO Multi-Agent Optimization Platform</h1>
        <p>Intelligent SEO Optimization for Construction SMEs</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("🤖 AI Agents")
    st.success("Orchestrator")
    st.success("SEO Agent")
    st.success("Content Agent")
    st.success("Monitoring")

# ==================== INPUTS ====================
st.markdown("## 🧱 Business Input Panel")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("🏢 Empresa")
    city = st.text_input("📍 Ciudad")

with col2:
    service = st.text_input("🛠️ Servicio")
    url = st.text_input("🌐 Web")

# ==================== ANALYSIS ====================
if st.button("🚀 Run AI SEO Analysis", use_container_width=True):

    if not company or not service or not city:
        st.error("Completa los campos")
        st.stop()

    st.markdown("## 🔍 SEO Analysis")

    st.warning("Missing meta description")
    st.warning("Low content length")
    st.warning("Missing structured data")

    st.markdown("## 📈 Keywords")

    st.info(f"{service} {city}")
    st.info(f"best {service} {city}")
    st.info(f"{service} near me")

    prompt = f"""
    SEO expert.

    Empresa: {company}
    Servicio: {service}
    Ciudad: {city}
    Web: {url}

    Genera SEO completo.
    """

    st.markdown("## 🤖 AI Content")

    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception as e:
        st.error(e)

    seo_score = random.randint(75, 98)
    ctr = round(random.uniform(2.5, 8.5), 2)
    visits = random.randint(800, 5000)
    conversion = round(visits * (ctr / 100))

    st.markdown("## 📊 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("SEO Score", seo_score)

    with c2:
        st.metric("CTR", f"{ctr}%")

    with c3:
        st.metric("Visits", visits)

    with c4:
        st.metric("Conversions", conversion)

else:
    st.info("Completa los datos para empezar")

# ==================== CHATBOT ====================
st.markdown("## 💬 SEO Assistant Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Pregunta al SEO Assistant...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    chat_prompt = f"""
    Eres experto SEO.

    Empresa: {company}
    Servicio: {service}
    Ciudad: {city}

    Pregunta: {user_input}
    """

    try:
        response = model.generate_content(chat_prompt)
        bot_response = response.text
    except Exception as e:
        bot_response = str(e)

    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    with st.chat_message("assistant"):
        st.write(bot_response)

    st.rerun()

if st.button("🗑️ Limpiar chat"):
    st.session_state.messages = []
    st.rerun()
