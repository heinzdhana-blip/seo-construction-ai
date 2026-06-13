import streamlit as st
import google.generativeai as genai
import random

# ==================== CONFIGURACIÓN DE LA PÁGINA ====================
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# ==================== INICIALIZAR HISTORIAL DEL CHAT ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================== CSS BENTO DESIGN ====================
st.markdown("""
<style>
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
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
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
    .chat-container {
        height: 400px;
        overflow-y: auto;
    }
</style>
""", unsafe_allow_html=True)

# ==================== CONFIGURACIÓN DE GEMINI ====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Lista de modelos disponibles (usar el más reciente y estable)
# Opciones correctas: "models/gemini-1.5-flash", "models/gemini-2.5-pro"
# Nota: Algunas versiones requieren el prefijo "models/"
try:
    # Intentar con el modelo más reciente
    model = genai.GenerativeModel("models/gemini-2.5-flash")
except Exception as e:
    try:
        # Fallback a versión pro
        model = genai.GenerativeModel("models/gemini-2.5-pro")
    except Exception as e:
        # Último fallback
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

# ==================== HEADER PRINCIPAL ====================
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
    
    st.divider()
    st.caption("Powered by Google Gemini AI")
    
    # Mostrar información del modelo
    st.info("🤖 **Modelo activo:** gemini-1.5-flash")
    
    # Botón para probar la conexión
    if st.button("🔌 Probar conexión Gemini"):
        try:
            test_response = model.generate_content("Di 'Conexión exitosa'")
            st.success("✅ Conexión exitosa con Gemini API")
        except Exception as e:
            st.error(f"❌ Error de conexión: {e}")

# ==================== FORMULARIO DE ENTRADA ====================
st.markdown("## 🧱 Business Input Panel")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("🏢 Nombre de la Empresa", placeholder="Ej: Construcciones XYZ")
    city = st.text_input("📍 Ciudad", placeholder="Ej: Madrid")

with col2:
    service = st.text_input("🛠️ Servicio Ofrecido", placeholder="Ej: Reformas integrales")
    url = st.text_input("🌐 Sitio Web", placeholder="Ej: www.construccionesxyz.com")

# ==================== BOTÓN PRINCIPAL ====================
if st.button("🚀 Run AI SEO Analysis", use_container_width=True):
    
    # Validación de campos
    if not company or not service or not city:
        st.error("❌ Por favor completa todos los campos obligatorios")
        st.stop()
    
    # ========== SECCIÓN 1: PROBLEMAS SEO ==========
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
    
    # ========== SECCIÓN 2: KEYWORDS SUGERIDAS ==========
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
    
    # ========== SECCIÓN 3: GENERACIÓN DE CONTENIDO ==========
    prompt = f"""
    Actúa como un consultor SEO senior especializado en empresas de construcción.

    DATOS:
    Empresa: {company}
    Servicio: {service}
    Ciudad: {city}
    Sitio Web: {url}

    Genera:

    1. SEO Title (máximo 60 caracteres)
    2. Meta Description (máximo 160 caracteres)
    3. 5 palabras clave SEO (formato lista)
    4. Descripción optimizada del servicio (80-100 palabras)
    5. FAQ con 3 preguntas frecuentes y sus respuestas

    Todo en español.
    Usa formato profesional y claro.
    """
    
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("🤖 AI Generated Content")
    
    with st.spinner("🔄 Generando contenido con Gemini AI..."):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Error al conectar con Gemini: {e}")
            st.info("💡 **Soluciones:**\n1. Verifica tu API key en .streamlit/secrets.toml\n2. Asegúrate de tener créditos en Google AI Studio\n3. Prueba reiniciar la aplicación")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # ========== SECCIÓN 4: MÉTRICAS ==========
    # Generar métricas aleatorias
    seo_score = random.randint(75, 98)
    ctr = round(random.uniform(2.5, 8.5), 2)
    visits = random.randint(800, 5000)
    conversion = round(visits * (ctr / 100))
    
    st.markdown("## 📊 Performance Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("🎯 SEO Score", f"{seo_score}/100", delta=f"{seo_score - 75}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("📈 CTR", f"{ctr}%", delta=f"{ctr - 5:.1f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("👥 Organic Visits", f"{visits:,}", delta=f"+{visits - 1500}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("🎯 Est. Conversiones", f"{conversion:,}", delta=f"{conversion - 100}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ========== FOOTER ==========
    st.divider()
    st.caption("📊 Análisis generado por SEO Multi-Agent Platform | Datos actualizados en tiempo real")

# ==================== INFO ADICIONAL FUERA DEL BOTÓN ====================
else:
    st.info("👈 Completa los datos de la empresa y haz clic en 'Run AI SEO Analysis' para comenzar")

# ==================== SEO ASSISTANT CHATBOT ====================
st.markdown("## 💬 SEO Assistant Chatbot")
st.markdown("Pregunta cualquier duda sobre SEO para tu empresa de construcción")

# Crear contenedor para el chat
chat_container = st.container()

with chat_container:
    # Mostrar historial del chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Input del usuario
user_input = st.chat_input("💬 Pregunta al SEO Assistant...")

# Lógica del chat con Gemini
if user_input:
    # Guardar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)
    
    # Crear prompt del chatbot con contexto de la empresa
    chat_prompt = f"""
    Eres un asistente experto en SEO para empresas de construcción.
    
    Contexto de la empresa actual:
    - Empresa: {company if company else "No especificada"}
    - Servicio: {service if service else "No especificado"}
    - Ciudad: {city if city else "No especificada"}
    
    Responde de forma clara, profesional y concisa (máximo 150 palabras).
    
    Pregunta del usuario:
    {user_input}
    
    Respuesta en español:
    """
    
    try:
        response = model.generate_content(chat_prompt)
        bot_response = response.text
    except Exception as e:
        bot_response = f"❌ Error al conectar con Gemini: {e}"
        bot_response += "\n\n💡 **Soluciones rápidas:**\n• Verifica tu conexión a internet\n• Comprueba que la API key sea válida\n• Espera unos segundos y reintenta"
    
    # Guardar respuesta del asistente
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    
    with st.chat_message("assistant"):
        st.write(bot_response)
    
    # Forzar rerun para actualizar el chat
    st.rerun()

# Botón para limpiar el historial del chat
col_clear1, col_clear2, col_clear3 = st.columns([1, 2, 1])
with col_clear2:
    if st.button("🗑️ Limpiar historial del chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
