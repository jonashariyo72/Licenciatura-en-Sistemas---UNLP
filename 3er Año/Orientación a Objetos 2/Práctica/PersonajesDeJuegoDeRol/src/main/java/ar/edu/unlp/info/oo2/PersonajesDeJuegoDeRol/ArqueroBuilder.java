package ar.edu.unlp.info.oo2.PersonajesDeJuegoDeRol;

public class ArqueroBuilder implements PersonajeBuilder{
	
	public Personaje construirPersonaje(String nombre) {
		return new Arquero (nombre, new ArmaArco(), new ArmaduraCuero(), "Disparo de flechas");
	}
}
