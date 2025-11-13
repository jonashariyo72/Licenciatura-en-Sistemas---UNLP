package ar.edu.unlp.info.oo1.PoolCar;

public class Vehiculo {
	
	private Conductor dueño;
	private String descripcion;
	private int capacidad;
	private int añoFab;
	private double valor;
	
	
	
	
	public Vehiculo(Conductor dueño, String descripcion, int capacidad, int añoFab, double valor) {
		super();
		this.dueño = dueño;
		this.descripcion = descripcion;
		this.capacidad = capacidad;
		this.añoFab = añoFab;
		this.valor = valor;
	}
	public Conductor getDueño() {
		return dueño;
	}
	public void setDueño(Conductor dueño) {
		this.dueño = dueño;
	}
	public String getDescripcion() {
		return descripcion;
	}
	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}
	public int getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}
	public int getAñoFab() {
		return añoFab;
	}
	public void setAñoFab(int añoFab) {
		this.añoFab = añoFab;
	}
	public double getValor() {
		return valor;
	}
	public void setValor(double valor) {
		this.valor = valor;
	}
	
	
}
