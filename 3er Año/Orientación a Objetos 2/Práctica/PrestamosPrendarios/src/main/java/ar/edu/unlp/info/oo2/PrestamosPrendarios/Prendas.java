package main.java.ar.edu.unlp.info.oo2.PrestamosPrendarios;


public abstract class Prendas {
	public double calcularValor() {
		return this.getValor() * this.getLiquidez();
	}
	
	protected abstract double getValor();
	
	protected abstract double getLiquidez();
}
