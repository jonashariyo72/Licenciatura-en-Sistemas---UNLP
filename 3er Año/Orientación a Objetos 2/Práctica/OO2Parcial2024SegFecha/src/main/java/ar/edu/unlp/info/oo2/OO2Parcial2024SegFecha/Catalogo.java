package ar.edu.unlp.info.oo2.OO2Parcial2024SegFecha;

import java.util.List;

public class Catalogo {
    private List<Componente> componentes;

    public Catalogo(List<Componente> componentes) {
        this.componentes = componentes;
    }

    public Componente getComponente(String descripcion) {
        return componentes.stream()
                .filter(c -> c.getDescripcion().equalsIgnoreCase(descripcion))
                .findFirst()
                .orElseThrow(() -> new IllegalArgumentException("Componente no encontrado: " + descripcion));
    }
}
