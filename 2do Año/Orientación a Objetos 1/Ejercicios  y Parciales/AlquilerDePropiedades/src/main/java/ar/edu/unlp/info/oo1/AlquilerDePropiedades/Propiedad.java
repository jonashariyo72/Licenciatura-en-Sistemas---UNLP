package ar.edu.unlp.info.oo1.AlquilerDePropiedades;

import java.time.LocalDate;
import java.util.List;

public class Propiedad  {
	private int direccion;
	private String nombreDescriptivo;
	private double precioPorNoche;
	private List<Reserva> reservas;
	
	
	public int getDireccion() {
		return direccion;
	}
	public void setDireccion(int direccion) {
		this.direccion = direccion;
	}
	public String getNombreDescriptivo() {
		return nombreDescriptivo;
	}
	public void setNombreDescriptivo(String nombreDescriptivo) {
		this.nombreDescriptivo = nombreDescriptivo;
	}
	public double getPrecioPorNoche() {
		return precioPorNoche;
	}
	public void setPrecioPorNoche(double precioPorNoche) {
		this.precioPorNoche = precioPorNoche;
	}
	

	// Uso de foreach reinventa la rueda. Reemplazar por streams, revisar el noneMatch, anyMatch
//	   public boolean estaDisponible(LocalDate fechaInicio, LocalDate fechaFin) {
//	        for (Reserva reserva : reservas) {
//	            if (reserva.seSuperpone(fechaInicio, fechaFin)) {
//	                return false; // Si alguna reserva se solapa, la propiedad no está disponible
//	            }
//	        }
//	        return true; // Si ninguna reserva se solapa, la propiedad está disponible
//	    }
	
	public boolean estaDisponible(DateLapse otroPeriodo) {
		return reservas.stream().noneMatch(reservas -> reservas.seSuperpone(otroPeriodo));
	}
	
	
	public void crearReserva (DateLapse unPeriodo, Usuario user) {
		if (this.estaDisponible(unPeriodo)) {
			Reserva r = new Reserva (unPeriodo, this, user);
			this.reservas.add(r);
		}
	}
	
	
	public void cancelarReserva (Reserva unaReserva) {
        if (unaReserva.estaEnCurso()) {
        	reservas.remove(unaReserva);
        }
       
	}
	
	public double montoTotal () {
		return this.reservas.stream()
		.mapToDouble(precio -> precio.montoTotal()).sum();
	}
	
	
	
	
	

	
}
