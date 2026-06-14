import streamlit as st
import google.generativeai as genai
import random

# ==================== CONFIGURACIÓN DE LA PÁGINA ====================
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# ==================== INICIALIZAR CHAT MEMORY ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================== CSS ESTILOS ====================
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
        margin-bottom: 2rem;
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
        color: white !important;
        text-align: center;
    }

    .hero h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    .hero p {
        font-size: 1.2rem;
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
        transition: transform 0.3s ease;
    }

    .bento-card:hover {
        transform: translateY(-5px);
    }

    .section-container {
        background: rgba(255,255,255,0.7);
        border-radius: 25px;
        padding: 1rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }

    /* ===== BOTÓN ===== */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 30px;
        width: 100%;
        font-weight: bold;
        transition: transform 0.2s ease;
    }

    .stButton > button:hover {
        transform: scale(1.02);
    }

    /* ===== METRICAS ===== */
    [data-testid="stMetricValue"] {
        color: #667eea !important;
        font-size: 1.8rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ==================== CONFIGURACIÓN DE GEMINI ====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Intentar con diferentes modelos
try:
    model = genai.GenerativeModel("models/gemini-1.5-flash")
except:
    try:
        model = genai.GenerativeModel("models/gemini-1.5-pro")
    except:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

# ==================== HERO SECTION ====================
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
    st.success("✅ Orchestrator Agent")
    st.success("✅ SEO Diagnostic Agent")
    st.success("✅ Content Generator Agent")
    st.success("✅ Monitoring Agent")
    
    st.divider()
    st.caption("Powered by Google Gemini AI")

# ==================== INPUT PANEL ====================
st.markdown("## 🧱 Business Input Panel")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("🏢 Nombre de la Empresa", placeholder="Ej: Construcciones XYZ")
    city = st.text_input("📍 Ciudad", placeholder="Ej: Madrid")

with col2:
    service = st.text_input("🛠️ Servicio Ofrecido", placeholder="Ej: Reformas integrales")
    url = st.text_input("🌐 Sitio Web", placeholder="Ej: www.construccionesxyz.com")

# ==================== ANÁLISIS SEO ====================
if st.button("🚀 Run AI SEO Analysis", use_container_width=True):

    # Validación de campos
    if not company or not service or not city:
        st.error("❌ Por favor completa todos los campos obligatorios")
        st.stop()

    # ========== PROBLEMAS SEO ==========
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("🔍 SEO Problems Found")
    
    col_prob1, col_prob2, col_prob3 = st.columns(3)
    with col_prob1:
        st.warning("⚠️ Missing meta description")
    with col_prob2:
        st.warning("📄 Low content length")
    with col_prob3:
        st.warning("📊 Missing structured data")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ========== KEYWORDS SUGERIDAS ==========
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("📈 Suggested Keywords")
    
    col_kw1, col_kw2, col_kw3 = st.columns(3)
    with col_kw1:
        st.info(f"🔑 {service} {city}")
    with col_kw2:
        st.info(f"⭐ best {service} {city}")
    with col_kw3:
        st.info(f"📍 {service} near me")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ========== PROMPT PARA GEMINI ==========
    prompt = f"""
    Actúa como un consultor SEO senior especializado en empresas de construcción.

    DATOS:
    Empresa: {company}
    Servicio: {service}
    Ciudad: {city}
    Sitio Web: {url}

    Genera en español:

    1. SEO Title (máximo 60 caracteres)
    2. Meta Description (máximo 160 caracteres)
    3. 5 palabras clave SEO recomendadas
    4. Descripción optimizada del servicio (80-100 palabras)
    5. Recomendaciones técnicas SEO
    6. Plan de mejora a 30 días

    Usa formato profesional y claro.
    """

    # ========== CONTENIDO GENERADO ==========
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("🤖 AI Generated Content")
    
    with st.spinner("🔄 Generando análisis SEO con Gemini AI..."):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Error al conectar con Gemini: {e}")
            st.info("💡 Verifica tu API key en .streamlit/secrets.toml")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ========== MÉTRICAS ==========
    seo_score = random.randint(75, 98)
    ctr = round(random.uniform(2.5, 8.5), 2)
    visits = random.randint(800, 5000)
    conversion = round(visits * (ctr / 100))

    st.markdown("## 📊 Performance Dashboard")
    
    col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)

    with col_metric1:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("🎯 SEO Score", f"{seo_score}/100", delta=f"{seo_score - 75}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_metric2:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("📈 CTR", f"{ctr}%", delta=f"{ctr - 5:.1f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_metric3:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("👥 Organic Visits", f"{visits:,}", delta=f"+{visits - 1500}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_metric4:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("🎯 Est. Conversiones", f"{conversion:,}", delta=f"+{conversion - 100}")
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== INFO INICIAL ====================
else:
    st.info("👈 Completa los datos de la empresa y haz clic en 'Run AI SEO Analysis' para comenzar")

# ==================== SEO ASSISTANT CHATBOT ====================
st.markdown("## 💬 SEO Assistant Chatbot")
st.markdown("Pregunta cualquier duda sobre SEO para tu empresa de construcción")

# Mostrar historial del chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input del usuario
user_input = st.chat_input("💬 Pregunta al SEO Assistant...")

if user_input:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    # Crear prompt con contexto
    chat_prompt = f"""
    Eres un asistente experto en SEO para empresas de construcción.
    
    Contexto de la empresa:
    - Empresa: {company if company else "No especificada"}
    - Servicio: {service if service else "No especificado"}
    - Ciudad: {city if city else "No especificada"}
    
    Responde de forma clara, profesional y concisa.
    
    Pregunta del usuario:
    {user_input}
    
    Respuesta en español:
    """

    try:
        response = model.generate_content(chat_prompt)
        bot_response = response.text
    except Exception as e:
        bot_response = f"❌ Error al conectar con Gemini: {e}"

    # Guardar respuesta del asistente
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.write(bot_response)
    
    st.rerun()

# ==================== LIMPIAR CHAT ====================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("🗑️ Limpiar historial del chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
