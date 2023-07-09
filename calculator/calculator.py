from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)
from werkzeug.exceptions import abort
from calculator.auxfunc import calculo_f2 

bp = Blueprint('calculator', __name__)

@bp.route('/')
def index():
    session['vasos'] = 6
    return redirect(url_for('calculator.basic_f2calculator', vasos=session['vasos']))

@bp.route('/create', methods=['POST'])
def create():
    session['vasos'] = None
    if request.method == 'POST':
        vasos = int(request.form['vasos'])
        session['vasos'] = vasos
        return redirect(url_for('calculator.basic_f2calculator', vasos=session['vasos']))
    # return render_template('calculator/create.html')

@bp.route('/basic_f2calculator/<int:vasos>', methods=['GET', 'POST'])
def basic_f2calculator(vasos):
    vasos = session['vasos']

    if request.method == 'POST':
        ref_dis_prom = {}
        test_dis_prom = {}
        tiempo = {}
        for vaso in range(1, vasos+1):
            ref_dis_prom[f'{vaso}'] = request.form[f'ref_dis_{vaso}']
            test_dis_prom[f'{vaso}'] = request.form[f'test_dis_{vaso}']
            tiempo[f'{vaso}'] = request.form[f't{vaso}']
  
        f2 = calculo_f2(ref_dis_prom, test_dis_prom)

        context ={
            'vasos':vasos,
            'f2':f2,
            'tiempo':tiempo,
            'ref_dis_prom':ref_dis_prom,
            'test_dis_prom':test_dis_prom
        }

        return render_template('calculator/basic_f2calculator.html', **context)

    return render_template('calculator/basic_f2calculator.html', vasos=vasos) 

@bp.route('/clear', methods=['GET', 'POST'])
def clear():
    vasos = session['vasos']
    return redirect(url_for('calculator.basic_f2calculator', vasos=vasos)) 

@bp.route('/update', methods=['GET', 'POST'])
def update():
    return ''