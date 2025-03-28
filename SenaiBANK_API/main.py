from flask import Flask, request, jsonify
from flask_cors import CORS
from jwt import encode, decode
from datetime import datetime

secret = open("secret.config").read()

api = Flask(__name__)
CORS(api)

users = []
user1 = {
    "id": 1,
    "name": "Douglas",
    "login": "douglas",
    "password": "123456",
    "balance": 10000,
    "token": ""
}
users.append(user1)

@api.route("/users/login", methods=["POST"])
def login():
    data = request.get_json()
    if "login" not in data: 
        return jsonify({"error": "Login ou senha inválidos"}), 400
    if "senha" not in data: 
        return jsonify({"error": "Login ou senha inválidos"}), 400

    for user in users:
        if user["login"] == data["login"] and user["password"] == data["senha"]:
            tokenData = {
                "userID": user["id"],
                "userName": user["name"],
                "date": datetime.now()
            }
            user["token"] = encode(tokenData, secret, algorithm="HS256")

            responseData = {
                "userID": user["id"],
                "userName": user["name"],
                "jwt_token": user["token"]
            }
            return jsonify(responseData), 200

    return jsonify({"error": "Login ou senha inválidos"}), 401

@api.route("/users/authorize", methods=["POST"])
def authorize():
    data = request.get_json()
    if "jwt_token" not in data: 
        return jsonify({"error": "token invalido"}), 401

    for user in users:
        if user["token"] == data["jwt_token"]:
            token = decode(data["jwt_token"], secret, algorithm="HS256")
            if token["userID"] == user["id"]:
                return jsonify({"status": "success"}), 200

    return jsonify({"error": "token invalido"}), 401

@api.route("/users/balance", methods=["GET"])
def getUserBalance():
    data = request.get_json()
    if "jwt_token" not in data: 
        return jsonify({"error": "usuario não autorizado"}), 401

    id = decode(data["jwt_token"], secret, algorithm="HS256")["userID"]
    for user in users:
        if user["id"] == id: 
            return jsonify({"balance": user["balance"]}), 200

    return jsonify({"error": "usuario não encontrado"}), 404