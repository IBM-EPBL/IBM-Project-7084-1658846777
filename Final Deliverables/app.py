from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def front():
    return render_template('front.html')
if __name__ =='__main__':
    app.run(debug=True)
