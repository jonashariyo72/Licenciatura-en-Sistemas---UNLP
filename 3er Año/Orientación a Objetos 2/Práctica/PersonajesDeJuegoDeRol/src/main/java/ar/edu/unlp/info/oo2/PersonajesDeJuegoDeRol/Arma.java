package ar.edu.unlp.info.oo2.PersonajesDeJuegoDeRol;

public interface Arma {
	
	public void meEnfrentoA (Armadura armadura);
	public void teEstasEnfrentandoAEspada(Arma arma);
	public void teEstasEnfrentandoABaston(Arma arma);
	public void teEstasEnfrentandoAArco(Arma arma);
	public String tipo();;
	public String daño();
}
