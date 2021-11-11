# Rock, Paper, Scissors

## Sobre
Rock, Paper, Scissors, também conhecido no Brasil como Pedra, Papel, Tesoura ou, do japonês, jokenpô, é um simples jogo recreativo de mãos para duas ou mais pessoas.

O jogo é bastante empregado como um método de escolha, assim como lançar moedas cara ou coroa, por exemplo. Mas embora pareça um jogo baseado em sorte, existe uma certa estratégia por trás de tudo.

[Cientistas descobriram](http://arxiv.org/pdf/1404.5199v1.pdf) que "se um jogador ganha um jogo, sua probabilidade de repetir a mesma ação no próximo jogo é consideravelmente alta".

Por outro lado, se um jogador perde duas ou mais vezes em sequência, ele joga o sinal que teria vencido o oponente na rodada anterior.

Funciona assim: o jogador A vem ganhando as rodadas, acaba de jogar "pedra" e ganha mais uma vez. Na próxima rodada, o jogador B provavelmente jogará "papel", que venceria na rodada anterior.

Essa estratégia se chama "ganha-continua, perde-muda".

Mas e se o adversário também conhece essa estratégia? A única certeza é um jogo bastante emocionante.

No projeto a seguir o computador escolherá uma das três opções aleatoriamente, sem analisar se perdeu ou ganhou e sem auferir a sua jogada.

Para saber mais sobre as regras "oficiais" do jogo acesse o site da [World Rock Paper Scissors Association](https://wrpsa.com/the-official-rules-of-rock-paper-scissors/).

## Como funciona
O algoritmo recebe do usuário a jogada que ele deseja fazer e, em seguida, o computador aleatoriamente também faz sua jogada.

Com base nas regras do jogo, é conferido e retornado o ganhador da partida ou se houve empate.

## Teste
Para executar o script online [clique aqui](https://replit.com/@vhsenna/rockpaperscissors#rock_paper_scissors.py).
