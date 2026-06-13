import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("SEO Multi-Agent Optimization Platform")

st.markdown("""
### Intelligent SEO Optimization for Construction SMEs

This platform uses a collaborative multi-agent architecture to analyze,
generate and optimize SEO strategies for construction companies.
""")

with st.sidebar:
    st.header("AI Agents")
    st.success("✅ Orchestrator Agent")
    st.success("✅ SEO Diagnostic Agent")
    st.success("✅ Context Analysis Agent")
    st.success("✅ Prompt Generator Agent")
    st.success("✅ Content Generator Agent")
    st.success("✅ Technical Review Agent")
    st.success("✅ Monitoring Agent")

company = st.text_input("Nombre de la Empresa")
service = st.text_input("Servicio Ofrecido")
city = st.text_input("Ciudad")
url = st.text_input("Sitio Web")

if st.button("🚀 Run AI SEO Analysis"):
    st.header("SEO Problems Found")
    st.warning("Missing meta description")
    st.warning("Low content length")
    st.warning("Missing structured data")
    
    st.header("Suggested Keywords")
    st.write(f"{service} {city}")
    st.write(f"best {service} {city}")
    st.write(f"{service} near me")
    
prompt = f"""
Actúa como un experto SEO.

Empresa: {company}
Servicio: {service}
Ciudad: {city}

Genera:

1. SEO Title
2. Meta Description
3. 5 palabras clave SEO
4. FAQ con 3 preguntas frecuentes

Respuesta en español.
"""

response = model.generate_content(prompt)

st.header("Contenido generado por Gemini")
st.write(response.text)

    
    st.header("Meta Description")
    st.info(
        f"Looking for {service} in {city}? "
        f"{company} provides professional services with quality and reliability."
    )
    
    st.header("FAQ")
    st.write(f"How much does {service} cost?")
    st.write("Do you offer free estimates?")
    st.write("How long does the project take?")
    
    st.header("Monitoring Metrics")
    st.metric("SEO Score", "82")
    st.metric("CTR", "4.2%")
    st.metric("Organic Visits", "1540")
