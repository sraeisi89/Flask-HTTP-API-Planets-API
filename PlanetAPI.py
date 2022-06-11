import flask
from flask import jsonify, render_template, abort
import requests

def get_planet_info(planet_name):
    response = requests.get(f'https://api.le-systeme-solaire.net/rest/bodies/{planet_name}')
    planet_info = response.json()
    list = []
    if planet_info["isPlanet"]:
        list.append(planet_info["mass"])
        list.append(planet_info["vol"])
        list.append(len(planet_info["moons"]))
    else:
        list.append(planet_info["mass"])
        list.append(planet_info["vol"])
        list.append("No moon")
    return list

def unique_requests(requests_list):
    unique_list = []
    for x in requests_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list




app = flask.Flask(__name__)
planet_requests = []

@app.errorhandler(404)
def planet_does_not_exists(e):
    return jsonify(error=str(e)), 404


@app.route("/planets/<name>")
def planets(name):
    planet_requests.append(name)
    planet_info = get_planet_info(name)
    if len(planet_info) > 0:
        response = {
            "mass": f"{planet_info[0]['massValue']} * 10^{planet_info[0]['massExponent']} kg",
            "volume": f"{planet_info[1]['volValue']} * 10^{planet_info[1]['volExponent']} km3",
            "moons": planet_info[2]
        }
        return jsonify(response)
    else:
        abort(404, description="PLANET DOES NOT EXISTS")


@app.route("/usage")
def usage():
    planets_requested = unique_requests(planet_requests)
    number_of_requests = []
    for name in planets_requested:
        number_of_requests.append(planet_requests.count(name))
    return render_template("index.html", planets_request=planets_requested, number_of_requests=number_of_requests)


if __name__ == "__main__":
    app.run(debug=True)



