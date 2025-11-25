# orion-jets
Maestría 2025 Programación: Proyecto sobre movimientos propios en Orión

## Instrucciones para estudiantes

Siga los pasos siguientes. Acuérdese hacer un commit de git después de cada cambio mayor

### Agregando los prerequisitos al proyecto

Correr los siguientes comandos

#### Librerías científicas
```sh
uv add astropy scipy regions
```

#### Librerías gráficas
```sh
uv add matplotlib seaborn
```

#### Cuadernos de Jupyter con widgets 
```sh
uv add jupyterlab ipykernel jupyterlab-widgets ipympl ipywidgets
```

#### Análisis de argumentos de la línea de comandos
```sh
uv add typer cyclopts
```

### Copiar los modulos de `src/orion_jets`

* `fileio.py` - abriendo imágenes FITS y archivos de regiones DS9
* `remote_data.py` - acceso remoto al archivos FITS
* `xcorr2d` - correlación cruzada en dos dimensiones

### Incorporar los datos FITS al proyecto

Este comando copia los archivos FITS del repo `orion-jets-data` y los instala en la carpeta `data/`

```sh
uv run scripts/fetch-data.py
```

Para ver más opciones:

```sh
uv run scripts/fetch-data.py
```

```
usage: fetch-data.py [-h] [--dest DEST] [--force] [--dry-run]

Download example FITS files from the orion-jets-data repository into a local data directory.

options:
  -h, --help            show this help message and exit
  --dest DEST           Destination directory for downloaded files (default: data).
  --force               Re-download files even if they already exist.
  --dry-run             Do not download; just print what would be done.
```


### Funciones selectas de `src/orion_jets`

#### `fileio.get_box_region_masks()`

#### `fileio.get_first_data_hdu()`

#### `xcorr2d.measure_shift_integer()`

#### `xcorr2d.measure_shift_gfit()`

### Corriendo pruebas con `pytest`

Instalar: 
```sh
uv add pytest
```

Escribir pruebas en `tests/test_*.py`

Por ejemplo, copiar `tests/test_xcorr2d_basic.py` de aquí

Correr todas las pruebas:
```sh
uv run pytest
```

Identifique y corrija cualquier error que se marca. Por ejemplo, `measure_shift_integer()` tiene un bug. 


### Inicializando el servidor de `jupyterlab`

```sh
uv run jupyter lab
```
o, si quiere más control, 
```sh
uv run jupyter lab --no-browser
```

Luego editar y correr los notebooks en tu browser

### Corriendo los scripts

P.ej., (después de crear el archivo `data/hh529-boxes.reg` con regiones de DS9):

```sh
cd datos
uv run ../scripts/proper-motion.py cutout-hh529-acs-2005.fits cutout-hh529-wfc3-2015.fits hh529-boxes.reg
```

### Avanzado


#### Checando tipos con `ty`

```sh
uvx ty check
```

#### Linting con `ruff`
