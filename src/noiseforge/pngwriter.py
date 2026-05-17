import struct
import zlib


PNGSIGNATURE = b'\x89PNG\r\n\x1a\n'


def createchunk(chunktype, data):

    chunk = chunktype + data

    return (
        struct.pack("!I", len(data)) +
        chunk +
        struct.pack(
            "!I",
            zlib.crc32(chunk) & 0xffffffff
        )
    )


def savepng(
    filename,
    width,
    height,
    pixels
):

    rawdata = b''

    for row in pixels:
        rawdata += b'\x00' + bytes(row)

    compressed = zlib.compress(rawdata)

    ihdr = struct.pack(
        "!IIBBBBB",
        width,
        height,
        8,
        0,
        0,
        0,
        0
    )

    with open(filename, "wb") as file:

        file.write(PNGSIGNATURE)

        file.write(
            createchunk(
                b'IHDR',
                ihdr
            )
        )

        file.write(
            createchunk(
                b'IDAT',
                compressed
            )
        )

        file.write(
            createchunk(
                b'IEND',
                b''
            )
        )
