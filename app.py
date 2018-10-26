from flask import Flask, render_template

app = Flask(_name_)

@app.route('/', methods=["GET"])
def homePage():
    return render_template('index.html')
#Run
app.run(host="0.0.0.0", port="8080", debug=True)