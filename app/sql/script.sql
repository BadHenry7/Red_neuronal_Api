create database proyecto

use proyecto

CREATE TABLE usuario (
  id int(4) NOT NULL,
  usuario varchar(30) NOT NULL,
  password varchar(30) NOT NULL,
  nombre varchar(65) NOT NULL,
  apellido varchar(65) NOT NULL,
  documento varchar(15) NOT NULL,
  telefono varchar(15) NOT NULL,
  id_rol int(4) NOT NULL
)


CREATE TABLE rol (
  id int(4) NOT NULL,
  nombre varchar(65) NOT NULL,
  descripcion text NOT NULL,
  estado tinyint(1) NOT NULL
)

CREATE TABLE atributo (
  id int(4) NOT NULL,
  nombre varchar(30) NOT NULL,
  descripcion text NOT NULL,
  estado tinyint(1) NOT NULL
) 


CREATE TABLE atrixusuario (
  id int(4) NOT NULL,
  id_usuario int(4) NOT NULL,
  id_atributo int(4) NOT NULL,
  valor varchar(30) NOT NULL,
  descripcion text NOT NULL,
  estado tinyint(1) NOT NULL
)



ALTER TABLE usuario
  ADD PRIMARY KEY (id),
  ADD UNIQUE KEY usuario (usuario),
  ADD UNIQUE KEY documento (documento),
  ADD KEY id_rol (id_rol)

ALTER TABLE atributo
  ADD PRIMARY KEY (id),
  ADD UNIQUE KEY nombre (nombre);

ALTER TABLE atrixusuario
  ADD PRIMARY KEY (id),
  ADD KEY id (id,id_usuario),
  ADD KEY id_atributo (id_atributo),
  ADD KEY id_usuario (id_usuario);

ALTER TABLE rol
  ADD PRIMARY KEY (id),
  ADD UNIQUE KEY nombre (nombre);

