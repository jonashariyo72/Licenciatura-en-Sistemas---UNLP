package finalObjetos1;

public class Oficina {
	private boolean estáAlquilada;
	private Persona inquilino;
	private double montoDiario;
	
	
	
	public Oficina() {
		super();
		this.estáAlquilada = false;
		this.inquilino = null;
		this.montoDiario = 0.00;
	}
	
	public void alquilar( Persona p, double monto) {
		this.estáAlquilada = true;
		this.inquilino = p;
		this.montoDiario = monto;
	}
	
	public boolean isEstáAlquilada() {
		return estáAlquilada;
	}
	public void setEstáAlquilada(boolean estáAlquilada) {
		this.estáAlquilada = estáAlquilada;
	}
	public Persona getInquilino() {
		return inquilino;
	}
	public void setInquilino(Persona inquilino) {
		this.inquilino = inquilino;
	}
	public double getMontoDiario() {
		return montoDiario;
	}
	public void setMontoDiario(double montoDiario) {
		this.montoDiario = montoDiario;
	}
	
	public boolean chequearDNI (int dni) {
		return estáAlquilada && dni == inquilino.getDni();
	}
	
}
