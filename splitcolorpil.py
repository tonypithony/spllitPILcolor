from PIL import Image

name = "merge.jpg" # 'd.jpg'
size = 1280

def color_split(image_name, kanaal):
    img = Image.open(image_name).resize((size, size), 1)
    # разложим изображение на каналы
    r, g, b = img.split()

    r.save(f'{image_name[:-4]}_r.jpg')
    g.save(f'{image_name[:-4]}_g.jpg')
    b.save(f'{image_name[:-4]}_b.jpg')

    if kanaal == 'r': return r
    elif kanaal == 'g': return g
    else: return b

def color_merge(r, g, b):
    img = Image.merge('RGB', (r, g, b))
    img.save("merge.jpg")


# R = color_split(name, 'r')
# G = color_split(name, 'g')
B = color_split(name, 'b')


# r = Image.open(f'{name[:-4]}_r.jpg')
# g = Image.open(f'{name[:-4]}_g.jpg')
# b = Image.open('image_with_watermark.jpg')

# color_merge(r, g, b)


# with Image.open(name) as logo:
        
#     # разложим изображение на каналы
#     r, g, b = logo.split()

#     # делаем что нибудь с каналами
#     # например применим метод Image.eval()  
#     # к каналу `B` с lambda-функцией
#     b = Image.eval(b, lambda x: 255 if x > 200 else 0)
    
#     # теперь объединим каналы без альфа слоя
#     img = Image.merge('RGB', (r, g, b))
#     img.save('python-logo_eval.png')