from flask import Flask, request, jsonify
from models.diet import Diet

app = Flask(__name__)

diets = []
diet_id_control = 1


@app.route('/diets', methods=['POST'])
def create_diet():
    global diet_id_control

    # recupera as informações da requisição
    data = request.get_json()

    # armazena as informações da requisição na variavel new_diet que utiliza a classe Diet
    new_diet = Diet(id=diet_id_control, name=data.get('name'), description=data.get('description'), date=data.get('date'),
                    isHealthy=data.get('isHealthy'))

    diet_id_control += 1
    diets.append(new_diet)

    return jsonify({"message": "Nova dieta criada com sucesso!", "id": new_diet.id}), 201


@app.route('/diets', methods=['GET'])
def get_diets():
    diets_list = [diet.to_dict() for diet in diets]

    output = {
        "diets": diets_list,
        "total_diets": len(diets_list)
    }

    return output


if __name__ == '__main__':
    app.run(debug=True)
