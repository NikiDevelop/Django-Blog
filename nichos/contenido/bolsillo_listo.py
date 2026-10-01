SITIO = {
    'nombre': 'Bolsillo Listo',
    'slug': 'bolsillo-listo',
    'eslogan': 'Tu dinero, claro: hipoteca, ahorro e inversión en España',
    'descripcion': 'Hacemos las cuentas de las decisiones que más se buscan: amortizar plazo o cuota, fijo o '
                   'variable, diésel o gasolina, dónde guardar el fondo de emergencia y cómo empezar a invertir.',
    'nicho': 'Finanzas personales',
    'icono': '💶',
    'color_primario': '#1d4ed8',
    'color_secundario': '#0b1d4d',
    'orden': 3,
    'por_que': """
<p>Según Google, en 2025 los españoles buscaron cómo <strong>proteger sus ahorros, su empleo y prepararse para
crisis económicas</strong>. Entre las comparativas «¿qué es mejor…?» más buscadas del año estuvieron
<strong>«Amortizar plazo o cuota»</strong> y <strong>«Diésel o gasolina»</strong>, y también destacaron las búsquedas
sobre comprar coche.</p>
<p>En 2026 la preocupación aumenta. El <strong>Euríbor cerró julio en el 2,855 %</strong>, su nivel más alto desde
septiembre de 2024. Según Kelisto, la revisión anual encarecía unos 780 € al año la cuota de una hipoteca variable
media. Al mismo tiempo, las búsquedas de «compra ahora, paga después» (BNPL) han crecido un 577 % en cinco años.</p>
<p>Son decisiones con mucho dinero en juego. Aquí se explican con ejemplos numéricos y sin vender ningún producto
financiero concreto.</p>
""",
    'fuentes': [
        {'titulo': 'Google: 2025 en búsquedas en España (apagón, IA, consultas financieras)', 'url': 'https://blog.google/intl/es-es/productos/2025-en-busquedas-de-google-espana-busca-respuestas-entre-el-apagon-la-ia-consultas-financieras-y-muchas-mas-preguntas/'},
        {'titulo': 'Ecommerce News: las búsquedas que definieron España en 2025', 'url': 'https://ecommerce-news.es/google-revela-las-busquedas-que-definieron-a-espana-en-2025/'},
        {'titulo': 'Europa Press / Bolsamanía: el Euríbor cierra julio de 2026 en el 2,855 %', 'url': 'https://www.bolsamania.com/noticias/mercados/economia--el-euribor-cierra-julio-en-el-2855-su-nivel-mas-alto-desde-septiembre-de-2024-y-avanza-alzas-hipotecarias--23165224.html'},
        {'titulo': 'Kelisto: el Euríbor encarece las hipotecas variables unos 780 € al año', 'url': 'https://assets.kelisto.es/press-releases/el-euribor-cae-ligeramente-en-junio-aunque-encarece-la-cuota-de-las-hipotecas-variables-en-780-euros-al-ano.docx.pdf'},
        {'titulo': 'Futur Finances: previsión de Funcas para el Euríbor', 'url': 'https://futurfinances.com/?p=51292'},
        {'titulo': 'Exploding Topics: tendencias de comportamiento del consumidor (BNPL)', 'url': 'https://explodingtopics.com/blog/consumer-behavior'},
    ],
}

AVISO_FINANZAS = """
<div class="aviso"><p><strong>Información educativa, no asesoramiento financiero personalizado.</strong> Los ejemplos
usan supuestos simplificados. Antes de firmar, pide a tu banco la simulación oficial y, si tienes dudas, consulta con
un asesor independiente.</p></div>
"""

