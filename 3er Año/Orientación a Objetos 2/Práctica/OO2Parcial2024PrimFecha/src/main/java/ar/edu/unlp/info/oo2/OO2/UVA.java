package ar.edu.unlp.info.oo2.OO2;

public class UVA extends Prestamo{

	public UVA(double monto, int cantCuotas, int cuotasAbonadas, double montoAbonado, Cliente cliente) {
		super(monto, cantCuotas, cuotasAbonadas, montoAbonado, cliente);
		
	}

	@Override
	protected double calcularAdicional() {
		return 0;
	}

	@Override
	public double getTasaInteres() {
//		return Indec.getIndiceInflacion();
		return 10000;
	}


}
