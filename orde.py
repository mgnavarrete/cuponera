import os
import shutil
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# CONFIGURACIÓN
ORIGEN = 'desorden'
DESTINO = 'media/fotos_cronologicas'

def get_date_taken(path):
    """Intenta sacar la fecha de la foto, si no puede, usa la fecha de creación del archivo"""
    try:
        image = Image.open(path)
        exifdata = image.getexif()
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            if tag == 'DateTimeOriginal':
                return datetime.strptime(exifdata.get(tag_id), "%Y:%m:%d %H:%M:%S")
    except:
        pass
    # Si falla, usar fecha de modificación del sistema
    timestamp = os.path.getmtime(path)
    return datetime.fromtimestamp(timestamp)

def organizar():
    if not os.path.exists(DESTINO):
        os.makedirs(DESTINO)

    archivos = [f for f in os.listdir(ORIGEN) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.mp4', '.mov'))]
    print(f"Procesando {len(archivos)} archivos...")

    files_with_dates = []

    for filename in archivos:
        path = os.path.join(ORIGEN, filename)
        date = get_date_taken(path)
        files_with_dates.append((date, filename))

    # Ordenar por fecha
    files_with_dates.sort(key=lambda x: x[0])

    # Renombrar y Mover
    for i, (date, filename) in enumerate(files_with_dates):
        ext = os.path.splitext(filename)[1]
        # Nuevo nombre: AÑO_MES_DIA_numero.jpg (Ej: 2021_09_09_001.jpg)
        new_name = f"{date.strftime('%Y_%m_%d')}_{i:03d}{ext}"
        
        shutil.copy2(os.path.join(ORIGEN, filename), os.path.join(DESTINO, new_name))
        print(f"Copiado: {filename} -> {new_name}")

    print("¡Listo! Fotos ordenadas en 'media/fotos_cronologicas'")

if __name__ == "__main__":
    organizar()