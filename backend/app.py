import os
from flask import Flask, send_from_directory
import openpyxl
from datetime import (
   datetime,
)
app = Flask(__name__)


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


# Pasta frontend (HTML, JS)
FRONTEND_DIR = os.path.join(BASE_DIR, "FrontEnd")

#Pasta static (CSS)
STATIC_DIR= os.path.join(BASE_DIR, "static")

DB_DIR = os.path.join (os.path.dirname(__file__), "..", "db")
EXCEL_FILE = os.path.join (DB_DIR, "clientes.xlsx")

COLUMNS = [
   "ID",
   "Nome",
   "CPF",
   "Email",
   "Telefone",
   "Endereço",
   "Observações",
   "Data Cadastro"

]

def init_excel():
   if not os.path.exists(DB_DIR):
      os.makedirs(DB_DIR)


   if not os.path.exists(EXCEL_FILE):
      workbook = openpyxl.Workbook()
      sheet = workbook.active
      sheet.title = "Clientes"
      sheet.append(COLUMNS)
      workbook.save(EXCEL_FILE)


app = Flask(__name__, static_folder=STATIC_DIR, static_url_path="/" + STATIC_DIR)

@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/consulta")
def consulta_page():
    return send_from_directory(FRONTEND_DIR, "consulta.html")

@app.route("/alterar")
def alterar_page():
 return send_from_directory (FRONTEND_DIR, "alterar.html")

@app.route("/assets/<path:filename>")
def assets(filname) : 
   return send_from_directory("../frontend/assets", filname)

@app.route("/cadastrar", methods=["POST"])
def cadastrar_cliente():


   try:
      data = request.json


      required_fields = ["nome", "cpf", "email", "telefone", "endereço"]
      if not all(field in data and data[field] in required_field):
         return(
            jsonify(
               {
                  "status": "error",
                  "message": "Todos os campos obrigatórios devem ser preenchidos.",
               }
            ),
            400,
         )
      workbook = openpyxl.load_workbook(EXCEL_FILE)
      sheet = workbook.active

      last_id = 0 
      if sheet.max_row > 1:
         last_id = sheet.cell(row=sheet.max_row, column=1).value or 0 
         new_id = last_id + 1 

if __name__ == "__main__":
    print("BASE_DIR", BASE_DIR)
    print("FRONTEND_DIR", FRONTEND_DIR)
    print("STATIC_DIR", STATIC_DIR)
    init_excel()
    app.run(debug=True)
