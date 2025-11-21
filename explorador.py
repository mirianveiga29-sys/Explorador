import streamlit as st

# Portada con estilo
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏔️ Explorador de Decisiones</h1>", unsafe_allow_html=True)

# Imagen de portada (ejemplo libre de Pixabay/Unsplash)
st.image("https://cdn.pixabay.com/photo/2017/08/01/00/14/mountain-2562565_1280.jpg", use_column_width=True)

# Narrativa inicial
st.markdown("""
### Imaginá que sos un explorador 🧭
Debés atravesar distintos escenarios para llegar a tu destino.  
Si bien estás solo, hay otras personas que también están explorando y, cada tanto, te cruzás con ellas.  

👉 Cada decisión que tomes marcará un **perfil** que refleja tu estilo de explorador.
""")

puntajes = {"Innovador":0, "Estratégico":0, "Colaborativo":0, "Audaz":0}

# Pregunta 1
resp1 = st.radio("1️⃣ El río caudaloso: Tenés que cruzar un río. ¿Qué hacés?",
                 ["🚣 Construís una balsa improvisada (Innovador)",
                  "🌉 Buscás un puente más adelante (Estratégico)",
                  "🤝 Pedís ayuda a otros viajeros (Colaborativo)",
                  "🧭 Te lanzás a cruzar nadando (Audaz)"])
if "Innovador" in resp1: puntajes["Innovador"] += 1
elif "Estratégico" in resp1: puntajes["Estratégico"] += 1
elif "Colaborativo" in resp1: puntajes["Colaborativo"] += 1
else: puntajes["Audaz"] += 1

# Pregunta 2
resp2 = st.radio("2️⃣ El camino oscuro: El sendero se divide en dos.",
                 ["💡 Inventás una forma alternativa de iluminarlo (Innovador)",
                  "🔆 Elegís el iluminado (seguro) (Estratégico)",
                  "⏳ Esperás a que otros decidan y los seguís (Colaborativo)",
                  "🌑 Elegís el oscuro (riesgoso) (Audaz)"])
if "Innovador" in resp2: puntajes["Innovador"] += 1
elif "Estratégico" in resp2: puntajes["Estratégico"] += 1
elif "Colaborativo" in resp2: puntajes["Colaborativo"] += 1
else: puntajes["Audaz"] += 1

# Pregunta 3
resp3 = st.radio("3️⃣ El cofre misterioso: Encontrás un cofre cerrado.",
                 ["🗝️ Intentás abrirlo con ingenio (Innovador)",
                  "📍 Lo marcás para volver después (Estratégico)",
                  "🤲 Consultás a otros para decidir juntos (Colaborativo)",
                  "🚶 Lo dejás y seguís (Audaz)"])
if "Innovador" in resp3: puntajes["Innovador"] += 1
elif "Estratégico" in resp3: puntajes["Estratégico"] += 1
elif "Colaborativo" in resp3: puntajes["Colaborativo"] += 1
else: puntajes["Audaz"] += 1

# Pregunta 4
resp4 = st.radio("4️⃣ La montaña bloquea tu paso.",
                 ["🔧 Diseñás una herramienta creativa para superarla (Innovador)",
                  "🛤️ Buscás un camino alternativo (Estratégico)",
                  "📡 Esperás ayuda externa (Colaborativo)",
                  "🧗 Escalás directamente (Audaz)"])
if "Innovador" in resp4: puntajes["Innovador"] += 1
elif "Estratégico" in resp4: puntajes["Estratégico"] += 1
elif "Colaborativo" in resp4: puntajes["Colaborativo"] += 1
else: puntajes["Audaz"] += 1

# Resultado final
if st.button("✨ Ver mi perfil ✨"):
    perfil = max(puntajes, key=puntajes.get)
    st.success(f"🎉 Tu perfil es: **{perfil}**")

    if perfil == "Innovador":
        st.info("""🌟 **Innovador**
- Creativo/a, curioso/a, buscás soluciones originales.
- Preferís probar ideas nuevas antes que seguir caminos tradicionales.
- 💪 Fortaleza: generás alternativas únicas y aportás frescura en los equipos.
- ⚠️ Riesgo: podés perder tiempo en experimentos poco prácticos si no medís impacto.""")
    elif perfil == "Estratégico":
        st.warning("""📊 **Estratégico**
- Analítico/a, planificador/a, orientado/a al largo plazo.
- Evaluás riesgos y beneficios antes de actuar.
- 💪 Fortaleza: anticipás problemas y organizás recursos con eficiencia.
- ⚠️ Riesgo: podés demorarte demasiado en decidir o ser percibido como excesivamente cauteloso.""")
    elif perfil == "Colaborativo":
        st.success("""🤝 **Colaborativo**
- Empático/a, comunicador/a, valorás el trabajo en equipo.
- Buscás apoyo, consultás y construís consensos con otros.
- 💪 Fortaleza: favorecés la cohesión grupal y potenciás la inteligencia colectiva.
- ⚠️ Riesgo: podés depender demasiado de la opinión ajena y perder autonomía.""")
    elif perfil == "Audaz":
        st.error("""⚡ **Audaz**
- Valiente, adaptable, tomás riesgos con confianza.
- Preferís actuar rápido y enfrentar lo desconocido.
- 💪 Fortaleza: inspirás dinamismo y capacidad de reacción en situaciones críticas.
- ⚠️ Riesgo: podés subestimar peligros y cometer errores por exceso de impulso.""")

        st.warning("👉 Sos analítico/a y planificador/a, pensás en el largo plazo.")
    elif perfil == "Colaborativo":
        st.success("👉 Valorás el trabajo en equipo y la comunicación.")
    elif perfil == "Audaz":
        st.error("👉 Te adaptás rápido y tomás riesgos con confianza.")
