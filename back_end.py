from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine, func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\WorkSpace\cosmetique_app\database.db'
db = SQLAlchemy(app)


class Client(db.Model):
  n_client = db.Column(db.Integer, primary_key=True)
  nom_client = db.Column(db.String(100), nullable=False)
  add_postale = db.Column(db.String(100), nullable=False)
  add_email = db.Column(db.String(100), nullable=False)
  tel = db.Column(db.String(100), nullable=False)
  facebook = db.Column(db.String(100))
  instagram = db.Column(db.String(100))

class Commande(db.Model):
  n_commande = db.Column(db.Integer, primary_key=True)
  date_commande = db.Column(db.DateTime, nullable=False)

class Livraison(db.Model):
  n_livraison = db.Column(db.Integer, primary_key=True)
  mode = db.Column(db.String(100), nullable=False)
  frais_livraison = db.Column(db.Float, nullable=False)
  date_livraison = db.Column(db.DateTime, nullable=False)

class Product(db.Model):
  n_product = db.Column(db.Integer, primary_key=True)
  prix_unitaire = db.Column(db.Float, nullable=False)

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
  n_client = db.session.query(func.max(Client.n_client)).scalar()+1
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

@app.route('/api/create_order', methods=['POST'])
def create_order():
  data = request.get_json()
  new_order = Commande(
    n_commande=data['n_commande'],
    date_commande=data['date_commande']
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
  order.date_commande = data['date_commande']
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