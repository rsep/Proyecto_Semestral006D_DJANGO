# Proyecto_Semestral006D_DJANGO
Proyecto Semestral 006D migrado a DJANGO





# Usuario Django en BD
- /*Script creacion usuario*/

ALTER SESSION SET "_ORACLE_SCRIPT" = true;

CREATE USER django_semestral IDENTIFIED BY django_semestral;

GRANT CONNECT, RESOURCE TO django_semestral;

ALTER USER django_semestral DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS;
