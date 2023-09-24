# Flask

## Installation

```bash
poetry add Flask
```

## Usage

```py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

```bash
flask run
```

## References

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
