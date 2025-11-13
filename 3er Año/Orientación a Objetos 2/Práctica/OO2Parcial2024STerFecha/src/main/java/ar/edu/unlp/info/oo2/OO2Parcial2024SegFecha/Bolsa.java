package ar.edu.unlp.info.oo2.OO2Parcial2024SegFecha;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Objects;

public class Bolsa extends Item {
	private double capacidad;
	private List<Item> items;
	
	public Bolsa(double capacidad) {
		this.capacidad = capacidad;
		this.items = new ArrayList();
	}
	
	public boolean guardarObjeto(Item item) {
		if(this.capacidadSuficiente(item.getEspacio())) {
			this.items.add(item);
			return true;
		}
		return this.items.stream()
						   .filter(i -> i.capacidadSuficiente(item.getEspacio()))
						   .findFirst()
						   .map(i -> i.guardarObjeto(item))
						   .orElse(false);
	}
	
	public Item buscarItemPorNombre(String nombre) {
		if(this.getNombre().equals(nombre)) {
			return this;
		}
		return this.items.stream()
						 .map(i -> i.buscarItemPorNombre(nombre))
						 .filter(Objects::nonNull)
						 .findFirst()
						 .orElse(null);
	}
	
	public double espacioMasGrande() {
		return this.items.stream()
						 .mapToDouble(Item::capacidadDisponible)
						 .max()
						 .orElse(-1);
	}
	
	public double capacidadDisponible() {
		return this.items.stream().mapToDouble(Item::capacidadDisponible).sum() + this.capacidadLocalDisponible();
	}
	
	private double capacidadLocalDisponible() {
		return this.capacidad - this.items.size();
	}

	protected boolean capacidadSuficiente(double espacio) {
		return this.capacidad - espacio >= 0;
	}
	@Override
	protected double getCapacidad() {
		// TODO Auto-generated method stub
		return this.capacidad;
	}
}


