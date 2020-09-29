from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_swagger_ui import get_swaggerui_blueprint

app = FlaskAPI(__name__)


def solve_word(word):
    counts = {}
    visited_chars = []

    for char in word:
        if char not in visited_chars:
            num_occurrences = str(word.count(char))
            if num_occurrences in counts:
                return False
            else:
                counts[num_occurrences] = char
                visited_chars.append(char)

    for i in range(len(counts)):
        if str(i+1) not in counts:
            return False

    return True


@app.route("/pyramid", methods=['POST'])
def is_pyramid():
    print('request received')
    if request.method == 'POST':

        try:
            word = request.get_data().decode('utf-8')

            if len(word) == 0:
                return 'EMPTY STRING', status.HTTP_200_OK

            is_pyramid = solve_word(word)
        except Exception as ex:
            print('Bad Request: ' + ex)
            return "Bad Request", status.HTTP_400_BAD_REQUEST

        return str(is_pyramid), status.HTTP_200_OK

    return "Method Not Allowed", status.HTTP_405_METHOD_NOT_ALLOWED


# Swagger functionality
SWAGGER_URL = '/swagger'
swagger_blueprint = get_swaggerui_blueprint(SWAGGER_URL,
                                            '/static/swagger.yml',
                                            config={'app_name':
                                                    'Fetch Rewards API'})

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(port=8888, debug=True)
