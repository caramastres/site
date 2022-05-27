import bcrypt
import sqlite3
import datetime
from platform import python_version


########################### START CLASS #######################################
class Connection(object):
    def __init__(self, db_name: str):
        self.id = None
        try:
            # conectando...
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            # imprimindo a versão do python
            print(f"Python version: {python_version()}")
            # lendo a versão do SQLite
            self.cursor.execute('SELECT SQLITE_VERSION()')
            self.data = self.cursor.fetchone()
            # imprimindo a versão do SQLite
            print(f"SQLite version: {self.data[0]}")
            # imprimindo nome do banco
            print(f"Banco de Dados: {db_name}\n")
        except sqlite3.Error as error:
            print('Fail', error)

    def commit_db(self):
        if self.conn:
            self.conn.commit()

    def close_db(self):
        if self.conn:
            self.conn.close()
            print("\nConexão fechada.")

    # Seleciona todos por ordem alfabetica
    def select_all(self):
        try:
            sql = 'SELECT * FROM alunos ORDER BY id'
            res = self.cursor.execute(sql)
            return res.fetchall()
        except sqlite3.Error as error:
            print('Fail', error)

    # Imprime todos campos dos alunos
    def print_all(self):
        lista = self.select_all()
        for campo in lista:
            print(f"{campo[0]} | {campo[1]} | {campo[2]} | {campo[3]} | {campo[4]} | {campo[6]} | {campo[7][:11]}")

########################### CADASTRO ##########################################
    # Cadastra novo aluno no banco de dados
    def cadastra_aluno(self, nome_entry: str, telefone_entry: str, nascimento_entry: str, email_entry: str, senha_entry: str, admin_entry: int):
        # CRIPTOGRAFIA
        pwd_enc = senha_entry.encode('utf-8')
        hash_psd = bcrypt.hashpw(pwd_enc, b'$2b$12$4f0MkkWy7dFBVqo9zaAuSu')
        date_now = datetime.datetime.now().isoformat(" ")
        insert_query = """INSERT INTO alunos (nome, telefone, nascimento, email, senha, admin, data) VALUES (?,?,?,?,?,?,?);"""
        data_sql = (nome_entry.strip().lower(), telefone_entry.strip(), nascimento_entry, email_entry.strip().lower(), hash_psd, admin_entry, date_now)
        try:
            self.cursor.execute(insert_query, data_sql)
            self.commit_db()
            print('Informações inseridas com sucesso.')
            return True
        except sqlite3.IntegrityError:
            print("Aviso: O e-mail deve ser único.")
            return False

########################### DELETA ALUNO ######################################
    # Deleta um aluno do banco de dados
    def deleta_aluno_by_email(self, email):
        try:
            self.cursor.execute("DELETE FROM alunos WHERE email = ?", (email.strip().lower(),))
            self.commit_db()
            print('Aluno deletado dos registros!')
        except sqlite3.Error as error:
            print('Fail', error)

    def deleta_aluno_by_id(self, id_aluno: int):
        try:
            self.cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,))
            self.commit_db()
            print('Aluno deletado dos registros!')
        except sqlite3.Error as error:
            print('Fail', error)

############################### AVALIAÇÕES ####################################
    def cadastra_avaliacao(self, id_aluno_sql: int, sexo_sql: str, altura_sql: float, peso_sql: float, fc_sql: int, pa_sql: str):
        date_sql = datetime.datetime.now().isoformat(" ")
        insert_query = """INSERT INTO avaliacao (id_aluno, data, sexo, altura, peso, fc, pa) VALUES (?,?,?,?,?,?,?);"""
        data = (id_aluno_sql, date_sql, sexo_sql.strip().lower(), altura_sql, peso_sql,
                fc_sql, pa_sql.strip())
        # Tentando conectar ao DB
        try:
            self.cursor.execute(insert_query, data)
            self.commit_db()
            print('Variables inserted successfully.')
            return True
        except sqlite3.IntegrityError as erro:
            print(f"Aviso: {erro}")
            return False

    def select_avaliacao_by_id_aluno(self, id_aluno_sql: int):
        try:
            sql = f"SELECT * FROM avaliacao WHERE id_aluno = '{id_aluno_sql}'"
            res = self.cursor.execute(sql)
            return res.fetchall()
        except sqlite3.Error as error:
            print('Fail', error)

    def print_avaliacao_by_id(self, id_aluno: int):
        lista = self.select_avaliacao_by_id_aluno(id_aluno)
        for i in lista:
            print(f"""\nId: {i[0]}\nData: {i[2]}\nSexo: {i[3]}\nAltura: {i[4]} metros\nPeso: {i[5]} kg\nFrequência Cardíaca: {i[6]} bpm\nPressão Arterial: {i[7]} (mmHg)""")

######################### AUTENTICAÇÃO ########################################
    # Autentica a senha
    def auth_pass(self, senha_entry: str, hash_senha: str):
        pswd_enc = senha_entry.encode('utf-8')
        if str(bcrypt.hashpw(pswd_enc, b'$2b$12$4f0MkkWy7dFBVqo9zaAuSu')) == hash_senha:
            return True
        else:
            return False

    def usuario_autenticado(self, email: str, senha_entry: str):
        try:
            sql = f"SELECT id, senha, nome FROM alunos WHERE email = '{email.strip().lower()}'"
            res = self.cursor.execute(sql)
            dados = res.fetchone()
            if dados == None:
                return self.email_error(email)
            self.id = int(dados[0])
            nome = str(dados[2])
            print(f"User: {nome}")
            hash_senha = str(dados[1])
            return self.auth_pass(senha_entry, hash_senha)
        except sqlite3.Error as error:
            print('Fail', error)

    def email_error(self, email):
        print(f"E-mail Inválido: {email}")
    
    def user_id(self):
        return self.id
    
    # SELECIONA ALUNO PELO ID
    def select_by_id(self, id_user: int):
        try:
            sql = f'SELECT * FROM alunos WHERE id = {id_user}'
            res = self.cursor.execute(sql)
            return res.fetchall()
        except sqlite3.Error as error:
            print('Fail', error)
        

############################### END ###########################################

#if __name__ == '__main__':
    #c = Connection('personal_database.db')

    #c.cadastra_aluno("Jackson Luís Agostinho", "(14) 99688-6035", "1976-07-01", "caramastres@gmail.com", "Ansomne619!", 1)
    #c.cadastra_aluno("Jackson Luís Agostinho", "(14) 99688-6035", "1976-07-01", "caramastres@yahoo.com.br", "Cthulhu215?", 1)
    #c.cadastra_aluno("Gracie Correa", "(14)99833-0448", "1984-05-30", "gracie-c@gmail.com", "30051984", 0)
    #c.cadastra_aluno("Pedro Pereira", "(11) 99876-5432", "1980-12-08", "pedro_pereira@hotmail.com", "AbCdEf1234", 0)

    #c.deleta_aluno_by_id(3)
    #c.deleta_aluno_by_email("pedro_pereira@hotmail.com")

    #c.print_all()
    #print(c.select_by_id(4))

    #c.cadastra_avaliacao(1,"masculino", 1.72, 75, 60, "120/75")
    #c.cadastra_avaliacao(1,"masculino", 1.73, 86, 80, "130/90")
    
    #c.print_avaliacao_by_id(4)
    
    #print(c.usuario_autenticado("caramastres@gmail.com", "Ansomne619!"))
    #print(c.usuario_autenticado("gracie-c@gmail.com", "30051984"))
    #print(c.usuario_autenticado("pedro_pereira@hotmail.com", "AbCdEf1234"))

    #c.close_db()