ARTICULOS = [
    {
        'slug': 'amortizar-plazo-o-cuota',
        'titulo': 'Amortizar hipoteca: ¿reducir plazo o cuota? Ejemplo con números',
        'resumen': 'Fue una de las comparativas más buscadas en España. Con un ejemplo real calculamos cuánto ahorras '
                   'en cada caso y cuándo conviene una u otra opción.',
        'categoria': 'Hipotecas',
        'palabra_clave': 'amortizar plazo o cuota',
        'icono': '🏠',
        'minutos_lectura': 8,
        'destacado': True,
        'contenido': """
<p>Tienes un dinero ahorrado y quieres adelantarlo a la hipoteca. El banco te pregunta: <strong>¿reducimos el plazo o
la cuota?</strong> No es una pregunta menor: la diferencia puede ser de miles de euros.</p>

<h2>El ejemplo</h2>
<p>Supongamos una hipoteca con estas condiciones:</p>
<ul>
  <li>Capital pendiente: <strong>150.000 €</strong></li>
  <li>Plazo restante: <strong>25 años</strong> (300 cuotas)</li>
  <li>Tipo de interés: <strong>3 % TIN</strong></li>
  <li>Cuota actual: <strong>711,32 €/mes</strong></li>
  <li>Intereses que pagarías hasta el final: <strong>63.395 €</strong></li>
</ul>
<p>Decides amortizar <strong>10.000 €</strong>. Estas son las dos opciones:</p>

<table>
  <thead><tr><th></th><th>Reducir cuota</th><th>Reducir plazo</th></tr></thead>
  <tbody>
    <tr><td>Nueva cuota</td><td>663,90 € (−47,42 €/mes)</td><td>711,32 € (igual)</td></tr>
    <tr><td>Plazo restante</td><td>25 años (igual)</td><td>22 años y 8 meses (−28 meses)</td></tr>
    <tr><td>Intereses que te ahorras</td><td>≈ 4.226 €</td><td><strong>≈ 10.426 €</strong></td></tr>
  </tbody>
</table>
<p>Con los mismos 10.000 €, <strong>reducir plazo ahorra unas 2,5 veces más intereses</strong>. La razón es que
dejas de pagar intereses durante 28 meses enteros.</p>

<h2>Cuándo conviene reducir la cuota</h2>
<ul>
  <li>Tu cuota supera el 30–35 % de tus ingresos netos y vas justo a fin de mes.</li>
  <li>Esperas una bajada de ingresos (jubilación, excedencia, paro).</li>
  <li>Tienes una hipoteca variable y temes nuevas subidas del Euríbor: una cuota más baja te da margen.</li>
  <li>Vas a invertir la diferencia mensual de forma disciplinada.</li>
</ul>

<h2>Cuándo conviene reducir el plazo</h2>
<ul>
  <li>Tu cuota es cómoda y quieres pagar lo mínimo en intereses.</li>
  <li>Te quedan muchos años de hipoteca: cuanto antes amortices, mayor el ahorro.</li>
  <li>Quieres terminar de pagar antes de jubilarte.</li>
</ul>

<h2>Antes de amortizar, revisa esto</h2>
<ol>
  <li><strong>Fondo de emergencia</strong>: no amortices si te quedas sin colchón. El dinero que metes en la hipoteca no
  se puede recuperar.</li>
  <li><strong>Deudas más caras</strong>: tarjetas revolving, préstamos personales o coche van primero.</li>
  <li><strong>Comisión por amortización anticipada</strong> (Ley 5/2019):
    <ul>
      <li>Hipoteca variable: máximo un 0,25 % durante los 3 primeros años o un 0,15 % durante los 5 primeros, según el
      contrato. Después, 0 %.</li>
      <li>Hipoteca fija: máximo un 2 % durante los 10 primeros años y un 1,5 % a partir de entonces.</li>
    </ul>
  </li>
  <li><strong>Deducción por vivienda habitual</strong>: si compraste antes de 2013 y aplicas el régimen transitorio,
  puede interesarte amortizar hasta completar los 9.040 € anuales deducibles.</li>
  <li><strong>Vinculaciones</strong>: comprueba que amortizar no te hace perder bonificaciones del tipo.</li>
</ol>

<p class="nota-info">Regla práctica: si dudas, amortiza reduciendo plazo. Siempre podrás pedir más adelante una
novación para bajar la cuota si la necesitas, aunque eso tendrá costes.</p>
""" + AVISO_FINANZAS,
    },
    {
        'slug': 'euribor-2026-hipoteca',
        'titulo': 'Euríbor en 2026: cómo afecta a tu hipoteca y qué puedes hacer',
        'resumen': 'El Euríbor cerró julio en el 2,855 %, máximo desde septiembre de 2024. Calculamos el impacto en '
                   'una hipoteca media y repasamos tus opciones: esperar, pasar a fijo, cambiar de banco o amortizar.',
        'categoria': 'Hipotecas',
        'palabra_clave': 'Euríbor 2026',
        'icono': '📈',
        'minutos_lectura': 7,
        'contenido': """
<p>Tras dos años de bajadas, el Euríbor ha vuelto a subir. Cerró julio de 2026 en el <strong>2,855 %</strong>, su
nivel más alto desde septiembre de 2024. Para quien tiene una hipoteca variable, la revisión anual vuelve a doler.</p>

<h2>Cuánto sube tu cuota: un ejemplo</h2>
<p>Hipoteca variable con 150.000 € pendientes, 25 años por delante y un diferencial de Euríbor + 0,80 %:</p>
<table>
  <thead><tr><th></th><th>Euríbor 2,10 %</th><th>Euríbor 2,855 %</th></tr></thead>
  <tbody>
    <tr><td>Tipo aplicado</td><td>2,90 %</td><td>3,655 %</td></tr>
    <tr><td>Cuota mensual</td><td>703,54 €</td><td>763,46 €</td></tr>
    <tr><td>Diferencia</td><td colspan="2"><strong>+59,92 €/mes ≈ +719 €/año</strong></td></tr>
  </tbody>
</table>
<p>Es una cifra muy cercana a la que estima Kelisto para la hipoteca variable media: unos 780 € más al año.</p>

<h2>¿Qué se espera?</h2>
<p>Las previsiones de Funcas apuntan a un Euríbor en torno al 2,68 % a finales de 2026 y al 2,52 % en 2027, es decir,
una ligera moderación. Pero las previsiones fallan a menudo: no tomes decisiones que solo funcionen si aciertan.</p>

<h2>Tus cinco opciones</h2>
<h3>1. No hacer nada</h3>
<p>Si la nueva cuota es asumible y te quedan pocos años, puede ser lo más sensato. Las subidas de tipos también
mejoran la rentabilidad de tus ahorros.</p>
<h3>2. Novación a tipo fijo o mixto con tu banco</h3>
<p>Cambias el tipo sin cambiar de entidad. Negocia: el banco no quiere perderte. Compara el tipo fijo ofrecido con lo
que pagarías si el Euríbor se mantiene.</p>
<h3>3. Subrogación a otro banco</h3>
<p>Llevas la hipoteca a otra entidad con mejores condiciones. La Ley 5/2019 limita la compensación por pasar de
variable a fijo al 0,15 % del capital durante los 3 primeros años del préstamo, y a cero después.</p>
<h3>4. Amortizar anticipadamente</h3>
<p>Si tienes ahorros por encima de tu fondo de emergencia, amortizar reduce el capital sobre el que se aplica el
Euríbor. Mira nuestro artículo sobre si conviene reducir plazo o cuota.</p>
<h3>5. Revisar vinculaciones y diferencial</h3>
<p>A veces el ahorro está en mejorar el diferencial con bonificaciones que ya tienes, como la nómina domiciliada.
Otras veces está en quitar seguros caros que no compensan.</p>

<h2>Checklist antes de decidir</h2>
<ul>
  <li>¿Cuánto supone la cuota sobre tus ingresos netos? Por encima del 35 %, prioriza la estabilidad.</li>
  <li>¿Cuántos años te quedan? Con menos de 8–10 años, cambiar a fijo suele compensar menos.</li>
  <li>¿Qué cuesta el cambio (notaría, registro, tasación y compensaciones)? Pide un desglose por escrito.</li>
  <li>Si tienes dificultades de pago, pregunta a tu banco por las medidas del Código de Buenas Prácticas y comprueba
  si cumples los requisitos.</li>
</ul>
""" + AVISO_FINANZAS,
    },
    {
        'slug': 'fondo-de-emergencia',
        'titulo': 'Fondo de emergencia: cuánto necesitas y dónde guardarlo en 2026',
        'resumen': 'Es la base de cualquier plan financiero. Cómo calcular tu cifra, dónde tenerlo para que rinda '
                   'sin perder liquidez y por qué tras el apagón conviene tener también algo de efectivo en casa.',
        'categoria': 'Ahorro',
        'palabra_clave': 'fondo de emergencia',
        'icono': '🛟',
        'minutos_lectura': 6,
        'contenido': """
<p>Un fondo de emergencia es dinero reservado <strong>solo</strong> para imprevistos: una avería, una baja, un despido
o una reparación urgente en casa. Su función es evitar que un problema puntual se convierta en una deuda cara.</p>

<h2>Cuánto necesitas</h2>
<p>La referencia habitual es entre <strong>3 y 6 meses de gastos esenciales</strong> (no de ingresos):</p>
<ul>
  <li><strong>3 meses</strong>: empleo estable, dos sueldos en casa, sin hijos.</li>
  <li><strong>6 meses</strong>: un solo sueldo, hijos a cargo o hipoteca.</li>
  <li><strong>9–12 meses</strong>: autónomos, ingresos variables o sectores inestables.</li>
</ul>

<h3>Ejemplo de cálculo</h3>
<table>
  <thead><tr><th>Gasto esencial mensual</th><th>Importe</th></tr></thead>
  <tbody>
    <tr><td>Alquiler o hipoteca</td><td>750 €</td></tr>
    <tr><td>Suministros (luz, agua, gas, internet)</td><td>150 €</td></tr>
    <tr><td>Comida</td><td>400 €</td></tr>
    <tr><td>Transporte</td><td>120 €</td></tr>
    <tr><td>Seguros y salud</td><td>80 €</td></tr>
    <tr><td>Otros imprescindibles</td><td>100 €</td></tr>
    <tr><td><strong>Total</strong></td><td><strong>1.600 €</strong></td></tr>
  </tbody>
</table>
<p>Fondo objetivo: entre <strong>4.800 €</strong> (3 meses) y <strong>9.600 €</strong> (6 meses).</p>

<h2>Dónde guardarlo</h2>
<p>Tiene que cumplir tres condiciones: <strong>seguro, líquido y separado</strong> de tu cuenta del día a día. La
rentabilidad es secundaria, aunque con los tipos actuales no hay excusa para tenerlo al 0 %.</p>
<ul>
  <li><strong>Cuenta remunerada</strong>: disponibilidad inmediata. Los depósitos están cubiertos por el Fondo de
  Garantía de Depósitos hasta 100.000 € por titular y entidad. Ideal para la parte que puedas necesitar mañana.</li>
  <li><strong>Letras del Tesoro</strong>: deuda del Estado a 3, 6, 9 o 12 meses. Puedes comprarlas sin comisiones en
  la web del Tesoro Público. Si necesitas el dinero antes del vencimiento, tendrás que venderlas en el mercado al
  precio que haya. Úsalas para la parte «profunda» del colchón, en escalera de vencimientos.</li>
  <li><strong>Fondo monetario</strong>: se recupera en 1–3 días hábiles y, como fondo de inversión, se puede traspasar
  sin tributar. Riesgo bajo, pero no está cubierto por el FGD.</li>
</ul>
<p class="nota-info">Estrategia mixta habitual: un mes de gastos en cuenta remunerada y el resto en Letras
escalonadas o en un fondo monetario.</p>

<h2>Lo que aprendimos del apagón</h2>
<p>El 28 de abril de 2025 muchos datáfonos y cajeros dejaron de funcionar durante horas. La Comisión Europea recomienda
a los ciudadanos estar preparados para ser autosuficientes durante 72 horas, y eso incluye <strong>algo de dinero en
efectivo</strong> en billetes pequeños. No hace falta mucho: lo suficiente para comida, farmacia y transporte durante
tres días.</p>

<h2>Fiscalidad</h2>
<p>Los intereses de cuentas y Letras tributan en la base del ahorro del IRPF: un 19 % para los primeros 6.000 € de
rendimientos y tipos crecientes a partir de ahí.</p>

<h2>Cómo construirlo sin sufrir</h2>
<ol>
  <li>Abre una cuenta solo para esto, mejor en otro banco para no verla a diario.</li>
  <li>Programa una transferencia automática el día que cobras.</li>
  <li>Empieza por un objetivo pequeño (1.000 €) y sube por tramos.</li>
  <li>Si lo usas, la prioridad número uno es reponerlo.</li>
</ol>
""" + AVISO_FINANZAS,
    },
    {
        'slug': 'compra-ahora-paga-despues',
        'titulo': '«Compra ahora, paga después»: cómo funciona y cuándo es una trampa',
        'resumen': 'Las búsquedas de BNPL han crecido un 577 % en cinco años. Te explicamos cómo funcionan los pagos '
                   'aplazados, qué cambia con la nueva directiva europea y las reglas para no endeudarte.',
        'categoria': 'Consumo',
        'palabra_clave': 'compra ahora paga después',
        'icono': '💳',
        'minutos_lectura': 6,
        'contenido': """
<p>«Paga en 3 plazos sin intereses» aparece ya en casi cualquier tienda online. Es el <em>Buy Now, Pay Later</em>
(BNPL), cuyas búsquedas han crecido un <strong>577 %</strong> en cinco años. Bien usado es cómodo. Mal usado, es la
forma más silenciosa de endeudarse.</p>

<h2>Cómo funciona</h2>
<ul>
  <li><strong>Fraccionamiento corto</strong>: divides la compra en 3–4 pagos, normalmente sin intereses. La tienda
  paga una comisión al proveedor del servicio.</li>
  <li><strong>Financiación larga</strong>: para compras grandes, a 6, 12 o más meses. Aquí suele haber intereses, a
  veces con una TAE elevada.</li>
</ul>
<p>En España lo ofrecen servicios como Klarna, PayPal (Paga en 3 plazos), Aplazame o SeQura, además de los propios
bancos con sus tarjetas.</p>

<h2>Los riesgos</h2>
<ol>
  <li><strong>Acumulación invisible</strong>: cada compra parece pequeña, pero cinco planes de pago activos suman una
  cuota mensual considerable.</li>
  <li><strong>Recargos por impago</strong>: si falla un cargo, puede haber comisiones e intereses de demora.</li>
  <li><strong>Ficheros de morosos</strong>: un impago puede acabar en un fichero de solvencia y complicarte una
  hipoteca o un préstamo.</li>
  <li><strong>Compra impulsiva</strong>: está diseñado para reducir la «fricción» de gastar.</li>
</ol>

<h2>Qué cambia con la nueva regulación</h2>
<p>La Directiva europea de crédito al consumo (UE) 2023/2225 incluye expresamente los pagos aplazados. Los Estados
debían trasponerla antes de noviembre de 2025 y se aplica desde noviembre de 2026. Obliga a evaluar la solvencia del
cliente y a dar información clara sobre costes, también en las compras pequeñas.</p>

<h2>Cinco reglas para usarlo bien</h2>
<ol>
  <li>Solo para compras <strong>planificadas</strong> que podrías pagar al contado hoy.</li>
  <li>Nunca más de uno o dos planes activos a la vez.</li>
  <li>Apunta las fechas de cargo en el calendario y asegúrate de tener saldo.</li>
  <li>Lee la TAE en las financiaciones largas: compárala con un préstamo personal.</li>
  <li>Nunca lo uses para gastos corrientes (comida, facturas): es la señal de que el presupuesto no cuadra.</li>
</ol>

<div class="aviso"><p><strong>Ojo con las tarjetas revolving.</strong> Si te ofrecen «pagar poco a poco» con una
tarjeta de crédito, comprueba la TAE: en este producto es habitual que supere el 20 %.</p></div>
""" + AVISO_FINANZAS,
    },
]

