# importando as bibliotecas
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# função de assinatura
def carimba_e_separa_paginas(arquivo_pdf, dados, nome):
    packet = io.BytesIO()

    # configurações do carimbo
    largura = dados[1]
    altura = dados[2]
    pos_horizontal = dados[3]
    pos_vertical = dados[4]

    carimbo = f"carimbos\{dados[0]}"

    # Cria um template em pdf do carimbo sem o fundo
    can = canvas.Canvas(packet, pagesize=letter)
    can.drawImage(image=carimbo, x=pos_horizontal, y=pos_vertical, width=largura,
                  height=altura, mask="auto")
    can.save()

    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    output = PdfFileWriter()
    page = arquivo_pdf
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # Finalizando o arquivo, salvando na pasta de saida
    outputStream = open(f'pdfsaida\{nome}.pdf', "wb")
    output.write(outputStream)
    outputStream.close()


def menu():
    lista = []

    print('Auto Carimbar PDF')
    print('Lista de PDFs')
    for num, nome in enumerate(nome_pdfs):
        print(f'{num} - {nome}')
    lista.append(int(input('Escolha o PDF: ')))
    print('Lista de Carimbos')
    for num, nome in enumerate(lista_carimbos):
        print(f'{num} - {nome[0].replace(".png", "")}')
    lista.append(int(input('Escolha o carimbo: ')))

    return lista


try:
    # listando arquivos na pasta de pdfs
    nome_pdfs = os.listdir('pdforigen')
except:
    print('Verificar as pastas PDFOrigen')

# configurar dados do carimbo manualmente
# lista de carimbos, tamanhos e posicionamento na pagina
# [carimbo, largura, altura, pos_horizontal, pos_vertical]

lista_carimbos \
    = [['Carimbo01.png', 174, 135, 200, 30],
       ['Carimbo02.png', 180, 110, 200, 20],
       ['Carimbo03.png', 185, 135, 200, 45],
       ['Carimbo04.png', 120, 85, 200, 55]]

pdf_carimbo = menu()

print('Carimbando Paginas...')

# carregando pdf
pdf = PdfFileReader(f'PDFOrigen\{nome_pdfs[pdf_carimbo[0]]}')

# pegando o numero de paginas
num_paginas = pdf.numPages

for c in range(0, num_paginas):
    pagina = pdf.getPage(c)
    texto = pagina.extractText()
    # nome = texto.replace('Data', ' ').split()[5]
    nome = f'default{c}'
    carimba_e_separa_paginas(pagina, lista_carimbos
    [pdf_carimbo[1]], nome)

print('Todos as Paginas Foram Carimbadas!')
