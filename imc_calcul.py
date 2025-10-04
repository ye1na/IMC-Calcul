taille = float(input("Quelle est ta taille en mètre ?"))
poids = float(input("Quelle est ton poids en kg ?"))
imc = poids/taille**2
if imc < 19.5 :
    print("Tu es en état de maigreur", imc)
if imc >= 18.5 and imc <= 25 :
    print("Tu as une corpulance normale", imc)
if imc >= 25 :
    print("Tu es en surpoids", imc)