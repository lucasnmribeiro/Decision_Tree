from sklearn import tree
import time

def perguntar_peso_textura():
    peso = input("How many grams are in the fruit? ")
    textura = input("What is the texture of the shell? (1 for Smooth, 0 for Irregular)")
    return [int(peso), int(textura)]

def continuar_interacao():
    resposta = input("Do you want to interact again? (y/n): ")
    return resposta.lower() == 'y'

def main():
    informacoes = [[150, 1], [140, 1], [160, 0], [130, 0]]
    frutas = [5, 5, 10, 10]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(informacoes, frutas)

    while True:
        nova_amostra = perguntar_peso_textura()
        resultado = clf.predict([nova_amostra])[0]
        print("The fruit is an Apple." if resultado == 5 else "The fruit is an Orange.")
        
        if not continuar_interacao():
            break

if __name__ == "__main__":
    main()
    time.sleep(5)  
