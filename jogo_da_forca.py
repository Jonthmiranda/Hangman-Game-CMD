#modulos
import random
import array

#variaveis
palavras = ['dicionário', 'intrínseco', 'prescindir', 'presunçoso', 'diligência', 'corroborar', 'intempérie',
            'perspicaz', 'recíproco', 'concessão', 'impressão', 'escrúpulo', 'inerente', 'respeito', 'peculiar',
            'denegrir', 'sagaz', 'âmago', 'negro', 'termo', 'êxito', 'mexer', 'nobre', 'senso', 'afeto', 'algoz',
            'imprescindível', 'condescendente', 'idiossincrasia', 'característica', 'concupiscência', 'extraordinário']
palav_esc = random.choice(palavras) #palavra aleatório do vetor palavras
vetor_letra = [] #letras
vetor_adiv = [] #adivinhando
vetor_ltent = [] #letras tentadas
tentativas = 6
let_tent = 1
#descobrindo quantas letras tem, gravando nos vetores
count = 0
for x in palav_esc:
    count += 1
    vetor_letra.insert(count, x)
    vetor_adiv.insert(count, ' _ ')

#iniciando game
letras = str
while vetor_letra != vetor_adiv:
    #caso erre 6 vezes
    if tentativas == 0:
        print("Infelizmente você perdeu!! a palavra era:", palav_esc)
        break
       
    print("Você tem ", tentativas, " tentativas\n")
    #imprimindo as letras ja tentadas
    for x in vetor_ltent:
        print(x, end="")
    print("\n")
       
    #imprimindo as letras adivinhadas
    for x in vetor_adiv:
        print(x, end="")
    #tentando adivinhar
    letras = str(input("\n\nDigite uma letra ou a palavra: \n"))
    print("\n")
   
    #se acertar a digitando a palavras
    if letras == palav_esc:
        #pulando varias linhas
        for x in range(10):
            print("\n")
        print("Parabens!!, você venceu")
        break
   
    tem_letra = 0
    countara = 0
    #caso tenha a letra
    for x in vetor_letra:
        if letras == x:
            vetor_adiv.pop(countara)
            vetor_adiv.insert(countara, letras)
            tem_letra = 1
        countara += 1
    #adicionando letra digitada no vetor
    vetor_ltent.insert(let_tent, letras)
    let_tent += 1
   
    #caso não tenha a letra
    if tem_letra == 0:
        tentativas -= 1
     
           
    #pulando varias linhas
    for x in range(10):
        print("\n")
       
#caso acerte a palavras  
else:
    #pulando varias linhas
    for x in range(10):
        print("\n")
    print("A palavra era", palav_esc)
    print("Parabens!! você venceu")