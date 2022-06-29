# Gastos-telefonicos

### Información sobre la estructura de las facturas y sobre el regex

```
Los números móviles y gastos que debemos extraer de la factura aparecen de la siguiente manera:
Un número movil de nueve dígitos que puede empezar por 6 o 7. Seguido del móvil va un número que puede tener como maximo 6 digitos separados por una coma y con un simbilo al lado ejmp. >>>> 208,333 •
La pelotita "•" representa el símbolo de euro. 

El regex queda de la siguiente manera >>>>> r"([6|7]\d{2} \d{3} \d{3})\n(-?\d{1,4},\d{1,4}\n)*(\d{1,4},\d{1,4}) •"

Si la estructura de la facura cambia en el futuro, el patrón podría ya no seguir funcionando y por lo tanto habría que modificarlo.

La modificación se ejecuta en /back/src/domain/services/bill_services.py en la linea 35
y el regex para obtener el total de todos los télefonos, en la función siguiente.
```
### Como añadir una nueva columna al excel
```
    Para añadir una una nueva columna, deberás ir a front/pages/BillPage, a la función exportDataToExcel y añadir un nuevo campo en el return.
``` 
### Como cambiar los puertos de Docker
```
    Para cambiar los puertos de Docker, deberas ir a ./docker-compose.yml y modificar las lineas 6 y 14.
```