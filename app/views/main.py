from flask import Blueprint, render_template, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app.forms import MovieForm
from app.models import Movies

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def index():
    form = MovieForm
    movie = Movies.query.filter()
    return render_template('main/index.html', form=form, posts=movie)


@main.route('/jiami/')
def jiami():
    return generate_password_hash('123456')


@main.route('/check/<password>')
def check(password):
    if check_password_hash(
            'pbkdf2:sha256:50000$Tx7XTa0Q$13b274957198b1e5950f0fb065844c427167f2995b0cf4e80c1ff19177520727',
            password):
        return '密码正确'
    else:
        return '密码错误'


@main.route('/generate_token/')
def generate_token():
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=3600)
    return s.dumps({'id': 250})


@main.route('/activate/<token>')
def activate(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except:
        return 'token有误'
    return str(data.get('id'))
