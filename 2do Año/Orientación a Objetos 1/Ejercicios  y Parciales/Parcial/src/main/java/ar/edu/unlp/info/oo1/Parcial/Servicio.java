package ar.edu.unlp.info.oo1.Parcial;

public abstract class Servicio {
	private double precioPorHora;
	private int cantHoras;
	private Contrato contrato;
	
	
	public Servicio(double precioPorHora, int cantHoras, Contrato contrato) {
		super();
		this.precioPorHora = precioPorHora;
		this.cantHoras = cantHoras;
		this.contrato = contrato;
	}
	
	
	
	public double getPrecioPorHora() {
		return precioPorHora;
	}



	public void setPrecioPorHora(double precioPorHora) {
		this.precioPorHora = precioPorHora;
	}



	public int getCantHoras() {
		return cantHoras;
	}



	public void setCantHoras(int cantHoras) {
		this.cantHoras = cantHoras;
	}



	public Contrato getContrato() {
		return contrato;
	}



	public void setContrato(Contrato contrato) {
		this.contrato = contrato;
	}



	public double calcularCosto () {
		return (this.precioPorHora * this.cantHoras) + calcularAdicional();
				}
	
	protected abstract double calcularAdicional();
	
	public boolean esMayor (double valor) {
		if (this.calcularCosto() > valor) {
			return true;
		}
		else return false;
	}
	
}
