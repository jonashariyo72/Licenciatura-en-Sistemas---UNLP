package ar.edu.unlp.info.oo1.PoolCar24;

import java.time.LocalDate;
import java.util.List;

public class Viaje {
	private String origen;
	private String destino;
	private double costo;
	private LocalDate fecha;
	private List<Usuario> pasajeros;
	public String getOrigen() {
		return origen;
	}
	public void setOrigen(String origen) {
		this.origen = origen;
	}
	public String getDestino() {
		return destino;
	}
	public void setDestino(String destino) {
		this.destino = destino;
	}
	public double getCosto() {
		return costo;
	}
	public void setCosto(double costo) {
		this.costo = costo;
	}
	public LocalDate getFecha() {
		return fecha;
	}
	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}
	public List<Usuario> getPasajeros() {
		return pasajeros;
	}
	public void setPasajeros(List<Usuario> pasajeros) {
		this.pasajeros = pasajeros;
	}
	
	public boolean ultimos30Dias () {
		LocalDate hace30Dias = LocalDate.now().minusDays(30);
		return (this.fecha.isAfter(hace30Dias) || this.fecha.isEqual(hace30Dias));
	}
}
