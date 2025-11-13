package ar.edu.unlp.info.oo1.PoolCar;

import java.time.LocalDate;
import java.util.List;

public class Viaje {
	private String origen;
	private String destino;
	private double costo;
	private Vehiculo vehiculo;
	private LocalDate fecha;
	private List<Usuario> pasajeros;
	
	
	
	public Viaje(String origen, String destino, double costo, Vehiculo vehiculo, LocalDate fecha){
		super();
		this.origen = origen;
		this.destino = destino;
		this.costo = costo;
		this.vehiculo = vehiculo;
		this.fecha = fecha;
	}
	
	
	
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
	public Vehiculo getVehiculo() {
		return vehiculo;
	}
	public void setVehiculo(Vehiculo vehiculo) {
		this.vehiculo = vehiculo;
	}
	public LocalDate getFecha() {
		return fecha;
	}
	public void setFecha(LocalDate fecha) {
		this.fecha = fecha;
	}
	
	public boolean hayCapacidad () {
		if (this.vehiculo.getCapacidad() > 0)
			return true;
		else return false;
	}
	
	public boolean esPosibleEnDias (Pasajero unPasajero) {
		if (LocalDate.now().isBefore(this.fecha.minusDays(2))) {
			this.pasajeros.add(unPasajero);
			return true;
		}
		return false;
	}
	
	public double valorVehiculo () {
		return this.vehiculo.getValor();
	}
}
