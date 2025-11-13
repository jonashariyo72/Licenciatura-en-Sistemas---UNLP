package ar.edu.unlp.info.oo1.PoolCar24;

import java.time.LocalDate;
import java.util.List;

public class Pasajero extends Usuario{
	
	private List<Viaje> viajesRealizados;
	

	public Pasajero(String nombre, double saldo) {
		super(nombre, saldo);
	}
	
	
//	public void registrarmeEnViaje (Viaje unViaje) {
//		if (LocalDate.now().isBefore(unViaje.getFecha().minusDays(2)) && (this.saldo > 0) && (unViaje.)
//)
//	}
	
	protected double calcularAdicional() {
		if (this.viajesRealizados.stream().anyMatch(v -> v.ultimos30Dias())) {
			return this.getSaldo() * 0.1;
		}
		else return 0.00;
	}
}
