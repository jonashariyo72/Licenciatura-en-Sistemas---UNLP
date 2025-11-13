package ar.edu.unlp.info.oo1.AlquilerDePropiedades;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Reserva {
	private DateLapse periodo;
	private Propiedad propiedad;
	private Usuario inquilino;
	
	
	
	
	public Reserva(DateLapse periodo, Propiedad propiedad, Usuario inquilino) {
		super();
		this.periodo = periodo;
		this.propiedad = propiedad;
		this.inquilino = inquilino;
	}

	public DateLapse getPeriodo() {
		return periodo;
	}

	public void setPeriodo(DateLapse periodo) {
		this.periodo = periodo;
	}

	public Propiedad getPropiedad() {
		return propiedad;
	}

	public void setPropiedad(Propiedad propiedad) {
		this.propiedad = propiedad;
	}

	public Usuario getInquilino() {
		return inquilino;
	}

	public void setInquilino(Usuario inquilino) {
		this.inquilino = inquilino;
	}

	public double montoTotal () {	
		return periodo.sizeInDays() * this.propiedad.getPrecioPorNoche(); 
	}
	
    public boolean seSuperpone(DateLapse otroPeriodo) {
    	return this.periodo.overlaps(otroPeriodo);
       // delegacion incorrecta, va en datelapse return !(this.fechaEgreso.isBefore(fechaInicio) || this.fechaIngreso.isAfter(fechaFin));
    }
    
    public boolean estaEnCurso () {
    	return (LocalDate.now().isBefore(this.periodo.getFrom()) || LocalDate.now().isAfter(this.periodo.getTo()));
    }
    
}
