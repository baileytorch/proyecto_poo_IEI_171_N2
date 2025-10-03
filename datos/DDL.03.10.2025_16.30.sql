USE iei_171_n2;

CREATE TABLE comuna(
    id INTEGER AUTO_INCREMENT,
    codigo_comuna CHAR(5) NOT NULL UNIQUE,
    nombre_comuna VARCHAR(60) NOT NULL,

    CONSTRAINT pk_comuna PRIMARY KEY (id)
);

CREATE TABLE direccion(
    id INTEGER AUTO_INCREMENT,
    calle VARCHAR(255) NULL,
    numero VARCHAR(10) NULL,
    departamento 
);