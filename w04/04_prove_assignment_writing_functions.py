import random
import tkinter as tk


def main():
    width = 800
    height = 600

    tk_root = tk.Tk()
    tk_root.geometry(f"{width}x{height}")

    frame = tk.Frame(tk_root)
    frame.master.title("Sky")
    frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # drawing elements
    draw_sky(canvas, width, '#87CEEB')
    draw_grass(canvas, width, height, grass_line_width=5)

    # multiple pine trees
    for i in range(0, width, 50):
        position_variation = random.randint(200, 300)
        draw_pine_tree(canvas, i, height - position_variation, 150)

    draw_sun(canvas, width - 150, 100, width - 50, 200)

    tk_root.mainloop()


def draw_grid_guide(canvas, top, left, right, bottom, spacing):
    for i in range(top, bottom, spacing):
        canvas.create_line(left, i, right, i)

    for i in range(left, right, spacing):
        canvas.create_line(i, top, i, bottom)


def draw_pine_tree(canvas, peak_x, peak_y, height, scale=1.0):
    trunk_width = (height / 10) * scale
    trunk_height = (height / 8) * scale
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = (height / 2) * scale
    skirt_height = (height - trunk_height) * scale
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    canvas.create_rectangle(trunk_left, skirt_bottom,
                            trunk_right, trunk_bottom,
                            outline="gray20", width=1, fill="tan3")

    canvas.create_polygon(peak_x, peak_y,
                          skirt_right, skirt_bottom,
                          skirt_left, skirt_bottom,
                          outline="gray20", width=1, fill="dark green")


def draw_grass(canvas, width, height, grass_line_width=1):
    min_grass_height = height * 0.1
    max_grass_height = height * 0.30
    green_range = ['#22577A', '#38A3A5', '#57CC99', '#80ED99']

    for i in range(0, width):
        grass_height = random.randrange(min_grass_height, max_grass_height)
        random_grass_fill = random.randint(0, len(green_range) - 1)
        random_width = random.randint(1, grass_line_width)
        canvas.create_line(i, height, i, height - grass_height, fill=green_range[random_grass_fill],
                           width=random_width)


def draw_sky(canvas, width, color):
    for i in range(0, width):
        canvas.create_line(0, i, width, i, fill=color)


def draw_sun(canvas, x0, y0, width, height):
    canvas.create_oval(x0, y0, width, height, width=1, fill='#ffa500', outline='#ffa500')


# Call the main function so that
# this program will start executing.
main()