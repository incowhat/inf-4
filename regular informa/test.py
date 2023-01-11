from time import sleep

def colorbyHue(step=1.0):
    import colorsys

    while True:
        for i in range(int(1528/step)):
            hue = i / int(1528/step) # cislo vsetkych farieb plnej saturacie od cervenej do cervenej
            r, g, b = colorsys.hsv_to_rgb(hue, 1, 1) # 3 cisla rgb 0-1
            yield f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}' # 0-1 => 0-255 => 00-ff

def colorbyRGB(step=1, rgb=[255, 0, 0]):
    while True:
        for _ in range(step):
            for n in range(3):
                if rgb[n] == 255:
                    if rgb[n-1] != 0:
                        rgb[n-1] -= 1
                    elif rgb[n-2] < 255:
                        rgb[n-2] += 1
                    else:
                        rgb[n] -= 1
            
        yield f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

if __name__ == '__main__':
    generators = (colorbyHue, colorbyRGB)
    
    qqq = 1
    for color in generators[0](5):
        print(qqq, color)
        if color == '#ff0001':
            exit()
        qqq += 1
        # sleep(1)