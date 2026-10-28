# Caso práctico 02 — Programación Orientada a Objetos (POO)

**Tema:** Herencia múltiple, orden de resolución de métodos (MRO) y composición en Python.

## Caso práctico

La Oficina de Tecnologías de la Información (OTI) de la UNSCH desarrolla en Python el sistema de matrícula del semestre 2026-II. Todo estudiante paga un derecho base de S/ 60.00, y el sistema debe contemplar tres situaciones especiales que modifican ese monto: quien se matricula fuera de fecha paga un recargo de S/ 15.00; quien tiene un índice académico desaprobatorio en el semestre anterior paga S/ 15.00 adicionales; y quien es beneficiario de la beca para estudiantes afectados por la violencia sociopolítica paga la mitad del monto que le corresponde.

El equipo de la OTI programó cada situación como una especialización de la matrícula general, de modo que cada una toma el monto calculado por la regla anterior y le aplica su propia modificación. Para atender a los estudiantes que reúnen las tres situaciones a la vez, dos programadores crearon por separado una modalidad combinada que reúne las tres especializaciones. El primero escribió primero la de beca, luego la de índice académico desaprobatorio y al final la de matrícula extemporánea. El segundo escribió primero la de índice académico desaprobatorio, luego la extemporánea y al final la de beca.

Días después, Luis Huamaní Cárdenas y Rosa Ccahuana Prado, ambos becarios afectados por la violencia sociopolítica, con índice académico desaprobatorio y matriculados fuera de fecha, presentaron un reclamo ante la OTI porque el sistema les cobró montos distintos, aunque estaban exactamente en la misma situación.

El jefe de la OTI te encarga analizar el caso: identificar las clases involucradas y qué tipo de relación existe entre ellas; determinar el orden en que Python resolvería el cálculo del costo en cada una de las dos versiones; calcular cuánto pagó cada estudiante; explicar con precisión la causa de la diferencia y por qué ninguno de los dos programadores cometió un error de sintaxis; señalar qué pasaría si alguien intentara combinar la matrícula general con una de sus especializaciones escribiendo primero la general; y proponer un rediseño que evite que el monto dependa de un detalle oculto en la definición de las clases y que permita decidir, para cada estudiante, en qué orden se aplican los cobros y si la beca debe aplicarse antes o después de los recargos.

---

## Análisis del caso

### 1. Identificación de las clases y sus relaciones

Para resolverlo utilizaremos cinco clases principales:

- **`Matricula`:** clase base que establece el costo de S/ 60.00.
- **`MatriculaExtemporanea`:** agrega S/ 15.00.
- **`MatriculaDesaprobatoria`:** agrega S/ 15.00.
- **`MatriculaBeca`:** aplica un descuento del 50 %.
- **`MatriculaCombinada`:** reúne las tres especializaciones mediante herencia múltiple. En el código se implementan dos versiones: `MatriculaCombinada1` y `MatriculaCombinada2`.

### 2. ¿Qué relación existe?

Existe una relación de **herencia**, porque las modalidades especiales son tipos de matrícula. Además, se utiliza **herencia múltiple** porque la matrícula combinada hereda de tres especializaciones.

### 3. Implementación del código con herencia múltiple

**[Ver el programa de herencia múltiple (`herencia_multiple.py`)](./herencia_multiple.py)**

El archivo incluye las dos versiones de matrícula combinada y muestra el orden de resolución de métodos (MRO) correspondiente a cada una.

### 4. Cálculo de cuánto pagó cada estudiante

**Primera versión: primero los recargos y al final el descuento.**

```text
Derecho base:                 S/ 60.00
Recargo por matrícula tardía: S/ 15.00
Recargo por índice bajo:      S/ 15.00
Subtotal:                    S/ 90.00
Beca del 50 %:              - S/ 45.00
TOTAL:                       S/ 45.00
```

**Cálculo:** `(60 + 15 + 15) × 0.50 = S/ 45.00`

**Segunda versión: primero el descuento y después los recargos.**

