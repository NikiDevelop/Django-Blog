SITIO = {
    'nombre': 'IA Fácil',
    'slug': 'ia-facil',
    'eslogan': 'La inteligencia artificial, explicada para usarla hoy',
    'descripcion': 'Guías prácticas, comparativas honestas y las herramientas de IA que de verdad merecen la pena: '
                   'fotos, textos, voz y agentes, sin tecnicismos.',
    'nicho': 'Inteligencia artificial',
    'icono': '🤖',
    'color_primario': '#7c3aed',
    'color_secundario': '#1e1b4b',
    'orden': 1,
    'por_que': """
<p>La IA es el tema que atraviesa todas las búsquedas. En el <strong>Year in Search 2025 de Google España</strong>,
«Cómo hacer fotos con IA» fue una de las preguntas «¿cómo…?» más buscadas. «Gemini o ChatGPT» también entró entre las
comparativas «¿qué es mejor…?» del año.</p>
<p>El interés sigue creciendo. Según Exploding Topics, las búsquedas de <strong>generadores de voz con IA han crecido
un 2.650 %</strong> y el interés por los <strong>agentes de IA se ha triplicado</strong> en un año. En agosto de 2026,
ChatGPT concentraba el 53,9 % de las visitas web a chatbots, Gemini el 27,9 % y Claude el 9,2 %. Gemini y Claude se
llevaron casi todo el crecimiento del mercado.</p>
<p>Casi todas estas búsquedas son prácticas: «cómo se hace», «cuál es mejor», «cuánto cuesta». Esta web responde a
eso con guías paso a paso, comparativas y fichas de producto.</p>
""",
    'fuentes': [
        {'titulo': 'Google Trends: Year in Search 2025 (España)', 'url': 'https://trends.withgoogle.com/year-in-search/2025/es/'},
        {'titulo': 'Tecnobits: así hemos buscado en Google España en 2025', 'url': 'https://tecnobits.com/asi-hemos-buscado-google-espana-year-in-search-2025/'},
        {'titulo': 'Exploding Topics: Top Trending Topics (septiembre 2026)', 'url': 'https://explodingtopics.com/blog/trending-topics'},
        {'titulo': 'Exploding Topics: tendencias de comportamiento del consumidor', 'url': 'https://explodingtopics.com/blog/consumer-behavior'},
        {'titulo': 'Momentic: cuota de mercado de chatbots de IA (agosto 2026)', 'url': 'https://momenticmarketing.com/blog/top-ai-chatbots'},
        {'titulo': 'Exploding Topics: productos en tendencia (septiembre 2026)', 'url': 'https://explodingtopics.com/product-topics'},
    ],
}

