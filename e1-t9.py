# Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

cadena = input( 'Digita un listado de paises separados por coma: ' )
countries = cadena.split( ',' )
countries = map( lambda country: country.strip().lower(), countries )
lista_paises_ordenados = sorted( set( countries ) )

print( lista_paises_ordenados )
