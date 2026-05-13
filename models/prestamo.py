from sqlalchemy import Column, Integer, ForeignKey, Date, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from config.database import Base

class Prestamo(Base):
    __tablename__ = 'prestamos'
    
    id = Column(Integer, primary_key=True)
    libro_id = Column(Integer, ForeignKey('libros.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    fecha_prestamo = Column(Date, nullable=False, default=datetime.now().date())
    fecha_devolucion = Column(Date, nullable=False)
    fecha_entrega = Column(Date, nullable=True)  # Fecha real de devolución
    
    # Relaciones
    libro = relationship("Libro", back_populates="prestamos")
    usuario = relationship("Usuario", back_populates="prestamos")
    
    @property
    def devuelto(self):
        return self.fecha_entrega is not None
    
    @property
    def vencido(self):
        if self.devuelto:
            return False
        return datetime.now().date() > self.fecha_devolucion
    
    def __repr__(self):
        return f"<Prestamo(id={self.id}, libro_id={self.libro_id}, usuario_id={self.usuario_id}, devuelto={self.devuelto})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'libro_id': self.libro_id,
            'usuario_id': self.usuario_id,
            'libro_titulo': self.libro.titulo if self.libro else None,
            'usuario_nombre': self.usuario.nombre if self.usuario else None,
            'fecha_prestamo': self.fecha_prestamo.isoformat() if self.fecha_prestamo else None,
            'fecha_devolucion': self.fecha_devolucion.isoformat() if self.fecha_devolucion else None,
            'fecha_entrega': self.fecha_entrega.isoformat() if self.fecha_entrega else None,
            'devuelto': self.devuelto,
            'vencido': self.vencido
        }
