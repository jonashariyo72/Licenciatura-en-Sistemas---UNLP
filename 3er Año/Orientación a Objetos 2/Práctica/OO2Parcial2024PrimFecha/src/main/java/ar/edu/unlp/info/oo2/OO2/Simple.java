package ar.edu.unlp.info.oo2.OO2;

public class Simple extends Prestamo {
	private double tasaInteres;
	
	

	public Simple(double monto, int cantCuotas, int cuotasAbonadas, double montoAbonado, Cliente cliente,
			double tasaInteres) {
		super(monto, cantCuotas, cuotasAbonadas, montoAbonado, cliente);
		this.tasaInteres = tasaInteres;
	}


	@Override
	protected double calcularAdicional() {
		return 5000;
	}


	@Override
	public double getTasaInteres() {
		return this.tasaInteres;
	}
	
	
	

}
