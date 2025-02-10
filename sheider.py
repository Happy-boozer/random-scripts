import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()

#(x − a)² + (y − b)² = R²
#x + y = 1 / a / b
def shader(x, y):
    # Ваш код здесь:
    r1 = int(((x * 2 - 1) ** 2 + (y * 2 - 1) ** 2))
    r2 = int(((x * 7 - 4.5) ** 2 + (y * 7 - 1.7) ** 2))
    angle = math.atan2(y - 0.6, x - 0.6)
    if -math.radians(30) < angle < math.radians(30):
        return 1, 1, 1
    return r1, r2, 1




main(shader)