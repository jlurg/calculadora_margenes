import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import requests
import rangos as r

# Función calculadora
def calcular_precio_venta():
  costo = float(entry_costo.get())
  condiciones_pago = condiciones[condicion.get()] * 0.2667
  # margen = margenes[seleccion.get()] + condiciones_pago
  lineas = [
    (0, 0), (1, r.mr_toncomp(costo)), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
    (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16),
    (17, 17), (18, 18)
  ]

  for linea in lineas:
    if linea[0] == margenes[seleccion.get()]:
      margen = linea[1] + condiciones_pago
  
  try:
    precio_venta = costo * (100 / (100 - margen))
    label_resultado["text"] = "Precio de venta: ${:.2f} +IVA".format(precio_venta)
  except ZeroDivisionError:
    label_resultado["text"] = "Elije un margen menor al 100%"


def calcular_tipo_cambio():
  global tipo_cambio_riversil
  usd = float(entry_usd.get())
  
  try:
    resultado_mxn = usd * tipo_cambio_riversil
    label_resultado_conv["text"] = "MXN: ${:.2f}".format(resultado_mxn)
  except ValueError:
    label_resultado_conv["text"] = "Ingresa una cantidad"

# Widgets
ventana = tk.Tk()
ventana.title("Calculadora de precio de venta")

frame = tk.Frame(ventana)
frame.pack(pady=10, padx=5)

# Fuente
fuente_titulo = ("TkDefaultFont", 16, "bold")

# canvas = tk.Canvas(frame, width=100, height=100)
# canvas.grid(row=0, column=0, columnspan=2)

# logo = tk.PhotoImage(file="img/LOGO2020.png")
# Canvas.create_image(25, 25, image=logo)
# label_logo = tk.Label(frame, image=logo)
# label_logo.grid(row=0, column=0, columnspan=2)

# Logo de la empresa
logo = Image.open("img/LOGO2020.png")
logo = logo.resize((600, 180), Image.LANCZOS)
imagen = ImageTk.PhotoImage(logo)

canvas = tk.Canvas(frame, width=620, height=240)
canvas.grid(row=0, column=0, rowspan=2, columnspan=4)
canvas.create_image(300, 100, image=imagen)

ttk.Separator(frame, orient="horizontal").grid(column=0, row=1, columnspan=4, sticky="ew", pady=0, padx=10)

label_costo = tk.Label(frame, text="Costo(sin IVA):")
label_costo.grid(row=2, column=0, sticky="W", padx=(10, 0))

entry_costo = tk.Entry(frame)
entry_costo.grid(row=2, column=1, sticky="W", padx=10)

# Menú para seleccionar la línea de artículos
label_seleccion = tk.Label(frame, text="Línea de artículo:")
label_seleccion.grid(row=3, column=0, sticky="W", padx=(10, 0))

seleccion = tk.StringVar()
seleccion.set("Papelería")
margenes = {"Papelería": 0, "Tóner compatible": 1, "Tóner original": 2, "Tinta compatible": 3,
           "Tinta original": 4, "Accesorios": 5, "Monitores": 6, "Laptops": 7, "PC Escritorio": 8,
           "Impresoras y Multifuncionales": 9, "Almacenamiento": 10, "Limpieza": 11, 
           "Celulares": 12, "Tablet": 13, "Licencias": 14, "Refacciones": 15, "Reguladores": 16,
           "Conectividad": 17, "Componentes": 18}

opciones = tk.OptionMenu(frame, seleccion, *margenes.keys())
opciones.grid(row=3, column=1, sticky="W", padx=10)

# Menú para seleccionar las condiciones de pago
label_condiciones = tk.Label(frame, text="Condiciones de pago:")
label_condiciones.grid(row=4, column=0, sticky="W", padx=(10, 0))

