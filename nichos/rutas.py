import posixpath


def ruta_relativa(destino, desde):
    """Enlace relativo de la página `desde` (una carpeta, acabada en /) a `destino`.

    Conserva la querystring y el ancla: ruta_relativa('/a/b/?x=1', '/a/c/') -> '../b/?x=1'
    """
    ruta, separador, resto = destino.partition('?')
    if not separador:
        ruta, separador, resto = destino.partition('#')
    relativa = posixpath.relpath(ruta, desde)
    if relativa == '.':
        relativa = './'
    elif ruta.endswith('/'):
        relativa += '/'
    return relativa + separador + resto
