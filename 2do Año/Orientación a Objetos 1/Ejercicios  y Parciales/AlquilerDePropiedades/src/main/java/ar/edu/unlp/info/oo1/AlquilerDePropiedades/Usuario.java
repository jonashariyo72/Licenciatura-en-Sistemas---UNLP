package ar.edu.unlp.info.oo1.AlquilerDePropiedades;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Usuario {
	private String nombre;
	private int direccion;
	private int DNI;
	private List<Propiedad> propiedades;
	
	public Usuario(String nombre, int direccion, int dNI) {
		super();
		this.nombre = nombre;
		this.direccion = direccion;
		DNI = dNI;
		this.propiedades = new ArrayList<>();
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public int getDireccion() {
		return direccion;
	}

	public void setDireccion(int direccion) {
		this.direccion = direccion;
	}

	public int getDNI() {
		return DNI;
	}

	public void setDNI(int dNI) {
		DNI = dNI;
	}
	
//	public double calcularRetribucion () {
//		
//	}

	}
	
	
	
	
