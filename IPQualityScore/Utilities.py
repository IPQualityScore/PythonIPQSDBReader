def uVarInt(bytes):
    x = 0
    s = 0
    for b in bytes:
        if b < 0x80:
            return x | (b << s)
        x |= (b & 0x7f) << s
        s += 7
    return 0