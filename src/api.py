from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from models.models import User, db
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('routes_auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        password = data['password']
        password_hash = generate_password_hash(password)
        new_user = User(name=name, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return render_template('home.html', message='Пользователь успешно зарегистрирован')
    return render_template('register.html')



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return render_template('home.html', message='Вы успешно вошли в систему')
        return render_template('home.html', message='Ошибка входа')
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('home.html', message='Вы успешно вышли из системы')


@auth.route('/users', methods=['GET'])
@login_required
def get_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)


@auth.route('/users/add', methods=['GET', 'POST'])
@login_required
def add_user():
    if request.method == 'POST':
        data = request.json
        name = data['name']
        email = data['email']
        password = data['password']
        password_hash = generate_password_hash(password)
        new_user = User(name=name, email=email, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'Пользователь успешно добавлен'})
    return render_template('add_user.html')


@auth.route('/users/<int:id>/update', methods=['GET', 'POST'])
@login_required
def update_user(id):
    user = User.query.get(id)
    if request.method == 'POST':
        data = request.form
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        if 'password' in data and data['password']:
            user.password_hash = generate_password_hash(data['password'])
        db.session.commit()
        return redirect(url_for('routes_auth.get_users'))
    return render_template('update_user.html', user=user)

@auth.route('/users/<int:id>/delete', methods=['POST'])
@login_required
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'Пользователь успешно удален'})

