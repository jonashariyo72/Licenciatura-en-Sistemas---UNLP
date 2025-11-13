package ar.edu.unlp.oo1.ejercicio1.impl;

import ar.edu.unlp.oo1.ejercicio1.WallPost;

/**
 * Completar esta clase de acuerdo a lo especificado en el cuadernillo
 *
 */
public class WallPostImpl implements WallPost {

	public String texto;
	public int cantLikes;
	public boolean destacado;
	
	
	public WallPostImpl() {
		this.texto = "";
		this.cantLikes = 0;
		this.destacado = false;
	}
	
	/*
	 * Este mensaje se utiliza para que una instancia de Wallpost se muestre de forma adecuada
	 */
    @Override
    public String toString() {
        return "WallPost {" +
            "text: " + getText() +
            ", likes: '" + getLikes() + "'" +
            ", featured: '" + isFeatured() + "'" +
            "}";
    }

	@Override
	public String getText() {
		return texto;
	}

	@Override
	public void setText(String text) {
		this.texto = text;
		
	}

	@Override
	public int getLikes() {
		return this.cantLikes;
	}

	@Override
	public void like() {
		this.cantLikes = this.cantLikes + 1;
		
	}

	@Override
	public void dislike() {
		this.cantLikes = this.cantLikes - 1;
		
	}

	@Override
	public boolean isFeatured() {
		return this.destacado;
	}

	@Override
	public void toggleFeatured() {
		if (this.destacado = true) {
			this.destacado = false;
		}
		else this.destacado = true;
			
		
	}

}
