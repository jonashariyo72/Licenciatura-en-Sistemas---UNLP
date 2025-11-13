package ar.edu.unlp.info.oo2.OO2;

public class Aceptado implements EstadoPrestamo{

	@Override
	public void pagarCuota(Prestamo p,double montoAPagar) {
		p.setCuotasAbonadas(p.getCuotasAbonadas() +  1);
		p.setMontoAbonado(p.getMontoAbonado() + montoAPagar);
		if (p.getCuotasAbonadas() == p.getCantCuotas()) {
			p.setEstado(new Finalizado());
		}
		
	}

	@Override
	public double gastosCancelacion(Prestamo p) {
		return p.montoRestante();
	}

}
