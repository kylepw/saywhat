from .twitter import fetch_tweets, is_valid_account
from flask import Blueprint, flash, render_template, request
from tweepy import TweepError

main = Blueprint('views', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    tweets = []
    if request.method == 'POST':
        error = None
        screen_name = request.form.get('screen_name')
        query = request.form.get('query')

        if not screen_name or not is_valid_account(screen_name):
            error = f"Invalid screen name {screen_name}."
        if not query:
            error = 'Query string required.'

        if error:
            flash(error)
            return render_template('index.html')

        try:
            tweets = fetch_tweets(screen_name=screen_name, query=query, limit=10)
        except TweepError:
            flash('Rate limit exceeded. Please wait 15 minutes.')

    print(tweets)

    return render_template('index.html', tweets=tweets)

@main.route('/search', methods=['GET'])
def search():
    return 'search'
