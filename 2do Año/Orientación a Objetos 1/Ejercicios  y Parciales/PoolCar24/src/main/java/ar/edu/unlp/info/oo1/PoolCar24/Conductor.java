package ar.edu.unlp.info.oo1.PoolCar24;

public class Conductor extends Usuario {
	private Vehiculo vehículo;

	public Conductor(String nombre, double saldo, Vehiculo vehículo) {
		super(nombre, saldo);
		this.vehículo = vehículo;
	}
	
	
	
	public Vehiculo getVehículo() {
		return vehículo;
	}



	public void setVehículo(Vehiculo vehículo) {
		this.vehículo = vehículo;
	}



	protected double calcularAdicional() {
		if ((2024 - this.vehículo.getAñoFab()) < 5) {
			return this.getSaldo() * 0.01;
	}
		else return this.getSaldo() * 0.1;
	}
}
