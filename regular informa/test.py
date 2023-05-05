def color_generator(step=1.0):
    import colorsys

    while True:
        for i in range(int(1528/step)):
            hue = i / int(1528/step)
            r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
            yield f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

color = color_generator()
while True:
    print(next(color_generator()))
