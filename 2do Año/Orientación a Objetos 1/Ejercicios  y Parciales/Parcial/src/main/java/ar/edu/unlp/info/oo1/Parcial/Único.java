package ar.edu.unlp.info.oo1.Parcial;

import java.time.DayOfWeek;
import java.time.LocalDate;

public class Único extends Contrato {
	private int cantDías;

	public Único(LocalDate fecha, Cliente cliente, Servicio servicio, int cantDías) {
		super(fecha, cliente, servicio);
		this.cantDías = cantDías;
	}
	
	protected double calcularAdicional() {
        LocalDate today = LocalDate.now();
        DayOfWeek dayOfWeek = today.getDayOfWeek();

        if ( dayOfWeek == DayOfWeek.SATURDAY || dayOfWeek == DayOfWeek.SUNDAY) {
        	return this.getServicio().calcularCosto() * 0.15;
        }
        else return 0.00;
	}
}
