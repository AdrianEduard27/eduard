from flask import Flask, request, render_template


app = Flask(__name__)


@app.route ('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        ip_address = request.remote_addr
        return render_template('welcome.html', name=name, ip_address=ip_address)
    return render_template ('index.html')
if __name__ == "__main__":
    app.run (host='0.0.0.0', port=5050, debug = True)


