import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

# ===============================
# Configuración principal
# ===============================
BG_COLOR = "#000a12"
PANEL_COLOR = "#102a3a"
TEXT_COLOR = "#e0f2ff"
ACCENT_COLOR = "#2ec4ff"
BOX_BG = "#000f1a"

LEFT_WIDTH = 850
RIGHT_WIDTH = 650

root = tk.Tk()
root.title("SIHYORA | CANSAT MISSION")
root.attributes("-fullscreen", True)
root.configure(bg=BG_COLOR)
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

# ===============================
# Barra superior
# ===============================
top_bar = tk.Frame(root, bg=BG_COLOR, height=70)
top_bar.pack(fill="x", side="top")

top_bar.grid_columnconfigure(0, weight=0)
top_bar.grid_columnconfigure(1, weight=1)
top_bar.grid_columnconfigure(2, weight=0)

logo_img = Image.open("logo/logo_shiyora.png").resize((170, 170))
logo = ImageTk.PhotoImage(logo_img)
tk.Label(top_bar, image=logo, bg=BG_COLOR).grid(row=0, column=0, sticky="nw", padx=10)

tk.Label(
    top_bar,
    text="SIHYORA |\nCANSAT MISSION",
    fg=TEXT_COLOR,
    bg=BG_COLOR,
    font=("Segoe UI", 25, "bold"),
    justify="left",
).grid(row=0, column=1, sticky="w", pady=20)

status_frame = tk.Frame(top_bar, bg=BG_COLOR)
status_frame.grid(row=0, column=2, sticky="ne", padx=20, pady=10)

battery_frame = tk.Frame(status_frame, bg=BG_COLOR)
battery_frame.pack(anchor="e")

# Crear icono de batería vertical
battery_img = Image.new("RGBA", (35, 50), (0, 0, 0, 0))
draw = ImageDraw.Draw(battery_img)

# Terminal positivo superior
draw.rectangle([12, 2, 23, 7], fill="#2ec4ff", outline="#1a8fb3", width=1)

# Cuerpo principal de la batería
draw.rectangle([7, 7, 28, 47], fill="#000f1a", outline="#2ec4ff", width=2)

# Nivel de carga (85%) - se llena de abajo hacia arriba
charge_height = int(35 * 0.85)
y_start = 47 - charge_height - 3
draw.rectangle([10, y_start, 25, 44], fill="#2ec4ff")

# Efecto de brillo en la parte superior de la carga
draw.rectangle([10, y_start, 25, y_start + 3], fill="#5ed4ff")

# Líneas divisorias horizontales para efecto de segmentos
for i in range(4):
    y = 14 + i * 8
    draw.line([10, y, 25, y], fill="#102a3a", width=1)

battery_icon = ImageTk.PhotoImage(battery_img)

tk.Label(battery_frame, image=battery_icon, bg=BG_COLOR).pack(side="left", padx=(0, 5))
tk.Label(
    battery_frame,
    text="BATERÍA: 85%",
    fg=TEXT_COLOR,
    bg=BG_COLOR,
    font=("Segoe UI", 12),
).pack(side="left", padx=5)

connection_frame = tk.Frame(status_frame, bg=BG_COLOR)
connection_frame.pack(anchor="e", pady=5)

connection_status = tk.Label(
    connection_frame,
    text="ESTADO DE CONEXIÓN: CONECTADO",
    fg="#7CFF7C",
    bg=BG_COLOR,
    font=("Segoe UI", 12),
)
connection_status.pack(side="left", padx=(0, 10))

is_connected = [True]  # Lista para mantener el estado mutable


def toggle_connection():
    if is_connected[0]:
        # Cambiar a desconectado
        is_connected[0] = False
        connection_status.config(text="ESTADO DE CONEXIÓN: DESCONECTADO", fg="#ff4444")
        connection_btn.config(text="CONECTAR", bg="#7CFF7C", fg="black")
    else:
        # Cambiar a conectado
        is_connected[0] = True
        connection_status.config(text="ESTADO DE CONEXIÓN: CONECTADO", fg="#7CFF7C")
        connection_btn.config(text="DESCONECTAR", bg="#ff4444", fg="white")


