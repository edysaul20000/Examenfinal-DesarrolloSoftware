#!/usr/bin/env bash

cd "$(dirname "$0")/.." || exit

# Colores
GREEN="\033[1;32m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
NC="\033[0m" #No-Color

errores=0
start_time=$(date +%s)

check_tool() {
	if ! command -v "$1" &>/dev/null; then
		echo -e "${YELLOW} Herramienta $1 no esta instalada. Se omitira.${NC}"
		return 1
	fi
	return 0
}

echo "Iniciando verificacion de código con linters..."
echo "***********************************************"


if check_tool flake8; then
	echo "*********************"
	echo "Ejecutando flake8"
	if flake8 tests/ --max-line-length=88 --select=E,W,F; then
		echo -e "${GREEN} No se encontraron errores con flake8${NC}"
	else
		echo -e "${RED} flake8 encontro errores${NC}"
		errores=1 
 	fi
fi

if check_tool shellcheck; then
	echo "======================"
	echo "Ejecutando shellcheck"
	if shellcheck scripts/*.sh ; then 
		echo -e "${GREEN} No se encontraron errores con shellcheck${NC}"
	else
		echo -e "${RED} shellcheck encontro errores${NC}"
	errores=1
	fi
fi

echo "------------------"
echo "Ejecutando tflint"
if [ -d "iac" ]; then
  if tflint --enable-all iac/; then
    echo "No se encontraron errores con tflint"
  else
    echo "tflint encontro errores"
    errores=1
  fi
else
  echo "No se encontro el directorio de IaC"
fi


echo "==============================================="
end_time=$(date +%s)
duration=$((end_time - start_time))

echo -e "${YELLOW} Resumen de linting:${NC}"
echo " Tiempo de ejecucion: ${duration}s"

if [ $errores -eq 1 ]; then
	echo -e "${RED} Se encontraron errores. Revisa los mensajes anteriores.${NC}"
	exit 1
else
	echo -e "${GREEN} Todos los linters pasaron correctamente.${NC}"
	exit 0
fi

fi [$error -eq]