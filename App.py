import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lib  # Importar librería funciones
import libreria_clases_proyecto1 as libc    # Importar libreria clases

# --- Menu lateral 
menu = st.sidebar.selectbox(
    "Navegacion",
    ["Home", 
     "Ejercicio 1", 
     "Ejercicio 2", 
     "Ejercicio 3", 
     "Ejercicio 4"]
)

# ---> Home
if menu == "Home":
    st.title("Mi Primer Proyecto con Python y Streamlit")
    
    # Logo personal (analítica)
    st.image("logo1.png", caption="Logo representativo", width=150) 
    
    # Información del estudiante
    st.subheader("Información del Estudiante")
    st.write("**Nombre completo:** Carlos Magallanes Loza")
    st.write("**Nombre del módulo:** Especialización Python for Analytics")
    st.write("**Información general:** Estudiante con dominio avanzado en Oracle SQL y PL/SQL, Actualmente enfocado en construir aplicaciones que integren automatización y trazabilidad para mejorar la eficiencia en proyectos de datos.")
    st.write("**Año:** 2026")
    
    # Descripción del Proyecto
    st.subheader("Descripción del Proyecto")
    st.write("Este proyecto busca construir una aplicación en Streamlit que permita estimar el esfuerzo de queries Oracle mediante un framework parametrizable, con trazabilidad y justificación automática.")

    # Tecnologías utilizadas
    st.subheader("Tecnologías Utilizadas")
    st.markdown("""
    - **Python** (Streamlit, librerías de automatización)
    - **Visual Studio Code**
    """)

# ------------------------------------------------------------------------------------------------------------------------------------
# --- Ejercicio 1 - Flujo de caja con listas
# ------------------------------------------------------------------------------------------------------------------------------------

elif menu == "Ejercicio 1":
    st.title("Ejercicio 1")
    st.title("Flujo de Caja con Listas")

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Breve descripción del ejercicio
    st.markdown("""
    Este módulo permite registrar movimientos financieros en una lista.
    Cada movimiento incluye: concepto, tipo (Ingreso/Gasto) y valor.
    """)

    # widgets para ingresar datos
    concepto = st.text_input("Concepto del movimiento")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=10.0)

    # Botón para agregar movimientos
    if st.button("Registrar movimiento"):
        st.session_state.movimientos.append({
            "concepto": concepto,
            "tipo": tipo,
            "valor": valor
        })
        st.success("Movimiento registrado correctamente.")

    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        st.subheader("Lista de movimientos")
        st.dataframe(df, use_container_width=True)

    # Cálculo y Resultado de Flujo de caja
    total_ingresos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Ingreso")
    total_gastos = sum(m["valor"] for m in st.session_state.movimientos if m["tipo"] == "Gasto")
    saldo_final = total_ingresos - total_gastos

    st.subheader("Totales")
    st.metric(f"Total de ingresos", f"{total_ingresos}")
    st.metric(f"Total de gastos", f"{total_gastos}")
    st.metric(f"Saldo final", f"{saldo_final}")

    if saldo_final > 0:
        st.markdown("El flujo de caja está **a favor**.")
    elif saldo_final < 0:
            st.error("El flujo de caja está **en contra**.")
    else:
            st.markdown("El flujo de caja está **equilibrado**.")

# ------------------------------------------------------------------------------------------------------------------------------------
# --- Ejercicio 2 - Registro con NumPy, arrays y DataFrame
# ------------------------------------------------------------------------------------------------------------------------------------
elif menu == "Ejercicio 2":
    st.title("Ejercicio 2")
    st.title("Registro con NumPy, Arrays y DataFrame")

    # Breve descripción del ejercicio
    st.markdown("""
    Este ejercicio permite registrar productos y ventas usando **NumPy** y luego convertirlos en un **DataFrame**.
    Cada registro incluye: nombre del producto, categoría, precio, cantidad y total.
    """)

    # Inicialización de arrays en session_state
    if "productos" not in st.session_state:
        st.session_state.productos = np.array([])   # nombres
        st.session_state.categorias = np.array([]) # categorías
        st.session_state.precios = np.array([])    # precios
        st.session_state.cantidades = np.array([]) # cantidades
        st.session_state.totales = np.array([])    # totales

    # Formulario de ingreso de datos 
    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Alimentos", "Bebidas", "Tecnología", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, step=1.0)
    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    # Botón para agregar registro 
    if st.button("Agregar registro"):
        total = precio * cantidad
        
        # Concatenar valores en arrays
        st.session_state.productos = np.append(st.session_state.productos, nombre)
        st.session_state.categorias = np.append(st.session_state.categorias, categoria)
        st.session_state.precios = np.append(st.session_state.precios, precio)
        st.session_state.cantidades = np.append(st.session_state.cantidades, cantidad)
        st.session_state.totales = np.append(st.session_state.totales, total)
        
        st.success("Registro agregado correctamente")

    # Tabla en DataFrame actualizada
    if st.session_state.productos.size > 0:
        df = pd.DataFrame({
            "Producto": st.session_state.productos,
            "Categoría": st.session_state.categorias,
            "Precio": st.session_state.precios,
            "Cantidad": st.session_state.cantidades,
            "Total": st.session_state.totales
        })
        
        st.subheader("Tabla de registros")
        st.dataframe(df, use_container_width=True)