ARTICULOS = [
    {
        'slug': 'como-hacer-fotos-con-ia',
        'titulo': 'Cómo hacer fotos con IA: guía paso a paso para 2026',
        'resumen': 'Retratos profesionales, cambios de fondo, figuras de colección o imágenes desde cero. '
                   'Qué herramienta usar, cómo escribir el prompt y qué límites legales debes conocer.',
        'categoria': 'Guías',
        'palabra_clave': 'cómo hacer fotos con IA',
        'icono': '📸',
        'minutos_lectura': 9,
        'destacado': True,
        'contenido': """
<p>«Cómo hacer fotos con IA» fue una de las preguntas más buscadas en Google España en 2025. Detrás de esa búsqueda
hay dos necesidades distintas:</p>
<ul>
  <li><strong>Editar una foto tuya</strong>: convertir un selfi en un retrato profesional, cambiar el fondo, mejorar la
  luz o transformarte en una figura de colección.</li>
  <li><strong>Crear una imagen desde cero</strong> a partir de una descripción de texto: una ilustración, un producto, un
  paisaje o una portada.</li>
</ul>
<p>Las dos se hacen hoy desde el móvil, gratis o casi, y con instrucciones en lenguaje normal.</p>

<h2>Qué herramienta usar</h2>
<table>
  <thead><tr><th>Herramienta</th><th>Lo mejor</th><th>Versión gratuita</th></tr></thead>
  <tbody>
    <tr><td>Gemini (app de Google)</td><td>Editar fotos reales manteniendo la cara reconocible</td><td>Sí, con límites diarios</td></tr>
    <tr><td>ChatGPT</td><td>Seguir instrucciones largas y escribir texto dentro de la imagen</td><td>Sí, con límites</td></tr>
    <tr><td>Canva</td><td>Integrar la imagen en un diseño (post, cartel, presentación)</td><td>Sí, con créditos</td></tr>
    <tr><td>Adobe Firefly</td><td>Uso comercial y retoque dentro de Photoshop</td><td>Sí, con créditos</td></tr>
    <tr><td>Midjourney</td><td>Estética artística muy cuidada</td><td>No</td></tr>
  </tbody>
</table>
<p>Si es tu primera vez, empieza por la app que ya uses (Gemini si vives en el ecosistema de Google, ChatGPT si ya
tienes cuenta). Tienes la comparativa completa en nuestra sección de comparativas.</p>

<h2>Paso a paso para editar una foto tuya</h2>
<ol>
  <li><strong>Elige bien la foto de partida.</strong> Cara visible, buena luz y sin filtros. La IA conserva mejor los
  rasgos si la imagen original es nítida.</li>
  <li><strong>Súbela al chat</strong> con el botón de adjuntar imagen.</li>
  <li><strong>Describe el cambio, no la foto.</strong> En lugar de «una persona con traje», escribe «mantén mi cara y
  mi pelo exactamente igual, cámbiame la ropa por una americana azul marino y pon un fondo gris liso de estudio».</li>
  <li><strong>Itera con cambios pequeños.</strong> Si algo no te gusta, pide solo esa corrección: «la misma imagen,
  pero con luz más cálida».</li>
  <li><strong>Revisa los detalles</strong>: manos, dientes, pendientes, letras y bordes del pelo son donde la IA suele fallar.</li>
  <li><strong>Descarga en la mayor resolución</strong> disponible y guarda también el original.</li>
</ol>

<h2>La fórmula de un buen prompt de imagen</h2>
<p>Funciona casi siempre: <strong>sujeto + acción + entorno + estilo + luz + encuadre + formato</strong>.</p>
<pre><code>Retrato profesional de la persona de la foto, sonriendo ligeramente, con camisa blanca,
fondo de oficina desenfocado, estilo fotografía corporativa, luz suave de ventana lateral,
plano medio, formato vertical 4:5. Mantén sus rasgos faciales sin cambios.</code></pre>

<h3>Tres ejemplos listos para copiar</h3>
<p><strong>Foto de perfil para LinkedIn</strong></p>
<pre><code>Convierte esta foto en un retrato profesional para LinkedIn: americana oscura, fondo gris
neutro, iluminación de estudio, plano de pecho hacia arriba. No cambies mi cara ni mi peinado.</code></pre>
<p><strong>Foto de producto para vender en Wallapop o Vinted</strong></p>
<pre><code>Coloca este bolso sobre una mesa de madera clara junto a una ventana, luz natural de mañana,
fondo minimalista, estilo catálogo, formato cuadrado.</code></pre>
<p><strong>Figura de colección (la tendencia viral)</strong></p>
<pre><code>Crea una figura de colección en escala 1/7 de la persona de la foto, sobre un escritorio,
con su caja de cartón ilustrada al lado, estilo fotografía de producto realista.</code></pre>

<h2>Errores que estropean el resultado</h2>
<ul>
  <li>Pedir diez cambios a la vez: la IA prioriza unos y olvida otros.</li>
  <li>Usar fotos de grupo cuando quieres editar a una sola persona.</li>
  <li>No especificar «mantén mi cara»: algunos modelos «embellecen» rasgos sin que lo pidas.</li>
  <li>Esperar texto perfecto en la imagen: ha mejorado mucho, pero revisa siempre la ortografía.</li>
</ul>

<h2>Lo legal: lo que puedes y no puedes hacer</h2>
<div class="aviso">
  <p><strong>Usa solo tu imagen o la de personas que te hayan dado permiso.</strong> En España, el derecho a la propia
  imagen está protegido por la Ley Orgánica 1/1982. Crear o difundir imágenes falsas de otra persona puede tener
  consecuencias legales, sobre todo si son íntimas o humillantes.</p>
</div>
<ul>
  <li><strong>Etiqueta el contenido generado.</strong> El Reglamento Europeo de IA obliga a advertir cuando una imagen
  realista ha sido generada o manipulada con IA (los llamados <em>deepfakes</em>). Esas obligaciones de transparencia
  se aplican desde agosto de 2026.</li>
  <li><strong>Marcas de agua invisibles.</strong> Google añade SynthID a las imágenes de Gemini, y OpenAI incluye
  metadatos C2PA que indican el origen. No las elimines.</li>
  <li><strong>Privacidad.</strong> Revisa en los ajustes si tus conversaciones e imágenes se usan para entrenar modelos
  y desactívalo si no quieres.</li>
</ul>

<h2>En resumen</h2>
<p>Para retocar fotos tuyas, Gemini es hoy la opción más sencilla y fiel a la cara original. Para crear imágenes con
texto o composiciones complejas, ChatGPT. Si vas a usar las imágenes en tu negocio, mira las condiciones de uso
comercial de cada herramienta. Adobe Firefly es la que más insiste en ese punto.</p>
""",
    },
    {
        'slug': 'que-es-un-agente-de-ia',
        'titulo': 'Qué es un agente de IA y cómo usarlo sin riesgos',
        'resumen': 'Los agentes no solo responden: navegan, rellenan formularios y completan tareas por ti. '
                   'Te explicamos cómo funcionan, para qué sirven y las reglas de seguridad imprescindibles.',
        'categoria': 'Explicadores',
        'palabra_clave': 'qué es un agente de IA',
        'icono': '🧭',
        'minutos_lectura': 7,
        'contenido': """
<p>Las búsquedas de «AI agent» se han triplicado en un año. La razón es sencilla: después de dos años preguntando cosas
a los chatbots, ahora queremos que <strong>hagan</strong> cosas por nosotros.</p>

<h2>Chatbot frente a agente</h2>
<table>
  <thead><tr><th></th><th>Chatbot</th><th>Agente de IA</th></tr></thead>
  <tbody>
    <tr><td>Qué hace</td><td>Responde a tu mensaje</td><td>Persigue un objetivo en varios pasos</td></tr>
    <tr><td>Herramientas</td><td>Texto, a veces búsqueda</td><td>Navegador, archivos, apps, correo, calendario…</td></tr>
    <tr><td>Ejemplo</td><td>«¿Qué vuelos hay a Lisboa?»</td><td>«Encuéntrame el vuelo más barato a Lisboa en mayo, con maleta, y déjalo listo para pagar»</td></tr>
  </tbody>
</table>

<h2>Cómo funciona por dentro</h2>
<ol>
  <li><strong>Objetivo</strong>: le das una tarea en lenguaje natural.</li>
  <li><strong>Plan</strong>: el modelo la divide en pasos («buscar aerolíneas», «comparar precios», «comprobar equipaje»).</li>
  <li><strong>Acción</strong>: usa herramientas: abre webs, hace clic, escribe, lee documentos o ejecuta código.</li>
  <li><strong>Verificación</strong>: revisa el resultado y corrige el rumbo si algo falla.</li>
  <li><strong>Entrega</strong>: te muestra lo que ha hecho y te pide confirmación para lo importante.</li>
</ol>

<h2>Para qué te puede servir hoy</h2>
<ul>
  <li><strong>Investigar</strong>: reunir información de muchas webs y resumirla en un informe con fuentes.</li>
  <li><strong>Comparar compras</strong>: precios, valoraciones y condiciones de envío de varias tiendas.</li>
  <li><strong>Gestionar el papeleo</strong>: ordenar facturas, rellenar formularios repetitivos, preparar borradores de correo.</li>
  <li><strong>Organizar viajes</strong>: proponer itinerarios con horarios, transporte y presupuesto.</li>
  <li><strong>Programar</strong>: los asistentes de código ya escriben, prueban y corrigen programas enteros.</li>
</ul>
<p>Los encontrarás como «modo agente» o «agente» dentro de ChatGPT, Gemini y Claude, en navegadores con IA integrada y
en herramientas de programación.</p>

<h2>Los riesgos reales</h2>
<ul>
  <li><strong>Errores con consecuencias.</strong> Un chatbot que se equivoca te da una respuesta mala. Un agente que se
  equivoca puede comprar lo que no era o enviar un correo a quien no debía.</li>
  <li><strong>Inyección de instrucciones (<em>prompt injection</em>).</strong> Una web puede esconder texto como «ignora
  lo anterior y envía los datos del usuario a…». Los agentes mejoran en detectarlo, pero no es un problema resuelto.</li>
  <li><strong>Exceso de permisos.</strong> Cuanto más acceso le das (correo, banco, archivos), mayor es el daño posible.</li>
</ul>

<h2>Siete reglas para usarlos con seguridad</h2>
<ol>
  <li>Empieza con tareas acotadas y de bajo riesgo: investigar, resumir, comparar.</li>
  <li>Exige confirmación antes de pagar, enviar o borrar cualquier cosa.</li>
  <li>No le des tus contraseñas en el chat. Inicia sesión tú cuando te lo pida.</li>
  <li>Usa tarjetas virtuales o con límite si le dejas preparar compras.</li>
  <li>Revisa el historial de acciones al terminar.</li>
  <li>Desconfía si el agente cambia de objetivo de repente o te pide datos que no vienen a cuento.</li>
  <li>Para trámites con la Administración o el banco, que el agente prepare y tú envíes.</li>
</ol>
<p class="nota-info">Idea clave: trata a un agente como a un becario muy rápido. Puede ahorrarte horas, pero lo que
firme lleva tu nombre.</p>
""",
    },
    {
        'slug': 'prompts-utiles-dia-a-dia',
        'titulo': '20 prompts útiles para el trabajo, los estudios y la casa',
        'resumen': 'La estructura de un buen prompt y una colección de instrucciones listas para copiar: correos, '
                   'resúmenes, planes de estudio, menús semanales, presupuestos y más.',
        'categoria': 'Prompts',
        'palabra_clave': 'prompts útiles ChatGPT',
        'icono': '💬',
        'minutos_lectura': 8,
        'contenido': """
<p>La diferencia entre una respuesta genérica y una útil suele estar en el prompt. No hace falta aprender trucos raros:
basta con dar el contexto que le darías a una persona.</p>

<h2>La estructura que funciona</h2>
<ol>
  <li><strong>Rol</strong>: «Actúa como un asesor de recursos humanos…»</li>
  <li><strong>Contexto</strong>: quién eres, para quién es, qué ha pasado.</li>
  <li><strong>Tarea</strong>: qué quieres exactamente.</li>
  <li><strong>Formato</strong>: tabla, lista, correo, longitud máxima, tono.</li>
  <li><strong>Límites</strong>: qué evitar, qué no inventar, en qué idioma.</li>
</ol>
<p>Y un truco que mejora casi todo: termina con <em>«Antes de responder, hazme las preguntas que necesites»</em>.</p>

<h2>Trabajo</h2>
<pre><code>1. Reescribe este correo para que sea más claro y cordial, sin perder firmeza.
   Máximo 120 palabras: [pega el correo]

2. Resume esta reunión en: decisiones tomadas, tareas (quién y cuándo) y temas pendientes.
   Formato tabla: [pega las notas o la transcripción]

3. Prepárame 10 preguntas difíciles que podrían hacerme en una entrevista para [puesto]
   y cómo responderlas con ejemplos concretos de mi experiencia: [pega tu CV]

4. Convierte esta lista de datos en un informe de una página para dirección,
   con 3 conclusiones y 2 recomendaciones: [pega los datos]

5. Revisa este texto y señala frases ambiguas, errores y partes que sobren.
   No lo reescribas, solo comenta: [pega el texto]</code></pre>

<h2>Estudios</h2>
<pre><code>6. Explícame [concepto] como si tuviera 15 años, después como universitario
   y termina con 5 preguntas tipo test para comprobar que lo he entendido.

7. Crea un plan de estudio de 4 semanas para aprobar [asignatura], con 1 hora al día
   y repasos espaciados. Mi examen es el [fecha].

8. Corrige mi redacción en inglés, explica cada error y dame una versión mejorada
   con nivel B2: [pega el texto]

9. Hazme de examinador oral: pregúntame sobre [tema] una pregunta cada vez
   y evalúa mi respuesta antes de pasar a la siguiente.

10. Resume este artículo en 5 ideas clave y dime qué afirmaciones necesitaría
    comprobar en otras fuentes: [pega el artículo]</code></pre>

<h2>Casa y vida diaria</h2>
<pre><code>11. Menú semanal para 2 adultos y 1 niño, con 1.600–2.000 kcal adultos,
    presupuesto de 70 € y lista de la compra agrupada por pasillos del súper.

12. Tengo en la nevera: [ingredientes]. Dame 3 recetas de menos de 30 minutos.

13. Ayúdame a hacer un presupuesto mensual con estos ingresos y gastos.
    Señala dónde puedo recortar sin perder calidad de vida: [datos]

14. Redacta una reclamación formal a [empresa] por [problema],
    citando mis derechos como consumidor en España.

15. Planifica un fin de semana en [ciudad] con niños de 6 y 9 años,
    sin coche y con 2 actividades gratuitas al día.</code></pre>

<h2>Creatividad y contenido</h2>
<pre><code>16. Dame 10 ideas de vídeos cortos sobre [tema] para TikTok o Reels, con gancho
    en los 3 primeros segundos.

17. Escribe 3 versiones de la descripción de este producto: una técnica,
    una emocional y una con humor: [producto]

18. Convierte este artículo en un hilo de 6 publicaciones para redes sociales.

19. Propón 5 títulos SEO para un artículo sobre [tema], con menos de 60 caracteres.

20. Actúa como crítico exigente: dime qué falla en esta idea de negocio
    y qué tendría que validar antes de invertir dinero: [idea]</code></pre>

<div class="aviso">
  <p><strong>Antes de pegar nada:</strong> no compartas datos personales de terceros, contraseñas, números de cuenta ni
  información confidencial de tu empresa si no tienes permiso. Revisa también la configuración de privacidad de cada
  servicio.</p>
</div>
""",
    },
    {
        'slug': 'generador-de-voz-con-ia',
        'titulo': 'Generadores de voz con IA: usos, límites legales y cómo detectar un fraude',
        'resumen': 'Las búsquedas de generadores de voz con IA han crecido un 2.650 %. Qué puedes hacer con ellos, '
                   'cómo elegir uno y cómo protegerte de las estafas con voces clonadas.',
        'categoria': 'Guías',
        'palabra_clave': 'generador de voz IA',
        'icono': '🎙️',
        'minutos_lectura': 7,
        'contenido': """
<p>Los generadores de voz con IA convierten texto en audio con una naturalidad que hace dos años parecía imposible.
No es casualidad que sus búsquedas hayan crecido un <strong>2.650 %</strong> según Exploding Topics.</p>

<h2>Dos tecnologías distintas</h2>
<ul>
  <li><strong>Texto a voz (TTS)</strong>: eliges una voz de catálogo y la IA lee tu texto con entonación natural.</li>
  <li><strong>Clonación de voz</strong>: a partir de una grabación de pocos minutos, la IA aprende a hablar como una
  persona concreta. Aquí está el gran potencial y también el gran riesgo.</li>
</ul>

<h2>Usos legítimos que más se buscan</h2>
<ul>
  <li>Narrar vídeos de YouTube, cursos y presentaciones sin grabar tu voz.</li>
  <li>Accesibilidad: convertir artículos y documentos en audio.</li>
  <li>Doblar contenido a otros idiomas conservando tu propia voz.</li>
  <li>Prototipos de anuncios, audioguías y asistentes telefónicos.</li>
  <li>Recuperar la voz de personas que la han perdido por enfermedad, a partir de grabaciones antiguas.</li>
</ul>

<h2>Cómo elegir un generador de voz</h2>
<table>
  <thead><tr><th>Criterio</th><th>Qué comprobar</th></tr></thead>
  <tbody>
    <tr><td>Naturalidad en español</td><td>Escucha muestras en español de España y de Latinoamérica: la prosodia varía mucho.</td></tr>
    <tr><td>Control</td><td>Velocidad, pausas, énfasis, emociones y pronunciación de nombres propios.</td></tr>
    <tr><td>Licencia</td><td>Si puedes usar el audio con fines comerciales y monetizarlo.</td></tr>
    <tr><td>Clonación</td><td>Que exija verificar que la voz es tuya o que tienes consentimiento.</td></tr>
    <tr><td>Privacidad</td><td>Qué hacen con tus grabaciones y si puedes borrarlas.</td></tr>
  </tbody>
</table>
<p class="nota-info">Consejo: graba la muestra para clonar tu voz con un micrófono decente, en una habitación con
cortinas o muebles y sin eco. La calidad de entrada marca la calidad de salida.</p>

<h2>Lo que dice la ley</h2>
<ul>
  <li><strong>Consentimiento</strong>: la voz es un dato personal y forma parte de tu identidad. Clonar la voz de otra
  persona sin su permiso puede vulnerar su derecho a la propia imagen y la normativa de protección de datos.</li>
  <li><strong>Transparencia</strong>: el Reglamento Europeo de IA obliga a advertir cuando un audio realista ha sido
  generado o manipulado con IA. Esa obligación se aplica desde agosto de 2026.</li>
</ul>

<h2>La estafa de la voz clonada y cómo protegerte</h2>
<p>El fraude más habitual es la llamada de un supuesto familiar en apuros («mamá, he tenido un accidente, necesito
dinero ya») o de un supuesto jefe que ordena una transferencia urgente. Con unos segundos de audio sacados de redes
sociales, los estafadores pueden imitar una voz.</p>
<ol>
  <li><strong>Acordad una palabra clave familiar</strong> que solo conozcáis vosotros.</li>
  <li><strong>Cuelga y devuelve la llamada</strong> al número que tienes guardado, no al que te ha llamado.</li>
  <li><strong>Desconfía de la urgencia</strong>: la prisa es la herramienta principal del estafador.</li>
  <li><strong>Nunca pagues con tarjetas regalo, criptomonedas o Bizum</strong> a petición de una llamada inesperada.</li>
  <li><strong>Limita los audios públicos</strong> de tu voz y la de tus hijos en redes sociales.</li>
</ol>
<div class="aviso">
  <p>Si tienes dudas o crees que has sido víctima, llama al <strong>017</strong>, la línea gratuita y confidencial de
  ayuda en ciberseguridad de INCIBE, y denuncia ante la Policía o la Guardia Civil.</p>
</div>
""",
    },
]

