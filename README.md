# Aplicativo Auto PDF Util

* **auto_carimbar_pdf.py** - ferramenta util para pegar um carimbo criado em uma imagem .png sem fundo e pegar um
arquivo PDF com várias páginas e realizar o desmembramento da cada página e carimbar em no local já pré definido
 em todas as páginas.
  
* Pode ser utilizado para adicionar bordas ou qual tipo de imagem .png com ou sem fundo sobre e um local predefinido na página do arquivo em pdf
* Pode ser utilizado em um arquivo pdf com uma ou mais páginas.
* Alterando as linhas:
'#' nome = texto.replace('Data', ' ').split()[5] -> remover o '#'
  
nome = f'default{c}' -> remover esta linha

É possível fazer o sistema pegar um texto específico dentro de cada página no arquivo e utilizar para dar nome  aos documentos finalizados.

nome = texto.replace('Data', ' ').split()[5] -> esta linha deve ser configurada para o sistema pegar o texto desejado presente dentro de cada página
para utilizar como nome do arquivo final.
