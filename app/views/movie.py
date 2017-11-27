from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.forms import MovieForm
from app.models import Movies

movie = Blueprint('movie', __name__)


@movie.route('/info/<int:movie_id>', methods=['GET', 'POST'])
def movie_info(movie_id):
    return render_template('movie/movie_info.html',movie_id=movie_id)
