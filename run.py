import os
from flask import Flask
from app import app


if __name__ == '__main__':
    app.secret_key = "andela"
    app.run(debug=True, port=5000)

