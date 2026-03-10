import os
from flask import Flask, send_from_directory

# Caminho base do projeto (uma pasta acima do backend)
BASE_DIR = os.path.abspaht(os.path.join(os.path.dirname(__file__), ".."))

# Pasta frontend (HTML e JS)
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

# Pasta static (CSS)
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, static_folder=STATIC_DIR,static_url_path="/"+ STATIC_DIR)


# ====================================
# ROTA PRINCIPAL (HTML)



@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR,"index.html")


#Página de Consulta
@app.route("/consulta")
def consulta_page():
    return send_from_directory(FRONTEND_DIR, "consulta.html")


#Página de Alteração 
@app.route("/alterar")
def alterar_page():
    return send_from_directory(FRONTEND_DIR, "alterar.html")


if __name__ == "_main_":
    print("BASE_DIR:", BASE_DIR)
    print("FRONTEND_DIR:", FRONTEND_DIR)
    print("STATIC_DIR:", STATIC_DIR)
    app.run(debug=True)



 
app.run()