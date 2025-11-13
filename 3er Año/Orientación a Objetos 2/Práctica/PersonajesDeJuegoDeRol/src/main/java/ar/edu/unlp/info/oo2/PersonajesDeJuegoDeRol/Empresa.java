package ar.edu.unlp.info.oo2.PersonajesDeJuegoDeRol;

public class Empresa {
	private PersonajeBuilder builder;
	
	
    public Personaje crearPersonaje(String tipo, String nombre) {
        PersonajeBuilder builder;
        switch (tipo.toLowerCase()) {
            case "mago": builder = new MagoBuilder(); break;
            case "guerrero": builder = new GuerreroBuilder(); break;
            case "arquero": builder = new ArqueroBuilder(); break;
            default: throw new IllegalArgumentException("Tipo desconocido: " + tipo);
        }
        return builder.construirPersonaje(nombre);
    }



	public PersonajeBuilder getBuilder() {
		return builder;
	}



	public void setBuilder(PersonajeBuilder builder) {
		this.builder = builder;
	}
	
	// crear un método para cada builder
}

