### BovClass
# bovclass / api
## API (Application Programming Interface) for predicting the quality of beef carcass, using the Machine Learning model trained using information on slaughter of animals from the Precoce MS program. For more detailed information on model design and training, [visit here](https://github.com/rafamarquesi/precoce-ms-classification).

**Flask**

## Ambiente de Desenvolvimento

Veja abaixo como instanciar o Flask em seu **ambiente local de desenvolvimento**.

Primeiramente copie os arquivos-exemplo de variáveis de ambiente e configure para seu ambiente local:

```
cp .env.example .env
cp .env.ci.example .env.ci
```

Repare que é necessário obter o DSN do Sentry na [_dashboard_ do Embrapa I/O](https://dashboard.embrapa.io).
O _PORT_, em .env.example, é a porta que o Nginx irá utilizar para servir a aplicação.

### Utilizando o Docker

Para simular os ambientes remotos (de _alpha_, _beta_ e _release_) localmente, suba a aplicação utilizando o [Docker](https://www.docker.com):

```
docker network create bovclass_api_development

env $(cat .env.ci) docker-compose up --force-recreate --build -d
```
