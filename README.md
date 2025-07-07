# Examenfinal-DesarrolloSoftware
**Alumno:** Edy Saul Serrano Arostegui
**Codigo:** 20211229B
## Estructura del proyecto:

```
PC4-Proyecto-14/
├── .github/
│   ├── workflows/           
│   └── ci.yaml    
├── microservicios/
│   ├── GestionProducto/         
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── app/
│   │       └── main.py
│   │       └── test/
│   │           └── test_productos.py       
│   └── ManejoUsuario/                   
│       ├── Dockerfile
│       ├── requirements.txt
│       └── app/
│           └── main.py
│           └── test/
│               └── test_usuarios.py         
└── scripts/
│    └── pltlint.sh   
├── docker-compose.yaml  
├── pytest.ini
├── requirements.txt
└── README.md    
```

## 1. Ramas

- `feature/tflint`: Aqui implemente tflint para verificar el cumplimiento de buenas practicas como maximo 88 digitos por linea y respetar los espacios con flake8.

- `feature/microservicio`: Se implementan los microservicios Gestion de productos y Manejo de Usuario.

- `tests/Servicios`: Se implementan los tests a los servicios A y B

- `feature/docker`: Se implementa los archivos docker a cada servicio

- `feature/docker-compose`: Se implementa el archivo docker-compose 

- `feature/pipeline`: Se implementa un pipeline para poder ejecutar mediante un job

Tengo un problema con los test que no se pueden ejecutar de manera correcta pero al funcionar, segun mi pipeline deberia correr correctamente.

## Configuración Inicial

Para trabajar con el proyecto, realiza los pasos a continuacion.

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/edysaul20000/Examenfinal-DesarrolloSoftware.git
    cd Examenfinal-DesarrolloSoftware/
    ```

2. **Crear y activar el entorno virtual**
    ```bash
    python3 -m venv EF
    source EF/bin/activate
    ```
3. **Ejecutar los test**
   ```bash
   pytest
   ```
