from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        current_time = datetime.now().time()
        greeting, image_filename = get_greeting(current_time)
        return render_template('index.html', greeting=greeting, user_name=user_name, image_filename=image_filename)

    return render_template('index.html')

def get_greeting(current_time):
    if datetime.strptime('06:00', '%H:%M').time() <= current_time < datetime.strptime('12:00', '%H:%M').time():
        return 'Good Morning', 'morning.jpg'
    elif datetime.strptime('12:00', '%H:%M').time() <= current_time < datetime.strptime('19:00', '%H:%M').time():
        return 'Good Afternoon', 'afternoon.jpg'
    elif datetime.strptime('19:00', '%H:%M').time() <= current_time <= datetime.strptime('23:59', '%H:%M').time():
        return 'Good Evening', 'evening.jpg'
    else:
        return 'Good Night', 'night.jpg'

if __name__ == '__main__':
    app.run(debug=True)
