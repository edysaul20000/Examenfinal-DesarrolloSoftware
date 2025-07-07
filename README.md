# Examenfinal-DesarrolloSoftware

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
│   │   └── app1/
│   │       └── appA.py      
│   └── ManejoUsuario/                   
│       ├── Dockerfile
│       ├── requirements.txt
│       └── app2/
│           └── appB.py       
└── scripts/
    └── pltlint.sh   
└── tests/
    └── test_inicial
├── docker-compose.yaml  
├── log.txt
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

