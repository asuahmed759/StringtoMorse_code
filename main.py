morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

def string_to_morse_code(input_string):
    input_string = input_string.upper()
    morse_code = ""

    for char in input_string:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char]+""
        else:
            morse_code += morse_code+""
    return morse_code

input_txt = input("Enter the string:")
result = string_to_morse_code(input_txt)
print("Morse Code:", result)

