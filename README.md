# Redes de Computadores 

## Como funciona o jogo

O jogo consiste em adivinhar um número que é gerado aleatoriamente pelo servidor, quando o cliente faz uma jogada indicando o número atual, o servidor retorna uma dica dizendo se a resposta é maior ou menor do que o número informado pelo jogador. 

Quando o número da jogada atual é igual a resposta, o jogador é informado que venceu e a instancia do cliente é encerrada, e os demais jogadores conectados e que ainda não acertaram continuam jogando.

## Observações Importantes

Para que um cliente possa se conectar a um servidor que esteja operando em outra máquina (ou na mesma), eles devem estar conectados à mesma rede de internet.

A porta utilizada no localhost foi a 9000.

## Instruções para a execução do código

Para rodar o servidor é necessário entrar no diretório "src" e em seguida executar o seguinte comando no terminal:

```c
python3 server.py
```

Após isso, o servidor estará rodando e com isso, clientes poderão iniciar o jogo com o número sorteado pelo servidor.

Para a conexão de um cliente, basta entrar novamente no diretório "src" e em seguida rodar o comando no terminal: 

```c
python3 client.py
```

Assim, uma nova instancia do cliente será criada e caso a conexão com o servidor seja estabelecida corretamente, o jogo irá começar. Será recebida uma mensagem indicando o inicio do jogo.

Além disso, mais de um cliente pode se conectar e jogar ao mesmo tempo (utilização de threads).
