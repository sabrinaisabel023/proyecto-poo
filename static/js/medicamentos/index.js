//Buscamos el boton de guardar
const btn_save_medicamentos = document.getElementById('btn-guardar')
//se valida que este exista en el dom
if(btn_save_medicamentos){
    //obtenemos su evento click
    btn_save_medicamentos.addEventListener('click',function(){
        //detenemos su accion por defecto
        event.preventDefault()
        // obtenemos el formulario de los datos por su id
        let form = document.getElementById('form-medicamentos')
        // lo pasamos por le formdata para serialiazar los datos
        let formdata = new FormData(form)
        //por medio de este metodo lo convertimos formato json
        let json = Object.fromEntries(formdata.entries())
        console.log(json)
        // validamos que los campos numericos esten bien ingresados
        if(json.concentracion_mg && json.concentracion_ml){
            // llamamos este metodo que envia lo datos al backend
            fetch('/guardar-medicamentos',{
                method:'post',
                headers:{
                    'Content-Type': 'application/json'
                },
                body:JSON.stringify(json),
            })
            // esperamos la respuesta si la respuesta es buena reiniciamos la pagina
            .then(response=>response.json())
            .then(data => location.reload())
            .catch(erro=>console.log(erro))
        }else{
            alert('Favor ingresar bien las concentraciones')
        }
    })
}