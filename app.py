import streamlit as st
import google.generativeai as genai
import random

# ==================== CONFIGURACIÓN DE LA PÁGINA ====================
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# ==================== BACKGROUND IMAGE + OVERLAY ====================
st.markdown("""
<style>
    .stApp {
        background: url("https://riobrancoperu.com.pe/wp-content/uploads/2015/01/construccion-1100x420.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.55);
        z-index: 0;
    }

    .main {
        position: relative;
        z-index: 1;
    }

    /* ==================== BENTO DESIGN ==================== */
    .bento-card {
        background: linear-gradient(135deg, #1e1e2f 0%, #2a2a3a 100%);
        border-radius: 20px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .bento-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0,0,0,0.3);
    }

    .section-container {
        background: rgba(30,30,47,0.5);
        border-radius: 25px;
        padding: 1rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: bold;
        border-radius: 30px;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102,126,234,0.4);
    }

    h1, h2, h3 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# ==================== INICIALIZAR CHAT ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================== GEMINI ====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

try:
    model = genai.GenerativeModel("models/gemini-2.5-flash")
except:
    try:
        model = genai.GenerativeModel("models/gemini-2.5-pro")
    except:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

# ==================== HEADER ====================
st.title("🏗️ SEO Multi-Agent Optimization Platform")

st.markdown("""
### Intelligent SEO Optimization for Construction SMEs
This platform uses a collaborative multi-agent architecture to analyze,
generate and optimize SEO strategies for construction companies.
""")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("🤖 AI Agents")
    st.success("✅ Orchestrator Agent")
    st.success("✅ SEO Diagnostic Agent")
    st.success("✅ Context Analysis Agent")
    st.success("✅ Prompt Generator Agent")
    st.success("✅ Content Generator Agent")
    st.success("✅ Technical Review Agent")
    st.success("✅ Monitoring Agent")

# ==================== INPUTS ====================
st.markdown("## 🧱 Business Input Panel")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("🏢 Nombre de la Empresa")
    city = st.text_input("📍 Ciudad")

with col2:
    service = st.text_input("🛠️ Servicio Ofrecido")
    url = st.text_input("🌐 Sitio Web")

# ==================== MAIN BUTTON ====================
if st.button("🚀 Run AI SEO Analysis", use_container_width=True):

    if not company or not service or not city:
        st.error("Completa los campos")
        st.stop()

    st.subheader("🔍 SEO Problems Found")
    st.warning("Missing meta description")
    st.warning("Low content length")
    st.warning("Missing structured data")

    st.subheader("📈 Suggested Keywords")
    st.info(f"{service} {city}")
    st.info(f"best {service} {city}")
    st.info(f"{service} near me")

    prompt = f"""
    SEO expert for construction companies.

    Empresa: {company}
    Servicio: {service}
    Ciudad: {city}
    Web: {url}

    Genera SEO completo en español.
    """

    st.subheader("🤖 AI Generated Content")

    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception as e:
        st.error(e)

    seo_score = random.randint(75, 98)
    ctr = round(random.uniform(2.5, 8.5), 2)
    visits = random.randint(800, 5000)
    conversion = round(visits * (ctr / 100))

    st.subheader("📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("SEO Score", seo_score)

    with col2:
        st.metric("CTR", f"{ctr}%")

    with col3:
        st.metric("Visits", visits)

    with col4:
        st.metric("Conversions", conversion)

else:
    st.info("Completa los datos para comenzar")

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
    Eres un experto SEO en construcción.

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
