from flask import Flask, render_template
app = Flask(__name__)
@app.route('/json')
def json():
    return render_template('json.html')

@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing") 
if __name__ == '__main__':
    app.run(debug=True)

