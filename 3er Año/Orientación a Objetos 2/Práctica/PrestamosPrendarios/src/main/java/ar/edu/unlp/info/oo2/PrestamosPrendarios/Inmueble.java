package main.java.ar.edu.unlp.info.oo2.PrestamosPrendarios;

public class Inmueble extends Prendas {
	private String direccion;
	private double superficie;
	private double costoM2;

	public Inmueble(String direccion, double superficie, double costoM2) {
		super();
		this.direccion = direccion;
		this.superficie = superficie;
		this.costoM2 = costoM2;
	}

	protected double getValor() {
		return this.superficie * this.costoM2;
	}

	protected double getLiquidez() {
		return 0.2;
	}
}
