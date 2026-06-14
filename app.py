import streamlit as st
import google.generativeai as genai
import random

# ==================== CONFIGURACIÓN ====================
st.set_page_config(
    page_title="SEO Construction AI",
    page_icon="🏗️",
    layout="wide"
)

# ==================== MEMORY ====================
if "messages" not in st.session_state:
    st.session_state.messages = []

if "generated_content" not in st.session_state:
    st.session_state.generated_content = ""

# 🔥 CONTROL DE FLUJO (CLAVE)
if "mode" not in st.session_state:
    st.session_state.mode = "input"

# ==================== INPUT STATE ====================
if "company" not in st.session_state:
    st.session_state.company = ""

if "city" not in st.session_state:
    st.session_state.city = ""

if "service" not in st.session_state:
    st.session_state.service = ""

if "url" not in st.session_state:
    st.session_state.url = ""

# ==================== CSS ====================
st.markdown("""
<style>
.hero {
    height: 40vh;
    background: url("https://riobrancoperu.com.pe/wp-content/uploads/2015/01/construccion-1100x420.jpg");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 0 0 25px 25px;
    position: relative;
}

.hero::before {
    content: "";
    position: absolute;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.55);
}

.hero h1, .hero p {
    position: relative;
    color: white !important;
}

.stButton > button {
    width: 100%;
    border-radius: 25px;
    background: linear-gradient(135deg,#667eea,#764ba2);
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ==================== GEMINI ====================
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

# ==================== HERO ====================
st.markdown("""
<div class="hero">
    <div>
        <h1 class="title">🏗️ SEO Multi-Agent Platform</h1>
        <p>AI SEO Optimization System</p>
    </div>
</div>

<style>
.title {
    font-size: 6rem;  /* 🔥 DOBLE DE GRANDE */
    font-weight: 800;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ==================== LAYOUT ====================
left_col, main_col, right_col = st.columns([1.2, 3.5, 1.3])

# ==================== LEFT ====================
with left_col:
    with st.expander("🤖 AI Agents", expanded=False):
        st.success("Orchestrator Agent")
        st.success("SEO Diagnostic Agent")
        st.success("Context Analysis Agent")
        st.success("Prompt Generator Agent")
        st.success("Content Generator Agent")
        st.success("Technical Review Agent")
        st.success("Monitoring Agent")
        st.success("Human Reviewer")

# ==================== MAIN ====================
with main_col:

    st.markdown("## 🧱 Business Input")

    col1, col2 = st.columns(2)

    with col1:
        st.session_state.company = st.text_input("Empresa", value=st.session_state.company)
        st.session_state.city = st.text_input("Ciudad", value=st.session_state.city)

    with col2:
        st.session_state.service = st.text_input("Servicio", value=st.session_state.service)
        st.session_state.url = st.text_input("Web", value=st.session_state.url)

    if st.button("🚀 Run AI SEO Analysis"):

        if not st.session_state.company or not st.session_state.city or not st.session_state.service:
            st.error("Completa todos los campos")
            st.stop()

        # 🔥 CAMBIAR MODO (IMPORTANTE)
        st.session_state.mode = "analyzed"

        st.markdown("## 🔍 SEO Analysis")
        st.warning("Missing meta description")
        st.warning("Low content length")
        st.warning("Missing structured data")

        st.markdown("## 📈 Keywords")
        st.info(f"{st.session_state.service} {st.session_state.city}")
        st.info(f"best {st.session_state.service} {st.session_state.city}")
        st.info(f"{st.session_state.service} near me")

        prompt = f"""
        SEO expert.

        Empresa: {st.session_state.company}
        Servicio: {st.session_state.service}
        Ciudad: {st.session_state.city}
        Web: {st.session_state.url}

        Genera SEO completo profesional.
        """

        try:
            response = model.generate_content(prompt)
            st.session_state.generated_content = response.text

        except Exception as e:
            st.error(e)
            st.stop()

    # ==================== SOLO SE MUESTRA SI YA ANALIZÓ ====================
    if st.session_state.mode == "analyzed":

        st.markdown("## 🤖 AI Content")
        st.write(st.session_state.generated_content)

        st.markdown("## 👨‍💼 Human Review")

        approval = st.radio(
            "Estado",
            ["Pendiente", "Aprobado", "Rechazado"],
            horizontal=True,
            key="approval"
        )

        notes = st.text_area("Comentarios", key="notes")

        st.markdown("## 📊 Dashboard")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("SEO Score", random.randint(75, 98))
        with c2:
            st.metric("CTR", f"{round(random.uniform(2,8),2)}%")
        with c3:
            st.metric("Visits", random.randint(1000,5000))

# ==================== CHAT ====================
with right_col:

    with st.expander("💬 SEO Assistant", expanded=True):

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])

        user_input = st.chat_input("Pregunta al SEO Assistant...")

        if user_input:

            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            chat_prompt = f"""
            Eres experto SEO.

            Empresa: {st.session_state.company}
            Servicio: {st.session_state.service}
            Ciudad: {st.session_state.city}

            Contexto:
            {st.session_state.generated_content}

            Pregunta:
            {user_input}
            """

            response = model.generate_content(chat_prompt)

            st.session_state.messages.append({
                "role": "assistant",
                "content": response.text
            })

            st.rerun()

        if st.button("🗑️ Limpiar chat"):
            st.session_state.messages = []
            st.rerun()
