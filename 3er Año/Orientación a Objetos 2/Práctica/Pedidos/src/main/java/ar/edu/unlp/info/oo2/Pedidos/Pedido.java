package ar.edu.unlp.info.oo2.Pedidos;

import java.time.LocalDate;
import java.time.Period;
import java.util.List;

public class Pedido {
	private Cliente cliente;
	private List<Producto> productos;
	private String formaPago;
	
	public Pedido(Cliente cliente, List<Producto> productos, String formaPago) {
		if (!"efectivo".equals(formaPago)	&& !"6 cuotas".equals(formaPago)
        && !"12 cuotas".equals(formaPago)) {
          throw new Error("Forma de pago incorrecta");
    }
    this.cliente = cliente;
    this.productos = productos;
    this.formaPago = formaPago;
    }
  public double getCostoTotal() {
	  this.productos.stream().mapToDouble(p -> p.getPrecio()).sum();
     
     
     double extraFormaPago = 0.00;
     if ("efectivo".equals(this.formaPago)) {
       extraFormaPago = 0;
     } else if ("6 cuotas".equals(this.formaPago)) {
       extraFormaPago = getCostoTotal() * 0.2;
       } else if ("12 cuotas".equals(this.formaPago)) {
    	   extraFormaPago = getCostoTotal() * 0.5;
       }	
     int añosDesdeFechaAlta = Period.between(this.cliente.getFechaAlta(), LocalDate.now()).getYears();
     // Aplicar descuento del 10% si el cliente tiene más de 5 años de antiguedad
     if (añosDesdeFechaAlta > 5) {
    	 return (getCostoTotal() + extraFormaPago) * 0.9;
     }
     return getCostoTotal() + extraFormaPago;
 }
}