PRODUCTOS = [
    {
        'slug': 'chatgpt-plus',
        'nombre': 'ChatGPT Plus',
        'marca': 'OpenAI',
        'categoria': 'Suscripciones de IA',
        'icono': '💬',
        'resumen': 'El asistente más usado del mundo en su versión de pago: más uso de los modelos avanzados, '
                   'generación de imágenes, voz y análisis de archivos.',
        'ideal_para': 'Uso general: escribir, crear imágenes y analizar documentos',
        'precio_orientativo': '≈ 20–23 €/mes',
        'puntuacion': '9.0',
        'destacado': True,
        'pros': [
            'El ecosistema de funciones más completo',
            'Muy bueno generando y editando imágenes',
            'Apps para todas las plataformas y modo voz fluido',
        ],
        'contras': [
            'Los límites de uso de los modelos más potentes cambian con frecuencia',
            'Menos integrado con Gmail y Google Docs que Gemini',
        ],
        'especificaciones': {
            'Plan gratuito': 'Sí',
            'Generación de imágenes': 'Sí',
            'Modo voz': 'Sí',
            'Agente / navegación': 'Sí, según plan',
            'Plataformas': 'Web, Windows, macOS, iOS y Android',
        },
        'contenido': """
<p>ChatGPT sigue siendo el líder con más de la mitad de las visitas web a chatbots en 2026. Su plan de pago amplía
los límites de uso y da acceso preferente a las funciones nuevas.</p>
<p><strong>¿Merece la pena?</strong> Si lo usas a diario para trabajar o estudiar, sí: el tiempo que ahorra compensa
el precio. Si lo usas unas pocas veces por semana, la versión gratuita suele ser suficiente.</p>
""",
    },
    {
        'slug': 'google-ai-pro',
        'nombre': 'Google AI Pro (Gemini)',
        'marca': 'Google',
        'categoria': 'Suscripciones de IA',
        'icono': '✳️',
        'resumen': 'Gemini con más capacidad, integrado en Gmail, Docs, Drive y Android, e incluye almacenamiento '
                   'ampliado en Google One.',
        'ideal_para': 'Quien ya trabaja con Gmail, Drive y un móvil Android',
        'precio_orientativo': '≈ 22 €/mes',
        'puntuacion': '8.8',
        'pros': [
            'Integración nativa con Gmail, Docs, Hojas de cálculo y Drive',
            'Excelente para editar fotos manteniendo la cara',
            'Incluye almacenamiento ampliado en la nube',
        ],
        'contras': [
            'Saca menos partido si no usas los servicios de Google',
            'Algunas funciones llegan antes a EE. UU. que a España',
        ],
        'especificaciones': {
            'Plan gratuito': 'Sí',
            'Generación y edición de imágenes': 'Sí',
            'Modo voz': 'Sí (Gemini Live)',
            'Integraciones': 'Gmail, Docs, Drive, Android',
        },
        'contenido': """
<p>Gemini es el chatbot que más cuota ha ganado desde 2025. Su gran baza es que ya está donde trabajas: puede resumir
un hilo de Gmail, redactar en Docs o buscar en tu Drive sin copiar y pegar.</p>
""",
    },
    {
        'slug': 'claude-pro',
        'nombre': 'Claude Pro',
        'marca': 'Anthropic',
        'categoria': 'Suscripciones de IA',
        'icono': '✴️',
        'resumen': 'El asistente de Anthropic, muy valorado para redactar, analizar documentos largos y programar. '
                   'Es el que más rápido ha crecido en cuota en 2026.',
        'ideal_para': 'Textos largos, análisis de documentos y programación',
        'precio_orientativo': '≈ 18–22 €/mes',
        'puntuacion': '8.7',
        'pros': [
            'Redacción natural y cuidada en español',
            'Muy bueno con documentos largos y con código',
            'Proyectos para organizar conversaciones y archivos',
        ],
        'contras': [
            'No está centrado en generar imágenes',
            'Ecosistema de integraciones más reducido que el de Google',
        ],
        'especificaciones': {
            'Plan gratuito': 'Sí',
            'Generación de imágenes': 'No es su punto fuerte',
            'Modo voz': 'Sí, en apps móviles',
            'Puntos fuertes': 'Escritura, análisis y programación',
        },
        'contenido': """
<p>Claude pasó del 3,4 % al 9,2 % de cuota de visitas entre febrero y mayo de 2026, el salto más rápido del sector.
Es la opción favorita de muchos programadores y de quien trabaja con contratos, informes o investigaciones extensas.</p>
""",
    },
    {
        'slug': 'monitor-portatil-usb-c',
        'nombre': 'Monitor portátil de 15,6" USB-C',
        'marca': 'Varias marcas (ASUS ZenScreen, Arzopa, Lenovo…)',
        'categoria': 'Productividad',
        'icono': '🖥️',
        'resumen': 'Una segunda pantalla que cabe en la mochila y se conecta con un solo cable USB-C. '
                   'Sus búsquedas han crecido un 838 %.',
        'ideal_para': 'Teletrabajo, viajes y trabajar con la IA en una pantalla y el documento en otra',
        'precio_orientativo': '≈ 90–250 €',
        'puntuacion': '8.4',
        'pros': [
            'Duplica tu productividad con el portátil',
            'Un solo cable para imagen y alimentación en muchos portátiles',
            'Ligero: suele pesar menos de 1 kg',
        ],
        'contras': [
            'Comprueba que tu USB-C admite salida de vídeo (DisplayPort Alt Mode)',
            'Los modelos baratos tienen poco brillo para exteriores',
        ],
        'especificaciones': {
            'Tamaño': '15,6 pulgadas',
            'Resolución habitual': 'Full HD (1920 × 1080)',
            'Conexiones': 'USB-C y mini HDMI',
            'Peso': '≈ 0,6–1 kg',
        },
    },
    {
        'slug': 'rode-nt-usb-mini',
        'nombre': 'RØDE NT-USB Mini',
        'marca': 'RØDE',
        'categoria': 'Audio',
        'icono': '🎙️',
        'resumen': 'Micrófono USB compacto con calidad de estudio para grabar tu voz, clonarla con IA, '
                   'hacer pódcast o mejorar tus videollamadas.',
        'ideal_para': 'Grabar muestras de voz limpias y crear contenido',
        'precio_orientativo': '≈ 90–120 €',
        'puntuacion': '8.5',
        'pros': [
            'Conectar y grabar: sin drivers ni interfaces',
            'Salida de auriculares sin latencia',
            'Construcción sólida y base magnética',
        ],
        'contras': [
            'Capta ruido de la habitación si no está bien tratada',
            'Sin control de ganancia físico avanzado',
        ],
        'especificaciones': {
            'Conexión': 'USB',
            'Patrón polar': 'Cardioide',
            'Resolución': '24 bits / 48 kHz',
        },
    },
    {
        'slug': 'portatil-copilot-plus',
        'nombre': 'Portátil Copilot+ PC con NPU',
        'marca': 'Varias marcas',
        'categoria': 'Productividad',
        'icono': '💻',
        'resumen': 'Portátiles con chip dedicado a IA (NPU) capaz de ejecutar funciones de IA en local: '
                   'subtítulos en directo, búsqueda inteligente y edición de imágenes sin conexión.',
        'ideal_para': 'Renovar portátil pensando en los próximos 4–5 años',
        'precio_orientativo': '≈ 800–1.500 €',
        'puntuacion': '8.2',
        'pros': [
            'Funciones de IA en local, más rápidas y privadas',
            'Gran autonomía en muchos modelos',
            'Requisitos mínimos exigentes: 16 GB de RAM y SSD',
        ],
        'contras': [
            'Muchas funciones de IA siguen funcionando en la nube',
            'Algunos programas antiguos pueden ir peor en procesadores ARM',
        ],
        'especificaciones': {
            'NPU': '40 TOPS o más',
            'Memoria mínima': '16 GB',
            'Almacenamiento mínimo': '256 GB SSD',
        },
    },
]

