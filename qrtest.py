import qrcode

def generar_qr(desde_link: str, nombre_archivo: str = "qr_link.png"):
    # Crear objeto QR
    qr = qrcode.QRCode(
        version=1,  # tamaño del código (1 es el más pequeño)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # tamaño de cada cuadro
        border=4,     # grosor del borde
    )

    # Añadir los datos (el link)
    qr.add_data(desde_link)
    qr.make(fit=True)

    # Crear la imagen
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardar en archivo
    img.save(nombre_archivo)
    print(f"✅ Código QR guardado como: {nombre_archivo}")


if __name__ == "__main__":
    link = input("Pega aquí tu link: ")
    generar_qr(link, "mi_qr.png")
