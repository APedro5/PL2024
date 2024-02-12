import math


def file_parser():
    with open('datasetExamesMedicos.csv', "r", encoding='utf-8') as file:
        content = file.read()

    lines = content.split("\n")
    lines.pop(0)
    dataset = []

    for line in lines:
        dataset.append(line.split(','))

    return dataset

#_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado

def modalidades_ordenadas():
    dataset = file_parser()
    modalidades = set()
    for _, _, _, _, _, _, _, _, modalidade, _, _, _, _ in dataset:
        modalidades.add(modalidade)
    return sorted(list(modalidades), key=lambda x: x.lower())

def atletas_aptidao():
    dataset = file_parser()
    total_atletas = len(dataset)
    aptos = 0

    for _, _, _, _, _, _, _, _, _, _, _, _, resultado in dataset:
        if resultado.lower() == 'true':
            aptos += 1

    inaptos = total_atletas - aptos
    aptosP = (aptos / total_atletas) * 100
    inaptosP = (inaptos / total_atletas) * 100

    struct = {'Aptos': aptosP, 'Inaptos': inaptosP}
    # print(struct)
    return struct

def distribuicao_por_escalao_etario():
    dataset = file_parser()

    distribuicao = {'[0-4]': 0, '[5-9]': 0, '[10-14]': 0, '[15-19]': 0, '[20-24]': 0,
                    '[25-29]': 0, '[30-34]': 0, '[35-39]': 0, '[40-44]': 0, '[45-49]': 0,
                    '[50-54]': 0, '[55-59]': 0, '[60-64]': 0, '[65-69]': 0, '[70-74]': 0,
                    '[75-79]': 0, '[80-84]': 0, '[85-89]': 0, '[90-94]': 0, '[95-99]': 0,
                    '[100+]': 0}

    for _, _, _, _, _, idade, _, _, _, _, _, _, _ in dataset:
        idade = int(idade)
        for faixa_etaria in distribuicao:
            if '+' in faixa_etaria:
                # Trata o caso especial de '100+'
                if faixa_etaria == '[100+]':
                    if idade >= 100:
                        distribuicao[faixa_etaria] += 1
                continue  # Pula para a próxima iteração
            inicio, fim = map(int, faixa_etaria[1:-1].split('-'))
            if inicio <= idade <= fim:
                distribuicao[faixa_etaria] += 1

    return distribuicao



print("\nAs modalidades desportivas ordenadas alfabeticamente são:")
for modalidade in modalidades_ordenadas():
    print(modalidade)


print("\nAs percentagens de atletas aptos e inaptos para a prática desportiva são:")
for resultado, percentagem in atletas_aptidao().items():
    print(f"{resultado}: {percentagem}%")


print("\nA distribuição de atletas por escalão etário é:")
for faixa_etaria, quantidade in distribuicao_por_escalao_etario().items():
    print(f"{faixa_etaria}: {quantidade} atletas")

print("\n")
