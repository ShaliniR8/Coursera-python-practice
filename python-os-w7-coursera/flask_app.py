from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('front.html')

@app.route('/report_errors')
def error_report():
    return render_template('report_errors.html')

@app.route('/user_stats')
def user_stats():
    return render_template('report_users.html')

if __name__ == '__main__':
    app.run()