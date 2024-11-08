# -*- coding: utf-8 -*-
"""SEMANA13_BASE_DE_DATOS_AVANZ_N00325354.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10WKvbX85INGHsmbLn0aN0bmFP6K1PjzP

Nombre: JESUS ENMANUEL AGUIRRE RAMOS

SEMANA 13

CURSO: BASE DE DATOS AVANZADA & BIG DATA

Para el Siguiente Ejercicio, se muestra a un Alumno, con las Notas Siguientes, T1, T2, T3 y EF:

Cursos;T1;T2;T3;EF

Matematicas;15;14;12;14

Computacion Grafica;16;14;19;16

Metodologia Universitaria;13;7;15;16

Base de Datos Avanzada;19;14;15;18

Modelamiento y Analisis de Software;20;14;16;18

Se desea hallar la Media, Moda, Mediana y la Correlaccion de todas las Notas Obtenidas en el progreso de su ciclo
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark = SparkSession.builder.appName("Semana13_N00325354").getOrCreate()

spark

"""INGRESO DE DATOS:"""

data_notas_jesus = [("Matematicas",15,14,12,14),("Computacion Grafica",16,14,19,16),("Metodologia Universitaria",13,7,15,16),("Base de Datos Avanzada",19,14,15,18),("Modelamiento y Analisis de Software",20,14,16,18)]
columns = ["Cursos","T1","T2","T3","EF"]
variable = spark.createDataFrame(data_notas_jesus,columns)

"""HALLAR LA MEDIA"""

variable.select(mean(col("T1")).alias("Media de la T1")).show()

variable.select(mean(col("T2")).alias("Media de la T2")).show()

variable.select(mean(col("T3")).alias("Media de la T3")).show()

variable.select(mean(col("EF")).alias("Media del Examen Final")).show()

variable.select(mean(col("T1")).alias("Media de la T1")).collect()[0]["Media de la T1"]

variable.select(mean(col("T2")).alias("Media de la T2")).collect()[0]["Media de la T2"]

variable.select(mean(col("T3")).alias("Media de la T3")).collect()[0]["Media de la T3"]

variable.select(mean(col("EF")).alias("Media del Examen Final")).collect()[0]["Media del Examen Final"]

"""HALLAR LA MEDIANA:"""

var_mediana_t1 = variable.approxQuantile("T1",[0.5],0.0)

print("La Mediana de la T1 es:", var_mediana_t1)

var_mediana_t2 = variable.approxQuantile("T2",[0.5],0.0)

print("La Mediana de la T2 es:", var_mediana_t2)

var_mediana_t3 = variable.approxQuantile("T3",[0.5],0.0)

print("La Mediana de la T3 es:", var_mediana_t3)

var_mediana_ef = variable.approxQuantile("EF",[0.5],0.0)

print("La Mediana del Examen Final es:", var_mediana_ef)

"""Hallar la Moda:"""

var_moda_t1 = variable.groupBy("T1").count().orderBy(col("count").desc()).first()

print("La moda de la T1 es:",var_moda_t1["T1"])

var_moda_t2 = variable.groupBy("T2").count().orderBy(col("count").desc()).first()

print("La moda de la T2 es:",var_moda_t2["T2"])

var_moda_t3 = variable.groupBy("T3").count().orderBy(col("count").desc()).first()

print("La moda de la T3 es:",var_moda_t3["T3"])

var_moda_ef = variable.groupBy("EF").count().orderBy(col("count").desc()).first()

print("La moda del Examen Final es:",var_moda_ef["EF"])

"""Hallar la Correlacion:"""

correlacion = variable.select(corr(col("T1"),col("T2")).alias("correlacion")).collect()[0]["correlacion"]

print("La correlacion de la T1 y la T2 es:",correlacion)

correlacion2 = variable.select(corr(col("T3"),col("EF")).alias("correlacion2")).collect()[0]["correlacion2"]

print("La correlacion de la T3 y el Examen Final es:",correlacion2)

print("La correlacion Total de todas las Notas es:", correlacion+correlacion2)