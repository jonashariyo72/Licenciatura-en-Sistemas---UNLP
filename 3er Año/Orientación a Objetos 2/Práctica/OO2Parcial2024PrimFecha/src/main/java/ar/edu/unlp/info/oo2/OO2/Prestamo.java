package ar.edu.unlp.info.oo2.OO2;

public abstract class Prestamo {
	private double monto;
	private int cantCuotas;
	private int cuotasAbonadas;
	private double montoAbonado;
	private EstadoPrestamo estado;
	private Cliente cliente;
	
	
	
	
	public Prestamo(double monto, int cantCuotas, int cuotasAbonadas, double montoAbonado, Cliente cliente) {
		super();
		this.monto = monto;
		this.cantCuotas = cantCuotas;
		this.cuotasAbonadas = 0;
		this.montoAbonado = 0;
		this.cliente = cliente;
		if (this.valorCuota() > cliente.getSueldo()) this.estado = new Error ();
		else this.estado = new Aceptado();
	}
	public double getMonto() {
		return monto;
	}
	public void setMonto(double monto) {
		this.monto = monto;
	}
	public int getCantCuotas() {
		return cantCuotas;
	}
	public void setCantCuotas(int cantCuotas) {
		this.cantCuotas = cantCuotas;
	}
	public int getCuotasAbonadas() {
		return cuotasAbonadas;
	}
	public void setCuotasAbonadas(int cuotasAbonadas) {
		this.cuotasAbonadas = cuotasAbonadas;
	}
	public double getMontoAbonado() {
		return montoAbonado;
	}
	public void setMontoAbonado(double montoAbonado) {
		this.montoAbonado = montoAbonado;
	}
	
	public double valorCuota () {
		return (this.monto / this.cantCuotas) * this.getTasaInteres();
	}
	 
	
	public double montoPagado () {
		return montoAbonado;
	}
	
	public double montoRestante () {
		return this.valorCuota() * (this.cantCuotas - this.cuotasAbonadas);
	}
	public EstadoPrestamo getEstado() {
		return estado;
	}
	public void setEstado(EstadoPrestamo estado) {
		this.estado = estado;
	}
	public abstract double getTasaInteres() ;
	
	public double calcularGastos () {
		return this.estado.gastosCancelacion(this) + this.montoRestante() * 0.1 + calcularAdicional();
	}
	protected abstract double calcularAdicional();
	
	
}