condicion = tk.StringVar()
condicion.set("Contado")
condiciones = {"Contado": 0, "Crédito 4 días": 4,"Credito 5 dias": 5, "Crédito 6 días": 6, 
              "Crédito 7 días": 7 ,"Credito 8 dias": 3, "Crédito 10 días": 1,
              "Credito 14 dias": 14, "Crédito 15 días": 15, "Crédito 20 días": 20,
              "Credito 21 dias": 21, "Credito 25 dias": 25, "Credito 28 dias": 28,
              "Crédito 29 días": 29, "Crédito 30 días": 30, "Marketing/redes": 0}

condicion_opciones = tk.OptionMenu(frame, condicion, *condiciones.keys())
condicion_opciones.grid(row=4, column=1, sticky="W", padx=10)

# Botón para ejecutar la función
boton_calcular = tk.Button(frame, text="Calcular", command=calcular_precio_venta)
boton_calcular.grid(row=5, column=0,columnspan=2, pady=10)

# Resultado 
label_frame = tk.LabelFrame(frame, text="Resultado:", font=fuente_titulo)
label_frame.config(height="400")
label_frame.grid(row=6, column=0, padx=10, pady=10, sticky="EW", columnspan=2)
# label_frame.pack(pady=10, anchor="center")

label_resultado = tk.Label(label_frame, text="")
# label_resultado.grid(row=5, column=0, columnspan=2)
label_resultado.pack(pady=10, anchor="w")

# API Open Exchange Rates para tipo de camnbio 
response = requests.get("https://openexchangerates.org/api/latest.json?app_id=09489b84a4044c19971fa53faa134139")
data = response.json()
tipo_cambio = data["rates"]["MXN"]
if tipo_cambio < 20:
  tipo_cambio_riversil = round(tipo_cambio, 2) + 2
else:
  tipo_cambio_riversil = round(tipo_cambio, 2) + 1

# Frame para el tipo de cambio
frame_cambio = tk.LabelFrame(frame, text="Conversor de USD a MXN", font=fuente_titulo)
frame_cambio.grid(row=2, column=2, columnspan=3, rowspan=5, pady=10, padx=10, sticky="NSEW")

label_tipo_cambio = tk.Label(frame_cambio, text=f"Tipo de cambio: {tipo_cambio_riversil}")
label_tipo_cambio.pack(pady=10, anchor="w")

label_usd = tk.Label(frame_cambio, text="USD:")
# label_usd.pack(pady=0, side="left")
label_usd.pack(anchor="w", padx=7)

entry_usd = tk.Entry(frame_cambio)
# entry_usd.pack(padx=5, side="right", pady=0)
entry_usd.pack()

boton_conversor = tk.Button(frame_cambio, text="Calcular", command=calcular_tipo_cambio)
boton_conversor.pack(anchor="center")

label_resultado_conv = tk.Label(frame_cambio, text="")
label_resultado_conv.pack(pady=10, anchor="w")

# Separador horizontal de la calculadora con el texto informativo
ttk.Separator(frame, orient="horizontal").grid(column=0, row=7, columnspan=4, sticky="ew", pady=10, padx=10)

# Instrucciones
label_instrucciones = tk.LabelFrame(frame, text="Instrucciones", font=fuente_titulo)
label_instrucciones.grid(row=8, column=0, columnspan=4, rowspan=4, padx=10, sticky="NSEW")

label_info = tk.Label(label_instrucciones, text="Este programa calcula el precio de venta de un producto para cada línea de artículo. Sigue las siguientes instrucciones:")
label_info.pack(anchor="w")
label_info1 = tk.Label(label_instrucciones, text="1. Ingresa el costo del artículo sin iva. (ej: 499.99)")
label_info1.pack(anchor="w")
label_info2 = tk.Label(label_instrucciones, text="2. Selecciona la línea de artículo.")
label_info2.pack(anchor="w")
label_info3 = tk.Label(label_instrucciones, text="3. Selecciona las condiciones de pago.")
label_info3.pack(anchor="w")
label_info3 = tk.Label(label_instrucciones, text="4. Click en calcular y recibirás el resultado")
label_info3.pack(anchor="w")

# Ejecución del programa
ventana.mainloop()
