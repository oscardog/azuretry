from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    print("hello")
    return 'success', 200

@app.route('/webhook', methods = ['GET','POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return 'success', 200
    elif request.method == 'GET':
        return('get'), 200
    else:
        abort(400)

if __name__ == '__main__':
    app.run()