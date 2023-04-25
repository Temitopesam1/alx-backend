#!/usr/bin/python3
""" Script of a flask framework project """

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello() -> str:
    """ A function to return HTML template  """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
# #!/usr/bin/env python3
# """A Basic Flask app.
# """
# from flask import Flask, render_template


# app = Flask(__name__)
# app.url_map.strict_slashes = False


# @app.route('/')
# def get_index() -> str:
#     """The home/index page.
#     """
#     return render_template('0-index.html')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
