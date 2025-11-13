package ar.edu.unlp.info.oo1.Parcial;

public class Parquización extends Servicio{
	private double costoMantenimiento;
	private int cantMaquinas;
	
	
	public Parquización(double precioPorHora, int cantHoras, Contrato contrato, double costoMantenimiento,
			int cantMaquinas) {
		super(precioPorHora, cantHoras, contrato);
		this.costoMantenimiento = costoMantenimiento;
		this.cantMaquinas = cantMaquinas;
	}


	public double getCostoMantenimiento() {
		return costoMantenimiento;
	}


	public void setCostoMantenimiento(double costoMantenimiento) {
		this.costoMantenimiento = costoMantenimiento;
	}


	public int getCantMaquinas() {
		return cantMaquinas;
	}


	public void setCantMaquinas(int cantMaquinas) {
		this.cantMaquinas = cantMaquinas;
	}
	
	protected double calcularAdicional () {
		return this.costoMantenimiento * this.cantMaquinas;
	}
	

}
