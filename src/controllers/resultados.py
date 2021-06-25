from src.server.instance import server
import sqlite3
from ..tratamento.convert_salvar import ConverteMetros, ConverterTempo

app, API = server.app, server.api


@app.route("/resultados")
class Resultados():
    def post(self, ):
        request = app.payload
        id_competicao = request['competicao']
        atleta = request['atleta']
        valor = request['valor']
        unidade = request['unidade']
        
        conn = sqlite3.connect('radar.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM competicoes WHERE id=:id',
                       {"id": id_competicao})
        resultado = cursor.fetchone()
        if resultado == None:
            return "Id nao corresponde a nenhuma competição", 400
        modalidade = resultado[2]
        nome_competicao = resultado[1]

        if resultado[3] == 1:
            if modalidade == "100M Rasos":
                valor = ConverterTempo(valor, unidade)

            if modalidade != "lancamento de dardos":
                cursor.execute(
                    'SELECT * FROM resultados WHERE atleta=:atleta AND modalidade=:modalidade', {"atleta": atleta, "modalidade": modalidade})
                if cursor.fetchall():
                    conn.close
                    return "Atleta já Participou dessa Competição", 400
                
            else:
                cursor.execute(
                    'SELECT count(1) FROM resultados WHERE atleta=:atleta AND modalidade=:modalidade', {"atleta": atleta, "modalidade": modalidade})
                c = cursor.fetchall()[0][0]
                if c >= 3:
                    conn.close
                    return "Atleta já teve 3 tentativas na competição", 400

            cursor.execute('INSERT INTO resultados VALUES (NULL)',
                           (id_competicao, nome_competicao, modalidade, atleta, valor))
            conn.commit()
            
            return 200
        return "Essa Competição já foi finalizada", 400
