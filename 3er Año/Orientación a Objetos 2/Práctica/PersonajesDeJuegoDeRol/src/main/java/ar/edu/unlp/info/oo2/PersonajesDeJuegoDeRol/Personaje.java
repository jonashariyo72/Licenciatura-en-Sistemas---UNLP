package ar.edu.unlp.info.oo2.PersonajesDeJuegoDeRol;

public abstract class Personaje {
	private String nombre;
	private Arma arma;
	private Armadura armadura;
	private String habilidad;
	private int vida;
	
	
	public Personaje(String nombre, Arma arma, Armadura armadura, String habilidad) {
		super();
		
		this.arma = arma;
		this.armadura = armadura;
		this.habilidad = habilidad;
		this.vida = 100;
	}
	public String getHabilidad() {
		return habilidad;
	}
	public void setHabilidad(String habilidad) {
		this.habilidad = habilidad;
	}
	public Armadura getArmadura() {
		return armadura;
	}
	public void setArmadura(Armadura armadura) {
		this.armadura = armadura;
	}
	public Arma getArma() {
		return arma;
	}
	public void setArma(Arma arma) {
		this.arma = arma;
	}
	public int getVida() {
		return vida;
	}
	public void setVida(int vida) {
		this.vida = vida;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	
}
