package ar.edu.unlp.info.oo1.PoolCar;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.LocalDate;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class PasajeroTest {
	Pasajero pasajero = new Pasajero ("Matías", 700.00);
	
	@BeforeEach
	void setUp() throws Exception {
		Conductor Jonás = new Conductor ("Jonás", 700.00, null);
		Vehiculo auto = new Vehiculo (Jonás, "Sabela compa", 5, 2015, 1000);
		LocalDate fecha = LocalDate.of (2024,7,20);
		Viaje viaje = new Viaje ("La Plata", "Santiago del Estero", 500.00, auto, fecha);
	}
	
	@Test
	public void TestRegistrarmeEnViaje () {
		Conductor Jonás = new Conductor ("Jonás", 700.00, null);
		Vehiculo auto = new Vehiculo (Jonás, "Sabela compa", 5, 2015, 1000);
		Pasajero p = new Pasajero ("Jonás", 700.00);
		LocalDate fecha = LocalDate.of (2024,7,20);
		Viaje viaje = new Viaje ("La Plata", "Santiago del Estero", 500.00, auto, fecha);
		for (int i = 0; i < 4; i++) {
			p.registrarmeEnViaje(viaje);
			p = new Pasajero ("Jonás", 700.00);
		}
		assertEquals (4,p.getViajesRealizados().size(), "Son 4 elementos");
		System.out.println(p.getViajesRealizados().size());
	}
	
//	@Test
//	public void TestCargarSaldo () {
//		pasajero.cargarSaldo(500.00);
//		assertEquals (1200.00, pasajero.getSaldo(), "El resultado debería dar 800");
//		System.out.println(pasajero.getSaldo());
//	}
//	
	
}
