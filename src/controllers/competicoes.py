from typing import List
from src.server.instance import server
import sqlite3

app, api = server.app, server.api
MODALIDADES = ["100M Rasos", "Lancamento de dardos"]


@api.route("/competicoes")
class Competicoes():
    def get(self,):
        conn = sqlite3.connect('radar.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM competicoes')
        resultado = cursor.fetchall()
        res_final = []
        for row in resultado:
           d = {
               "id": row[0],
               "nome": row[1],
               "modalidade": row[2],
               "em_andamento": row[3]
           }
           res_final.append(d)

        return res_final, 200

    def post(self,):
        request = api.payload
        nome = request['nome']
        modalidade = request['modalidade']

        if modalidade in MODALIDADES:
            conn = sqlite3.connect('radar.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM competicoes WHERE nome=:nome AND modalidade=:modalidade',
                           {"nome": nome, "modalidade": modalidade})
            if cursor.fetchall():
                conn.close()
                return "Competição já cadastrada", 400

            cursor.execute("INSERT INTO competicoes VALUES (NULL, ?, ?, 1)",
                           (nome, modalidade))
            conn.commit()

            cursor.execute('SELECT * FROM competicoes WHERE nome=:nome AND modalidade=:modalidade',
                           {"nome": nome, "modalidade": modalidade})

            resultado = cursor.fetchall()
            res_final = []
            for row in resultado:
                d = {
                "id": row[0],
                "nome": row[1],
                "modalidade": row[2],
                "em_andamento": row[3]
                }
                res_final.append(d)

            return res_final, 200

        else:
            return "Modalidade nao existe! Utilize no campo Modalidade: ('100M Rasos' ou 'lancamento de dardos')", 400

    def put(self,):
        request = api.payload
        id_competicao = int(request['id'])
        conn = sqlite3.connect('radar.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE competicoes SET em_andamento = 0 WHERE id=:id',{"id": id_competicao})
        conn.commit()
        conn.close()
        return "Competição Finalizada ", 200
