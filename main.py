from burgos.mysql_handler import Mysql

database = Mysql({"host": "agenciaboz.com.br", "user": "python", "password": "SucessoZOP2022!", "database": "bapkasor_sistema"}, '')
database.connect()

loja = input("Loja: ")
login = f"{loja.split(' ')[-2].lower()+loja.split(' ')[-1]}@bapkasorvetes.com.br"
print(f"login: {login}")
password = f"Bapka{loja.split(' ')[-2].lower()+loja.split(' ')[-1]}2022!"
print(f"password: {password}")

database.run(f"""INSERT INTO mottu_token (loja, login, password) values ("{loja}", "{login}", "{password}");""")
print(f"{loja} signed into database")