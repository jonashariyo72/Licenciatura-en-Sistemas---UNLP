package ar.edu.unlp.info.oo2.OO2Parcial2024SegFecha;

public class Jugador {
	private String nombre;
	private Bolsa bolsa;
	
	public Jugador(String nombre, double capacidad) {
		this.setNombre(nombre);
		this.bolsa = new Bolsa(capacidad);
	}
	
	public void guardarObjeto(Item item) {
		this.bolsa.guardarObjeto(item);
	}
	
	public Item buscarItemPorNombre(String nombre) {
		return this.bolsa.buscarItemPorNombre(nombre);
	}
	
	public double espacioMasGrande() {
		return this.bolsa.espacioMasGrande();
	}
	
	public double capacidadDisponible() {
		return this.bolsa.capacidadDisponible();
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
}
