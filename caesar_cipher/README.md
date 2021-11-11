# Caesar Cipher

## Sobre
A técnica Cifra de César é um dos métodos mais antigos e simples de criptografia. É simplesmente um tipo de cifra de substituição, ou seja, cada letra de um determinado texto é substituída por outra de acordo com um número fixo de posições acima ou abaixo do alfabeto.

Por exemplo, com uma troca de 3 posições, a letra A seria substituída pela letra D, B por E, C por F, e assim por diante.

![](img/caesar3.svg)

O método criptográfico ganhou esse nome em homenagem a Júlio César, ditador romano, que o usou para se comunicar com seus generais.

A transformação pode ser feita ao alinhar os dois alfabetos: o alfabeto cifrado e o alfabeto normal rotacionado à direita ou esquerda por um determinado número de posições.

Por exemplo, uma cifra usando uma rotação à esquerda de três posições.

>Normal:   ABCDEFGHIJKLMNOPQRSTUVWXYZ
>
>Cifrado:  DEFGHIJKLMNOPQRSTUVWXYZABC

Para criptografar uma mensagem, deve-se simplesmente observar cada letra da mensagem na linha "Normal" e escrever a letra correspondente na linha "Cifrado". Para descriptografar, basta fazer o contrário.

>Normal:   Olá, mundo
>
>Cifrado:  ROD  PXQGR

## Como funciona
O usuário deve informar se deseja encriptar ou decodificar uma mensagem. Após isso, digita a mensagem e o número de posições.

Ao final o programa vai retornar a mensagem de forma encriptada ou decodificada.

## Teste
Para executar o script online [clique aqui](https://replit.com/@vhsenna/caesarcipher#main.py).
