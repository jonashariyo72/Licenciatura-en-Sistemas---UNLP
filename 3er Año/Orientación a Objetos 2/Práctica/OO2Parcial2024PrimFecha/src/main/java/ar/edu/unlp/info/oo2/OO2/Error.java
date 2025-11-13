package ar.edu.unlp.info.oo2.OO2;

public class Error implements EstadoPrestamo{

	@Override
	public void pagarCuota(Prestamo p, double montoAPagar) {
		  throw new IllegalArgumentException("El estado del préstamo entró en Error");
	}

	@Override
	public double gastosCancelacion(Prestamo p) {
		throw new IllegalArgumentException("El estado del préstamo entró en Error");
	}

}
