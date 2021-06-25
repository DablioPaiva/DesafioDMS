from src.server.instance import server
import sqlite3
from ..tratamento.convert_saida import SaidaTempo

app, api = server.app, server.api


@api.route("/ranking")
class Resultados():
    def post(self, ):
        request = api.payload
        id_competicao = request['id']
        conn = sqlite3.connect('radar.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM competicoes WHERE id=:id_competicao',
                           {"id_competicao": id_competicao})
        competicao = cursor.fetchone()
        if competicao == None:
            return "Id nao corresponde a nenhuma competição", 400
        cursor.execute('SELECT * FROM resultados WHERE modalidade=:modalidade ORDER BY valor DESC',
                           {"modalidade": competicao[2]})
       
        resultado = cursor.fetchall()
        if competicao[2] == '100M Rasos':
            res_final = []
            for row in resultado:
                d = {
                "Atleta": row[4],
                "Pontuação": SaidaTempo(row[5])
                }
                res_final.append(d)
            return res_final, 200

        if competicao[2] == 'Lancamento de dardos':
            cursor.execute('SELECT atleta, max(valor) FROM resultados WHERE modalidade="lancamento de dardos" GROUP BY atleta HAVING COUNT(atleta) > 1 ORDER BY valor DESC')
            res_final = []
            resultado = cursor.fetchall()
            for row in resultado:
                d = {
                "Atleta": row[0],
                "Pontuação": row[1]
                }
                res_final.append(d)
            return res_final, 200
        
            

        