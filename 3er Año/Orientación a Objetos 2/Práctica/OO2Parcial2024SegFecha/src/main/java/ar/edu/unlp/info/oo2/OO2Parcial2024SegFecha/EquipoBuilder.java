package ar.edu.unlp.info.oo2.OO2Parcial2024SegFecha;

public abstract class EquipoBuilder {
    protected Catalogo catalogo;

    public EquipoBuilder(Catalogo catalogo) {
        this.catalogo = catalogo;
    }

    public abstract void setProcesador();
    public abstract void setMemoriaRam();
    public abstract void setAlmacenamiento();
    public abstract void setTarjetaGrafica();
    public abstract void setGabinete();
    public abstract void setFuente();
}