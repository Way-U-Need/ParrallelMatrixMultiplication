import mp_mat_mult
from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    if request.method == 'POST':
        form_data = request.form
        numProcessors = int(request.form['numProcessors'])
        lowerLimit = int(request.form['lowerLimit'])
        upperLimit = int(request.form['upperLimit'])
        n = int(request.form['n'])
        m = int(request.form['m'])
        print(lowerLimit, upperLimit, n, m)
        matIn1, matIn2,timeForExecPar, matOutPar,matOutSeq, result=mp_mat_mult.parrallel_matrix_multiplication(lowerLimit, upperLimit, n, m )
        print(result)
        return render_template('data.html',numProcessors=numProcessors,matIn1=matIn1, matIn2=matIn2,timeForExecPar=timeForExecPar, 
                                        matOutPar=matOutPar,matOutSeq=matOutSeq,result=result)

# app.run(host='0.0.0.0', port=80, threaded=True)
