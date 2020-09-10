# waiter
Microserviço responsável por atender os clienter, respondendo as opções do menu, realizando  os pedidos e verificando 
se estão prontos.

## APIs

### GET /menu
Lista as opções do menu.

Exemplo de resposta:
```json
[
    {
        "id": 1,
        "name": "Batata Frita",
        "type": "FOOD"
    }
]
```

### POST /order

Realiza um pedido. 

O padrão do body da request deverá ser como no exemplo:
```json
{
    "orderId": 1,
    "items": [
        {
            "id": 1,
            "type": "FOOD"
        },
        {
            "id": 5,
            "type": "FOOD"
        }
    ]
}
```

Onde os **id** e **type** são ids e types dos itens do menu. O campo **orderId** é o identificado do pedido realizado.

Os pedidos de comida (o tipo food) são enviados para a fila do [cooker](../cooker).

Também é adicionado na fila balcão os itens enviados aos consumidores com o status de PENDING.

### GET /order

Verifica se um pedido está pronto.

Essa API verifica na fila balcão se os itens já estão prontos, caso estejam alteram o status do pedido para DONE. 

Exemplo de resposta para esta API é:
```json
[
    {
        "order_id": 2,
        "item_id": 1,
        "status": "DONE"
    },
    {
        "order_id": 2,
        "item_id": 5,
        "status": "PENDING"
    }
]
```

## Consumer

Este microsserviço também possui uma interface [consumer](./consumer.py) para consumir os itens enviados para o balcão. 

## Instalando a aplicação

Para instalar a aplicação, tenha o [Python](https://www.python.org/) na versão 3.7+.

Execute o comando abaixo para instalar as dependências:
```shell script
python3 -m pip install -r requirements
```

## Testando Local
Execute o comando:
```shell script
docker-compose up
```
Isso irá subir um banco de dados Mongodb na porta 27017. Rode a aplicação.
Caso seja necessário, altera as propriedades de execução da aplicação em [application.ini](application.ini).

Após isso execute a aplicação.

**Observação:** é necessário prover o Kafka para execução deste microsserviço. 