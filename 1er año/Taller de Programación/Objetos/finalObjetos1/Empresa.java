package finalObjetos1;

public class Empresa {
	private String nombre;
	private String direccion;
	private Oficina [] [] oficinas;
	
	
	public Empresa(String nombre, String direccion) {
		super();
		this.nombre = nombre;
		this.direccion = direccion;
		this.oficinas = new Oficina [3] [10];
		//recorrer la matriz, creando cada oficina.
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getDireccion() {
		return direccion;
	}
	public void setDireccion(String direccion) {
		this.direccion = direccion;
	}
	public Oficina[][] getOficinas() {
		return oficinas;
	}
	
	public void realizarAlquiler (Persona p, double monto, int piso, int oficina ) {
	
		if ((piso <= 3) && (oficina <= 10)) {
			oficinas[piso - 1][oficina - 1].alquilar(p,monto)
		}
		else System.out.println("Numero de piso u oficina inválidos");
	}
	
	public void liberarOficina (int dni) {
		boolean ok = false;
		int i = 0;
		while ((i < 3) && (!ok)) {
			int j = 0;
			while ((j < 10) && (!ok)) {
				if (this.oficinas[i][j].chequearDNI(dni)) {
					this.oficinas[i][j].liberar();
					ok = true;
				}
				j++;
			}
			i++;
		}
	}
	
	public void incrementar () {
		double incremento = 0.00;
		for (int i = 0; i < 3; i++) {
			incremento =+ 0.05;
			for (int j = 0; j < 0; j++) {
				if (this.oficinas[i][j].isEstáAlquilada()) {
					//this.oficinas[i][j].setMontoDiario(this.oficinas[i][j].getMontoDiario() + (this.oficinas[i][j].getMontoDiario() * incremento));
					this.oficinas[i][j].incrementarMonto(incremento));

				}
			}
		}
	}
	
	public int cantOficinas (int piso) {
		int cant = 0;
		for (int i = 0; i < 10; i++) {
			if (this.oficinas[piso-1][i].isEstáAlquilada()) {
				cant++;
			}
		}
		return cant;
	}
	
	
}