PRODUCTOS = [
    {
        'slug': 'letras-del-tesoro',
        'nombre': 'Letras del Tesoro (compra directa)',
        'marca': 'Tesoro Público',
        'categoria': 'Ahorro',
        'icono': '🏛️',
        'resumen': 'Deuda pública española a corto plazo que se compra sin comisiones en la web del Tesoro. '
                   'Muy segura y con rentabilidad ligada a los tipos del BCE.',
        'ideal_para': 'Ahorro a 3–12 meses y la parte «profunda» del fondo de emergencia',
        'precio_orientativo': 'Desde 1.000 €',
        'puntuacion': '8.8',
        'destacado': True,
        'pros': [
            'Riesgo muy bajo: las emite el Estado',
            'Sin comisiones comprando en la cuenta directa del Tesoro',
            'Rendimientos sin retención (se declaran en la renta)',
        ],
        'contras': [
            'Para recuperar el dinero antes del vencimiento hay que venderlas en el mercado',
            'La subasta fija el precio: no sabes la rentabilidad exacta hasta que se celebra',
        ],
        'especificaciones': {
            'Plazos': '3, 6, 9 y 12 meses',
            'Importe mínimo': '1.000 € y múltiplos',
            'Comisiones': '0 € en la cuenta directa del Tesoro',
            'Fiscalidad': 'Rendimiento del capital mobiliario, sin retención',
        },
    },
    {
        'slug': 'cuenta-remunerada',
        'nombre': 'Cuenta remunerada sin comisiones',
        'marca': 'Varias entidades',
        'categoria': 'Ahorro',
        'icono': '🏦',
        'resumen': 'Cuenta que paga intereses por tu saldo, con disponibilidad inmediata y protegida por el Fondo de '
                   'Garantía de Depósitos.',
        'ideal_para': 'La parte del fondo de emergencia que puedes necesitar mañana',
        'precio_orientativo': 'Gratis',
        'puntuacion': '8.5',
        'pros': [
            'Liquidez inmediata',
            'Cubierta hasta 100.000 € por titular y entidad',
            'Sin riesgo de mercado',
        ],
        'contras': [
            'Muchas ofertas tienen límite de saldo o duración',
            'Algunas exigen vinculación (nómina, recibos)',
        ],
        'especificaciones': {
            'Garantía': 'Fondo de Garantía de Depósitos (hasta 100.000 €)',
            'Liquidez': 'Inmediata',
            'Fiscalidad': 'Retención del 19 % sobre los intereses',
        },
        'contenido': """
<p>Compara siempre la TAE, el saldo máximo remunerado, la duración de la oferta y las condiciones de permanencia.
Desconfía de las rentabilidades muy por encima del mercado que exigen contratar otros productos.</p>
""",
    },
    {
        'slug': 'roboadvisor-indexado',
        'nombre': 'Roboadvisor de fondos indexados',
        'marca': 'Varias (Indexa Capital, MyInvestor, Finizens…)',
        'categoria': 'Inversión',
        'icono': '📊',
        'resumen': 'Gestión automatizada de una cartera diversificada de fondos indexados según tu perfil de riesgo. '
                   'Rebalancea por ti y es traspasable sin tributar.',
        'ideal_para': 'Invertir a largo plazo sin tener que elegir fondos',
        'precio_orientativo': 'Comisión total ≈ 0,4–0,8 % al año',
        'puntuacion': '8.6',
        'pros': [
            'Diversificación mundial desde importes bajos',
            'Rebalanceo automático',
            'Ventajas fiscales de los fondos traspasables',
        ],
        'contras': [
            'La bolsa puede caer mucho a corto plazo',
            'Las comisiones, aunque bajas, se suman cada año',
        ],
        'especificaciones': {
            'Horizonte recomendado': '10 años o más',
            'Fiscalidad': 'Traspasos entre fondos sin tributar',
            'Riesgo': 'Según el perfil elegido',
        },
    },
    {
        'slug': 'app-fintonic',
        'nombre': 'Fintonic',
        'marca': 'Fintonic',
        'categoria': 'Apps',
        'icono': '📱',
        'resumen': 'App española que agrupa tus cuentas y tarjetas, categoriza los gastos automáticamente y avisa de '
                   'cargos y comisiones.',
        'ideal_para': 'Saber en qué se va el dinero cada mes',
        'precio_orientativo': 'Gratis',
        'puntuacion': '7.9',
        'pros': [
            'Conecta con la mayoría de bancos españoles',
            'Categorización automática de gastos',
            'Alertas de recibos y comisiones',
        ],
        'contras': [
            'Te ofrecerá productos financieros propios y de terceros',
            'Debes dar acceso de lectura a tus cuentas',
        ],
        'especificaciones': {
            'Plataformas': 'iOS y Android',
            'Funciones': 'Agregador de cuentas, presupuestos y alertas',
        },
    },
    {
        'slug': 'libro-bogle',
        'nombre': 'El pequeño libro para invertir con sentido común',
        'marca': 'John C. Bogle',
        'categoria': 'Libros',
        'icono': '📘',
        'resumen': 'El clásico del fundador de Vanguard sobre por qué los fondos indexados de bajo coste ganan a la '
                   'mayoría de gestores a largo plazo.',
        'ideal_para': 'Entender la inversión pasiva antes de empezar',
        'precio_orientativo': '≈ 15–20 €',
        'puntuacion': '9.0',
        'pros': [
            'Breve, claro y con datos',
            'Cambia la forma de ver las comisiones',
        ],
        'contras': [
            'Ejemplos centrados en EE. UU.',
        ],
        'especificaciones': {
            'Autor': 'John C. Bogle',
            'Tema': 'Inversión indexada',
        },
    },
    {
        'slug': 'libro-psicologia-del-dinero',
        'nombre': 'La psicología del dinero',
        'marca': 'Morgan Housel',
        'categoria': 'Libros',
        'icono': '📗',
        'resumen': 'Historias breves sobre cómo nuestras emociones y sesgos deciden más que las fórmulas en lo que '
                   'hacemos con el dinero.',
        'ideal_para': 'Mejorar hábitos financieros sin tecnicismos',
        'precio_orientativo': '≈ 15–20 €',
        'puntuacion': '8.9',
        'pros': [
            'Muy ameno, capítulos cortos',
            'Ideas aplicables desde el primer día',
        ],
        'contras': [
            'No es un manual práctico paso a paso',
        ],
        'especificaciones': {
            'Autor': 'Morgan Housel',
            'Tema': 'Comportamiento y hábitos financieros',
        },
    },
]

