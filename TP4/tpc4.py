import re
import sys
from tokenizer import analexer

def analex(inp):
    with open(inp, 'r') as f:
        content = f.read()


    analexer.input(content)

    for token in analexer:
        print(token)

def main(argv):
    if len(argv) != 2:
        print("Utilize: python(3) tpc3.py nome_do_ficheiro")
        sys.exit(1)

    analex(argv[1])

if __name__ == "__main__":
    main(sys.argv)
