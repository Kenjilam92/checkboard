from flask import Flask, render_template
app=Flask(__name__)

@app.route ('/')
def Eight_by_Eight():
    return render_template(
        'checkboard.html',
        rows=8,
        columns=8,
        color1='class='+'red',color2='class='+'black'
        )
@app.route ('/<x>')
def x_by_Eight(x):
    return render_template(
        'checkboard.html',
        rows=8,
        columns=int(x),
        color1='class='+'red',color2='class='+'black'
        )
@app.route ('/<x>/<y>')
def x_by_y(x,y):
    return render_template(
        'checkboard.html',
        rows=int(y),
        columns=int(x),
        color1='class='+'red',
        color2='class='+'black'
        )
@app.route ('/<x>/<y>/<c1>/<c2>')
def x_by_y_and_colors(x,y,c1,c2):
    return render_template(
        'checkboard.html',
        rows=int(y),
        columns=int(x),
        color1='style='+f'background-color:{c1}',
        color2='style='+f'background-color:{c2}'
        )
    # return render_template('checkboard.html')

if __name__=="__main__":  
    app.run(debug=True) 