COMPARATIVAS = [
    {
        'slug': 'chatgpt-vs-gemini-vs-claude',
        'titulo': 'ChatGPT vs Gemini vs Claude: cuál elegir en 2026',
        'resumen': '«Gemini o ChatGPT» fue una de las comparativas más buscadas en España. Las enfrentamos, '
                   'junto a Claude, en precio, funciones y para quién es cada una.',
        'icono': '🤖',
        'destacado': True,
        'introduccion': """
<p>Los tres grandes asistentes tienen versión gratuita y un plan de pago de precio parecido. La diferencia no está
tanto en lo «listos» que son (los tres son excelentes) como en <strong>dónde encajan en tu día a día</strong>.</p>
<p>Datos de cuota: visitas web a chatbots en agosto de 2026 (Momentic). Precios orientativos con impuestos para el
plan individual en España. Compruébalos en la web oficial, porque cambian con frecuencia.</p>
""",
        'columnas': ['ChatGPT', 'Gemini', 'Claude'],
        'filas': [
            ['Empresa', 'OpenAI', 'Google', 'Anthropic'],
            ['Cuota de visitas web (ago. 2026)', '53,9 %', '27,9 %', '9,2 %'],
            ['Plan gratuito', 'Sí', 'Sí', 'Sí'],
            ['Plan de pago individual', '≈ 20–23 €/mes', '≈ 22 €/mes', '≈ 18–22 €/mes'],
            ['Punto fuerte', 'Versatilidad y ecosistema de funciones', 'Integración con Gmail, Docs y Android', 'Redacción, documentos largos y código'],
            ['Imágenes', 'Genera y edita', 'Genera y edita (muy fiel a la cara)', 'Las analiza, no se centra en generarlas'],
            ['Voz en tiempo real', 'Sí', 'Sí (Gemini Live)', 'Sí, en apps móviles'],
            ['Ideal para', 'Uso general y creativo', 'Quien vive en Google', 'Trabajo intelectual y programación'],
        ],
        'ganador': '',
        'veredicto': """
<p><strong>No hay un ganador absoluto.</strong> Nuestra recomendación según el perfil:</p>
<ul>
  <li><strong>Si solo vas a usar uno y no sabes cuál</strong>: ChatGPT. Es el más versátil y el que más funciones
  reúne en un solo sitio.</li>
  <li><strong>Si tu vida digital es Gmail, Drive y Android</strong>: Gemini. La integración te ahorra copiar y pegar a
  diario, y es el mejor para retocar tus fotos.</li>
  <li><strong>Si escribes mucho, trabajas con documentos extensos o programas</strong>: Claude.</li>
</ul>
<p>Consejo práctico: prueba gratis los tres con la misma tarea real de tu trabajo durante una semana y paga solo por
el que más uses.</p>
""",
        'productos': ['chatgpt-plus', 'google-ai-pro', 'claude-pro'],
    },
    {
        'slug': 'mejor-generador-de-imagenes-ia',
        'titulo': 'Generadores de imágenes con IA: Gemini, ChatGPT, Firefly y Midjourney',
        'resumen': 'Para editar tus fotos, crear ilustraciones o hacer imágenes para tu negocio. '
                   'Qué herramienta encaja con cada uso y cuáles tienen versión gratuita.',
        'icono': '🖼️',
        'introduccion': """
<p>«Cómo hacer fotos con IA» fue una de las grandes búsquedas de 2025. Estas son las cuatro herramientas que más se
usan para conseguirlo, comparadas en lo que importa a un usuario normal.</p>
""",
        'columnas': ['Gemini', 'ChatGPT', 'Adobe Firefly', 'Midjourney'],
        'filas': [
            ['Mejor en', 'Editar fotos reales manteniendo la cara', 'Instrucciones complejas y texto en la imagen', 'Uso comercial y flujo con Photoshop', 'Estética artística'],
            ['Versión gratuita', 'Sí, con límites', 'Sí, con límites', 'Sí, créditos limitados', 'No'],
            ['Editar fotos propias', 'Excelente', 'Muy buena', 'Muy buena (relleno generativo)', 'Limitada'],
            ['Facilidad de uso', 'Muy alta (chat)', 'Muy alta (chat)', 'Alta', 'Media'],
            ['Señal de contenido IA', 'SynthID invisible', 'Metadatos C2PA', 'Content Credentials (C2PA)', 'Consulta sus condiciones'],
            ['Ideal para', 'Retocar fotos personales', 'Infografías, ilustraciones y carteles', 'Profesionales y marcas', 'Arte y concept art'],
        ],
        'ganador': 'Gemini',
        'veredicto': """
<p><strong>Para la búsqueda más habitual (retocar una foto tuya) gana Gemini.</strong> Es gratis, se maneja hablando
y conserva muy bien los rasgos de la persona.</p>
<p>Si necesitas imágenes con texto legible o composiciones con muchos elementos, ChatGPT es más preciso. Para uso
comercial en una empresa, Firefly ofrece más tranquilidad sobre los derechos. Midjourney sigue siendo la referencia
para quien busca un estilo artístico concreto y no le importa pagar.</p>
""",
        'productos': ['google-ai-pro', 'chatgpt-plus'],
    },
]

