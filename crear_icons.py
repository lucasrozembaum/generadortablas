import zlib
import struct

def generar_png(width, height, r, g, b):
    raw_data = bytearray()
    for _ in range(height):
        raw_data.append(0)  # Filtro PNG: None
        raw_data.extend([r, g, b] * width)
    
    comprimido = zlib.compress(bytes(raw_data))
    
    def bloque(tipo, datos):
        return struct.pack('>I', len(datos)) + tipo + datos + struct.pack('>I', zlib.crc32(tipo + datos) & 0xffffffff)
    
    png = b'\x89PNG\r\n\x1a\n'
    png += bloque(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
    png += bloque(b'IDAT', comprimido)
    png += bloque(b'IEND', b'')
    return png

# Verde oficial (#136b33)
with open("icon-192.png", "wb") as f:
    f.write(generar_png(192, 192, 19, 107, 51))

with open("icon-512.png", "wb") as f:
    f.write(generar_png(512, 512, 19, 107, 51))

print("Imagenes PNG oficiales generadas con exito.")