COMPARATIVAS = [
    {
        'slug': 'diesel-gasolina-hibrido-electrico',
        'titulo': 'Diésel, gasolina, híbrido o eléctrico: cuál compensa en 2026',
        'resumen': '«Diésel o gasolina» fue una de las comparativas más buscadas en España. La ampliamos con híbridos '
                   'y eléctricos: coste por kilómetro, etiqueta DGT, zonas de bajas emisiones y mantenimiento.',
        'icono': '🚗',
        'destacado': True,
        'introduccion': """
<p>La pregunta clásica ya no tiene dos respuestas, sino cuatro. Además del precio del combustible, ahora pesan la
<strong>etiqueta ambiental de la DGT</strong> y las <strong>zonas de bajas emisiones (ZBE)</strong>, obligatorias en
los municipios de más de 50.000 habitantes desde la Ley de Cambio Climático.</p>
<p>*Coste de energía calculado con supuestos orientativos: gasóleo ≈ 1,45 €/l, gasolina ≈ 1,55 €/l y electricidad
doméstica en horario valle ≈ 0,15–0,22 €/kWh. Recalcúlalo con tus precios.</p>
""",
        'columnas': ['Diésel', 'Gasolina', 'Híbrido (HEV)', 'Eléctrico (BEV)'],
        'filas': [
            ['Etiqueta DGT (coche nuevo)', 'C', 'C', 'ECO', '0 emisiones'],
            ['Acceso a ZBE', 'Con restricciones en algunas ciudades', 'Con restricciones en algunas ciudades', 'Amplio', 'Total'],
            ['Precio de compra', 'Medio-alto', 'El más bajo', 'Medio', 'Alto (consulta ayudas vigentes)'],
            ['Consumo orientativo', '≈ 4,5–5,5 l/100 km', '≈ 5,5–7 l/100 km', '≈ 4–5 l/100 km', '≈ 14–18 kWh/100 km'],
            ['Coste de energía por 100 km*', '≈ 6,5–8 €', '≈ 8,5–11 €', '≈ 6–8 €', '≈ 2–4 € cargando en casa'],
            ['Coste anual a 15.000 km*', '≈ 1.090 €', '≈ 1.450 €', '≈ 1.050 €', '≈ 430 €'],
            ['Mantenimiento', 'Más caro (FAP, AdBlue, EGR)', 'Medio', 'Medio', 'El más bajo'],
            ['Ideal si', 'Haces más de 20.000 km/año en carretera', 'Haces pocos km y uso mixto', 'Conduces mucho por ciudad', 'Puedes cargar en casa o en el trabajo'],
        ],
        'ganador': 'Híbrido (HEV)',
        'veredicto': """
<p><strong>Para la mayoría de conductores sin punto de carga propio, el híbrido (HEV) es la opción más equilibrada</strong>:
etiqueta ECO, consumo bajo en ciudad y sin cambiar de hábitos.</p>
<ul>
  <li>Si <strong>puedes cargar en casa</strong>, el eléctrico es el que menos cuesta por kilómetro, con diferencia.</li>
  <li>El <strong>diésel</strong> solo compensa si haces muchos kilómetros por carretera y no dependes de entrar en ZBE.</li>
  <li>La <strong>gasolina</strong> es la opción barata de compra para quien conduce poco.</li>
</ul>
""",
    },
    {
        'slug': 'donde-guardar-tus-ahorros',
        'titulo': 'Cuenta remunerada vs Letras del Tesoro vs fondo monetario vs fondo indexado',
        'resumen': 'Cuatro sitios para tu dinero con riesgos, plazos y fiscalidad muy distintos. Qué usar para el '
                   'fondo de emergencia, para el ahorro a corto plazo y para invertir a largo.',
        'icono': '🏦',
        'introduccion': """
<p>No hay un «mejor producto», sino el producto adecuado para cada <strong>plazo</strong>. La regla de oro: el dinero
que puedes necesitar en menos de 3–5 años no debería estar en bolsa.</p>
""",
        'columnas': ['Cuenta remunerada', 'Letras del Tesoro', 'Fondo monetario', 'Fondo indexado'],
        'filas': [
            ['Para qué sirve', 'Fondo de emergencia', 'Ahorro a 3–12 meses', 'Aparcar dinero con liquidez', 'Invertir a 10 años o más'],
            ['Riesgo', 'Muy bajo (FGD hasta 100.000 €)', 'Muy bajo (deuda del Estado)', 'Bajo', 'Alto a corto plazo'],
            ['Liquidez', 'Inmediata', 'Al vencimiento (o venta en mercado)', '1–3 días hábiles', '2–4 días hábiles'],
            ['Rentabilidad', 'Según la oferta del banco', 'Ligada a los tipos del BCE', 'Ligada a los tipos del BCE', 'Mayor a largo plazo, con altibajos'],
            ['Comisiones', 'Normalmente ninguna', 'Ninguna comprando en el Tesoro', 'Bajas', 'Bajas en indexados'],
            ['Fiscalidad', 'Tributa cada año (retención 19 %)', 'Tributa al vencimiento, sin retención', 'Traspasable sin tributar', 'Traspasable sin tributar'],
            ['Ideal para', 'Tener el dinero siempre a mano', 'Gastos con fecha conocida', 'Esperar una decisión', 'Jubilación y patrimonio'],
        ],
        'ganador': '',
        'veredicto': """
<p><strong>Úsalos por capas.</strong> Pon un mes de gastos en una cuenta remunerada y el resto del fondo de
emergencia en Letras escalonadas o en un fondo monetario. A partir de ahí, el dinero que no vas a tocar en 10 años
puede ir a fondos indexados, idealmente con aportaciones periódicas.</p>
""",
        'productos': ['cuenta-remunerada', 'letras-del-tesoro', 'roboadvisor-indexado'],
    },
    {
        'slug': 'hipoteca-fija-variable-mixta',
        'titulo': 'Hipoteca fija, variable o mixta en 2026',
        'resumen': 'Con el Euríbor de nuevo al alza, ¿qué tipo de hipoteca conviene firmar? Comparamos estabilidad, '
                   'coste esperado y comisiones.',
        'icono': '🔑',
        'introduccion': """
<p>Elegir el tipo de hipoteca es apostar por cómo evolucionarán los tipos de interés durante décadas. Como nadie lo
sabe, la pregunta correcta es otra: <strong>¿cuánta incertidumbre puede soportar tu economía familiar?</strong></p>
""",
        'columnas': ['Fija', 'Variable', 'Mixta'],
        'filas': [
            ['Cuota', 'Igual toda la vida del préstamo', 'Cambia en cada revisión según el Euríbor', 'Fija unos años y después variable'],
            ['Riesgo de subida', 'Ninguno', 'Total', 'Solo en el tramo variable'],
            ['Tipo inicial', 'Más alto', 'Más bajo si el Euríbor baja', 'Intermedio'],
            ['Comisión máxima por amortizar (Ley 5/2019)', '2 % los 10 primeros años; 1,5 % después', '0,25 % los 3 primeros años o 0,15 % los 5 primeros', 'Según el tramo y el contrato'],
            ['Ideal para', 'Presupuestos ajustados y plazos largos', 'Plazos cortos y colchón para subidas', 'Quien quiere estabilidad los primeros años'],
        ],
        'ganador': 'Fija',
        'veredicto': """
<p><strong>Para la mayoría de compradores de primera vivienda con plazos de 25–30 años, la fija aporta la tranquilidad
que necesita un presupuesto familiar.</strong> La variable puede salir más barata si los tipos bajan, pero solo es
recomendable si tu cuota sigue siendo cómoda con un Euríbor 2–3 puntos más alto. La mixta es un término medio útil si
prevés ingresos mayores en el futuro.</p>
""",
    },
]

