"""
4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de
Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão
Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de
Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro
possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

Percebendo a ideia de que um ponto igual tem uma única distancia de outro ponto, tanto o carro quanto o caminhão se
encontram em um mesmo ponto na reta, que equivale a estrada, desta forma estão na mesma distância tanto de Ribeirão
Preto, quanto de Franca.

"""
carro = 0
caminhao = 100
minuto = 10

while caminhao > 0:
    carro += 110 / (3.6 * 60)

    if minuto > 0:
        minuto -= 1

    if minuto == 5:
        caminhao -= 80 / (3.6 * 60)
    elif minuto == 0:
        caminhao -= 80 / (3.6 * 60)

    # Mesmo q a distancia não seja exatamente igual aqui levamos um número aproximado para demonstrar este fato, pois
    # no exato momento em que eles estão um ao lado do outro, eles se encontram no mesmo ponto, desta forma a distancia
    # de Ribeirãao Preto é a mesma.
    if int(carro) == int(caminhao):
        print('Eles estão na mesma distância de Riberão Preto quando se cruzam na rodovia!')
        break
