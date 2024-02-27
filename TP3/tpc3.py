import re
import sys

def somador_on_off(inp):
    with open(inp, 'rb') as f:
        content = f.read()

    somar = True
    resultado = 0
    i = 0

    while i < len(content):
        char = chr(content[i])

        if re.match(r'O', char, re.IGNORECASE):
            i += 1
            if re.match(r'N', chr(content[i]), re.IGNORECASE):
                somar = True
                i += 1
        elif re.match(r'F', char, re.IGNORECASE):
            i += 1
            if re.match(r'F', chr(content[i]), re.IGNORECASE):
                somar = False
                i += 1
        elif char == '=':
            print(resultado)
            i += 1
        elif char == '-':
            i += 1
            char = chr(content[i])
            if re.match(r'\d', char) and somar:
                resultado_aux = 0
                while i < len(content) and re.match(r'\d', chr(content[i])):
                    resultado_aux *= 10
                    resultado_aux += int(chr(content[i]))
                    i += 1
                resultado -= resultado_aux
        elif re.match(r'\d', char) and somar:
            resultado_aux = 0
            while i < len(content) and re.match(r'\d', chr(content[i])):
                resultado_aux *= 10
                resultado_aux += int(chr(content[i]))
                i += 1
            resultado += resultado_aux
        else:
            i += 1

def main(argv):
    if len(argv) != 2:
        print("Utilize: python(3) tpc3.py nome_do_ficheiro")
        sys.exit(1)

    somador_on_off(argv[1])

if __name__ == "__main__":
    main(sys.argv)
