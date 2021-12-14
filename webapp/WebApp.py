from flask import Flask, redirect, url_for, render_template, request, flash
import pandas as pd 

#Create Flash app
app = Flask(__name__)

@app.route("/", methods=['GET'])
def main_page():
    return redirect(url_for('home'))


@app.route("/home", methods=['GET', 'POST'])
def home():

    options = {
      'CS_SEXO', 'CS_GESTANT', 'CS_RACA',
       'NOSOCOMIAL', 'FEBRE', 'TOSSE',
       'GARGANTA', 'DISPNEIA', 'DESC_RESP', 
       'SATURACAO', 'DIARREIA', 'VOMITO',
       'PUERPERA',  'CARDIOPATI',
       'HEMATOLOGI', 'SIND_DOWN','HEPATICA',
       'ASMA', 'DIABETES', 'NEUROLOGIC',
       'PNEUMOPATI','IMUNODEPRE', 'RENAL',
       'OBESIDADE', 'VACINA', 'ANTIVIRAL',
       'DOR_ABD', 'FADIGA',
       'PERD_OLFT', 'PERD_PALA', 'DOSE_1_COV',
       'DOSE_2_COV'  
    }

    names = {
      'SEXO':['Masculino','Feminino'], 'GESTANT':['Sim', 'Não', 'Ignorado'], 'RAÇA':['Branca', 'Preta'],
       'NOSOCOMIAL':['Sim', 'Não', 'Ignorado'], 'FEBRE':['Sim', 'Não', 'Ignorado'], 'TOSSE':['Sim', 'Não', 'Ignorado'],
       'GARGANTA':['Sim', 'Não', 'Ignorado'], 'DISPNEIA':['Sim', 'Não', 'Ignorado'], 'DESC_RESP':['Sim', 'Não', 'Ignorado'], 
       'SATURACAO':['Sim', 'Não', 'Ignorado'], 'DIARREIA':['Sim', 'Não', 'Ignorado'], 'VOMITO':['Sim', 'Não', 'Ignorado'],
       'PUERPERA':['Sim', 'Não', 'Ignorado'],  'CARDIOPATI':['Sim', 'Não', 'Ignorado'],
       'HEMATOLOGI':['Sim', 'Não', 'Ignorado'], 'SIND_DOWN':['Sim', 'Não', 'Ignorado'],'HEPATICA':['Sim', 'Não', 'Ignorado'],
       'ASMA':['Sim', 'Não', 'Ignorado'], 'DIABETES':['Sim', 'Não', 'Ignorado'], 'NEUROLOGIC':['Sim', 'Não', 'Ignorado'],
       'PNEUMOPATI':['Sim', 'Não', 'Ignorado'],'IMUNODEPRE':['Sim', 'Não', 'Ignorado'], 'RENAL':['Sim', 'Não', 'Ignorado'],
       'OBESIDADE':['Sim', 'Não', 'Ignorado'], 'VACINA':['Sim', 'Não', 'Ignorado'], 'ANTIVIRAL':['Sim', 'Não', 'Ignorado'],
       'DOR_ABD':['Sim', 'Não', 'Ignorado'], 'FADIGA':['Sim', 'Não', 'Ignorado'],
       'PERD_OLFT':['Sim', 'Não', 'Ignorado'], 'PERD_PALA':['Sim', 'Não', 'Ignorado'], 'DOSE_1_COV':['Sim', 'Não', 'Ignorado'],
       'DOSE_2_COV':['Sim', 'Não', 'Ignorado']  
    }


    if request.method=="GET":
        return render_template('home.html', data=names)

    elif request.method=="POST":
        result = {}
        for cols in names.keys():
            answer = request.form[cols] 
            print(cols, ": ",answer)
            result[cols]=[answer]
        
        print(result)
        result_df = pd.DataFrame(result)
        result_dummy = pd.get_dummies(result_df)
        print(result_dummy.head())
        result_dummy.to_clipboard()
        return render_template('home.html', data=names)


if __name__ == "__main__":
    app.run(debug=True)
