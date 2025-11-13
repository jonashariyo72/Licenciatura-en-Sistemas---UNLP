package main.java.ar.edu.unlp.info.oo2.PrestamosPrendarios;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Alquiler extends Prendas {
	private LocalDate fechaInicio;
	private LocalDate fechaFin;
	private double costoMensual;
	
	public Alquiler(LocalDate fechaInicio, LocalDate fechaFin, double costoMensual) {
		super();
		this.fechaInicio = fechaInicio;
		this.fechaFin = fechaFin;
		this.costoMensual = costoMensual;
	}

	public int calcularMesesRestantes() {
		return (int) ChronoUnit.MONTHS.between(fechaInicio, fechaFin);
	}
	
	protected double getValor() {
		return this.calcularMesesRestantes() * this.costoMensual;
	}

	protected double getLiquidez() {
		return 0.9;
	}
}
