package ar.edu.unlp.info.oo1.Parcial;

import java.util.ArrayList;
import java.util.List;

public class Cliente {
	private String nombre;
	private String direccion;
	private List<Contrato> contratos;
	
	
	public Cliente(String nombre, String direccion) {
		super();
		this.nombre = nombre;
		this.direccion = direccion;
		this.contratos = new ArrayList<Contrato> ();
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


	public List<Contrato> getContratos() {
		return contratos;
	}


	public void setContratos(List<Contrato> contratos) {
		this.contratos = contratos;
	}
	
	
	public double montoTotal () {
		return this.contratos.stream().mapToDouble(c -> c.calcularMonto()).sum();
	}
}
