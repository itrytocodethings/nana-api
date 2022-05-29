import json
from app import app, db
from flask import render_template, redirect, jsonify, request
from app.util import hashpass, verifypass
from app.models import User, Note
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route('/api/register', methods=['POST'])
def register():
    """Register function receives username, email, password. Validates and inserts record into DB"""
    req = request.get_json()
    user = User.query.filter_by(username=req['username']).first() or User.query.filter_by(email=req['email']).first()
    if (req['username'] and req['email'] and req['password']) and user:
        resp = f"{req['username']} already taken." if user.username == req['username'] else f"{user.email} already registered."
        return jsonify(resp), 409
    new_user = User(username=req['username'], email=req['email'], password=hashpass(req['password']))
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize(), 200

@app.route('/api/login', methods=['POST'])
def generate_token():
    """Endpoint to generate a JWT auth token and log user in"""
    req = request.get_json()

    # verify username & password
    user = User.query.filter_by(username=req['username']).first()

    if user is None or not verifypass(req['password'], user.password):
        return jsonify({'message': 'Invalid username/password combination'}), 401
    
    # create a new token with user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({"token": access_token, "user_id": user.id})


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return '&#128175;'

