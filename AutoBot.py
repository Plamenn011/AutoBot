import tkinter as tk
import customtkinter as ctk
import random
import time
import threading
import pyautogui
import os
from PIL import Image, ImageTk

# Configuración del motor gráfico
ctk.set_appearance_mode("Dark")
bot_activo = False

# 🔑 Diccionario para traducir los nombres del menú a los comandos reales de PyAutoGUI
TRADUCTOR_TECLAS = {
    "W": "w",
    "A": "a",
    "S": "s",
    "D": "d",
    "Barra Espaciadora": "space",
    "Flecha Arriba": "up",
    "Flecha Abajo": "down",
    "Flecha Izquierda": "left",
    "Flecha Derecha": "right"
}

def pulsar_tecla_aleatoria(min_minutos, max_minutos, tecla_seleccionada):
    global bot_activo
    segundos_minimo = min_minutos * 60
    segundos_maximo = max_minutos * 60
    
    # Averiguamos qué comando real de teclado corresponde a lo elegido en el menú
    tecla_real = TRADUCTOR_TECLAS.get(tecla_seleccionada, "space")
    print(f"Bot iniciado. Rango: {min_minutos} a {max_minutos} min. Tecla: {tecla_real}")
    
    while bot_activo:
        if segundos_minimo == 0 and segundos_maximo == 0:
            tiempo_espera = 0.5
        else:
            tiempo_espera = random.randint(int(segundos_minimo), int(segundos_maximo))
            
        for i in range(101):
            if not bot_activo:
                break
            barra_progreso.set(i / 100)
            label_porcentaje.configure(text=f"{i}% PROCESS")
            time.sleep(tiempo_espera / 100)
            
        if not bot_activo:
            break
            
        # 🚀 Pulsamos la tecla que el usuario ha elegido en el desplegable
        pyautogui.press(tecla_real)
        print(f"¡Clack! Tecla '{tecla_real}' pulsada.")
        
        barra_progreso.set(0)
        label_porcentaje.configure(text="0% PROCESS")

def activar_bot():
    global bot_activo
    if not bot_activo:
        bot_activo = True
        label_estado.configure(text="SYS_STATUS: ONLINE 🟢", text_color="#00FF66")
        panel_central.configure(border_color="#00FF66")
        
        min_valor = int(combo_min.get())
        max_valor = int(combo_max.get())
        tecla_elegida = combo_tecla.get() # <--- Leemos la tecla del menú
        
        if min_valor > max_valor:
            max_valor = min_valor
            combo_max.set(str(max_valor))
        
        hilo = threading.Thread(target=pulsar_tecla_aleatoria, args=(min_valor, max_valor, tecla_elegida))
        hilo.start()

def desactivar_bot():
    global bot_activo
    bot_activo = False
    label_estado.configure(text="SYS_STATUS: INACTIVE 🔴", text_color="#FF334B")
    panel_central.configure(border_color="#00DCE6")
    barra_progreso.set(0)
    label_porcentaje.configure(text="0% PROCESS")

def salir_programa():
    desactivar_bot()
    ventana.destroy()

# --- CONFIGURACIÓN DE LA INTERFAZ MAESTRA ---
ventana = ctk.CTk()
ventana.title("Predator Engine - Anti-AFK Overclock Module")
ventana.attributes("-fullscreen", True)
ventana.configure(fg_color="#03070A")

ancho = ventana.winfo_screenwidth()
alto = ventana.winfo_screenheight()

canvas = tk.Canvas(ventana, width=ancho, height=alto, bg="#03070A", highlightthickness=0)
canvas.pack(fill="both", expand=True)

try:
    carpeta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(carpeta_actual, "fondo.png")
    imagen_original = Image.open(ruta_imagen)
    imagen_redimensionada = imagen_original.resize((ancho, alto), Image.Resampling.LANCZOS)
    fondo_gaming = ImageTk.PhotoImage(imagen_redimensionada)
    canvas.create_image(0, 0, image=fondo_gaming, anchor="nw")
except Exception as e:
    print("Error al cargar el fondo:", e)

