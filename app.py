import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# Configuración de Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash")

# Título principal
st.title("🏗️ SEO Multi-Agent Optimization Platform")

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

# Formulario
company = st.text_input("Nombre de la Empresa")
service = st.text_input("Servicio Ofrecido")
city = st.text_input("Ciudad")
url = st.text_input("Sitio Web")

# Botón principal
if st.button("🚀 Run AI SEO Analysis"):
    # Diagnóstico SEO simulado
    st.header("🔍 SEO Problems Found")
    
    st.warning("Missing meta description")
    st.warning("Low content length")
    st.warning("Missing structured data")
    
    # Keywords simuladas
    st.header("📈 Suggested Keywords")
    
    st.write(f"{service} {city}")
    st.write(f"best {service} {city}")
    st.write(f"{service} near me")
    
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
    
    try:
        response = model.generate_content(prompt)
        
        st.header("🤖 Contenido generado por Gemini")
        st.write(response.text)
    
    except Exception as e:
        st.error(f"Error al conectar con Gemini: {e}")
    
    # Métricas
    st.header("📊 Monitoring Metrics")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("SEO Score", "82")
    
    with col2:
        st.metric("CTR", "4.2%")
    
    with col3:
        st.metric("Organic Visits", "1540")
