from flask import Flask
from flask import app

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = app(self.app,
            version="1,0",
            title="API Olimpíadas",
            description="API Olimpíadas",
            doc="/docs"
        )
    def run(self,):
        self.app.run(
            debug=True
        )

server = Server()