canvas.create_oval(ancho//2 - 280, alto//2 - 280, ancho//2 + 280, alto//2 + 280, outline="#05979E", width=2)

# 📐 PANEL CENTRAL DE COMANDO
panel_central = ctk.CTkFrame(ventana, fg_color="#091118", corner_radius=24, border_width=3, border_color="#00DCE6")
panel_central.place(relx=0.5, rely=0.5, anchor="center")

titulo = ctk.CTkLabel(panel_central, text="AutoBot", font=("Impact", 32), text_color="#0FF5FF")
titulo.pack(pady=(40, 5), padx=60)

subtitulo = ctk.CTkLabel(panel_central, text="ANTI-AFK SYSTEM CONTROL", font=("Arial", 11, "bold"), text_color="#536D7E")
subtitulo.pack(pady=(0, 20))

label_estado = ctk.CTkLabel(panel_central, text="SYS_STATUS: INACTIVE 🔴", font=("Consolas", 15, "bold"), text_color="#FF334B")
label_estado.pack(pady=(0, 25))

separador1 = ctk.CTkFrame(panel_central, fg_color="#07696E", height=2, width=320)
separador1.pack(pady=10)

# 🕒 SECCIÓN DE TIEMPOS
label_seccion = ctk.CTkLabel(panel_central, text="TIEMPO ENTRE ACCIONES", font=("Impact", 16), text_color="#00B5BD")
label_seccion.pack(pady=10)

frame_min = ctk.CTkFrame(panel_central, fg_color="transparent")
frame_min.pack(pady=5, fill="x", padx=40)
label_min = ctk.CTkLabel(frame_min, text="MIN TIME:", font=("Arial", 12, "bold"), text_color="#89A1B3")
label_min.pack(side="left", padx=10)
combo_min = ctk.CTkComboBox(frame_min, values=[str(i) for i in range(11)], state="readonly", font=("Consolas", 14, "bold"), fg_color="#0A393B", border_color="#00DCE6", button_color="#00DCE6", button_hover_color="#07696E", width=120)
combo_min.set("1")
combo_min.pack(side="right", padx=10)

frame_max = ctk.CTkFrame(panel_central, fg_color="transparent")
frame_max.pack(pady=5, fill="x", padx=40)
label_max = ctk.CTkLabel(frame_max, text="MAX TIME:", font=("Arial", 12, "bold"), text_color="#89A1B3")
label_max.pack(side="left", padx=10)
combo_max = ctk.CTkComboBox(frame_max, values=[str(i) for i in range(11)], state="readonly", font=("Consolas", 14, "bold"), fg_color="#0A393B", border_color="#00DCE6", button_color="#00DCE6", button_hover_color="#07696E", width=120)
combo_max.set("2")
combo_max.pack(side="right", padx=10)

# 🆕 🎛️ NUEVA SECCIÓN: SELECCIÓN DE TECLA (Misma estética Predator)
separador_tecla = ctk.CTkFrame(panel_central, fg_color="#07696E", height=2, width=320)
separador_tecla.pack(pady=15)

label_titulo_tecla = ctk.CTkLabel(panel_central, text="TECLA DE SIMULACIÓN", font=("Impact", 16), text_color="#00B5BD")
label_titulo_tecla.pack(pady=5)

frame_tecla = ctk.CTkFrame(panel_central, fg_color="transparent")
frame_tecla.pack(pady=5, fill="x", padx=40)
label_tecla_txt = ctk.CTkLabel(frame_tecla, text="INPUT KEY:", font=("Arial", 12, "bold"), text_color="#89A1B3")
label_tecla_txt.pack(side="left", padx=10)

opciones_teclas = list(TRADUCTOR_TECLAS.keys()) # Saca la lista de palabras ("W", "A", etc.)
combo_tecla = ctk.CTkComboBox(frame_tecla, values=opciones_teclas, state="readonly", font=("Consolas", 12, "bold"), fg_color="#0A393B", border_color="#00DCE6", button_color="#00DCE6", button_hover_color="#07696E", width=150)
combo_tecla.set("Barra Espaciadora") # Selección inicial
combo_tecla.pack(side="right", padx=10)

separador2 = ctk.CTkFrame(panel_central, fg_color="#07696E", height=2, width=320)
separador2.pack(pady=20)

# 📊 PANEL DE SUPERVISIÓN
label_info_barra = ctk.CTkLabel(panel_central, text="TIEMPO HASTA SIGUIENTE ACCIÓN", font=("Impact", 13), text_color="#05979E")
label_info_barra.pack(pady=(5, 2))

label_porcentaje = ctk.CTkLabel(panel_central, text="0% PROCESS", font=("Consolas", 12, "bold"), text_color="#0FF5FF")
label_porcentaje.pack(pady=2)

barra_progreso = ctk.CTkProgressBar(panel_central, width=280, height=8, fg_color="#0A393B", progress_color="#0FF5FF")
barra_progreso.set(0)
barra_progreso.pack(pady=(0, 25))

# 🕹️ BOTONERA DE ACCIÓN
btn_encender = ctk.CTkButton(panel_central, text="Activar ANTI-AFK", font=("Impact", 16), fg_color="#00B5BD", hover_color="#07696E", text_color="#03070A", height=48, corner_radius=12, command=activar_bot)
btn_encender.pack(pady=10, fill="x", padx=40)

btn_apagar = ctk.CTkButton(panel_central, text="Detener ANTI-AFK", font=("Impact", 16), fg_color="#FF334B", hover_color="#CC283B", text_color="white", height=48, corner_radius=12, command=desactivar_bot)
btn_apagar.pack(pady=10, fill="x", padx=40)

btn_salir = ctk.CTkButton(panel_central, text="Salir a WINDOWS", font=("Arial", 11, "bold"), fg_color="transparent", hover_color="#0A393B", text_color="#536D7E", border_width=1, border_color="#304454", command=salir_programa)
btn_salir.pack(pady=(25, 25))

ventana.mainloop()
