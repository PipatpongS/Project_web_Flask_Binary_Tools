def text_to_binary(text: str) -> list:
    binary = []
    for char in text:
        binary.append(bin(ord(char))[2:])
    return binary

def binary_to_text(binary_list: list) -> str:
    text = ""
    for b in binary_list:
        try:
            if b.strip():
                decimal = int(b, 2)
                text += chr(decimal)
        except:
            text += "?"
    return text