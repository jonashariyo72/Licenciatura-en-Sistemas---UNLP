package ar.edu.unlp.info.oo1.PoolCar;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Pasajero extends Usuario {
	private List<Viaje> viajesRealizados = new ArrayList<>();

	

	public Pasajero(String nombre, double saldo) {
		super(nombre, saldo);
	}



	public void registrarmeEnViaje (Viaje unViaje) {
		if ((unViaje.hayCapacidad()) && (unViaje.esPosibleEnDias(this)) && (this.getSaldo() > 0.00)){
			this.viajesRealizados.add(unViaje);
		}
	}
	



	public List<Viaje> getViajesRealizados() {
		return viajesRealizados;
	}




	@Override
	protected double calcularBonificacion(double unMonto, Viaje unViaje) {
		if (this.viajesRealizados.size() > 0) {
			return unMonto - 500;
		}
		return unMonto;
	}

	private boolean realizoViajes () {
		return this.viajesRealizados.stream().anyMatch(v -> v.getFecha().isAfter(LocalDate.now().minusDays(30)));
	}

	@Override
	protected double cobrarComision(double unMonto) {
		if (this.realizoViajes()) {
			return unMonto + (unMonto * 0.1);
		}
		return unMonto;
	}
	
}
