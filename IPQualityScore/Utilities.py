def uVarInt(bytes):
    x = 0
    s = 0
    i = 0
    while i < len(bytes):
        b = bytes[i]
        if b < 0x80:
            return x | b<<s

        x |= b&0x7f << s
        s += 7
        i += 1

    return 0