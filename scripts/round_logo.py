from PIL import Image, ImageDraw

# Открываем JPEG
img = Image.open("logo-site.png").convert("RGBA")
w, h = img.size

# Создаём маску с закруглёнными углами
radius = 24  # px
mask = Image.new("L", (w, h), 0)
draw = ImageDraw.Draw(mask)
draw.rounded_rectangle((0, 0, w - 1, h - 1), radius=radius, fill=255)

# Применяем маску к альфа-каналу
result = Image.new("RGBA", (w, h), (0, 0, 0, 0))
result.paste(img, (0, 0), mask)

result.save("logo.png")
print(f"Saved logo.png ({w}x{h}, radius={radius}px)")