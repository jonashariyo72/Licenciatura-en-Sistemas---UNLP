package ar.edu.unlp.info.oo2.OO2Parcial2024SegFecha;

public abstract class Item {
	private double espacio;
	private String nombre;
	
	public abstract Item buscarItemPorNombre(String nombre);
	public abstract boolean guardarObjeto(Item item);
	protected abstract double getCapacidad();
	protected abstract boolean capacidadSuficiente(double espacio);
	protected double getEspacio() {
		return espacio;
	}

	protected String getNombre() {
		return nombre;
	}
	
	public abstract double capacidadDisponible();
	
}
