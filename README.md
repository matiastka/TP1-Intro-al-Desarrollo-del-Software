<h1>CarTrader</h1>
<h2>Introducción</h2>
<div>
<p>CarTrader es una pagina de compra-venta de autos</p>
</div>
<h2>Tecnologías utilizadas</h2>
<div>
<ul>
	<li>HTML</li>
	<li>Boostrap/CSS</li>
	<li>Javascript</li>
	<li>Python</li>
	<li>Flask</li>
	<li>PSQL</li>
</ul>
</div>
<h2>Instalar</h2>
<div>
	
	cd TP1-Intro-al-Desarrollo-del-Software/
 	virtualenv venv
	source venv/bin/activate
 	pip install flask
  	pip install flask-cors
   	pip install flask_sqlalchemy
    pip install psycopg2
     
</div>
<h2>Ejecutar</h2>
<p>Primero tienes que descargar el repostorio, despues tienes que levantar un servidor para el backend <b>(puedes usar python o flask)</b> y otro para el frontend.</p>
<h3>Backend</h3>
<div>
	
	cd TP1-Intro-al-Desarrollo-del-Software/
 	source venv/bin/activate
  	cd backend/
<p>Si es con Python:</p>

	python3 main.py
<p>Si es con Flask:</p>

	flask --app main --debug run -h localhost -p 5000
</div>
<h3>Frontend</h3>
<div>
	
	cd TP1-Intro-al-Desarrollo-del-Software/frontend/
 	python3 -m http.server
</div>
