CREATE database TEST;
use TEST;
--DROP TABLE CONTRATO;
CREATE TABLE contrato (
  nivel_entidad VARCHAR(255) NOT NULL,
  nombre_entidad VARCHAR(255) NOT NULL,
  nit_entidad VARCHAR(255) NOT NULL,
  departamento_entidad VARCHAR(255) NOT NULL,
  municipio_entidad VARCHAR(255) NOT NULL,
  estado_proceso VARCHAR(255) NOT NULL,
  modalidad VARCHAR(255) NOT NULL,
  objeto_contrato VARCHAR(600) NOT NULL,
  objeto_proceso VARCHAR(600) NOT NULL,
  tipo_de_contrato VARCHAR(255) NOT NULL,
  fecha_firma DATE NOT NULL,
  fecha_inicio VARCHAR(50) NOT NULL,
  fecha_fin VARCHAR(50) NOT NULL,
  tipo_contrato VARCHAR(255) NOT NULL,
  numero_contrato VARCHAR(255) NOT NULL,
  numero_proceso VARCHAR(255) NOT NULL,
  valor_contrato DECIMAL(15,2) NOT NULL,
  nombre_razon_social VARCHAR(255) NOT NULL,
  url_contrato VARCHAR(255) NOT NULL,
  origen VARCHAR(255) NOT NULL,
  documento VARCHAR(40) NULL,
  year_firma VARCHAR(6) NOT NULL,
  month_firma VARCHAR(6) NOT NULL,
  fecha_firma_yyyymm VARCHAR(20) NOT NULL
  -- ,PRIMARY KEY (numero_contrato)
);