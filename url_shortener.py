from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)
url_mapping = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@app.route('/', methods=['GET', 'POST'])
def shorten_url():
    if request.method == 'POST':
        original_url = request.form['url']
        short_code = generate_short_code()
        url_mapping[short_code] = original_url
        return f"Shortened URL: {request.host}/{short_code}"
    return '''
        <form method="post">
            <input type="text" name="url" placeholder="Enter URL" required>
            <input type="submit" value="Shorten">
        </form>
    '''

@app.route('/<short_code>')
def redirect_to_original(short_code):
    if short_code in url_mapping:
        original_url = url_mapping[short_code]
        return redirect(original_url)
    return "Short URL not found."

if __name__ == '__main__':
    app.run(debug=True)
