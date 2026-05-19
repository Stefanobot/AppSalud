import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la interfaz móvil (Responsive)
st.set_page_config(page_title="App IPS La Vida es Una", page_icon="🏥", layout="centered")

# Inicializar las listas COMPLETAMENTE VACÍAS (Sin datos de simulación)
if 'votos_atencion' not in st.session_state:
    st.session_state.votos_atencion = []
if 'votos_calidez' not in st.session_state:
    st.session_state.votos_calidez = []
if 'votos_satisfaccion' not in st.session_state:
    st.session_state.votos_satisfaccion = []

# Control de la pantalla actual
if 'pantalla_actual' not in st.session_state:
    st.session_state.pantalla_actual = "Inicio"

def ir_a(pantalla):
    st.session_state.pantalla_actual = pantalla

# ==============================================================================
# PANTALLA 1: INICIO (LOGIN)
# ==============================================================================
if st.session_state.pantalla_actual == "Inicio":
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>🏥 IPS La Vida es Una</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Gestión de Calidad y Humanización en Salud</p>", unsafe_allow_html=True)
    
    st.write("##")
    st.write("### Bienvenido al Sistema Institucional")
    st.write("Por favor, seleccione su rol para ingresar a la plataforma:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👤 Soy Paciente", use_container_width=True):
            ir_a("Paciente")
            st.rerun()
            
    with col2:
        if st.button("🩺 Soy Personal de Salud", use_container_width=True):
            ir_a("Personal_Salud")
            st.rerun()
            
    st.write("---")
    st.caption("📍 Sede Bogotá - Proyecto de Aula de Estadística Inferencial")

# ==============================================================================
# PANTALLA 2: PANTALLA DEL PACIENTE (EVALUACIÓN DEL SERVICIO)
# ==============================================================================
elif st.session_state.pantalla_actual == "Paciente":
    st.markdown("<h2 style='color: #0284C7;'>🥰 Tu opinión nos importa. Ayúdanos a mejorar</h2>", unsafe_allow_html=True)
    st.write("Para la IPS La Vida es Una, detrás de cada dato hay una historia humana. Califique su experiencia hoy:")
    
    with st.form("formulario_paciente", clear_on_submit=True):
        p1 = st.radio(
            "1. ¿El personal médico te escuchó con atención y empatía?",
            options=["😊 Muy Feliz / Satisfecho", "😐 Neutral", "😢 Triste / Insatisfecho"]
        )
        
        p2 = st.radio(
            "2. ¿Recibiste un trato cálido, digno y respetuoso?",
            options=["😊 Muy Feliz / Satisfecho", "😐 Neutral", "😢 Triste / Insatisfecho"]
        )
        
        p3 = st.radio(
            "3. Califica tu satisfacción general con el servicio el día de hoy:",
            options=["😊 Muy Feliz / Satisfecho", "😐 Neutral", "😢 Triste / Insatisfecho"]
        )
        
        enviar = st.form_submit_button("Registrar Mi Experiencia")
        
        if enviar:
            # Al responder, sumamos un 1 (Satisfecho/Neutral) o un 0 (Insatisfecho) en tiempo real
            st.session_state.votos_atencion.append(1 if "😊" in p1 or "😐" in p1 else 0)
            st.session_state.votos_calidez.append(1 if "😊" in p2 or "😐" in p2 else 0)
            st.session_state.votos_satisfaccion.append(1 if "😊" in p3 or "😐" in p3 else 0)
            st.success("¡Muchas gracias! Tu valiosa opinión ha sido guardada para humanizar nuestros servicios.")
            
    if st.button("⬅️ Volver al Inicio"):
        ir_a("Inicio")
        st.rerun()

