from flask import Flask

app = Flask(__name__)

@app.get('/')
def index():

  return {'hello': 'World'}

if __name__ == "__main__":
  app.run()