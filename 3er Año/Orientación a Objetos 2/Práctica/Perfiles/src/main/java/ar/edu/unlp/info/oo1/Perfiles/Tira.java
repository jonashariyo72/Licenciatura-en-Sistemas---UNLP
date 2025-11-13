package ar.edu.unlp.info.oo1.Perfiles;

public class Tira {
	private int milimetros;
	
	
	

	public Tira(int milimetros) {
		super();
		this.milimetros = 6150;
	}

	public int getMilimetros() {
		return milimetros;
	}

	public void setMilimetros(int milimetros) {
		this.milimetros = milimetros;
	}

	
	public boolean hacerCorte (int cant, int medida) {
		if (this.getMilimetros() > (cant * medida)) {
			this.milimetros =- (cant * medida);
			System.out.println("La cantidad de milímetros que le quedan a esta tira son de: ");
			System.out.println(this.milimetros);
		}
	}
}
