import argparse
from collections import Counter

from PIL import Image


def rgb_to_cmyk(rgb):
    ...
    divided_red = rgb[0] / 255
    divided_green = rgb[1] / 255
    divided_blue = rgb[2] / 255
    divided_rgb = [
        divided_red,
        divided_green, 
        divided_blue
    ]

    k = round(
        (1 - max(divided_rgb)) * 100
    )
    c = round(
        ((1 - divided_red - k) / (1 - k)) * 100
    )
    m = round(
        ((1 - divided_green - k) / (1 - k)) * 100
    )
    y = round(
        ((1 - divided_blue - k) / (1 - k)) * 100
    )

    return (c, m, y, k)

def rgb_to_hsv(rgb):
    ...
    max_pick = max(rgb)
    min_pick = min(rgb)

    v = max_pick
    v = round(v)

    s = 0
    if (v != 0):
        s = round(((v - min_pick) / v) * 100)

    h = max_pick
    if (h == min_pick):
        h = 0
    elif (rgb.index(max_pick) == 0):
        h = (rgb[1] - rgb[2]) / (max_pick - min_pick)
    elif (rgb.index(max_pick) == 1):
        h = 2 + (rgb[2] - rgb[0]) / (max_pick - min_pick)
    elif (rgb.index(max_pick) == 2):
        h = 4 + (rgb[0] - rgb[1]) / (max_pick - min_pick)
    
    h = abs(h * 60)
    h = round(h % 360)

    return (h, s, v)

def get_most_common_color(image_path):
    img = Image.open(image_path)
    img = img.resize((100, 100))

    pixels = list(img.getdata())
    most_common_pixel = Counter(pixels).most_common(1)[0][0]

    return most_common_pixel


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process an image to get the most common color in RGB, CMYK, and HSV.")
    parser.add_argument('--imgsource', type=str, required=True, help='Path to the source image file')
    args = parser.parse_args()

    rgb = get_most_common_color(args.imgsource)

    
    print(f"""
    RGB
    Red: {rgb[0]} - Green: {rgb[1]} - Blue: {rgb[2]}""")
    cmyk = rgb_to_cmyk(rgb)
    print(f"""----------------------------------------------------------------------
    CMYK
    Cian: {cmyk[0]} - Magenta: {cmyk[1]} - Yellow: {cmyk[2]} - Black: {cmyk[3]}""")
    hsv = rgb_to_hsv(rgb)
    print(f"""----------------------------------------------------------------------
    HSV
    Hue: {hsv[0]} - Saturation: {hsv[1]} - Value: {hsv[2]}
    """)


