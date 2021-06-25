from flask import Flask
from flask import API

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = API(self.app,
            version="1,0",
            title="Desafio DMS Olimpíadas",
            description="API Olimpíadas",
            doc="/docs"
        )
    def run(self,):
        self.app.run(
            debug=True
        )

server = Server()
