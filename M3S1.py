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