# ==============================================================================
# PANTALLA 3: PANTALLA DEL MÉDICO (CÁPSULAS DE HUMANIZACIÓN)
# ==============================================================================
elif st.session_state.pantalla_actual == "Personal_Salud":
    st.markdown("<h2 style='color: #1E3A8A;'>🩺 Panel del Personal Asistencial y Administrativo</h2>", unsafe_allow_html=True)
    st.write("Seleccione el área a la que desea ingresar:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📚 Ver Cápsulas de Formación"):
            ir_a("Capsulas")
            st.rerun()
    with col2:
        if st.button("📊 Ver Panel Administrativo / Analítico"):
            ir_a("Administrativa")
            st.rerun()
            
    st.write("##")
    if st.button("⬅️ Volver al Inicio"):
        ir_a("Inicio")
        st.rerun()

elif st.session_state.pantalla_actual == "Capsulas":
    st.markdown("<h2 style='color: #0284C7;'>📚 Cápsulas de Humanización en Salud</h2>", unsafe_allow_html=True)
    st.write("Plan de formación continua enfocado en el fortalecimiento de la empatía y la comunicación asertiva:")
    
    st.info("💡 **Módulo 1: Comunicación Asertiva**\n\n_La humanización comienza cuando el personal de salud reconoce al paciente como una persona integral y no solo como un número de cama o diagnóstico._")
    
    st.info("💡 **Módulo 2: Manejo de la Empatía en Consulta**\n\n_Escuchar activamente al paciente reduce la incertidumbre y mitiga significativamente los temores y expectativas del usuario._")
    
    if st.button("⬅️ Volver al Menú Anterior"):
        ir_a("Personal_Salud")
        st.rerun()

# ==============================================================================
# PANTALLA 4: PANTALLA ADMINISTRATIVA (CÁLCULO EN TIEMPO REAL)
# ==============================================================================
elif st.session_state.pantalla_actual == "Administrativa":
    st.markdown("<h2 style='color: #1E3A8A;'>📊 Panel Administrativo de Analítica Inferencial</h2>", unsafe_allow_html=True)
    st.write("Dirección Estratégica - Datos consolidados dinámicamente según las respuestas recibidas.")
    
    datos = st.session_state.votos_satisfaccion
    n = len(datos)
    
    # CONTROL DE DATOS VACÍOS: Si nadie ha votado, no hacemos operaciones matemáticas
    if n == 0:
        st.warning("📥 **Esperando datos de origen:** En este momento no hay encuestas registradas en el sistema. Los indicadores estadísticos se activarán automáticamente cuando el primer paciente registre su experiencia.")
    else:
        # Si ya hay datos, calculamos la proporción real en caliente
        satisfechos = sum(datos)
        proporcion_p = satisfechos / n
        
        # Calcular Intervalo de Confianza al 95% para la proporción
        z_95 = 1.96
        error_estandar = np.sqrt((proporcion_p * (1 - proporcion_p)) / n)
        limite_inferior = max(0.0, proporcion_p - (z_95 * error_estandar))
        limite_superior = min(1.0, proporcion_p + (z_95 * error_estandar))
        
        # Métricas Visuales Dinámicas
        col1, col2, col3 = st.columns(3)
        col1.metric("Muestra Real ($n$)", value=n)
        col2.metric("Proporción Sat. ($p$)", value=f"{proporcion_p:.1%}")
        col3.metric("Nivel de Confianza", value="95%")
        
        st.write("---")
        st.subheader("Análisis Automático Integrado")
        st.success(f"**Intervalo de Confianza al 95% = [ {limite_inferior:.1%} a {limite_superior:.1%} ]**")
        
        # Barra porcentual interactiva
        st.write("### Distribución de la Satisfacción General Actual")
        st.progress(proporcion_p, text=f"Porcentaje de Satisfacción Activa: {proporcion_p:.1%}")
        
        # Evaluación de los rangos institucionales mínimos
        if limite_inferior >= 0.75:
            st.info("✅ **Nivel de satisfacción óptimo:** Los indicadores de calidad humana se mantienen estables dentro de los rangos institucionales aceptables.")
        else:
            st.error("⚠️ **Alerta Crítica:** El límite inferior del intervalo de confianza ha caído por debajo del estándar óptimo (75%). Se sugiere revisar las bitácoras del personal asistencial.")
        
    if st.button("⬅️ Volver al Menú Anterior"):
        ir_a("Personal_Salud")
        st.rerun()
