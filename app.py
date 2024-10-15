#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Welcome to Superheroes GET API</h1>'

@app.route('/heroes')
def heroes():

    heroes = [hero.to_dict() for hero in Hero.query.all()]

    response = make_response(
        heroes,
        200
    )

    return response


@app.route('/heroes/<int:id>', methods=['GET'])
def hero_by_id(id):
    hero = Hero.query.filter(Hero.id == id).first()

    if hero == None:
        response_body = {
            "error": "Hero not found."
        }
        response = make_response(response_body, 404)

        return response

    else:
        if request.method == 'GET':

            hero_dict= hero.to_dict()

            response = make_response(
                hero_dict,
                200
            )

        return response
    


@app.route('/powers')
def powers():

    powers = [power.to_dict() for power in Power.query.all()]

    response = make_response(
        powers,
        200
    )

    return response


@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def power_by_id(id):
    power = Power.query.filter_by(id=id).first()
    
    if power == None:
        response_body = {
            "error": "Power not found"
        }
        response = make_response(response_body, 404)

        return response

    else:
        if request.method == 'GET':
            power_dict = power.to_dict()

            response = make_response(
                power_dict,
                200
            )

            return response

        elif request.method == 'PATCH':  

            description = request.form.get('description') 
            if len(description) < 20:
                response_body = {
                    "error": "Validation errors"
                }
                response = make_response(response_body, 404)

                return response
            else: 
                for attr in request.form:
                    setattr(power, attr, request.form.get(attr))

                    db.session.add(power)
                    db.session.commit()

                    power_dict = power.to_dict()

                response = make_response(
                    power_dict,
                    200
                )
                return response
        
        

@app.route('/hero_powers', methods=['GET','POST'])
def heropower():
    if request.method == 'GET':
        hero_powers = []
        for hp in HeroPower.query.all():
            hp_dict = hp.to_dict()
            hero_powers.append(hp_dict)

        response = make_response(
            hero_powers,
            200
        )

        return response
    elif request.method == 'POST':
        strength = request.form.get('strength')
        if strength in ['Strong', 'Weak', 'Average']:
            new_heropower = HeroPower(
                strength = request.form.get("strength"),
                power_id = request.form.get("power_id"),
                hero_id = request.form.get("hero_id"),
            )
            
            db.session.add(new_heropower)
            db.session.commit()

            hp_dict = new_heropower.to_dict()

            response = make_response(
                hp_dict,
                201
            )

            return response
        else:
            response_body = {
                "errors": "Validation errors"
            }
            response = make_response(response_body, 404)

            return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)