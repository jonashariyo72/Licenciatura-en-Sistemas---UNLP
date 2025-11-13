package ar.edu.unlp.info.oo1.Parcial;

public class Limpieza extends Servicio{
	private double tarifaMínima;

	public Limpieza(double precioPorHora, int cantHoras, Contrato contrato, double tarifaMínima) {
		super(precioPorHora, cantHoras, contrato);
		this.tarifaMínima = tarifaMínima;
	}
	
	protected double calcularAdicional () {
		if ((this.getCantHoras() * this.getPrecioPorHora()) < this.tarifaMínima) {
			return this.tarifaMínima;
		}
		else return 0.00;
	}
}
