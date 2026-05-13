from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Libro(Base):
    __tablename__ = 'libros'
    
    id = Column(Integer, primary_key=True)
    titulo = Column(String(200), nullable=False)
    genero = Column(String(50))
    año_publicacion = Column(Integer)
    autor_id = Column(Integer, ForeignKey('autores.id'), nullable=False)
    
    # Relaciones
    autor = relationship("Autor", back_populates="libros")
    prestamos = relationship("Prestamo", back_populates="libro")
    
    def __repr__(self):
        return f"<Libro(id={self.id}, titulo='{self.titulo}', genero='{self.genero}', año={self.año_publicacion})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'año_publicacion': self.año_publicacion,
            'autor_id': self.autor_id,
            'autor': self.autor.nombre if self.autor else None
        }
