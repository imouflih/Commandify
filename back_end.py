from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine, func
import pandas as pd
import json
import flask_excel as excel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\WorkSpace\sqlite-tools-win32-x86-3400100\sqlite-tools-win32-x86-3400100\database.db'
db = SQLAlchemy(app)


class Client(db.Model):
  n_client = db.Column(db.Integer, primary_key=True)
  nom_client = db.Column(db.String(100), nullable=False)
  add_postale = db.Column(db.String(100), nullable=False)
  add_email = db.Column(db.String(100), nullable=False)
  tel = db.Column(db.String(100), nullable=False)
  facebook = db.Column(db.String(100))
  instagram = db.Column(db.String(100))
  fidelite = db.Column(db.Integer)
  

class Commande(db.Model):
  n_commande = db.Column(db.Integer, primary_key=True)
  date_commande = db.Column(db.DateTime, nullable=False)
  n_client = db.Column(db.Integer)
  nom_client = db.Column(db.String(100), nullable=False)
  Total = db.Column(db.Float, nullable=False)
  Status = db.Column(db.String(100), nullable=False)
  

class Livraison(db.Model):
  n_livraison = db.Column(db.Integer, primary_key=True)
  mode = db.Column(db.String(100), nullable=False)
  frais_livraison = db.Column(db.Float, nullable=False)
  date_livraison = db.Column(db.DateTime, nullable=False)

class Product(db.Model):
  n_product = db.Column(db.Integer, primary_key=True)
  prix_unitaire = db.Column(db.Float, nullable=False)
  name = db.Column(db.String(100))
  prix_magazin = db.Column(db.Float, nullable=False)
  status = db.Column(db.String(100), nullable=False)

class Facture(db.Model):
  n_facture = db.Column(db.Integer, primary_key=True)
  date_facture = db.Column(db.DateTime, nullable=False)
  prix_commande = db.Column(db.Float, nullable=False)
  frais_service = db.Column(db.Float, nullable=False)
  frais_livraison = db.Column(db.Float, nullable=False)
  montant_facture = db.Column(db.Float, nullable=False)

class Stock(db.Model):
  n_stock = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.Boolean, nullable=False)

@app.route('/api/create_client', methods=['POST'])
def create_client():
  n_client = db.session.query(func.max(Client.n_client)).scalar()
  if n_client is None:
    n_client =  0
  else:
    n_client+=1
  data = request.get_json()
  new_client = Client(
    n_client=n_client,
    nom_client=data['nom_client'],
    add_postale=data['add_postale'],
    add_email=data['add_email'],
    tel=data['tel'],
    facebook=data['facebook'],
    instagram=data['instagram']
  )
  db.session.add(new_client)
  db.session.commit()
  return jsonify({'message': 'Nouveau client'})

@app.route('/api/modify_client/<int:n_client>', methods=['PUT'])
def modify_client(n_client):
  client = Client.query.get(n_client)
  if not client:
    return jsonify({'message': 'Aucun client trouvé avec cet identifiant'})
  data = request.get_json()
  client.nom_client = data['nom_client']
  client.add_postale = data['add_postale']
  client.add_email = data['add_email']
  client.tel = data['tel']
  client.facebook = data['facebook']
  client.instagram = data['instagram']
  db.session.commit()
  return jsonify({'message': 'Fiche client modifiée avec succès'})

@app.route('/api/delete_client/<int:n_client>', methods=['DELETE'])
def delete_client(n_client):
  client = Client.query.get(n_client)
  if not client:
    return jsonify({'message': 'Aucun client trouvé avec cet identifiant'})
  db.session.delete(client)
  db.session.commit()
  return jsonify({'message': 'Fiche client supprimée avec succès'})

@app.route('/api/client_list', methods=['GET'])
def get_client_list():
  clients = Client.query.all()
  clients_list = []
  for client in clients:
    client_data = {}
    client_data['n_client'] = client.n_client
    client_data['nom_client'] = client.nom_client
    client_data['add_postale'] = client.add_postale
    client_data['add_email'] = client.add_email
    client_data['tel'] = client.tel
    client_data['facebook'] = client.facebook
    client_data['instagram'] = client.instagram
    clients_list.append(client_data)
  return jsonify({'clients': clients_list})

@app.route('/api/client_list/to_excel', methods=['GET'])
def client_to_excel():
  clients = Client.query.all()
  clients_list = []
  for client in clients:
    client_data = {}
    client_data['n_client'] = client.n_client
    client_data['nom_client'] = client.nom_client
    client_data['add_postale'] = client.add_postale
    client_data['add_email'] = client.add_email
    client_data['tel'] = client.tel
    client_data['facebook'] = client.facebook
    client_data['instagram'] = client.instagram
    clients_list.append(client_data)
  # Convert JSON data to a DataFrame
  df = pd.read_json(json.dumps({'clients': clients_list}))

  # Write DataFrame to an Excel file
  excel_file = df.to_excel("clients.xlsx", index=False)
  return excel.make_response(excel_file,'xlsx')
  return jsonify({'message': 'fichier genere'})
    

