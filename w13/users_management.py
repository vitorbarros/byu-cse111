import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify

api = Flask(__name__)

DATABASE_FILE = 'users_management.db'

"""API routes"""


@api.route('/users', methods=['POST'])
def post_user():
    if not user_create_validation(request.json):
        return jsonify({"message": "name, username and password  are required"}), 422

    connection = db_connection(DATABASE_FILE)

    user = {'name': request.json['name'], 'username': request.json['username'], 'password': request.json['password']}

    db_resp = create(connection, user)

    items = []
    for row in db_resp:
        items.append({
            'id': row[0],
            'name': row[1],
            'username': row[2],
            'password': row[3]
        })

    return jsonify(items[len(items) - 1]), 201


@api.route('/users', methods=['GET'])
def get_users():
    connection = db_connection(DATABASE_FILE)
    db_resp = retrieve(connection)

    items = []
    for row in db_resp:
        items.append({
            'id': row[0],
            'name': row[1],
            'username': row[2],
            'password': row[3]
        })

    return jsonify(items), 200


"""Application"""


def user_create_validation(json_request):
    if 'name' in json_request and json_request['name'] == "" \
            or 'username' in json_request and json_request['username'] == "" \
            or 'password' in json_request and json_request['password'] == "":
        return False

    return True


def db_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_users_tables(conn):
    try:
        if conn is not None:
            c = conn.cursor()

            sql = """CREATE TABLE IF NOT EXISTS users (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                name text NOT NULL,
                                username text NOT NULL,
                                password text NOT NULL
                            );"""

            c.execute(sql)
    except Error as e:
        print(e)


def create(conn, user):
    """create new user"""
    create_users_tables(conn)
    conn.execute("INSERT INTO users (name, username, password) values (?, ?, ?)",
                 (user['name'], user['username'], user['password']))
    conn.commit()

    return conn.execute("SELECT * FROM users WHERE username=?", (user['username'],))


def retrieve(conn):
    """retrieve all users"""
    return conn.execute("SELECT * FROM users")


def main():
    api.run()


if __name__ == "__main__":
    main()
