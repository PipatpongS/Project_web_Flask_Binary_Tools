def text_to_binary(text: str) -> list:
    binary = []
    for i in text:
        ascii = ord(i)
        char_binary = ""
        while True:
            rem = ascii % 2
            char_binary += str(rem)
            divisible = ascii // 2
            if divisible == 0: break
            ascii = divisible
        while len(char_binary) < 8:
            char_binary += str(0)
        binary.append(char_binary[::-1])
    return binary

def show_bianry(binary: list) -> None:
    for i in binary:
        print(i, end = " ")

def binary_to_text(binary: list) -> str:
    text = ""
    for i in binary:
        decimal = 0
        binary_inv = i[::-1]
        for j in range(len(i)):
            tmp = int(binary_inv[j]) * (2**j)
            decimal += tmp
        text += chr(decimal)
    return text