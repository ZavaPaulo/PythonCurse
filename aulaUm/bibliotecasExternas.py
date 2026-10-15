#BIBLIOTECAS EXTERNAS
import time, random, qrcode
print("Aguarde...")
time.sleep(4)
print("Pronto")
while True:
    numeroAleatorio = random.randint(1, 1000)
    print(numeroAleatorio)
    time.sleep(0.5)
    if numeroAleatorio % 2 == 0:
        break

img = qrcode.make("youtube.com")
img.save("qr_yt.png")