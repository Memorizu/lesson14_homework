from flask import Blueprint, jsonify

from bp_main.utils import *

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.get('/')
def main_page():
    return "Главная страница"


@main_blueprint.get('/movie/<title>')
def page_by_movie(title):
    query = search_by_title(title)
    return jsonify(query)


@main_blueprint.get('/movie/<int:first_year>/to/<int:second_year>')
def page_searching_by_years(first_year, second_year):
    query = search_by_release_year(first_year, second_year)
    return jsonify(query)


@main_blueprint.get('/rating/<rating>')
def page_searching_by_rating(rating):
    data = search_by_rating(rating)
    return jsonify(data)


@main_blueprint.get('/genre/<genre>')
def page_by_genre(genre):
    data = search_by_genre(genre)
    return jsonify(data)
