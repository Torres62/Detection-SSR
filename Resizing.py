from PIL import Image
import os

src_path = r'C:\Users\Jupiter\Desktop\FOTOS'
dir_path = r'C:\Users\Jupiter\Desktop\TESTE'
index = 0

for file_name in os.listdir(src_path):

    image = Image.open(os.path.join(src_path, file_name))
    output = image.resize((960, 720), Image.ANTIALIAS)

    if 0 <= index < 50:
        path = r'C:\Users\Jupiter\Desktop\TESTE\1'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 50 <= index < 100:
        path = r'C:\Users\Jupiter\Desktop\TESTE\2'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 100 <= index < 150:
        path = r'C:\Users\Jupiter\Desktop\TESTE\3'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 150 <= index < 200:
        path = r'C:\Users\Jupiter\Desktop\TESTE\4'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 200 <= index < 250:
        path = r'C:\Users\Jupiter\Desktop\TESTE\5'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 250 <= index < 300:
        path = r'C:\Users\Jupiter\Desktop\TESTE\6'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 300 <= index < 350:
        path = r'C:\Users\Jupiter\Desktop\TESTE\7'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 350 <= index < 400:
        path = r'C:\Users\Jupiter\Desktop\TESTE\8'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 400 <= index < 450:
        path = r'C:\Users\Jupiter\Desktop\TESTE\9'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 450 <= index < 500:
        path = r'C:\Users\Jupiter\Desktop\TESTE\10'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 500 <= index < 550:
        path = r'C:\Users\Jupiter\Desktop\TESTE\11'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 550 <= index < 600:
        path = r'C:\Users\Jupiter\Desktop\TESTE\12'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 600 <= index < 650:
        path = r'C:\Users\Jupiter\Desktop\TESTE\13'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 650 <= index < 700:
        path = r'C:\Users\Jupiter\Desktop\TESTE\14'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 700 <= index < 750:
        path = r'C:\Users\Jupiter\Desktop\TESTE\15'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 750 <= index < 800:
        path = r'C:\Users\Jupiter\Desktop\TESTE\16'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 800 <= index < 850:
        path = r'C:\Users\Jupiter\Desktop\TESTE\17'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 850 <= index < 900:
        path = r'C:\Users\Jupiter\Desktop\TESTE\18'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 900 <= index < 950:
        path = r'C:\Users\Jupiter\Desktop\TESTE\19'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 950 <= index < 1000:
        path = r'C:\Users\Jupiter\Desktop\TESTE\20'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1000 <= index < 1050:
        path = r'C:\Users\Jupiter\Desktop\TESTE\21'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1050 <= index < 1100:
        path = r'C:\Users\Jupiter\Desktop\TESTE\22'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1100 <= index < 1150:
        path = r'C:\Users\Jupiter\Desktop\TESTE\23'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1150 <= index < 1200:
        path = r'C:\Users\Jupiter\Desktop\TESTE\24'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1200 <= index < 1250:
        path = r'C:\Users\Jupiter\Desktop\TESTE\25'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1250 <= index < 1300:
        path = r'C:\Users\Jupiter\Desktop\TESTE\26'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1300 <= index < 1350:
        path = r'C:\Users\Jupiter\Desktop\TESTE\27'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1350 <= index < 1400:
        path = r'C:\Users\Jupiter\Desktop\TESTE\28'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1400 <= index < 1450:
        path = r'C:\Users\Jupiter\Desktop\TESTE\29'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1450 <= index < 1500:
        path = r'C:\Users\Jupiter\Desktop\TESTE\30'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1500 <= index < 1550:
        path = r'C:\Users\Jupiter\Desktop\TESTE\31'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1550 <= index < 1600:
        path = r'C:\Users\Jupiter\Desktop\TESTE\32'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1600 <= index < 1650:
        path = r'C:\Users\Jupiter\Desktop\TESTE\33'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1650 <= index < 1700:
        path = r'C:\Users\Jupiter\Desktop\TESTE\34'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1700 <= index < 1750:
        path = r'C:\Users\Jupiter\Desktop\TESTE\35'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1750 <= index < 1800:
        path = r'C:\Users\Jupiter\Desktop\TESTE\36'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1800 <= index < 1850:
        path = r'C:\Users\Jupiter\Desktop\TESTE\37'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1850 <= index < 1900:
        path = r'C:\Users\Jupiter\Desktop\TESTE\38'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1900 <= index < 1950:
        path = r'C:\Users\Jupiter\Desktop\TESTE\39'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    if 1950 <= index < 2000:
        path = r'C:\Users\Jupiter\Desktop\TESTE\40'
        if not os.path.exists(path):
            os.mkdir(path)
        output_name = os.path.join(path, file_name)
        output.save(output_name, "JPEG", quality=95)

    index += 1