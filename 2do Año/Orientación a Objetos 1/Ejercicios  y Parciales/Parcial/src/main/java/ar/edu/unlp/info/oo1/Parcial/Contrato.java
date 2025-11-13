package ar.edu.unlp.info.oo1.Parcial;

import java.time.LocalDate;

public abstract class Contrato {
	private LocalDate fecha;
	private Cliente cliente;
	private Servicio servicio;
	
	
	public Contrato(LocalDate fecha, Cliente cliente, Servicio servicio) {
		super();
		this.fecha = fecha;
		this.cliente = cliente;
		this.servicio = servicio;
	}
	
	
	
	public LocalDate getFecha() {
		return fecha;
	}



	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}



	public Cliente getCliente() {
		return cliente;
	}



	public void setCliente(Cliente cliente) {
		this.cliente = cliente;
	}



	public Servicio getServicio() {
		return servicio;
	}



	public void setServicio(Servicio servicio) {
		this.servicio = servicio;
	}



	public double calcularMonto () {
		return servicio.calcularCosto() + calcularAdicional();
	}
	
	protected abstract double calcularAdicional();
}
