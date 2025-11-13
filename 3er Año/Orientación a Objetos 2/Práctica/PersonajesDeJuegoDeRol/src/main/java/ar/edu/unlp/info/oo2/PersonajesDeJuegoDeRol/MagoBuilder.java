package ar.edu.unlp.info.oo2.PersonajesDeJuegoDeRol;

public class MagoBuilder implements PersonajeBuilder {
	
    public Personaje construirPersonaje(String nombre) {
        return new Mago(nombre, new ArmaBaston(), new ArmaduraCuero(), "magia");
    }
}

