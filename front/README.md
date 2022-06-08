# Aplicación para la extracción e imputación de telefonos

## Configuración del proyecto

```
npm install
```

### Ejecutar servidor de desarrollo

```
npm run serve
```

### Generar archivos de distribución

```
npm run build
```

### Instalar el modulo xlsx

```
npm install xlsx
```
### Información sobre la estructura de las facturas y sobre el regex

```
Los números móviles y gastos que nos interesan extraer de la factura aparecen de la siguiente manera:
Un número movil de nueve dígitos que puede empezar por 6 o 7. En el caso de empezar por 7 el siguiente numero no puede ser un 0 en le resto de los casos los digitos van del 0-9. Seguido del móvil va un número que puede tener como maximo 6 digitos separados por una coma y con un simbilo al lado ejmp. >>>> 208,333 •
La pelotita "•" representa el símbolo de euro. 

El regex queda de la siguiente manera >>>>> r"([6|7]\d{2} \d{3} \d{3})\n(-?\d{1,4},\d{1,4}\n)*(\d{1,4},\d{1,4}) •"

Si la estructura de la facura cambia en el futuro, el patrón podría ya no seguir siendo válido y por lo tanto habría que modificarlo.
```

