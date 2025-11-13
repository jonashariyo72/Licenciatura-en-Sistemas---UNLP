package ar.edu.unlp.info.oo1.Parcial;

import java.time.LocalDate;

public class Prolongado extends Contrato {
	private int cantDías;

	public Prolongado(LocalDate fecha, Cliente cliente, Servicio servicio, int cantDías) {
		super(fecha, cliente, servicio);
		this.cantDías = cantDías;
	}
	
	protected double calcularAdicional () {
		if (this.cantDías > 5) {
			return (this.getServicio().calcularCosto() * this.cantDías) - (this.getServicio().calcularCosto() * 0.1);
		}
		else return (this.getServicio().calcularCosto() * this.cantDías);	
	}
}
