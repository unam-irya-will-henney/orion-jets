# orion-jets
Maestría 2025 Programación: Proyecto sobre movimientos propios en Orión

## Instrucciones para estudiantes

Siga los pasos siguientes. Acuérdese hacer un commit de git después de cada cambio mayor

### Agregar los prerequisitos al proyecto

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

Requisitos básicos de jupyter lab. 

```sh
uv add jupyterlab ipykernel
```

Requisitos para emplear *widgets* (elementos interactivos) dentro de los notebooks

```sh
uv add jupyterlab-widgets ipympl ipywidgets
```


#### Análisis de argumentos de la línea de comandos
```sh
uv add typer cyclopts
```

#### Revisando los paquetes instalados en su proyecto

```sh
uv tree --depth 1
```
```
Resolved 129 packages in 15ms
orion-jets v0.1.0
├── astropy v7.1.1
├── cyclopts v4.2.4
├── ipykernel v7.1.0
├── ipympl v0.9.8
├── ipywidgets v8.1.8
├── jupyterlab v4.5.0
├── jupyterlab-widgets v3.0.16
├── matplotlib v3.10.7
├── pytest v9.0.1
├── regions v0.11
├── scipy v1.16.3
├── seaborn v0.13.2
└── typer v0.20.0
```

### Copiar los modulos de `src/orion_jets`

* `fileio.py` - abriendo imágenes FITS y archivos de regiones DS9
* `remote_data.py` - acceso remoto al archivos FITS
* `xcorr2d` - correlación cruzada en dos dimensiones

### Copiar los scripts de `scripts/`

* `fetch-data.py`
* `proper-motion.py`

### Incorporar los datos FITS al proyecto

Este comando copia los archivos FITS del repo [`unam-irya-will-henney/orion-jets-data`](https://github.com/unam-irya-will-henney/orion-jets-data) y los instala en la carpeta `data/`

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

### Clase final - jueves 27 de noviembre 2025


#### Corriendo pruebas con `pytest`

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


#### Checando tipos con `ty`

```sh
uvx ty check
```

#### Linting con `ruff`
