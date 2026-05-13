-- Script SQL generado por SQLAlchemy para el Sistema de Biblioteca
-- Este script crea todas las tablas y relaciones necesarias

-- Crear base de datos (descomentar si es necesario)
-- CREATE DATABASE IF NOT EXISTS biblioteca;
-- USE biblioteca;

-- Tabla de Autores
CREATE TABLE autores (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    nombre VARCHAR(100) NOT NULL, 
    nacionalidad VARCHAR(50), 
    PRIMARY KEY (id)
);

-- Tabla de Usuarios
CREATE TABLE usuarios (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    nombre VARCHAR(100) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    telefono VARCHAR(20), 
    PRIMARY KEY (id), 
    UNIQUE (email)
);

-- Tabla de Libros
CREATE TABLE libros (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    titulo VARCHAR(200) NOT NULL, 
    genero VARCHAR(50), 
    año_publicacion INTEGER, 
    autor_id INTEGER NOT NULL, 
    PRIMARY KEY (id), 
    FOREIGN KEY(autor_id) REFERENCES autores (id)
);

-- Tabla de Préstamos
CREATE TABLE prestamos (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    libro_id INTEGER NOT NULL, 
    usuario_id INTEGER NOT NULL, 
    fecha_prestamo DATE NOT NULL, 
    fecha_devolucion DATE NOT NULL, 
    fecha_entrega DATE, 
    PRIMARY KEY (id), 
    FOREIGN KEY(libro_id) REFERENCES libros (id),
    FOREIGN KEY(usuario_id) REFERENCES usuarios (id)
);

-- Índices para mejorar el rendimiento
CREATE INDEX ix_libros_autor_id ON libros (autor_id);
CREATE INDEX ix_prestamos_libro_id ON prestamos (libro_id);
CREATE INDEX ix_prestamos_usuario_id ON prestamos (usuario_id);
CREATE INDEX ix_prestamos_fecha_devolucion ON prestamos (fecha_devolucion);
CREATE INDEX ix_prestamos_fecha_entrega ON prestamos (fecha_entrega);

-- Datos de ejemplo (opcional)
-- Autores
INSERT INTO autores (nombre, nacionalidad) VALUES 
('Gabriel García Márquez', 'Colombiana'),
('J.K. Rowling', 'Británica'),
('Stephen King', 'Estadounidense');

-- Usuarios
INSERT INTO usuarios (nombre, email, telefono) VALUES 
('Ana Martínez', 'ana.martinez@email.com', '555-1234'),
('Carlos López', 'carlos.lopez@email.com', '555-5678');

-- Libros
INSERT INTO libros (titulo, genero, año_publicacion, autor_id) VALUES 
('Cien años de soledad', 'Realismo mágico', 1967, 1),
('El amor en los tiempos del cólera', 'Novela romántica', 1985, 1),
('Harry Potter y la piedra filosofal', 'Fantasía', 1997, 2),
('Harry Potter y el prisionero de Azkaban', 'Fantasía', 1999, 2),
('El resplandor', 'Terror', 1977, 3);

-- Préstamos (fechas actuales)
INSERT INTO prestamos (libro_id, usuario_id, fecha_prestamo, fecha_devolucion) VALUES 
(1, 1, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 7 DAY)),
(3, 2, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY));
