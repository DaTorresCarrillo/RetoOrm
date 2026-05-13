from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base

class Autor(Base):
    __tablename__ = 'autores'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    nacionalidad = Column(String(50))
    
    # Relación uno a muchos con libros
    libros = relationship("Libro", back_populates="autor")
    
    def __repr__(self):
        return f"<Autor(id={self.id}, nombre='{self.nombre}', nacionalidad='{self.nacionalidad}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'nacionalidad': self.nacionalidad
        }
