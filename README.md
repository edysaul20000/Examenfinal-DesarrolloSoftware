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