# ------------------------------------------------------------------------------------------------------------------------------------
# --- Ejercicio 3 - Uso de funciones desde una librería externa
# ------------------------------------------------------------------------------------------------------------------------------------
elif menu == "Ejercicio 3":
    st.title("Ejercicio 3")
    st.title("Uso de Funciones desde una Librería Externa")

    st.markdown("""
    Este ejercicio conecta funciones de una librería externa con **Streamlit**.
    El alumno debe seleccionar una función, ingresar parámetros y ver el resultado,
    además de guardar un histórico en una tabla.
    """)

    # Inicializar histórico
    if "resultados" not in st.session_state:
        st.session_state.resultados = []

    # Seleccionar una función deacuerdo al área de trabajo
    funcion = st.selectbox(
        "Selecciona una función",
        [
            "Calcular métricas de clasificación",
            "Calcular disponibilidad de sistema",
            "Calcular tiempo de transferencia de archivo",
            "Calcular tasa de error de transacciones",
            "Calcular almacenamiento de respaldo"
        ]
    )

    # Widgets y ejecución según función
    if funcion == "Calcular métricas de clasificación":
        tp = st.number_input("True Positives (TP)", min_value=0, step=1)
        fp = st.number_input("False Positives (FP)", min_value=0, step=1)
        fn = st.number_input("False Negatives (FN)", min_value=0, step=1)
        if st.button("Ejecutar"):
            resultado = lib.calcular_metricas_clasificacion(tp, fp, fn)
            st.write("Resultado:", resultado)
            st.session_state.resultados.append(
                {"Función": funcion, "Entrada": f"TP={tp}, FP={fp}, FN={fn}", "Resultado": resultado}
            )

    elif funcion == "Calcular disponibilidad de sistema":
        tiempo_total = st.number_input("Tiempo total (horas)", min_value=0.0, step=1.0)
        tiempo_caida = st.number_input("Tiempo de caída (horas)", min_value=0.0, step=1.0)
        if st.button("Ejecutar"):
            resultado = lib.calcular_disponibilidad_sistema(tiempo_total, tiempo_caida)
            st.write("Resultado:", resultado)
            st.session_state.resultados.append(
                {"Función": funcion, "Entrada": f"Total={tiempo_total}, Caída={tiempo_caida}", "Resultado": resultado}
            )

    elif funcion == "Calcular tiempo de transferencia de archivo":
        tamano = st.number_input("Tamaño del archivo (MB)", min_value=0.0, step=1.0)
        velocidad = st.number_input("Velocidad (Mbps)", min_value=0.1, step=0.1)
        if st.button("Ejecutar"):
            resultado = lib.calcular_tiempo_transferencia_archivo(tamano, velocidad)
            st.write("Resultado:", resultado)
            st.session_state.resultados.append(
                {"Función": funcion, "Entrada": f"Tamaño={tamano}, Velocidad={velocidad}", "Resultado": resultado}
            )

    elif funcion == "Calcular tasa de error de transacciones":
        fallidas = st.number_input("Transacciones fallidas", min_value=0, step=1)
        totales = st.number_input("Transacciones totales", min_value=1, step=1)
        if st.button("Ejecutar"):
            resultado = lib.calcular_tasa_error_transacciones(fallidas, totales)
            st.write("Resultado:", resultado)
            st.session_state.resultados.append(
                {"Función": funcion, "Entrada": f"Fallidas={fallidas}, Totales={totales}", "Resultado": resultado}
            )

    elif funcion == "Calcular almacenamiento de respaldo":
        usuarios = st.number_input("Número de usuarios", min_value=1, step=1)
        archivos = st.number_input("Archivos por usuario", min_value=1, step=1)
        tamano_promedio = st.number_input("Tamaño promedio por archivo (MB)", min_value=0.1, step=0.1)
        factor = st.number_input("Factor de respaldo", min_value=0.1, step=0.1)
        if st.button("Ejecutar"):
            resultado = lib.calcular_almacenamiento_respaldo(usuarios, archivos, tamano_promedio, factor)
            st.write("Resultado:", resultado)
            st.session_state.resultados.append(
                {"Función": funcion, "Entrada": f"Usuarios={usuarios}, Archivos={archivos}, Tamaño={tamano_promedio}, Factor={factor}", "Resultado": resultado}
            )

    # Mostrar histórico en una tabla de tipo DataFrame
    if st.session_state.resultados:
        df = pd.DataFrame(st.session_state.resultados)
        st.subheader("Histórico de resultados")
        st.dataframe(df, use_container_width=True)


