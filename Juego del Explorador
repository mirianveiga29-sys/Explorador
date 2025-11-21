import streamlit as st

# Título principal con emoji
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 Explorador de Decisiones</h1>", unsafe_allow_html=True)
st.write("Responde las preguntas y descubrí tu perfil.\n")

puntajes = {"Innovador":0, "Estratégico":0, "Colaborativo":0, "Audaz":0}

# Pregunta 1
resp1 = st.radio("1️⃣ El río caudaloso: Tenés que cruzar un río. ¿Qué hacés?",
                 ["🚣 Construís una balsa improvisada",
                  "🌉 Buscás un puente más adelante",
                  "🤝 Pedís ayuda a otros viajeros"])
if resp1.startswith("🚣"): puntajes["Innovador"] += 1
elif resp1.startswith("🌉"): puntajes["Estratégico"] += 1
else: puntajes["Colaborativo"] += 1

# Pregunta 2
resp2 = st.radio("2️⃣ El camino oscuro: El sendero se divide en dos.",
                 ["🔆 Elegís el iluminado (seguro)",
                  "🌑 Elegís el oscuro (riesgoso)",
                  "⏳ Esperás más información"])
if resp2.startswith("🔆"): puntajes["Estratégico"] += 1
elif resp2.startswith("🌑"): puntajes["Audaz"] += 1
else: puntajes["Estratégico"] += 1

# Pregunta 3
resp3 = st.radio("3️⃣ El cofre misterioso: Encontrás un cofre cerrado.",
                 ["🗝️ Intentás abrirlo con ingenio",
                  "🚶 Lo dejás y seguís",
                  "📍 Lo marcás para volver después"])
if resp3.startswith("🗝️"): puntajes["Innovador"] += 1
elif resp3.startswith("🚶"): puntajes["Audaz"] += 1
else: puntajes["Estratégico"] += 1

# Pregunta 4
resp4 = st.radio("4️⃣ El cruce final: Llegás a una montaña que bloquea tu paso.",
                 ["🧗 Escalás directamente",
                  "🛤️ Buscás un camino alternativo",
                  "📡 Esperás ayuda externa"])
if resp4.startswith("🧗"): puntajes["Audaz"] += 1
elif resp4.startswith("🛤️"): puntajes["Estratégico"] += 1
else: puntajes["Colaborativo"] += 1

# Resultado final
if st.button("✨ Ver mi perfil ✨"):
    perfil = max(puntajes, key=puntajes.get)
    st.success(f"🎉 Tu perfil es: **{perfil}**")

    if perfil == "Innovador":
        st.info("👉 Sos creativo/a y resolutivo/a, buscás soluciones originales.")
    elif perfil == "Estratégico":
        st.warning("👉 Sos analítico/a y planificador/a, pensás en el largo plazo.")
    elif perfil == "Colaborativo":
        st.success("👉 Valorás el trabajo en equipo y la comunicación.")
    elif perfil == "Audaz":
        st.error("👉 Te adaptás rápido y tomás riesgos con confianza.")
