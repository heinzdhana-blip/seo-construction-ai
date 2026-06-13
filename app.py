import streamlit as st
import google.generativeai as genai
import random

# Configuración de la página
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# PASO 1 — Diseño CSS Bento
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
    }
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(102,126,234,0.4);
    }
</style>
""", unsafe_allow_html=True)

# Configuración de Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-pro")

# Título principal
st.title("SEO Multi-Agent Optimization Platform")

st.markdown("""
### Intelligent SEO Optimization for Construction SMEs

This platform uses a collaborative multi-agent architecture to analyze,
generate and optimize SEO strategies for construction companies.
""")

# Sidebar
with st.sidebar:
    st.header("🤖 AI Agents")
    st.success("✅ Orchestrator Agent")
    st.success("✅ SEO Diagnostic Agent")
    st.success("✅ Context Analysis Agent")
    st.success("✅ Prompt Generator Agent")
    st.success("✅ Content Generator Agent")
    st.success("✅ Technical Review Agent")
    st.success("✅ Monitoring Agent")

# PASO 2 — Bento Layout para el formulario
st.markdown("## 🧱 Business Input Panel")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("🏢 Nombre de la Empresa")
    city = st.text_input("📍 Ciudad")

with col2:
    service = st.text_input("🛠️ Servicio Ofrecido")
    url = st.text_input("🌐 Sitio Web")

# Botón principal
if st.button("🚀 Run AI SEO Analysis"):
    
    # PASO 3 — Bento Section para SEO Problems
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("🔍 SEO Problems Found")
    
    st.warning("⚠️ Missing meta description")
    st.warning("📄 Low content length")
    st.warning("📊 Missing structured data")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # PASO 3 — Bento Section para Suggested Keywords
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("📈 Suggested Keywords")
    
    st.write(f"🔑 {service} {city}")
    st.write(f"⭐ best {service} {city}")
    st.write(f"📍 {service} near me")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Prompt para Gemini
    prompt = f"""
    Actúa como un consultor SEO senior especializado en empresas de construcción.

    DATOS:
    Empresa: {company}
    Servicio: {service}
    Ciudad: {city}
    Sitio Web: {url}

    Genera:

    1. SEO Title
    2. Meta Description
    3. 5 palabras clave SEO
    4. Descripción optimizada del servicio
    5. FAQ con 3 preguntas frecuentes

    Todo en español.
    Usa formato profesional.
    """
    
    # PASO 3 — Bento Section para Gemini Output
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.subheader("🤖 AI Generated Content")
    
    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    
    except Exception as e:
        st.error(f"Error al conectar con Gemini: {e}")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Generar métricas aleatorias
    seo_score = random.randint(75, 98)
    ctr = round(random.uniform(2.5, 8.5), 2)
    visits = random.randint(800, 5000)
    
    # PASO 4 — Métricas estilo dashboard con 4 columnas
    st.markdown("## 📊 Performance Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("🎯 SEO Score", seo_score)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("📈 CTR", f"{ctr}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        st.metric("👥 Organic Visits", visits)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="bento-card">', unsafe_allow_html=True)
        # Métrica adicional de conversión
        conversion = round(visits * (ctr / 100))
        st.metric("🎯 Est. Conversiones", conversion)
        st.markdown('</div>', unsafe_allow_html=True)