# ------------------------------------------------------------------------------------------------------------------------------------
# --- Ejercicio 4 - Uso de clases desde una librería externa con CRUD
# ------------------------------------------------------------------------------------------------------------------------------------
elif menu == "Ejercicio 4":
    st.title("Ejercicio 4")
    st.title("Proyectos de Inversión con CRUD")

    st.markdown("""
    Este ejercicio conecta la clase **ProyectoInversion** con **Streamlit**.
    El alumno puede crear proyectos, visualizar métricas financieras, actualizarlas y eliminarlas.
    """)

    # Inicializar lista de proyectos
    if "proyectos" not in st.session_state:
        st.session_state.proyectos = []

    # Crear pestañas
    tab1, tab2, tab3, tab4 = st.tabs(["Crear", "Leer", "Actualizar", "Eliminar"])

    # -> Crear
    with tab1:
        st.subheader("Crear proyecto de inversión")
        nombre = st.text_input("Nombre del proyecto")
        inversion = st.number_input("Inversión inicial", min_value=0.0, step=100.0)
        tasa = st.number_input("Tasa de descuento (%)", min_value=0.0, step=0.1)

        # Entrada de flujos como lista separada por comas
        flujos_str = st.text_input("Flujos de caja (separados por comas)", "1000,1200,1500")
        flujos = [float(x.strip()) for x in flujos_str.split(",")] if flujos_str else []

        if st.button("Crear proyecto"):
            try:
                nuevo = libc.ProyectoInversion(nombre, inversion, flujos, tasa)
                st.session_state.proyectos.append(nuevo)
                st.success("Proyecto creado correctamente")
            except Exception as e:
                st.error(f"Error: {e}")

    # -> Leer
    with tab2:
        st.subheader("Lista de proyectos")
        if st.session_state.proyectos:
            data = [p.resumen() for p in st.session_state.proyectos]
            df = pd.DataFrame(data)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No hay proyectos registrados aún.")

    # -> Actualizar
    with tab3:
        st.subheader("Actualizar proyecto")
        if st.session_state.proyectos:
            seleccion = st.selectbox("Selecciona proyecto para actualizar", [p.nombre_proyecto for p in st.session_state.proyectos])
            nueva_inversion = st.number_input("Nueva inversión inicial", min_value=0.0, step=100.0)
            nueva_tasa = st.number_input("Nueva tasa de descuento (%)", min_value=0.0, step=0.1)
            nuevos_flujos_str = st.text_input("Nuevos flujos (separados por comas)", "1000,1200,1500")
            nuevos_flujos = [float(x.strip()) for x in nuevos_flujos_str.split(",")] if nuevos_flujos_str else []

            if st.button("Actualizar proyecto"):
                for p in st.session_state.proyectos:
                    if p.nombre_proyecto == seleccion:
                        p.inversion_inicial = nueva_inversion
                        p.tasa_descuento_pct = nueva_tasa
                        p.flujos = nuevos_flujos
                        st.success(f"Proyecto '{seleccion}' actualizado correctamente")
        else:
            st.info("No hay proyectos para actualizar.")

    # -> Eliminar
    with tab4:
        st.subheader("Eliminar proyecto")
        if st.session_state.proyectos:
            eliminar = st.selectbox("Selecciona proyecto para eliminar", [p.nombre_proyecto for p in st.session_state.proyectos])
            if st.button("Eliminar proyecto"):
                st.session_state.proyectos = [p for p in st.session_state.proyectos if p.nombre_proyecto != eliminar]
                st.warning(f"Proyecto '{eliminar}' eliminado")
        else:
            st.info("No hay proyectos para eliminar.")