connection_btn = tk.Button(
    connection_frame,
    text="DESCONECTAR",
    bg="#ff4444",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=15,
    pady=5,
    bd=0,
    command=toggle_connection,
)
connection_btn.pack(side="left")

# ===============================
# Contenedor principal
# ===============================
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Panel izquierdo (WAITING)
left_panel = tk.Frame(
    main_frame,
    bg=PANEL_COLOR,
    width=LEFT_WIDTH,
    highlightbackground=ACCENT_COLOR,
    highlightthickness=2,
)
left_panel.pack(side="left", fill="both", padx=5)
left_panel.pack_propagate(False)

tk.Label(
    left_panel,
    text="WAITING FOR STEREOSCOPIC IMAGE...",
    fg=TEXT_COLOR,
    bg=PANEL_COLOR,
    font=("Segoe UI", 25),
).pack(expand=True)

# Panel derecho (gráficas)
right_panel = tk.Frame(
    main_frame,
    bg=PANEL_COLOR,
    width=RIGHT_WIDTH,
    highlightbackground=ACCENT_COLOR,
    highlightthickness=2,
)
right_panel.pack(side="right", fill="both", expand=True, padx=5)
right_panel.pack_propagate(False)

for r in range(3):
    right_panel.grid_rowconfigure(r, weight=1)
for c in range(2):
    right_panel.grid_columnconfigure(c, weight=1)


def graph_box(parent, title, row, col, colspan=1):
    box = tk.Frame(
        parent, bg=BOX_BG, highlightbackground="#1a4a5a", highlightthickness=1
    )
    box.grid(row=row, column=col, columnspan=colspan, padx=10, pady=10, sticky="nsew")

    tk.Label(
        box, text=title, fg=ACCENT_COLOR, bg=BOX_BG, font=("Segoe UI", 10, "bold")
    ).pack(anchor="w", padx=10, pady=(6, 0))

    tk.Frame(box, bg="#071821").pack(fill="both", expand=True, padx=10, pady=10)


graph_box(right_panel, "TEMPERATURE (°C)", 0, 0)
graph_box(right_panel, "PRESSURE (hPa)", 0, 1)
graph_box(right_panel, "VELOCITY (km/h)", 1, 0)
graph_box(right_panel, "ALTITUDE (m)", 1, 1)
graph_box(right_panel, "ACCELERATION (m/s²)", 2, 0, colspan=2)

# ===============================
# Barra inferior (CENTRADO CORRECTO)
# ===============================
bottom_bar = tk.Frame(
    root,
    bg=PANEL_COLOR,
    height=80,
    highlightbackground=ACCENT_COLOR,
    highlightthickness=2,
)
bottom_bar.pack(fill="x", side="bottom")
bottom_bar.pack_propagate(False)

# Contenedor izquierdo (misma referencia que WAITING)
bottom_left = tk.Frame(bottom_bar, bg=PANEL_COLOR, width=LEFT_WIDTH)
bottom_left.pack(side="left", fill="y")
bottom_left.pack_propagate(False)

tk.Button(
    bottom_left,
    text="EXPORT DATA",
    bg=ACCENT_COLOR,
    fg="black",
    font=("Segoe UI", 12, "bold"),
    relief="flat",
    padx=20,
    pady=10,
    bd=0,
    highlightthickness=0,
).place(relx=0.5, rely=0.5, anchor="center")

# Contenedor derecho (misma referencia que GRÁFICAS)
bottom_right = tk.Frame(bottom_bar, bg=PANEL_COLOR, width=RIGHT_WIDTH)
bottom_right.pack(side="right", fill="both", expand=True)
bottom_right.pack_propagate(False)

tk.Label(
    bottom_right,
    text="ALTITUDE: 1,200 m",
    fg=ACCENT_COLOR,
    bg=PANEL_COLOR,
    font=("Segoe UI", 20, "bold"),
).place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
