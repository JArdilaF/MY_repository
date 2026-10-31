import turtle
import math
import random
import time

# ── Configuración de pantalla ──────────────────────────────────────────────
screen = turtle.Screen()
screen.title("I Love You ♥")
screen.bgcolor("#1a0a0f")
screen.setup(width=700, height=600)
screen.tracer(0)

def goto(t, x, y):
    t.penup(); t.goto(x, y); t.pendown()

# ── 1. Estrellas (instantáneo al inicio) ──────────────────────────────────
stars = turtle.Turtle()
stars.hideturtle()
random.seed(42)
star_positions = [
    (random.randint(-330, 330), random.randint(-270, 270))
    for _ in range(55)
]
for sx, sy in star_positions:
    if abs(sx) < 160 and abs(sy) < 140:
        continue
    size = random.choice([1, 1, 2, 2, 3])
    stars.penup(); stars.goto(sx, sy); stars.pendown()
    stars.dot(size, random.choice(["#ffffff", "#ffccdd", "#ffaacc"]))

# Mini corazones en esquinas (también instantáneos)
def draw_heart_instant(t, cx, cy, scale, fill_color, outline_color, outline_w):
    t.pensize(outline_w)
    t.fillcolor(fill_color)
    t.pencolor(outline_color)
    a0 = math.radians(0)
    x0 = scale * 16 * math.sin(a0) ** 3
    y0 = scale * (13*math.cos(a0) - 5*math.cos(2*a0) - 2*math.cos(3*a0) - math.cos(4*a0))
    goto(t, cx + x0, cy + y0)
    t.begin_fill()
    for deg in range(0, 361):
        a = math.radians(deg)
        x = scale * 16 * math.sin(a) ** 3
        y = scale * (13*math.cos(a) - 5*math.cos(2*a) - 2*math.cos(3*a) - math.cos(4*a))
        t.goto(cx + x, cy + y)
    t.end_fill()

mini = turtle.Turtle(); mini.hideturtle()
corner_hearts = [(-290, 220), (290, 220), (-290, -210), (290, -210)]
for hx, hy in corner_hearts:
    draw_heart_instant(mini, hx, hy, 2.2, "#880022", "#cc0044", 1)

screen.update()

# ── 2. Animación del corazón en ~5 segundos ───────────────────────────────
#
# Estrategia: precalcular los 360 puntos del contorno exterior (halo)
# y del corazón principal, luego avanzar con tracer(1) y delay calibrado
# para que todo el recorrido dure exactamente TARGET_SECONDS.

TARGET_SECONDS = 5.0

def heart_points(cx, cy, scale, steps=360):
    pts = []
    for deg in range(0, steps + 1):
        a = math.radians(deg)
        x = cx + scale * 16 * math.sin(a) ** 3
        y = cy + scale * (13*math.cos(a) - 5*math.cos(2*a) - 2*math.cos(3*a) - math.cos(4*a))
        pts.append((x, y))
    return pts

# Calculamos puntos de las dos capas del corazón
pts_shadow = heart_points(0, 20, 9.8)
pts_main   = heart_points(0, 20, 9.2)
pts_glow   = heart_points(-30, 70, 2.5)

total_steps = len(pts_shadow) + len(pts_main) + len(pts_glow)
# delay en ms por paso para completar en TARGET_SECONDS
delay_ms = max(1, int((TARGET_SECONDS * 1000) / total_steps))

screen.tracer(1)
screen.delay(delay_ms)

# -- Halo / sombra exterior --
h_shadow = turtle.Turtle(); h_shadow.hideturtle()
h_shadow.pensize(1); h_shadow.pencolor("#5c0020"); h_shadow.fillcolor("#5c0020")
h_shadow.penup(); h_shadow.goto(pts_shadow[0]); h_shadow.pendown()
h_shadow.begin_fill()
for pt in pts_shadow[1:]:
    h_shadow.goto(pt)
h_shadow.end_fill()

# -- Corazón principal --
h_main = turtle.Turtle(); h_main.hideturtle()
h_main.pensize(2); h_main.pencolor("#ff3366"); h_main.fillcolor("#cc0033")
h_main.penup(); h_main.goto(pts_main[0]); h_main.pendown()
h_main.begin_fill()
for pt in pts_main[1:]:
    h_main.goto(pt)
h_main.end_fill()

# -- Brillo interior --
h_glow = turtle.Turtle(); h_glow.hideturtle()
h_glow.pensize(1); h_glow.pencolor("#ffcccc"); h_glow.fillcolor("#ff99aa")
h_glow.penup(); h_glow.goto(pts_glow[0]); h_glow.pendown()
h_glow.begin_fill()
for pt in pts_glow[1:]:
    h_glow.goto(pt)
h_glow.end_fill()

# ── 3. Al terminar: frase y decoración (instantáneos) ────────────────────
screen.tracer(0)

# Líneas decorativas
deco = turtle.Turtle(); deco.hideturtle()
deco.pencolor("#ff3366"); deco.pensize(1)
goto(deco, -110, -50); deco.forward(220)
goto(deco, -80,  -58); deco.forward(160)

# Sombra del texto
txt = turtle.Turtle(); txt.hideturtle()
goto(txt, 3, -43)
txt.pencolor("#5c0020")
txt.write("I LOVE YOU", align="center", font=("Georgia", 28, "bold"))

# Texto principal
goto(txt, 0, -45)
txt.pencolor("#ffffff")
txt.write("I LOVE YOU", align="center", font=("Georgia", 28, "bold"))

screen.update()
screen.mainloop()