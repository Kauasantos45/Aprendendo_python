#M3S1
#Para a atividade desta semana, você deverá criar um interator que irá iterar os dados da API (Application Interface) da tabela FIPE e retornar os carros de uma determinada marca de veículos (essa deverá ser passada para a classe que fará o papel de interator no momento da instanciação, neste caso use o ID de uma marca).

#Para trazer esses dados, será necessário interagir com a API da FIPE disponível nesse endereço: https://deividfortuna.github.io/fipe/. Dicas:

#Para listar as marcas use a URL:  https://parallelum.com.br/fipe/api/v1/carros/marcas dessa forma serão listadas todas as marcas que a API possui. Escolha uma para ser usada na próxima etapa, grave o ID dela para ser usado no seu código.
#Nesta etapa use a marca selecionada para poder retornar os veículos que essa marca possui usando a URL: https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos
#Ao chamar esse endpoint, será retornada uma resposta que possui um nó, no formato JSON, com os modelos dos veículos que ela possui.
#Seu interator deverá inteirar em cada um desses modelos e trazer informações do nome e ID do veículo da marca selecionada.



import requests

class FipeIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = None
        self.index = 0

    def fetch_modelos(self):
        headers = {'user-agent': 'app-teste'}
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{self.marca_id}/modelos"
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            self.modelos = data['modelos']
        else:
            raise Exception("O id informado nao pertence a nenhuma marca")

    def __iter__(self):
        return self

    def __next__(self):
        if self.modelos is None:
            self.fetch_modelos()

        if self.index < len(self.modelos):
            carro = self.modelos[self.index]
            self.index += 1
            return carro['nome'], carro['codigo']
        else:
            raise StopIteration

marca_id = 100

iterador = FipeIterator(marca_id)

for nome, codigo in iterador:
    print(f"Nome: {nome}, Código: {codigo}")
