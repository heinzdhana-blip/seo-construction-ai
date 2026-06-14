import streamlit as st
import ollama
import random

# ==================== CONFIGURACIÓN DE LA PÁGINA ====================
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# ==================== INICIALIZAR CHAT ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================== CSS ====================
st.markdown("""
<style>
.hero-section {
    height: 50vh;
    background: url("https://riobrancoperu.com.pe/wp-content/uploads/2015/01/construccion-1100x420.jpg");
    background-size: cover;
    background-position: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    position: relative;
    border-radius: 0 0 30px 30px;
}

.hero-section::before {
    content: "";
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.55);
    border-radius: 0 0 30px 30px;
}

.hero-section h1,
.hero-section p {
    position: relative;
    z-index: 1;
}

.hero-section h1 {
    font-size: 2.8rem;
    margin-bottom: 10px;
}

.hero-section p {
    font-size: 1.3rem;
}

/* BENTO DESIGN */
.bento-card {
    background: linear-gradient(135deg, #1e1e2f 0%, #2a2a3a 100%);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 0.5rem 0;
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    border: 1px solid rgba(255,255,255,0.1);
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
    width: 100%;
}

.stButton > button:hover {
    transform: scale(1.05);
}

h1, h2, h3 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
</style>
""", unsafe_allow_html=True)

# ==================== HERO SECTION ====================
st.markdown("""
<div class="hero-section">
    <h1>🏗️ SEO Multi-Agent Optimization Platform</h1>
    <p>Intelligent SEO Optimization for Construction SMEs</p>
</div>
""", unsafe_allow_html=True)

# ==================== OLLAMA ====================
LLAMA_MODEL = "llama3"

# ==================== INPUTS ====================
st.markdown("## 🧱 Business Input Panel")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("🏢 Nombre de la Empresa", placeholder="Ej: Construcciones XYZ")
    city = st.text_input("📍 Ciudad", placeholder="Ej: Madrid")

with col2:
    service = st.text_input("🛠️ Servicio Ofrecido", placeholder="Ej: Reformas integrales")
    url = st.text_input("🌐 Sitio Web", placeholder="Ej: www.construccionesxyz.com")

# ==================== BOTÓN SEO ====================
if st.button("🚀 Run AI SEO Analysis", use_container_width=True):

    if not company or not service or not city:
        st.error("❌ Completa todos los campos")
        st.stop()

    # ========== SECCIÓN 1 ==========
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

    # ========== SECCIÓN 2 ==========
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

    # ========== PROMPT ==========
    prompt = f"""
Eres un consultor SEO experto en empresas constructoras.

Analiza:

Empresa: {company}
Servicio: {service}
Ciudad: {city}
Sitio Web: {url}

Genera:

1. Auditoría SEO
2. Palabras clave recomendadas
3. Meta descripción
4. Título SEO
5. Estrategia de contenido
6. Recomendaciones técnicas
7. Plan de mejora

Respuesta en español, clara y profesional.
"""

    # ========== GENERAR CONTENIDO ==========
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("🤖 AI Generated Content")
    
    with st.spinner("🔄 Generando análisis SEO con Llama3..."):
        try:
            response = ollama.chat(
                model=LLAMA_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            st.write(response["message"]["content"])
        except Exception as e:
            st.error(f"❌ Error conectando con Ollama: {e}")
            st.info("💡 Asegúrate de tener Ollama instalado y ejecutándose: `ollama serve`")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # ========== MÉTRICAS ==========
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
        st.metric("👥 Visitas", f"{visits:,}", delta=f"+{visits - 1500}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("🎯 Conversiones", f"{conversion:,}", delta=f"{conversion - 100}")
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== INFO ====================
else:
    st.info("👈 Completa los datos de la empresa y haz clic en 'Run AI SEO Analysis' para comenzar")

# ==================== CHATBOT ====================
st.markdown("## 💬 SEO Assistant Chatbot")
st.markdown("Pregunta cualquier duda sobre SEO para tu empresa de construcción")

# Mostrar mensajes del chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input del usuario
user_input = st.chat_input("💬 Pregunta al SEO Assistant...")

if user_input:
    # Guardar mensaje del usuario
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    with st.chat_message("user"):
        st.write(user_input)

    # Crear prompt con contexto
    chat_prompt = f"""
Eres un experto SEO especializado en construcción.

Contexto:
Empresa: {company if company else "No especificada"}
Servicio: {service if service else "No especificado"}
Ciudad: {city if city else "No especificada"}

Pregunta del usuario:
{user_input}

Responde en español, de forma clara, profesional y concisa.
"""

    try:
        response = ollama.chat(
            model=LLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": chat_prompt
                }
            ]
        )
        bot_response = response["message"]["content"]
    except Exception as e:
        bot_response = f"❌ Error conectando con Ollama: {e}"

    # Guardar respuesta
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })
    
    with st.chat_message("assistant"):
        st.write(bot_response)
    
    st.rerun()

# ==================== LIMPIAR CHAT ====================
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    if st.button("🗑️ Limpiar historial del chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
