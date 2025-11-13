package ar.edu.unlp.info.oo1.PoolCar;
public abstract class Usuario {
	private String nombre;
	private double saldo;
	
	
	
	public Usuario(String nombre, double saldo) {
		super();
		this.nombre = nombre;
		this.saldo = saldo;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public double getSaldo() {
		return saldo;
	}
	public void setSaldo(double saldo) {
		this.saldo = saldo;
	}
	
	public void descontarSaldo (double unMonto, Viaje unViaje) {
		saldo = saldo - calcularBonificacion(unMonto, unViaje);
	}
	
	protected abstract double calcularBonificacion(double unMonto, Viaje unViaje);
	
	public void cargarSaldo (double unMonto) {
		saldo = saldo + cobrarComision (unMonto);
	}
	
	protected abstract double cobrarComision(double unMonto);
}
