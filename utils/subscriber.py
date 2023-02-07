from flask import Flask, request, jsonify
import json
import schedule
import time

app = Flask(__name__)

def add_user(user_id, plan, vip):
    subscriptions[user_id] = {
        "plan": plan,
        "vip": vip,
        "timestamp": time.time()
    }

    # Save the updated subscriptions to the JSON file
    with open('subscriptions.json', 'w') as f:
        json.dump(subscriptions, f)

def remove_user(user_id):
    if user_id in subscriptions:
        del subscriptions[user_id]

        # Save the updated subscriptions to the JSON file
        with open('subscriptions.json', 'w') as f:
            json.dump(subscriptions, f)
    else:
        print("User not found")

# Charger les informations sur les abonnements à partir d'un fichier JSON
with open('subscriptions.json', 'r') as f:
    subscriptions = json.load(f)

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # Récupérer les informations sur l'abonnement à partir de la requête
    data = request.get_json()
    user_id = data['user_id']
    plan = data['plan']
    vip = data['vip']
    
    # Ajouter l'abonnement à la liste des abonnements
    subscriptions[user_id] = {
        'plan': plan,
        'VIP' : vip,
        'timestamp': datetime.datetime.now().timestamp()

    }
    
    with open('subscriptions.json', 'w') as f:
        json.dump(subscriptions, f)
    
    return jsonify({'message': 'Successfully subscribed!'})

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    data = request.get_json()
    user_id = data['user_id']
    
    if user_id in subscriptions:
        del subscriptions[user_id]
        
        with open('subscriptions.json', 'w') as f:
            json.dump(subscriptions, f)
        
        return jsonify({'message': 'Successfully unsubscribed!'})
    else:
        return jsonify({'message': 'User is not subscribed!'})

import datetime

def reset_subscriptions():
    for user_id in subscriptions:
        subscriptions[user_id]['plan'] = 'free'
        subscriptions[user_id]['vip'] = 'False'

    with open('subscriptions.json', 'w') as f:
        json.dump(subscriptions, f)




