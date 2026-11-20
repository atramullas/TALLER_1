# Proyecto Base

- Clona este proyecto en tu ordenador

- Implementa en `analsis.py` las siguientes funcionalidades:
	- total facturado
	- ventas por categoria
	- producto más vendido

- Crea/Actualiza tu repositorio remoto con estas funcionalidades

- Crea un notebook `panel.ipnyb` donde implementes estas funcionalidades:
	- el producto con más ingresos
	- filtra las ventas por un vendedor concreto
	- calcula el ticket medio

- Crea/Actualiza tu repositorio remoto con estas funcionalidades


- Desde Github modifica el contenido del fichero README.md, 
"#Esto es mi primer proyecto en TTAD"

- Desde Github modifica el contenido del fichero README.md,
- "#Esto es mi primer proyecto en TTAD"

- ¿Qué instrucciones tienes que ejecutar en tu terminal del proyecto para integrar los nuevos cambios remotos en tu repositorio local? Investiga los comandos git necesarios para resolver el conflicto.

Al ejecutar Git pull, Git detectó que ya tenía archivos sin fusionar (unmerged files) / conflictos pendientes de una fusión anterior incompleta.
1. Ejecutar Git status en la terminal para ver exactamente qué ficheros están marcados como both modified o unmerged.
2. Eliminar las líneas con <<<<<<<, ======= ni >>>>>>> y guardar.
3. Subir los cambios a Github. Ejecutar: 
git add . 
git commit -m "Resolver conflicto de fusión"
git branch -M main
git remote add origin https://github.com/atramullas/TALLER_1.git
git push -u origin main

- Entrega la URL del repositorio; y el texto generado tras ejecutar el comando `git log` en tu proyecto. 