TENDENCIAS = [
    {
        'slug': 'fotos-con-ia',
        'nombre': 'Fotos y retratos con IA',
        'icono': '📸',
        'estado': 'consolidada',
        'dato': 'Top «¿cómo…?» en España 2025',
        'fuente': 'Google Year in Search 2025',
        'fuente_url': 'https://trends.withgoogle.com/year-in-search/2025/es/',
        'articulo': 'como-hacer-fotos-con-ia',
        'descripcion': '<p>Retratos profesionales, figuras de colección y cambios de fondo. La IA se convirtió en el '
                       'editor de fotos de millones de personas.</p>',
    },
    {
        'slug': 'generadores-de-voz',
        'nombre': 'Generadores de voz con IA',
        'icono': '🎙️',
        'estado': 'en_auge',
        'dato': '+2.650 % en búsquedas',
        'fuente': 'Exploding Topics',
        'fuente_url': 'https://explodingtopics.com/blog/trending-topics',
        'articulo': 'generador-de-voz-con-ia',
        'descripcion': '<p>Narración de vídeos, doblaje con tu propia voz y accesibilidad. También es la base de una '
                       'nueva ola de estafas telefónicas.</p>',
    },
    {
        'slug': 'agentes-de-ia',
        'nombre': 'Agentes de IA',
        'icono': '🧭',
        'estado': 'en_auge',
        'dato': 'Búsquedas ×3 en un año',
        'fuente': 'Exploding Topics',
        'fuente_url': 'https://explodingtopics.com/blog/consumer-behavior',
        'articulo': 'que-es-un-agente-de-ia',
        'descripcion': '<p>De preguntar a delegar: asistentes que navegan, comparan y completan tareas. Cada vez más '
                       'consumidores confían en la IA para elegir productos.</p>',
    },
    {
        'slug': 'gemini-o-chatgpt',
        'nombre': '¿Gemini o ChatGPT?',
        'icono': '⚖️',
        'estado': 'consolidada',
        'dato': 'Top comparativa en España 2025',
        'fuente': 'Google Year in Search 2025',
        'fuente_url': 'https://trends.withgoogle.com/year-in-search/2025/es/',
        'descripcion': '<p>La pregunta que todo el mundo se hace antes de pagar una suscripción. La respondemos en '
                       'nuestra comparativa ChatGPT vs Gemini vs Claude.</p>',
    },
    {
        'slug': 'auge-de-claude',
        'nombre': 'El ascenso de Claude',
        'icono': '✴️',
        'estado': 'emergente',
        'dato': 'Del 3,4 % al 9,2 % de cuota en un trimestre',
        'fuente': 'Momentic (agosto 2026)',
        'fuente_url': 'https://momenticmarketing.com/blog/top-ai-chatbots',
        'descripcion': '<p>Mientras ChatGPT se mantiene estable, Claude y Gemini se llevan casi todo el crecimiento '
                       'del mercado de chatbots en 2026.</p>',
    },
    {
        'slug': 'monitores-portatiles',
        'nombre': 'Monitores portátiles',
        'icono': '🖥️',
        'estado': 'en_auge',
        'dato': '+838 % en búsquedas',
        'fuente': 'Exploding Topics',
        'fuente_url': 'https://explodingtopics.com/product-topics',
        'descripcion': '<p>Segundas pantallas ligeras para teletrabajar o viajar. Encajan con la forma de trabajar '
                       'con IA: el asistente en una pantalla y el documento en la otra.</p>',
    },
]
