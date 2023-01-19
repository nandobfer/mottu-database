from burgos.mysql_handler import Mysql

database = Mysql({"host": "agenciaboz.com.br", "user": "python", "password": "SucessoZOP2022!", "database": "bapkasor_sistema"}, '')
database.connect()

loja = input("Loja: ")
login = input("Email de login: ")
password = input("Senha: ")

database.run(f"""INSERT INTO mottu_token (loja, login, password) values ("{loja}", "{login}", "{password}");""")
print(f"{loja} signed into database")