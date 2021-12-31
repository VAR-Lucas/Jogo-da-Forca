import random
filmes = ['vingadores', 'homem aranha', 'doce vinganca', 'harry potter', 'anaconda', 'encanto', 'venom', 'Infiltrado', 'demolidor','luca']

print('você pode errar seis vezes a letra.')

print('Escolha o tipo de palavra: ')
print()
print('1 - filmes')
print()
tipo_de_palavra = int(input('Escreva a opção: '))


palavra_oculta=[]
letras_corretas = []
if tipo_de_palavra == 1:
    palavra = filmes[random.randint(0, len(filmes)-1)]
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


