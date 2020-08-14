# bartender
Microserviço responsável por preparar as "bebidas" dos pedidos enviados pelos [waiters](../waiter).

### Ações

Este microsserviço coleta os itens na fila de drink (drinks) e os processa. 
Cada item possui um tempo de preparo (timer) o qual é aguardado para cada item.
Após pronto, o item é adicionado a fila do balcão.

### Instalando a aplicação

Para instalar a aplicação, tenha o [Python](https://www.python.org/) na versão 3.7+.

Execute o comando abaixo para instalar as dependências:
```shell script
python3 -m pip install -r requirements
```

### Testando Local
Execute o comando:
```shell script
docker-compose up
```
Isso irá subir um banco de dados Mongodb na porta 27019. Rode a aplicação.
Caso seja necessário, altera as propriedades de execução da aplicação em [application.ini](application.ini).

Após isso execute a aplicação.

**Observação:** é necessário prover o Kafka para execução deste microsserviço. 