TENDENCIAS = [
    {
        'slug': 'amortizar-plazo-o-cuota',
        'nombre': '¿Amortizar plazo o cuota?',
        'icono': '🏠',
        'estado': 'consolidada',
        'dato': 'Top comparativa en España 2025',
        'fuente': 'Google Year in Search 2025',
        'fuente_url': 'https://trends.withgoogle.com/year-in-search/2025/es/',
        'articulo': 'amortizar-plazo-o-cuota',
        'descripcion': '<p>Una de las grandes dudas financieras del año. La respuesta corta: reducir plazo ahorra más '
                       'intereses; reducir cuota da más margen mensual.</p>',
    },
    {
        'slug': 'euribor-al-alza',
        'nombre': 'Euríbor al alza',
        'icono': '📈',
        'estado': 'en_auge',
        'dato': '2,855 % en julio de 2026',
        'fuente': 'Europa Press / Bolsamanía',
        'fuente_url': 'https://www.bolsamania.com/noticias/mercados/economia--el-euribor-cierra-julio-en-el-2855-su-nivel-mas-alto-desde-septiembre-de-2024-y-avanza-alzas-hipotecarias--23165224.html',
        'articulo': 'euribor-2026-hipoteca',
        'descripcion': '<p>Máximo desde septiembre de 2024. Las revisiones anuales de las hipotecas variables vuelven '
                       'a encarecer la cuota.</p>',
    },
    {
        'slug': 'compra-ahora-paga-despues',
        'nombre': 'Compra ahora, paga después',
        'icono': '💳',
        'estado': 'en_auge',
        'dato': '+577 % en 5 años',
        'fuente': 'Exploding Topics',
        'fuente_url': 'https://explodingtopics.com/blog/consumer-behavior',
        'articulo': 'compra-ahora-paga-despues',
        'descripcion': '<p>La mitad de los adultos en EE. UU. ya lo ha usado y en Europa llega una regulación más '
                       'estricta desde noviembre de 2026.</p>',
    },
    {
        'slug': 'diesel-o-gasolina',
        'nombre': '¿Diésel o gasolina?',
        'icono': '🚗',
        'estado': 'consolidada',
        'dato': 'Top comparativa en España 2025',
        'fuente': 'Google Year in Search 2025',
        'fuente_url': 'https://trends.withgoogle.com/year-in-search/2025/es/',
        'descripcion': '<p>Comprar coche sigue siendo una de las grandes decisiones de gasto. Ahora con la etiqueta DGT '
                       'y las ZBE como factores clave.</p>',
    },
    {
        'slug': 'blindar-los-ahorros',
        'nombre': 'Blindar los ahorros',
        'icono': '🛟',
        'estado': 'consolidada',
        'fuente': 'Google España, 2025 en búsquedas',
        'fuente_url': 'https://blog.google/intl/es-es/productos/2025-en-busquedas-de-google-espana-busca-respuestas-entre-el-apagon-la-ia-consultas-financieras-y-muchas-mas-preguntas/',
        'articulo': 'fondo-de-emergencia',
        'descripcion': '<p>Las búsquedas reflejan preocupación por proteger los ahorros y el empleo, y por prepararse '
                       'para crisis económicas.</p>',
    },
]
