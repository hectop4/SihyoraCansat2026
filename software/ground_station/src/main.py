import tkinter as tk
from PIL import Image, ImageTk

# ===============================
# Configuración principal
# ===============================
BG_COLOR = "#000a12"
PANEL_COLOR = "#102a3a"
TEXT_COLOR = "#e0f2ff"
ACCENT_COLOR = "#2ec4ff"
BOX_BG = "#000f1a"

LEFT_WIDTH = 520
RIGHT_WIDTH = 650

root = tk.Tk()
root.title("SIHYORA | CANSAT MISSION")
root.geometry("1200x700")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

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
    justify="left"
).grid(row=0, column=1, sticky="w", pady=20)

status_frame = tk.Frame(top_bar, bg=BG_COLOR)
status_frame.grid(row=0, column=2, sticky="ne", padx=20, pady=10)

battery_frame = tk.Frame(status_frame, bg=BG_COLOR)
battery_frame.pack(anchor="e")

battery_img = Image.open("logo/logo_bateria.png").resize((70, 70))
battery_icon = ImageTk.PhotoImage(battery_img)

tk.Label(battery_frame, image=battery_icon, bg=BG_COLOR).pack(side="left")
tk.Label(
    battery_frame,
    text="BATERÍA: 85%",
    fg=TEXT_COLOR,
    bg=BG_COLOR,
    font=("Segoe UI", 12)
).pack(side="left", padx=5)

tk.Label(
    status_frame,
    text="ESTADO DE CONEXIÓN: CONECTADO",
    fg="#7CFF7C",
    bg=BG_COLOR,
    font=("Segoe UI", 12)
).pack(anchor="e", pady=5)

# ===============================
# Contenedor principal
# ===============================
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Panel izquierdo (WAITING)
left_panel = tk.Frame(main_frame, bg=PANEL_COLOR, width=LEFT_WIDTH)
left_panel.pack(side="left", fill="both", padx=5)
left_panel.pack_propagate(False)

tk.Label(
    left_panel,
    text="WAITING FOR STEREOSCOPIC IMAGE...",
    fg=TEXT_COLOR,
    bg=PANEL_COLOR,
    font=("Segoe UI", 14)
).pack(expand=True)

# Panel derecho (gráficas)
right_panel = tk.Frame(main_frame, bg=PANEL_COLOR, width=RIGHT_WIDTH)
right_panel.pack(side="right", fill="both", expand=True, padx=5)
right_panel.pack_propagate(False)

for r in range(2):
    right_panel.grid_rowconfigure(r, weight=1)
for c in range(2):
    right_panel.grid_columnconfigure(c, weight=1)

def graph_box(parent, title, row, col):
    box = tk.Frame(parent, bg=BOX_BG)
    box.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    tk.Label(
        box,
        text=title,
        fg=ACCENT_COLOR,
        bg=BOX_BG,
        font=("Segoe UI", 10, "bold")
    ).pack(anchor="w", padx=10, pady=(6, 0))

    tk.Frame(box, bg="#071821").pack(fill="both", expand=True, padx=10, pady=10)

graph_box(right_panel, "TEMPERATURE (°C)", 0, 0)
graph_box(right_panel, "PRESSURE (hPa)", 0, 1)
graph_box(right_panel, "VELOCITY (km/h)", 1, 0)
graph_box(right_panel, "ACCELERATION (m/s²)", 1, 1)

# ===============================
# Barra inferior (CENTRADO CORRECTO)
# ===============================
bottom_bar = tk.Frame(root, bg=PANEL_COLOR, height=80)
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
    pady=10
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
    font=("Segoe UI", 20, "bold")
).place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()