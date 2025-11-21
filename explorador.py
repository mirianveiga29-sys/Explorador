import streamlit as st

# Portada con estilo
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏔️ Explorador de Decisiones</h1>", unsafe_allow_html=True)
st.image("https://cdn.pixabay.com/photo/2017/08/01/00/14/mountain-2562565_1280.jpg", use_column_width=True)

st.markdown("""
### Imaginá que sos un explorador 🧭
Debés atravesar distintos escenarios para llegar a tu destino.
Si bien estás solo, hay otras personas que también están explorando y, cada tanto, te cruzás con ellas.

👉 Cada decisión que tomes marcará un **perfil** que refleja tu estilo de explorador.
""")

puntajes = {"Innovador": 0, "Estratégico": 0, "Colaborativo": 0, "Audaz": 0}

# Pregunta 1: El río
opciones1 = [
    "Construís una balsa improvisada",
    "Buscás un puente más adelante",
    "Pedís ayuda a otros viajeros",
    "Te lanzás a cruzar nadando",
]
resp1 = st.radio("1️⃣ El río caudaloso: Tenés que cruzar un río. ¿Qué hacés?", opciones1, index=None)
if resp1:
    asignacion1 = {
        opciones1[0]: "Innovador",
        opciones1[1]: "Estratégico",
        opciones1[2]: "Colaborativo",
        opciones1[3]: "Audaz",
    }
    puntajes[asignacion1[resp1]] += 1

# Pregunta 2: El camino oscuro
opciones2 = [
    "Inventás una forma alternativa de iluminarlo",
    "Elegís el iluminado (seguro)",
    "Esperás a que otros decidan y los seguís",
    "Elegís el oscuro (riesgoso)",
]
resp2 = st.radio("2️⃣ El camino oscuro: El sendero se divide en dos.", opciones2, index=None)
if resp2:
    asignacion2 = {
        opciones2[0]: "Innovador",
        opciones2[1]: "Estratégico",
        opciones2[2]: "Colaborativo",
        opciones2[3]: "Audaz",
    }
    puntajes[asignacion2[resp2]] += 1

# Pregunta 3: El cofre
opciones3 = [
    "Intentás abrirlo con ingenio",
    "Lo marcás para volver después",
    "Consultás a otros para decidir juntos",
    "Lo dejás y seguís",
]
resp3 = st.radio("3️⃣ El cofre misterioso: Encontrás un cofre cerrado.", opciones3, index=None)
if resp3:
    asignacion3 = {
        opciones3[0]: "Innovador",
        opciones3[1]: "Estratégico",
        opciones3[2]: "Colaborativo",
        opciones3[3]: "Audaz",
    }
    puntajes[asignacion3[resp3]] += 1

# Pregunta 4: La montaña
opciones4 = [
    "Diseñás una herramienta creativa para superarla",
    "Buscás un camino alternativo",
    "Esperás ayuda externa",
    "Escalás directamente",
]
resp4 = st.radio("4️⃣ La montaña bloquea tu paso.", opciones4, index=None)
if resp4:
    asignacion4 = {
        opciones4[0]: "Innovador",
        opciones4[1]: "Estratégico",
        opciones4[2]: "Colaborativo",
        opciones4[3]: "Audaz",
    }
    puntajes[asignacion4[resp4]] += 1

# Pregunta 5: El refugio destruido
opciones5 = [
    "Improvisás un nuevo refugio con materiales disponibles",
    "Retrocedés y planificás otra ruta segura",
    "Te unís a otros exploradores para reconstruirlo juntos",
    "Te quedás igual, enfrentando la noche sin refugio",
]
resp5 = st.radio("5️⃣ El refugio destruido: Llegás a tu destino, pero el refugio está destruido. ¿Qué hacés?", opciones5, index=None)
if resp5:
    asignacion5 = {
        opciones5[0]: "Innovador",
        opciones5[1]: "Estratégico",
        opciones5[2]: "Colaborativo",
        opciones5[3]: "Audaz",
    }
    puntajes[asignacion5[resp5]] += 1

# Resultado final
if st.button("✨ Ver mi perfil ✨"):
    respuestas_completas = all([resp1, resp2, resp3, resp4, resp5])
    if not respuestas_completas:
        st.warning("Por favor, respondé todas las preguntas antes de ver el perfil.")
    else:
        perfil = max(puntajes, key=puntajes.get)
        st.success(f"🎉 Tu perfil es: **{perfil}**")

        if perfil == "Innovador":
            st.info("""
🌟 Innovador
- Creativo/a, curioso/a, buscás soluciones originales.
- Preferís probar ideas nuevas antes que seguir caminos tradicionales.
- 💪 Fortaleza: generás alternativas únicas y aportás frescura en los equipos.
- ⚠️ Riesgo: podés perder tiempo en experimentos poco prácticos si no medís impacto.
""")

        elif perfil == "Estratégico":
            st.warning("""
📊 Estratégico
- Analítico/a, planificador/a, orientado/a al largo plazo.
- Evaluás riesgos y beneficios antes de actuar.
- 💪 Fortaleza: anticipás problemas y organizás recursos con eficiencia.
- ⚠️ Riesgo: podés demorarte demasiado en decidir o ser percibido como excesivamente cauteloso.
""")

        elif perfil == "Colaborativo":
            st.success("""
🤝 Colaborativo
- Empático/a, comunicador/a, valorás el trabajo en equipo.
- Buscás apoyo, consultás y construís consensos con otros.
- 💪 Fortaleza: favorecés la cohesión grupal y potenciás la inteligencia colectiva.
- ⚠️ Riesgo: podés depender demasiado de la opinión ajena y perder autonomía.
""")

        elif perfil == "Audaz":
            st.error("""
⚡ Audaz
- Valiente, adaptable, tomás riesgos con confianza.
- Preferís actuar rápido y enfrentar lo desconocido.
- 💪 Fortaleza: inspirás dinamismo y capacidad de reacción en situaciones críticas.
- ⚠️ Riesgo: podés subestimar peligros y cometer errores por exceso de impulso.
""")
