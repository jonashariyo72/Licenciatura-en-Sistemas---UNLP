package main.java.ar.edu.unlp.info.oo2.PrestamosPrendarios;

import java.util.ArrayList;
import java.util.List;

public class PrendaCombinada extends Prendas {
	private List<Prendas> prendas;
	
	public PrendaCombinada() {
		this.prendas = new ArrayList<Prendas>();
	}
	
	public void agregarPrenda(Prendas p) {
		this.prendas.add(p);
	}


	protected double getValor() {
		return this.prendas.stream().mapToDouble(p -> p.getValor()).sum();
	}

	protected double getLiquidez() {
		return 0.5;
	}
}
