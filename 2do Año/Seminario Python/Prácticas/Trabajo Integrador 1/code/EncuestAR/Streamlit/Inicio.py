import streamlit as st

st.header("📋 Inicio")
st.title("Encuest.AR")
st.markdown("## Bienvenido a Encuest.AR")
st.write("Usá el menú de la izquierda para navegar por las secciones.")
st.markdown("""
*Encuest.AR* es una aplicacion para ver y buscar datos de la *Encuesta Permanente de Hogares (EPH)*, hecha por el INDEC.

La EPH junta informacion sobre las condiciones de vida y el trabajo de la gente en Argentina. Cada trimestre se cargan
dos archivos: uno con datos de los hogares y otro con datos de las personas.

En esta app vas a poder ver datos sobre educacion, ocupacion, vivienda, ingresos y otras cosas.

---

### Como usar la app

1. **Carga los datos y actualiza el dataset**  
   - Ve a **Carga de datos**, clickea en **Browse Files**, sube los archivos EPH (hogares e individuos) y haz clic en **Actualizar dataset** para generar los CSV unificados en `results/`.

3. **Explorar y filtrar**  
   - Selecciona en el menú lateral la sección que quieras (Demografía, Vivienda, Empleo, Educación, Ingresos).  
   - Ajusta año, trimestre o aglomerado con los controles de cada página para ver los gráficos y tablas.
""")