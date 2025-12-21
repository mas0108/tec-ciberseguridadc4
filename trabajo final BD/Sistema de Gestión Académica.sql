create database gestion_academica;
use gestion_academica;
create table departamento(
id_departamento int auto_increment primary key,
nombre varchar(100),
descriccion text
);

 CREATE TABLE estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    matricula VARCHAR(20) UNIQUE NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    fecha_nacimiento DATE
);

CREATE TABLE profesor (
    id_profesor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo VARCHAR(100),
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE curso (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    codigo VARCHAR(20) UNIQUE NOT NULL,
    creditos INT NOT NULL,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);

CREATE TABLE clase (
    id_clase INT AUTO_INCREMENT PRIMARY KEY,
    id_curso INT NOT NULL,
    id_profesor INT NOT NULL,
    periodo VARCHAR(20),
    horario VARCHAR(50),
    aula VARCHAR(20),
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso),
    FOREIGN KEY (id_profesor) REFERENCES profesor(id_profesor)
);

CREATE TABLE inscripcion (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_estudiante INT NOT NULL,
    id_clase INT NOT NULL,
    fecha_inscripcion DATE,
    FOREIGN KEY (id_estudiante) REFERENCES estudiante(id_estudiante),
    FOREIGN KEY (id_clase) REFERENCES clase(id_clase)
);

CREATE TABLE calificacion (
    id_calificacion INT AUTO_INCREMENT PRIMARY KEY,
    id_inscripcion INT NOT NULL,
    nota DECIMAL(5,2),
    observaciones TEXT,
    FOREIGN KEY (id_inscripcion) REFERENCES inscripcion(id_inscripcion)
);



INSERT INTO departamento (nombre, descriccion) VALUES
('Informática', 'Departamento de sistemas y computación'),
('Matemáticas', 'Departamento de matemáticas aplicadas'),
('Administración', 'Departamento de gestión y negocios');

INSERT INTO profesor (nombre, apellido, correo, id_departamento) VALUES
('Carlos', 'Ramírez', 'carlos.ramirez@uni.edu', 1),
('Ana', 'Gómez', 'ana.gomez@uni.edu', 1),
('Luis', 'Martínez', 'luis.martinez@uni.edu', 2),
('María', 'Fernández', 'maria.fernandez@uni.edu', 3);

INSERT INTO estudiante (matricula, nombre, apellido, correo, fecha_nacimiento) VALUES
('2025-001', 'Juan', 'Pérez', 'juan.perez@est.uni.edu', '2002-05-12'),
('2025-002', 'Laura', 'Rodríguez', 'laura.rodriguez@est.uni.edu', '2001-11-03'),
('2025-003', 'Miguel', 'Santos', 'miguel.santos@est.uni.edu', '2003-02-20'),
('2025-004', 'Andrea', 'López', 'andrea.lopez@est.uni.edu', '2002-08-14'),
('2025-005', 'Pedro', 'García', 'pedro.garcia@est.uni.edu', '2001-01-30');

INSERT INTO curso (nombre, codigo, creditos, id_departamento) VALUES
('Base de Datos', 'INF101', 4, 1),
('Programación I', 'INF102', 4, 1),
('Cálculo I', 'MAT101', 5, 2),
('Administración General', 'ADM101', 3, 3);

INSERT INTO clase (id_curso, id_profesor, periodo, horario, aula) VALUES
(1, 1, '2025-1', 'Lun-Mie 8:00-10:00', 'A101'),
(2, 2, '2025-1', 'Mar-Jue 10:00-12:00', 'B202'),
(3, 3, '2025-1', 'Lun-Vie 7:00-9:00', 'C303'),
(4, 4, '2025-1', 'Sab 9:00-12:00', 'D404');

INSERT INTO inscripcion (id_estudiante, id_clase, fecha_inscripcion) VALUES
(1, 1, CURDATE()),
(2, 1, CURDATE()),
(3, 2, CURDATE()),
(4, 3, CURDATE()),
(5, 4, CURDATE());

INSERT INTO calificacion (id_inscripcion, nota, observaciones) VALUES
(1, 85, 'Buen desempeño'),
(2, 90, 'Excelente'),
(3, 78, 'Debe reforzar práctica'),
(4, 88, 'Buen dominio'),
(5, 92, 'Muy responsable');



SELECT 
    e.nombre AS estudiante,
    e.apellido AS apellido_estudiante,
    cu.nombre AS curso,
    p.nombre AS maestro,
    p.apellido AS apellido_maestro,
    ca.nota
FROM estudiante e
JOIN inscripcion i ON e.id_estudiante = i.id_estudiante
JOIN clase c ON i.id_clase = c.id_clase
JOIN curso cu ON c.id_curso = cu.id_curso
JOIN profesor p ON c.id_profesor = p.id_profesor
JOIN calificacion ca ON i.id_inscripcion = ca.id_inscripcion;





SELECT e.nombre, e.apellido, AVG(ca.nota) AS promedio
FROM estudiante e
JOIN inscripcion i ON e.id_estudiante = i.id_estudiante
JOIN calificacion ca ON i.id_inscripcion = ca.id_inscripcion
GROUP BY e.id_estudiante
ORDER BY promedio DESC
LIMIT 5;






