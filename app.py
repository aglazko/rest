from flask import Flask, jsonify, request, Response, json
from rest.test import validAnimalObject

app = Flask(__name__)
print(__name__)

animals = [
    {
        'id': 234,
        'center_id': 90,
        'name': 'zozo',
        'age': 3,
        'species': 'cat',
        'price': 560
    },
{
        'id': 235,
        'center_id': 90,
        'name': 'zo',
        'age': 3,
        'species': 'ct',
        'price': 56
    },
{
        'id': 236,
        'center_id': 96,
        'name': 'zu',
        'age': 3,
        'species': 'cat',
        'price': 590
    },
{
        'id': 237,
        'center_id': 90,
        'name': 'zl',
        'age': 3,
        'species': 'c',
        'price': 50
    }
]


@app.route('/animals')
def get_animals():
    return jsonify({'animals': animals})


@app.route('/animals', methods=['POST'])
def add_animal():
    request_data = request.get_json()
    if (validAnimalObject(request_data)):
        new_animal = {
            "id": request_data["id"],
            "center_id": request_data["center_id"],
            "name": request_data["name"],
            "age": request_data["age"],
            "species": request_data["species"],
            "price": request_data["price"]
        }
        animals.insert(0, new_animal)
        response = Response("", 201, mimetype='application/json')
        response.headers['Location'] = '/animals/' + str(new_animal['id'])
        return response
    else:
        invalidAnimalObjectErrorMsg = {
            "error": "Invalid animal object passed in request",
            "helpString": "Data passed in similar to this: { 'id': 237, 'center_id': 90, 'name': 'zl', 'age': 3,"
                          "'species': 'c','price': 50"
        }
        response = Response(json.dumps(invalidAnimalObjectErrorMsg), status=400, mimetype='application/json')
        return response


@app.route('/animals/<int:id>')
def get_animal_by_id(id):
    return_value = {}
    for animal in animals:
        if animal["id"] == id:
            return_value = animal
    return jsonify(return_value)


@app.route('/animals/<int:id>', methods=['PUT'])
def replace_animals(id):
    request_data = request.get_json()
    new_animal = {
        "id": id,
        "center_id": request_data["center_id"],
        "name": request_data["name"],
        "age": request_data["age"],
        "species": request_data["species"],
        "price": request_data["price"]
    }
    for animal in animals:
        currentid = animal["id"]
        if currentid == id:
            animal = new_animal
    response = Response("", status=204)


app.run(port=5000)
