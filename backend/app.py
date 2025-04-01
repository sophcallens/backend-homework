import pathlib as pl

import numpy as np
import pandas as pd

from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

data = pl.Path(__file__).parent.absolute() / 'data'

# Charger les données CSV
associations_df = pd.read_csv(data / 'associations_etudiantes.csv')
evenements_df = pd.read_csv(data / 'evenements_associations.csv')

## Vous devez ajouter les routes ici : 

# Vérifier si le serveur est actif
@app.route('/api/alive', methods=['GET'])
def check_alive():
    return jsonify({"message": "Alive"}), 200

# Liste de toutes les associations
@app.route('/api/associations', methods=['GET'])
def list_associations():
    return jsonify(associations_df['id'].tolist()), 200

# Détails d'une association
@app.route('/api/association/<int:id>', methods=['GET'])
def get_association(id):
    association = associations_df[associations_df['id'] == id].to_dict(orient='records')
    if not association:
        return jsonify({"error": "Association not found"}), 404
    return jsonify(association[0]), 200

# Liste de tous les événements
@app.route('/api/evenements', methods=['GET'])
def list_events():
    return jsonify(evenements_df['id'].tolist()), 200

# Détails d'un événement
@app.route('/api/evenement/<int:id>', methods=['GET'])
def get_event(id):
    event = evenements_df[evenements_df['id'] == id].to_dict(orient='records')
    if not event:
        return jsonify({"error": "Event not found"}), 404
    return jsonify(event[0]), 200

# Liste des événements d'une association
@app.route('/api/association/<int:id>/evenements', methods=['GET'])
def list_events_by_association(id):
    assoc_events = evenements_df[evenements_df['association_id'] == id].to_dict(orient='records')
    return jsonify(assoc_events), 200



if __name__ == '__main__':
    app.run(debug=False)
