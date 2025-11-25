# orion-jets
Maestría 2025 Programación: Proyecto sobre movimientos propios en Orión

## New version using `uv init --package`

## Agregando los prerequisitos al proyecto

Librerías científicas
```sh
uv add astropy scipy regions
```

Librerías gráficas
```sh
uv add matplotlib seaborn
```

Cuadernos de Jupyter 
```sh
uv add jupyterlab ipykernel jupyterlab-widgets ipympl ipywidgets
```

Análisis de argumentos de la línea de comandos
```sh
uv add typer cyclopts
```

## Sumando los datos FITS al proyecto

```sh
uv run scripts/fetch-data.py
```

## Funciones selectas de `src/orion_jets`

### `fileio.get_box_region_masks()`

### `fileio.get_first_data_hdu()`

### `xcorr2d.measure_shift_integer()`

### `xcorr2d.measure_shift_gfit()`


## Inicializando el servidor de `jupyterlab`

```sh
uv run jupyter lab
```
o, si quiere más control, 
```sh
uv run jupyter lab --no-browser
```

Luego editar y correr los notebooks en tu browser

## Corriendo los scripts

P.ej., 

```sh
cd datos
uv run ../scripts/proper-motion.py cutout-hh529-acs-2005.fits cutout-hh529-wfc3-2015.fits hh529-boxes.reg
```

## Avanzado

### Corriendo pruebas con `pytest`

Instalar: 
```sh
uv add pytest
```

Escribir pruebas en `tests/test_*.py`

Correr todas las pruebas:
```sh
uv run pytest
```

### Checando tipos con `ty`

```sh
uvx ty check
```