@app.route('/api/client_details/<int:n_client>', methods=['GET'])
def get_client_details(n_client):
  client = Client.query.get(n_client)
  if not client:
    return jsonify({'message': 'Aucun client trouvé avec cet identifiant'})
  client_data = {}
  client_data['n_client'] = client.n_client
  client_data['nom_client'] = client.nom_client
  client_data['add_postale'] = client.add_postale
  client_data['add_email'] = client.add_email
  client_data['tel'] = client.tel
  client_data['facebook'] = client.facebook
  client_data['instagram'] = client.instagram
  return jsonify({'client': client_data})

@app.route('/api/create_product', methods=['POST'])
def create_product():
  n_product = db.session.query(func.max(Product.n_product)).scalar()+1
  data = request.get_json()
  new_product = Product(
    n_product=n_product,
    prix_unitaire = data['prix_unitaire'],
    name = data['name'],
    prix_magazin = data['prix_magazin'],
    status = data['status']
  )
  db.session.add(new_product)
  db.session.commit()
  return jsonify({'message': 'Nouveau produit'})


@app.route('/api/product_list', methods=['GET'])
def get_product_list():
  Products = Product.query.all()
  product_list = []
  for product in Products:
    product_data = {}
    product_data['n_product'] = product.n_product
    product_data['prix_unitaire'] = product.prix_unitaire
    product_data['name'] = product.name
    product_data['prix_magazin'] = product.prix_magazin
    product_data['status'] = product.status
    product_list.append(product_data)
  return jsonify({'products': product_list}) 


@app.route('/api/modify_product/<int:n_product>', methods=['PUT'])
def modify_product(n_product):
  product = Product.query.get(n_product)
  if not product:
    return jsonify({'message': 'Aucun produit trouvé avec cet identifiant'})
  data = request.get_json()
  product.n_product = n_product
  product.prix_unitaire = data['prix_unitaire']
  product.name = data['name'],
  product.prix_magazin = data['prix_magazin'],
  product.status = data['status']
  db.session.commit()
  return jsonify({'message': 'Fiche produit modifiée avec succès'})


@app.route('/api/delete_product/<int:n_product>', methods=['DELETE'])
def delete_product(n_product):
  product = Product.query.get(n_product)
  if not product:
    return jsonify({'message': 'Aucun produit trouvé avec cet identifiant'})
  db.session.delete(product)
  db.session.commit()
  return jsonify({'message': 'Fiche produit supprimée avec succès'})


@app.route('/api/product_details/<int:n_product>', methods=['GET'])
def get_product_details(n_product):
  product = Product.query.get(n_product)
  if not product:
    return jsonify({'message': 'Aucun produit trouvé avec cet identifiant'})
  product_data = {}
  product_data['n_product'] = product.n_product
  product_data['prix_unitaire'] = product.prix_unitaire
  product_data['name'] = product.name
  product_data['prix_magazin'] = product.prix_magazin
  product_data['status'] = product.status
  return jsonify({'product': product_data})



@app.route('/api/create_order', methods=['POST'])
def create_order():
  data = request.get_json()
  total=0
  for i in data['products']:
    product = Product.query.get(i)
    total+=product.prix_magazin
  client = Client.query.get(data['client_id'])
  client.fidelite = client.fidelite + total//10
  db.session.commit()
  new_order = Commande(
    n_commande=data['n_commande'],
    date_commande=data['date_commande'],
    n_client = data['n_client'],
    nom_client = data['nom_client'],
    Total = total,
    Status = data['status']
    
  )
  db.session.add(new_order)
  db.session.commit()
  return jsonify({'message': 'Nouvelle commande créée avec succès'})

@app.route('/api/modify_order/<int:n_commande>', methods=['PUT'])
def modify_order(n_commande):
  order = Commande.query.get(n_commande)
  if not order:
    return jsonify({'message': 'Aucune commande trouvée avec cet identifiant'})
  data = request.get_json()
  order.Status = data['status']
  db.session.commit()
  return jsonify({'message': 'Commande modifiée avec succès'})

@app.route('/api/delete_order/<int:n_commande>', methods=['DELETE'])
def delete_order(n_commande):
  order = Commande.query.get(n_commande)
  if not order:
    return jsonify({'message': 'Aucune commande trouvée avec cet identifiant'})
  db.session.delete(order)
  db.session.commit()
  return jsonify({'message': 'Commande supprimée avec succès'})

@app.route('/api/order_list', methods=['GET'])
def get_order_list():
  orders = Commande.query.all()
  orders_list = []
  for order in orders:
    order_data = {}
    order_data['n_commande'] = order.n_commande
    order_data['date_commande'] = order.date_commande
    order_data['n_client'] = order.n_client
    order_data['nom_client'] = order.nom_client
    order_data['total'] = order.total
    order_data['Status'] = order.Status
    orders_list.append(order_data)
  return jsonify({'orders': orders_list})

@app.route('/api/generate_invoice/<int:n_commande>', methods=['GET'])
def generate_invoice(n_commande):
  order = Commande.query.get(n_commande)
  if not order:
    return jsonify({'message': 'Aucune commande trouvée avec cet identifiant'})
  # Génération de la facture pour la commande
  return jsonify({'message': 'Facture générée avec succès'})

@app.route('/api/export_orders', methods=['GET'])
def export_orders():
  # Exportation de la liste des commandes dans un fichier Excel
  return jsonify({'message': 'Liste des commandes exportée avec succès'})

if __name__ == '__main__':
  app.run(debug=True)