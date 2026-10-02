// Versión en HTML estático: sin servidor, los filtros y el buscador funcionan en el navegador.
(function () {
  'use strict';

  var params = new URLSearchParams(window.location.search);

  // Minúsculas y sin tildes, para que «euribor» encuentre «Euríbor»
  function normalizar(texto) {
    return (texto || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }

  // Filtros por categoría (blog y productos) o por estado (tendencias)
  function aplicarFiltro(clave) {
    var tarjetas = document.querySelectorAll('[data-' + clave + ']');
    var chips = document.querySelectorAll('.chips a');
    if (!tarjetas.length || !chips.length) return;

    var valor = params.get(clave);
    tarjetas.forEach(function (tarjeta) {
      tarjeta.hidden = Boolean(valor) && tarjeta.dataset[clave] !== valor;
    });
    chips.forEach(function (chip) {
      var valorChip = new URL(chip.href, window.location.href).searchParams.get(clave);
      if ((valorChip || '') === (valor || '')) {
        chip.setAttribute('aria-current', 'true');
      } else {
        chip.removeAttribute('aria-current');
      }
    });
  }

  function crear(etiqueta, clase, texto) {
    var nodo = document.createElement(etiqueta);
    if (clase) nodo.className = clase;
    if (texto) nodo.textContent = texto;
    return nodo;
  }

  function buscar() {
    var datos = document.getElementById('indice-busqueda');
    var contenedor = document.getElementById('busqueda-resultados');
    if (!datos || !contenedor) return;

    var q = (params.get('q') || '').trim();
    document.querySelectorAll('input[name="q"]').forEach(function (campo) { campo.value = q; });
    if (!q) return;

    var titulo = document.querySelector('.cabecera-pagina h1');
    if (titulo) titulo.textContent = 'Resultados para «' + q + '»';

    var terminos = normalizar(q).split(/\s+/);
    var indice = JSON.parse(datos.textContent);
    var resultados = indice.filter(function (elemento) {
      var texto = normalizar([elemento.titulo, elemento.resumen, elemento.texto, elemento.tipo].join(' '));
      return terminos.every(function (termino) { return texto.indexOf(termino) !== -1; });
    });

    resultados.forEach(function (elemento) {
      var tarjeta = crear('a', 'comparativa-tarjeta');
      tarjeta.href = elemento.url;
      tarjeta.appendChild(crear('span', 'comparativa-tarjeta__icono', elemento.icono));
      tarjeta.appendChild(crear('span', 'etiqueta', elemento.tipo));
      tarjeta.appendChild(crear('strong', '', elemento.titulo));
      tarjeta.appendChild(crear('span', '', elemento.resumen));
      contenedor.appendChild(tarjeta);
    });

    var total = document.getElementById('busqueda-total');
    total.textContent = resultados.length + (resultados.length === 1 ? ' resultado' : ' resultados');
    total.hidden = false;
    document.getElementById('busqueda-vacia').hidden = resultados.length > 0;
  }

  document.addEventListener('DOMContentLoaded', function () {
    aplicarFiltro('categoria');
    aplicarFiltro('estado');
    buscar();
  });
})();
