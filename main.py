from flask import Flask,render_template,jsonify,request
from clases.medicamentos import Medicamentos
from clases.pacientes import Paciente,TratamientoPaciente
from datetime import datetime


# arrays donde se alamcenaran los objetos creados
lista_mediacamentos = []
lsita_pacientes = []

#inicio del flask
app = Flask(__name__)

#ruta principal que llevara al template inicial y mandara los datos de los arrays
@app.route('/')
def index():
    data = []
    data_paciente = []
    for med in lista_mediacamentos:
        dic = {
            'id':med.id,
            'nombre':med.nombre,
            'presentacion':med.presentacion,
            'concentracion_mg':med.concentracion_mg,
            'concentracion_ml':med.concentracion_ml,
        }
        data.append(dic)
    
    for pac in lsita_pacientes:
        dic = {
            'paciente':pac.getNombrePacienteCompleto(),
            'identificacion':pac.getIdentificacion(),
            'edad':pac.getEdad(),
            'medicamento':pac.nombre_medicamento,
            'dosis':pac.dosis,
            'administracion':round(pac.administracion,3),
            'tiempo':pac.tiempo
        }
        data_paciente.append(dic)
      
    
    return render_template('index.html',lista=data,lista_paciente=data_paciente)


#Ruta para la pagina de medicamentos que se le envia los datos del listado de medicamentos
@app.route('/medicamentos')
def medicamentos():
    data = []
    for med in lista_mediacamentos:
        dic = {
            'id':med.id,
            'nombre':med.nombre,
            'presentacion':med.presentacion,
            'concentracion_mg':med.concentracion_mg,
            'concentracion_ml':med.concentracion_ml,
        }
        data.append(dic)
    return render_template('medicamentos/index.html',lista=data)

#ruta que guarda los medicamentos recibe los datos de la pagina y crea los objetos que ya creados son puestos en su respectivo array
@app.route('/guardar-medicamentos',methods=["POST"])
def guardarMedicamentos():
    data = request.get_json()
    arr = len(lista_mediacamentos)
    med = Medicamentos(
        id=arr+1,
        nombre=data['nombre'],
        presentacion=data['presentacion'],
        concentracion_mg=int(data['concentracion_mg']),
        concentracion_ml=int(data['concentracion_ml']),
    )
    lista_mediacamentos.append(med)
    
    return jsonify({'data':200})


#ruta que guarda los pacientes recibe los datos de la pagina y crea los objetos que ya creados son puestos en su respectivo array
@app.route('/guardar-paciente',methods=['POST'])
def guardarPaciente():
    data = request.get_json()
    id_med = int(data['medicamento'])
    med = None
    for i in lista_mediacamentos:
        if i.id == id_med:
            med = i
            break
    
    tratamiento = TratamientoPaciente(
        nombre=data['nombre'],
        apellido=data['apellido'],
        identificacion=data['identificacion'],
        dosis=int(data['dosis']),
        peso=float(data['peso']),
        fecha_nacimiento=datetime.strptime(data['fecha_nacimiento'], '%Y-%m-%d'),
        tm=int(data['tiempo']),
        bool_peso=data['bool_peso'],
        nom_med=med.nombre
        
    )
    tratamiento.calculo_dosis(medicamento=med)
    lsita_pacientes.append(tratamiento)
    return jsonify({'data':200})

if __name__ == '__main__':
    app.run(debug=True)