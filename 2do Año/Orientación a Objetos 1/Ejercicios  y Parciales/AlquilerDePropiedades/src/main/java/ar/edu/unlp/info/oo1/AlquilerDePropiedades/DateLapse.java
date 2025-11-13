package ar.edu.unlp.info.oo1.AlquilerDePropiedades;

import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class DateLapse {
    private LocalDate from;
    private LocalDate to;

    // Constructor
    public DateLapse(LocalDate from, LocalDate to) {
        this.from = from;
        this.to = to;
    }

    // Retorna la fecha de inicio del rango
    public LocalDate getFrom() {
        return from;
    }

    // Retorna la fecha de fin del rango
    public LocalDate getTo() {
        return to;
    }

    // Retorna la cantidad de días entre 'from' y 'to'
    public int sizeInDays() {
        return (int) ChronoUnit.DAYS.between(from, to);
    }

    // Retorna true si 'other' está entre 'from' y 'to'
    public boolean includesDate(LocalDate other) {
        return (other.equals(from) || other.isAfter(from)) && (other.equals(to) || other.isBefore(to));
    }
    
    public boolean overlaps(DateLapse anotherDateLapse) {
        return this.from.isBefore(anotherDateLapse.getTo()) && 
               this.to.isAfter(anotherDateLapse.getFrom());
    }
}

