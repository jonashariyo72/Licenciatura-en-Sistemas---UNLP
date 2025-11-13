package ar.edu.unlp.info.oo2.PersonajesDeJuegoDeRol;

public class GuerreroBuilder implements PersonajeBuilder{

	@Override
	public Personaje construirPersonaje(String nombre) {
		return new Guerrero(nombre, new ArmaEspada(), new ArmaduraAcero(), "Combate cuerpo a cuerpo");
	}

}
