from sklearn import tree
import time

def perguntar_peso_textura():
    peso = input("Quantos gramas tem a fruta?")
    textura = input("Qual é a textura da casca? (1 para Suave, 0 para Irregular)")
    return [int(peso), int(textura)]

def continuar_interacao():
    resposta = input("Deseja continuar? (s/n): ")
    return resposta.lower() == 'y'

def main():
    informacoes = [[150, 1], [140, 1], [160, 0], [130, 0]]
    frutas = [5, 5, 10, 10]

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(informacoes, frutas)

    while True:
        nova_amostra = perguntar_peso_textura()
        resultado = clf.predict([nova_amostra])[0]
        print("A fruta é uma maçã." if resultado == 5 else "A fruta é uma laranja.")
        
        if not continuar_interacao():
            break

if __name__ == "__main__":
    main()
    time.sleep(5)  
