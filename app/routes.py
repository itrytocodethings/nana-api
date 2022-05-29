from app import app, db
from flask import render_template, redirect, jsonify, request
from app.util import hashpass, verifypass
from app.models import User, Note


@app.route('/api/register', methods=['POST'])
def register():
    """Register function receives username, email, password. Validates and inserts record into DB"""
    if request.method == 'POST':
        req = request.get_json()
        user = User.query.filter_by(username=req['username']).first() or User.query.filter_by(email=req['email']).first()
        if (req['username'] and req['email'] and req['password']) and user:
            resp = f"{req['username']} already taken." if user.username == req['username'] else f"{user.email} already registered."
            return jsonify(resp), 422
        new_user = User(username=req['username'], email=req['email'], password=hashpass(req['password']))
        db.session.add(new_user)
        db.session.commit()
    return new_user.serialize(), 200

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return '&#128175;'

