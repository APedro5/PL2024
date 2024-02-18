import re
import sys

def converter(lines):
    i = 0
    result = []
    while i < len(lines):
        if lines[i].startswith("\n"):

            if len(lines[i].strip()) == 0:
                result.append("")
            i += 1

        elif lines[i] == "":
            result.append("")
            i+=1

        elif lines[i].startswith("#"):
            level = lines[i].count('#')
            text = lines[i][level+1:].strip()
            result.append(f"<h{level}>{text}</h{level}>\n")
            i += 1
        
        elif lines[i].startswith("> "):
            text = lines[i][2:].strip()
            result.append(f"<blockquote>\n<p>{text}</p>\n</blockquote>\n")
            i += 1
        
        elif lines[i].startswith("---"):
            result.append("<hr>\n")
            i += 1
        
        elif re.match(r'^\s*\d+\.', lines[i]):
            result.append("<ol>\n")
            while i < len(lines) and re.match(r'^\s*\d+\.', lines[i]):
                items = [item.strip() for item in re.split(r'\s*\d+\.\s*', lines[i])[1:] if item]
                result.extend([f'<li>{item}</li>\n' for item in items])
                i += 1
            result.append("</ol>\n")
        
        elif lines[i].startswith("  - "):
            result.append("<ul>\n")
            while i < len(lines) and lines[i].startswith("  - "):
                text = lines[i][4:].strip()
                result.append(f"<li>{text}</li>\n")
                i += 1
            result.append("</ul>\n")

        else:
            lines[i] = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', lines[i])
            lines[i] = re.sub(r'\*(.*?)\*', r'<i>\1</i>', lines[i])
            lines[i] = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', lines[i])
            lines[i] = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', lines[i])
            lines[i] = re.sub(r'`([^`]+)`', r'<code>\1</code>', lines[i])
            result.append(f"<p>{lines[i]}</p>\n")
            i += 1

    return result

def md_to_html(inp):
    with open(inp, "r", encoding='utf-8') as file:
        content = file.read()

    lines = content.split("\n")
    result = converter(lines)
    out = inp.replace(".md", ".html")

    with open(out, 'w') as html_file:
        for converted_line in result:
            html_file.write(converted_line)

def main(inp):
    md_to_html(inp[1])

if __name__ == "__main__":
    main(sys.argv)
