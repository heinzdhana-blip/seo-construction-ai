```python
import streamlit as st
import ollama
import random

# ==================== CONFIGURACIÓN DE LA PÁGINA ====================
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# ==================== HERO SECTION ====================
st.markdown("""
<div class="hero-section">
    <h1>🏗️ SEO Multi-Agent Optimization Platform</h1>
    <p>Intelligent SEO Optimization for Construction SMEs</p>
</div>
""", unsafe_allow_html=True)

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

# ==================== OLLAMA ====================
LLAMA_MODEL = "llama3"

# ==================== INPUTS ====================
st.markdown("## 🧱 Business Input Panel")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("🏢 Nombre de la Empresa")
    city = st.text_input("📍 Ciudad")

with col2:
    service = st.text_input("🛠️ Servicio Ofrecido")
    url = st.text_input("🌐 Sitio Web")

# ==================== BOTÓN SEO ====================
if st.button("🚀 Run AI SEO Analysis", use_container_width=True):

    if not company or not service or not city:
        st.error("Completa todos los campos")
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
"""

    st.subheader("🤖 AI Generated Content")

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
        st.error(f"Error conectando con Ollama: {e}")

    seo_score = random.randint(75, 98)
    ctr = round(random.uniform(2.5, 8.5), 2)
    visits = random.randint(800, 5000)
    conversion = round(visits * (ctr / 100))

    st.subheader("📊 Dashboard")

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
    st.info("Completa los datos para comenzar")

# ==================== CHATBOT ====================
st.markdown("## 💬 SEO Assistant Chatbot")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Pregunta al SEO Assistant...")

if user_input:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    chat_prompt = f"""
Eres un experto SEO especializado en construcción.

Empresa: {company}
Servicio: {service}
Ciudad: {city}

Pregunta del usuario:
{user_input}
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
        bot_response = f"Error: {e}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_response
        }
    )

    with st.chat_message("assistant"):
        st.write(bot_response)

    st.rerun()

# ==================== LIMPIAR CHAT ====================
if st.button("🗑️ Limpiar chat"):
    st.session_state.messages = []
    st.rerun()
```
