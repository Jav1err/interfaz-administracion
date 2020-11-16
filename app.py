from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
	app.debug = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/test'
else:
	app.debug = False
	app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
	__tablename__ = 'prueba'
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(200))
	apellidos = db.Column(db.String(200))
	rut = db.Column(db.String(200))
	relacion = db.Column(db.String(200))
	correo = db.Column(db.String(200))
	telefono = db.Column(db.Integer)
	nombreempresa = db.Column(db.String(200))
	rutempresa = db.Column(db.String(200))
	tipooperacion = db.Column(db.String(200))
	monto = db.Column(db.Integer)
	moneda = db.Column(db.String(200))
	plazo = db.Column(db.String(200))
	fondo = db.Column(db.String(200))
	direccion = db.Column(db.String(200))
	rol = db.Column(db.String(200))
	tienetasacion = db.Column(db.String(200))
	valortasacion = db.Column(db.Integer)
	hipoteca = db.Column(db.String(200))
	saldoporpagar = db.Column(db.Integer)
	antiguedad = db.Column(db.Integer)
	auditados = db.Column(db.String(200))
	administradores = db.Column(db.Integer)
	ventasanuales = db.Column(db.Integer)
	cantidadempleados = db.Column(db.Integer)
	ventasclientes = db.Column(db.Integer)
	activostotales = db.Column(db.Integer)
	inventario = db.Column(db.Integer)
	cuentasporcobrar = db.Column(db.Integer)
	activoscorriente = db.Column(db.Integer)
	deudacorriente = db.Column(db.Integer)
	patrimonio = db.Column(db.Integer)
	resultadooperacional = db.Column(db.Integer)
	utilidad = db.Column(db.Integer)
	dividendos = db.Column(db.Integer)

	def __init__(self, nombre, apellidos, rut, relacion, correo, telefono, nombreempresa, rutempresa, tipooperacion, monto, moneda, plazo, fondo, direccion, rol, tienetasacion, valortasacion, hipoteca, saldoporpagar, antiguedad, auditados, administradores, ventasanuales, cantidadempleados, ventasclientes, activostotales, inventario, cuentasporcobrar, activoscorriente, patrimonio, resultadooperacional, utilidad, dividendos):
		self.nombre = nombre
		self.apellidos = apellidos
		self.rut = rut
		self.relacion = relacion
		self.correo = correo
		self.telefono = telefono
		self.nombreempresa = nombreempresa
		self.rutempresa = rutempresa
		self.tipooperacion = tipooperacion
		self.monto = monto
		self.moneda = moneda
		self.plazo = plazo
		self.fondo = fondo
		self.direccion = direccion
		self.rol = rol
		self.tienetasacion = tienetasacion
		self.valortasacion = valortasacion
		self.hipoteca = hipoteca
		self.saldoporpagar = saldoporpagar
		self.antiguedad = antiguedad
		self.auditados = auditados
		self.administradores = administradores
		self.ventasanuales = ventasanuales
		self.cantidadempleados = cantidadempleados
		self.ventasclientes = ventasclientes
		self.activostotales = activostotales
		self.inventario = inventario
		self.cuentasporcobrar = cuentasporcobrar
		self.activoscorriente = activoscorriente
		self.deudacorriente = deudacorriente
		self.patrimonio = patrimonio
		self.resultadooperacional = resultadooperacional
		self.utilidad = utilidad
		self.dividendos = dividendos

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
	if request.method == 'POST':
		nombre = request.form['nombre']
		apellidos = request.form['apellidos']
		rut = request.form['rut']
		relacion = request.form['relacion']
		correo = request.form['correo']
		telefono = request.form['telefono']
		nombreempresa = request.form['nombreempresa']
		rutempresa = request.form['rutempresa']
		tipooperacion = request.form['tipooperacion']
		monto = request.form['monto']
		moneda = request.form['moneda']
		plazo = request.form['plazo']
		fondo = request.form['fondo']
		direccion = request.form['direccion']
		rol = request.form['rol']
		tienetasacion = request.form['tienetasacion']
		valortasacion = request.form['valortasacion']
		hipoteca = request.form['hipoteca']
		saldoporpagar = request.form['saldoporpagar']
		antiguedad = request.form['antiguedad']
		auditados = request.form['auditados']
		administradores = request.form['administradores']
		ventasanuales = request.form['ventasanuales']
		cantidadempleados = request.form['cantidadempleados']
		ventasclientes = request.form['ventasclientes']
		activostotales = request.form['activostotales']
		inventario = request.form['inventario']
		cuentasporcobrar = request.form['cuentasporcobrar']
		activoscorriente = request.form['activoscorriente']
		deudacorriente = request.form['deudacorriente']
		patrimonio = request.form['patrimonio']
		resultadooperacional = request.form['resultadooperacional']
		utilidad = request.form['utilidad']
		dividendos = request.form['dividendos']

		# print(nombre, apellidos, rut, relacion, correo, telefono)
		if nombre == '' or apellidos == '' or rut == '' or correo == '' or telefono == '':
			return render_template('index.html', message='Ingrese los datos requeridos')
		if db.session.query(Feedback).filter(Feedback.rut == rut).count() == 0:
			data = Feedback(nombre, apellidos, rut, relacion, correo, telefono, nombreempresa, rutempresa, tipooperacion, monto, moneda, plazo, fondo, direccion, rol, tienetasacion, hipoteca)
			db.session.add(data)
			db.session.commit()
			return render_template('succes.html')
		return render_template('index.html', message='Ya ingresó datos')


if __name__ == '__main__':
	app.run()