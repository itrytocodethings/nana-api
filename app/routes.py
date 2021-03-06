import json
from webbrowser import get
from app import app, db
from flask import render_template, redirect, jsonify, request
from app.util import hashpass, verifypass
from app.models import User, Note
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

@app.route('/api/register', methods=['POST'])
def register():
    """Register function receives username, email, password. Validates and inserts record into DB"""
    req = request.get_json()

    # does user exist? checking by email or username
    user = User.query.filter_by(username=req['username'].lower()).first() or User.query.filter_by(email=req['email'].lower()).first()
    if (req['username'] and req['email'] and req['password']) and user:
        resp = f"{req['username'].title()} already taken." if user.username == req['username'].lower() else f"{user.email} already registered."
        return jsonify(resp), 409

    new_user = User(username=req['username'].lower(), email=req['email'].lower(), password=hashpass(req['password']))
    db.session.add(new_user)
    db.session.commit()
    return new_user.serialize(), 200

@app.route('/api/login', methods=['POST'])
def generate_token():
    """Endpoint to generate a JWT auth token and log user in"""
    req = request.get_json()

    # verify username & password
    user = User.query.filter_by(username=req['username'].lower()).first()

    if user is None or not verifypass(req['password'], user.password):
        return jsonify({'message': 'Invalid username/password combination'}), 401
    
    # create a new token with user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({"token": access_token, "user_id": user.id, "user": user.serialize()}), 200

@app.route('/api/note', methods=['POST'])
@jwt_required()
def note():
    current_user_id = get_jwt_identity() #get user id from token
    user = User.query.get(current_user_id)
    req = request.get_json()
    new_note = Note(note_title=req['note_title'], note_body=req['note_body'], plain_text=req['plain_text'], owner_id=user.id)
    db.session.add(new_note)
    db.session.commit()
    # returns the current users updated list of notes.
    return jsonify(user.serialize()['notes'])

@app.route('/api/note/<int:note_id>', methods=['PUT','DELETE'])
@jwt_required()
def handle_note(note_id):
    if request.method == 'PUT':
        req = request.get_json()
        note = Note.query.get(note_id)
        user = User.query.get(get_jwt_identity()) #current user
        for key in req.keys():
            #sets a named attribute on instance of Note. Could be one or two attributes of the note. Either or. Title or Body.
            setattr(note, key, req[key]) 
            db.session.commit()
        return jsonify(user.serialize()['notes'])

    if request.method == 'DELETE':
        # get current logged in user, get current note, delte note from db and return updated array of notes.
        user = User.query.get(get_jwt_identity())
        note = Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        return jsonify(user.serialize()['notes'])


@app.route('/api/u', methods=['GET'])
@jwt_required()
def get_user():
    user = User.query.get(get_jwt_identity())
    return jsonify(user.serialize())

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return '&#128175;'

