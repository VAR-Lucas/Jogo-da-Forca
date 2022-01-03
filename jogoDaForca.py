from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

PATH = r'C:\Users\Lucas\Documents\Meus-projetos\Jogo-da-Forca\chromedriver.exe'

class chrome:
    def __init__(self):
        self.driver = webdriver.Chrome(PATH)
        


def buscarFilmes(self):
    driver = self.driver
    print('entrou')

    driver.get('https://www.google.com/search?q=filmes&source=hp&ei=bOLRYZjnMtuo1sQPy72doAE&iflsig=ALs-wAMAAAAAYdHwfFakP8mmezB1T3xOX575zNcreEZX&ved=0ahUKEwiYzeSpzZP1AhVblJUCHcteBxQQ4dUDCAc&uact=5&oq=filmes&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyBQgAEIAEMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoICC4QgAQQsQM6BQguEIAEOggIABCxAxCDAToOCC4QgAQQsQMQxwEQ0QM6CAguELEDEIMBUABYtgdg6gloAHAAeACAAckBiAHjCJIBBTAuNS4xmAEAoAEB&sclient=gws-wiz')
    filmes = []
    def inserirFilmes():
        filme = driver.find_element(By.CSS_SELECTOR, 'div[data-index="0"]').text
        filmes.append(filme)
    inserirFilmes()
    botao_proximo = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[7]/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div[3]/div/g-expandable-container/div/g-expandable-content[1]/span/div/div/div[2]/div/g-scrolling-carousel/div[3]/g-right-button/g-fab')
    for x in range(3):
        botao_proximo.click()
        time.sleep(0.5)
        inserirFilmes()
    driver.quit()
    del filmes[0:-1]
    palavras = filmes[0].split('\n')
    return palavras


def buscarMusicas(self):
    driver = self.driver
    driver.get('https://open.spotify.com/playlist/37i9dQZF1DX0FOF1IUWK1W')
    print('entrou')
    time.sleep(8)
    palavras=[]
    for x in range(1, 45):
        Musica = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[3]/div/div[2]/div[2]/div[%d]/div/div[2]/div/div'%x).text
        palavras.append(Musica)
    driver.quit()
    return palavras

    

def buscarJogos(self):
    driver = self.driver
    driver.get('https://www.epicgames.com/store/pt-BR/collection/top-sellers')
    print('entrou')
    time.sleep(4)
    palavras=[]
    for x in range(1, 26):
        NomeJogo = driver.find_element(By.XPATH, '//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div/div/div[2]/section[2]/div/section/ul/div[%d]/div/div/div/a/div/div/div[2]/span/div'%x).text 
        palavras.append(NomeJogo)
    driver.quit()
    return palavras


print('você pode errar seis vezes a letra.')

print('Escolha o tipo de palavra: ')
print('\n1 - Filmes\n')
print('\n2 - Musicas\n')
print('\n3 - Jogos\n')

tipo_de_palavra = int(input('Escreva a opção: '))


palavra_oculta=[]
letras_corretas = []
if tipo_de_palavra:
    navegador = chrome()
if tipo_de_palavra == 1:
    palavras = buscarFilmes(navegador)
elif tipo_de_palavra == 2:
    palavras = buscarMusicas(navegador)
elif tipo_de_palavra == 3:
    palavras = buscarJogos(navegador)
else:
    print('caractere invalido')

time.sleep(10)
palavra = palavras[random.randint(0, len(palavras)-1)]
print(palavra)
for x in range(len(palavra)):
    palavra_oculta.append("*")
    letras_corretas.append(palavra[x])
if ' ' in palavra:
    numero = palavra.index(' ')
    palavra_oculta[numero] = palavra[numero]


print(palavra_oculta)
print()

letrasTendadas = []
letras_mostradas = []


def trocarCaractere():
    substituto = letras_mostradas[-1]
    for x in range(len(palavra)):
        if palavra[x] == substituto:
            palavra_oculta[x] = substituto


tentativas = 6
while True:
    print('palavra: ', end=(''))
    for x in range(len(palavra_oculta)):
        print(palavra_oculta[x], end=(''))
    print()
    print('Letras tendadas: ',end='')
    for y in range(len(letrasTendadas)):
        print(letrasTendadas[y], end=('| '))
    print()

    letra = input('Digite uma letra: ').lower()
    if letra in letrasTendadas:
        print('Essa letra já foi tentada.')
        
    else:        
        letrasTendadas.append(letra)
        print()

        if letra in letras_corretas:
            print('A letra ',letra,' está na palavra.')
            letras_mostradas.append(letra)
            trocarCaractere()

        else:
            print('A letra ',letra,' não está na palavra.')
            tentativas -= 1
            print('você ainda tem', tentativas, 'tentativas' )

        if tentativas == 0:
            print('Você perdeu')
            break

        elif palavra_oculta == letras_corretas:
            print('A palavra era',palavra)
            print('Você venceu')
            break
