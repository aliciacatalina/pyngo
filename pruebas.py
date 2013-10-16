#Caso 1
# Programa simple exitoso
model {
	vars {
		int : gasolina;
		int[5] : destinos, distancia;
		int[5] : costodetraslado;

	}

	data {
		distancia = 100, 20, 30, 400, 55;
		destinos = 6, 7, 8, 9, 10; 
		gasolina = 10;

	}

	MIN = for i in .fabricas {

			costodetraslado[i] = distancia[i] * gasolina;
	}

	where {
		costodetraslado[1] > costodetraslado[2];
		costodetraslado[2] < costodetraslado[4];
	}
}

#Caso 2
#Incluyendo funciones y cambio de scope

func iva (float p) {
	float precio_iva = p * .16;

	return precio_iva;
}

model {
	vars {
		float[10] precios;
		float[10] precios_coniva;
	}

	data {
		precios = 10.0, 23.50, 24.10, 1.50, 2.30, 4.50, 60.0, 8.90, 34.90, 3.99;
	}

	MIN = for i in .precios {
		precios = precios[i] + iva(precios[i]);
	}
}

#Caso 3
