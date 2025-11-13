package ar.edu.unlp.info.oo1.PoolCar24;

import java.time.LocalDate;

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

	public void cargarSaldo (double unMonto) {
		this.saldo += unMonto - calcularAdicional();
	}
	
	protected abstract double calcularAdicional() ;
		
	
	
}
