package ar.edu.unlp.info.oo2.OO2Parcial2024SegFecha;

public class ItemConcreto extends Item {

	@Override
	public Item buscarItemPorNombre(String nombre) {
		if(this.getNombre().equals(nombre)) {
			return this;
		}
		return null;
	}

	@Override
	public boolean guardarObjeto(Item item) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	protected double getCapacidad() {
		// TODO Auto-generated method stub
		return 0;
	}

	public double capacidadDisponible() {
		return 0;
	}
	
	@Override
	protected boolean capacidadSuficiente(double espacio) {
		// TODO Auto-generated method stub
		return false;
	}

	
}