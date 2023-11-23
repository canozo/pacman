# pypac
Pacman made in Python with Pyglet

> Recomendado utilizar Python 3.10

Es necesario dependencias de `Pyglet` y `Pillow (PIL)`, en la terminal:

```
python3 -m pip install pyglet Pillow
```

> Dependiendo de su instalación de Python, el comando cambiaria entre `python`, `python3` o `py -3`.

## Notas
Si la velocidad del juego es muy alta, se puede ajustar el valor en el archivo `game.py` línea `67`:

```py
# Velocidad Normal
pyglet.clock.schedule_interval(self.update, 1 / 1000)

# Velocidad Lenta
pyglet.clock.schedule_interval(self.update, 1 / 100)
```

## MacOS o Linux
Es necesario agregar el path al directorio del repositorio a la variable de entorno `PYTHONPATH`.
Este comando se debe ejecutar cada vez que se inicia la terminal donde inician el juego:

```
export PYTHONPATH="$PYTHONPATH:/Users/<username>/pacman/"
python3 pypac/main.py
```

## Windows
Es necesario agregar el path al directorio del repositorio a la variable de entorno `PYTHONPATH`.
Este comando se debe ejecutar cada vez que se inicia la terminal donde inician el juego:

```
set PYTHONPATH=%PYTHONPATH%;C:\Users\<username>\Documents\pacman\
python3 pypac\main.py
```