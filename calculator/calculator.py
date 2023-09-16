from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)
from werkzeug.exceptions import abort
from calculator.auxfunc import calculo_f2 

bp = Blueprint('calculator', __name__)

@bp.route('/')
def index():
    session['tiempos'] = 5
    return redirect(url_for('calculator.basic_f2calculator', tiempos=session['tiempos']))

@bp.route('/create', methods=['POST'])
def create():
    session['tiempos'] = None
    if request.method == 'POST':
        tiempos = int(request.form['tiempos'])
        session['tiempos'] = tiempos
        return redirect(url_for('calculator.basic_f2calculator', tiempos=session['tiempos']))
    # return render_template('calculator/create.html')

@bp.route('/basic_f2calculator/<int:tiempos>', methods=['GET', 'POST'])
def basic_f2calculator(tiempos):
    tiempos = session['tiempos']

    if request.method == 'POST':
        ref_dis_prom = {}
        test_dis_prom = {}
        # puede que vaya a tener que cambiar el nombre de la variable tiempo
        tiempo_input = {} 
        for tiempo in range(1, tiempos+1):
            ref_dis_prom[f'{tiempo}'] = request.form[f'ref_dis_{tiempo}']
            test_dis_prom[f'{tiempo}'] = request.form[f'test_dis_{tiempo}']
            tiempo_input[f'{tiempo}'] = request.form[f't{tiempo}']
  
        f2 = calculo_f2(ref_dis_prom, test_dis_prom)

        context ={
            'tiempos':tiempos,
            'f2':f2,
            'tiempo_input':tiempo_input,
            'ref_dis_prom':ref_dis_prom,
            'test_dis_prom':test_dis_prom
        }

        return render_template('calculator/basic_f2calculator.html', **context)

    return render_template('calculator/basic_f2calculator.html', tiempos=tiempos) 

@bp.route('/clear', methods=['GET', 'POST'])
def clear():
    tiempos = session['tiempos']
    return redirect(url_for('calculator.basic_f2calculator', tiempos=tiempos)) 

@bp.route('/update', methods=['GET', 'POST'])
def update():
    return ''