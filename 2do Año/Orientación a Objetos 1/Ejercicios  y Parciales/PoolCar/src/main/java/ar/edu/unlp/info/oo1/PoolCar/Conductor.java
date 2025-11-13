package ar.edu.unlp.info.oo1.PoolCar;

public class Conductor extends Usuario {
	private Vehiculo vehiculo;
	
	

	public Conductor(String nombre, double saldo, Vehiculo vehiculo) {
		super(nombre, saldo);
		this.vehiculo = vehiculo;
	}

	@Override
	protected double calcularBonificacion(double unMonto, Viaje unViaje) {
		return unMonto - (unViaje.valorVehiculo() / 0.1);
	}

	@Override
	protected double cobrarComision(double unMonto) {
		if ((this.vehiculo.getAñoFab() - 2024) <= 5) {
			return unMonto * 0.01;
		}
		return unMonto * 0.1;
	}
	
	
}
