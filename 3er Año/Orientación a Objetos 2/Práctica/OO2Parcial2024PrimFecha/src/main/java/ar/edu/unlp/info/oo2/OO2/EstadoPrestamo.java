package ar.edu.unlp.info.oo2.OO2;

public interface EstadoPrestamo {
	
	public void pagarCuota (Prestamo p, double montoAPagar);
	
	public double gastosCancelacion (Prestamo p);
}
