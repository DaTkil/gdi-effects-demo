from GDI_effects.GDI import Effects
import threading
import time

print("CHAOS MODE WITH TEXT STARTED")

start = time.time()
duration = 180  # 3 minutes

def glitch():
    Effects.glitch_screen(50)

def copy():
    Effects.copy_screen(50)

def rainbow():
    Effects.rainbow_blink(50)

def text():
    Effects.type_text("Hacked", 100)

while time.time() - start < duration:
    threads = [
        threading.Thread(target=glitch),
        threading.Thread(target=copy),
        threading.Thread(target=rainbow),
        threading.Thread(target=text)
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

print("DONE")