```text
Derecho base:                 S/ 60.00
Beca del 50 %:              - S/ 30.00
Monto con beca:               S/ 30.00
Recargo por matrícula tardía: S/ 15.00
Recargo por índice bajo:      S/ 15.00
TOTAL:                       S/ 60.00
```

**Cálculo:** `(60 × 0.50) + 15 + 15 = S/ 60.00`

> **Nota:** El enunciado no especifica qué versión se aplicó a cada estudiante. Si se asigna la primera versión a Luis y la segunda a Rosa, Luis pagaría **S/ 45.00** y Rosa **S/ 60.00**.

### 5. Explicación de la causa de la diferencia

La diferencia es de **S/ 15.00**. No se debe a un error de cálculo matemático, sino al orden en que Python resuelve y ejecuta los métodos mediante `super()`.

En la primera versión, el orden MRO es:

```text
MatriculaCombinada1 → MatriculaBeca → MatriculaDesaprobatoria
→ MatriculaExtemporanea → Matricula → object
```

En la segunda versión, el orden MRO es:

```text
MatriculaCombinada2 → MatriculaDesaprobatoria → MatriculaExtemporanea
→ MatriculaBeca → Matricula → object
```

Las llamadas a `super().costo()` realizan primero el cálculo de la siguiente clase del MRO; al regresar, cada especialización aplica su modificación. Por eso cambia el resultado final.

### 6. ¿Por qué ningún programador cometió un error de sintaxis?

Porque Python permite que una clase herede de varias clases y que se invoquen métodos mediante `super()`.

Ambas definiciones son válidas, y Python puede establecer un orden de resolución de métodos (**MRO**) para cada una.

El problema no es sintáctico, sino de **diseño**: cambiar el orden de las clases modifica el resultado del cálculo.

### 7. ¿Qué pasaría al colocar primero la clase general?

```python
class MatriculaIncorrecta(Matricula, MatriculaBeca):
    pass
```

Python genera un **`TypeError`** al intentar definir la clase, porque `MatriculaBeca` ya hereda de `Matricula`. El nuevo orden exige buscar primero en `Matricula`, pero la jerarquía exige que su especialización `MatriculaBeca` aparezca antes. No se puede construir un MRO consistente.

### 8. Propuesta de rediseño: composición

Mi alternativa es utilizar **composición**: una matrícula contiene una lista de ajustes, y cada ajuste modifica el costo de manera independiente.

**[Ver el programa de la propuesta con composición (`composicion.py`)](./composicion.py)**

#### ¿Qué solucionamos con este rediseño?

Ahora el orden de aplicación de los ajustes es explícito. Ya no depende del MRO de Python. La universidad puede establecer una regla uniforme para todos los estudiantes.

Por ejemplo, si se aplican primero los recargos y finalmente el descuento de la beca, ambos estudiantes pagarían **S/ 45.00**. Si se aplica la beca al derecho base y luego se suman los recargos, ambos pagarían **S/ 60.00**. La propuesta permite elegir y aplicar una sola regla de forma consistente.

### 9. ¿En qué orden se deben aplicar los cobros y la beca? ¿La beca debe aplicarse antes o después de los recargos?

El orden de aplicación depende de la política establecida por la universidad. Si la beca se aplica antes de los recargos, el estudiante pagaría **S/ 60.00**; si se aplica después, pagaría **S/ 45.00**.

**Mi postura:** aplicar primero el descuento del 50 % de la beca sobre el derecho base de matrícula de S/ 60.00, quedando **S/ 30.00**. Posteriormente, se suman los recargos de S/ 15.00 por matrícula extemporánea y S/ 15.00 por índice académico desaprobatorio, obteniendo un **total de S/ 60.00**.

Este criterio permite mantener el beneficio de la beca y, al mismo tiempo, responsabilizar al estudiante por los recargos adicionales.

---

## Archivos del repositorio

| Archivo | Descripción |
|---|---|
| [`herencia_multiple.py`](./herencia_multiple.py) | Programa original con las dos versiones de herencia múltiple y sus MRO. |
| [`composicion.py`](./composicion.py) | Propuesta de rediseño con ajustes aplicados en orden explícito. |

Para ejecutar los programas desde la terminal:

```bash
python herencia_multiple.py
python composicion.py
```