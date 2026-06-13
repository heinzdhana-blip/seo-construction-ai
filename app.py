import streamlit as st

st.set_page_config(
page_title="SEO Construction AI",
page_icon="🏗️",
layout="wide"
)

st.title("🏗️ SEO Construction AI")
st.subheader("Sistema Multiagente para Optimización SEO")

with st.sidebar:
st.header("AI Agents")
st.success("✅ Orchestrator Agent")
st.success("✅ SEO Diagnostic Agent")
st.success("✅ Context Analysis Agent")
st.success("✅ Prompt Generator Agent")
st.success("✅ Content Generator Agent")
st.success("✅ Technical Review Agent")
st.success("✅ Monitoring Agent")

company = st.text_input("Company Name")
service = st.text_input("Service Offered")
city = st.text_input("City")
url = st.text_input("Website URL")

if st.button("🚀 Run AI SEO Analysis"):

```
st.header("SEO Problems Found")
st.warning("Missing meta description")
st.warning("Low content length")
st.warning("Missing structured data")

st.header("Suggested Keywords")
st.write(f"{service} {city}")
st.write(f"best {service} {city}")
st.write(f"{service} near me")

st.header("SEO Title")
st.success(f"{company} | Professional {service} in {city}")

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
st.metric("Organic Visits", "1,540")
```
