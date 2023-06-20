import requests

class FipeCarIterator:
    def __init__(self, marca_id):
        self.marca_id = marca_id
        self.modelos = []
        self.index = 0
    