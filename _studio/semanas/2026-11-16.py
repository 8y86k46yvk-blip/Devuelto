# Contenido de Devuelto · semana del 16 al 22 de noviembre de 2026
# [[texto]] = texto en verde. Datos legales comprobados el 16/11/2026:
# art. 36.4 LAU (1 mes + interés legal), interés legal 2026 = 3,25 %, art. 20.1 LAU (Ley 12/2023,
# vigente desde 26/05/2023), art. 11 LAU (6 meses + 30 días, indemnización pactada máx. 1 mes/año),
# art. 36.5 LAU (garantía adicional máx. 2 meses), LO 1/2025 (MASC desde 03/04/2025, 30 días),
# juicio verbal sin abogado hasta 2.000 €, prescripción 5 años, multa de Consumo a Alquiler Seguro
# (3,6 M€, firme en vía administrativa desde abril de 2026).

AVISO = "Información general, no es asesoramiento jurídico."
TAGS_F = "#fianza #alquiler #inquilinos #vivienda #derechosdelinquilino"
TAGS_A = "#alquiler #inmobiliaria #inquilinos #leydevivienda #vivienda"
CTA_F = "→ Calcula cuánto te deben en devuelto.app (enlace en el perfil)"
CTA_A = "→ Calcula cuánto puedes recuperar en devuelto.app (enlace en el perfil)"

def cap(body, cta, tags):
    return f"{body}\n\n{cta}\n\n{AVISO}\n{tags}"

POSTS = [
# ───────────── LUNES 16 ─────────────
{"id": "v01", "tipo": "video", "fecha": "2026-11-16T10:00:00", "cta": "fianza", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Fianza", "texto": "Tu casero tiene [[un mes]] para devolverte la fianza."},
  {"t": "ley", "ref": "Art. 36.4 · Ley de Arrendamientos Urbanos", "texto": "La fianza que deba devolverse devengará el interés legal transcurrido un mes desde la entrega de las llaves."},
  {"t": "texto", "titulo": "El reloj empieza el día que [[entregas las llaves]].", "cuerpo": "No cuando el casero revisa el piso. Ni cuando lo vuelve a alquilar."},
  {"t": "numero", "num": "3,25 %", "sub": "de interés anual desde que se pasa ese mes. Es el interés legal del dinero en 2026."},
  {"t": "texto", "titulo": "Si te descuenta algo, tiene que [[justificarlo]].", "cuerpo": "Con facturas o presupuestos. Un «ya veremos» no vale."},
 ],
 "texto": cap("Tu casero no puede tardar lo que quiera en devolverte la fianza.\n\nLa ley le da un mes desde que entregas las llaves. Pasado ese mes, lo que te deba empieza a generar intereses: un 3,25 % anual en 2026.\n\nY si te descuenta algo, tiene que justificarlo.", CTA_F, TAGS_F)},

{"id": "c01", "tipo": "carrusel", "fecha": "2026-11-16T13:00:00", "cta": "fianza",
 "titulo_tiktok": "Qué puede descontarte tu casero de la fianza (y qué no)",
 "slides": [
  {"t": "portada", "kicker": "Guárdalo", "titulo": "Qué puede descontarte tu casero de la fianza [[(y qué no)]]"},
  {"t": "lista", "etiqueta": "Sí puede", "titulo": "Lo que sí te pueden descontar", "items": ["Rentas que hayas dejado sin pagar", "Suministros a tu cargo pendientes: luz, agua, gas…", "Daños que hayas causado tú, justificados con factura o presupuesto"]},
  {"t": "texto", "etiqueta": "No puede", "titulo": "El desgaste normal", "cuerpo": "Pintura envejecida, suelos con roce, marcas del uso diario. Vivir en una casa la desgasta, y eso no lo pagas tú."},
  {"t": "texto", "etiqueta": "No puede", "titulo": "Lo que ya estaba mal cuando entraste", "cuerpo": "Si tienes fotos o un inventario de la entrada, no te pueden cobrar daños que ya existían."},
  {"t": "texto", "etiqueta": "No puede", "titulo": "Una «multa» por irte antes", "cuerpo": "Si llevabas 6 meses y avisaste con 30 días, solo cabe la indemnización pactada en el contrato: como mucho, un mes por año que faltara. Si no hay nada pactado, nada."},
  {"t": "texto", "etiqueta": "No puede", "titulo": "Importes sin justificar", "cuerpo": "Cualquier descuento tiene que poder demostrarse. Pide siempre el detalle por escrito."},
  {"t": "cta"},
 ],
 "texto": cap("Guárdalo para cuando dejes el piso.\n\nTu casero puede descontar de la fianza rentas sin pagar, suministros pendientes y daños que hayas causado tú. Lo que no puede es cobrarte el desgaste normal, lo que ya estaba mal cuando entraste o una «multa» que no esté en el contrato.", CTA_F, TAGS_F)},

{"id": "v02", "tipo": "video", "fecha": "2026-11-16T18:00:00", "cta": "agencia", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Inmobiliarias", "texto": "¿Pagaste [[un mes de agencia]] al alquilar tu piso?"},
  {"t": "mito", "mito": "Los honorarios de la inmobiliaria los paga siempre el inquilino.", "real": "Desde mayo de 2023, en los alquileres de vivienda los paga el propietario."},
  {"t": "ley", "ref": "Art. 20.1 · Ley de Arrendamientos Urbanos", "texto": "Los gastos de gestión inmobiliaria y los de formalización del contrato serán a cargo del arrendador."},
  {"t": "texto", "titulo": "Da igual [[cómo lo llamen]].", "cuerpo": "«Gestión», «estudio de solvencia», «apertura de expediente»… Si es un servicio para alquilar el piso del propietario, no te toca pagarlo."},
  {"t": "texto", "titulo": "Si ya lo pagaste, [[puedes reclamarlo]].", "cuerpo": "Guarda la factura o el justificante de la transferencia."},
 ],
 "texto": cap("Si alquilaste tu vivienda desde el 26 de mayo de 2023 y la inmobiliaria te cobró sus honorarios, ese dinero lo tenía que pagar el propietario.\n\nLo dice el artículo 20.1 de la Ley de Arrendamientos Urbanos, y da igual el nombre que le pusieran al cobro.\n\nOjo: no se aplica a los alquileres de temporada.", CTA_A, TAGS_A)},

# ───────────── MARTES 17 ─────────────
{"id": "v03", "tipo": "video", "fecha": "2026-11-17T10:00:00", "cta": "fianza", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Paso a paso", "texto": "Antes de entregar las llaves, haz [[estas 3 cosas]]."},
  {"t": "paso", "n": "1", "titulo": "Graba el piso", "cuerpo": "Vídeo y fotos de cada habitación, con fecha. Es tu prueba de cómo lo dejaste."},
  {"t": "paso", "n": "2", "titulo": "Pide un justificante de la entrega", "cuerpo": "Un papel firmado con la fecha en que devuelves las llaves. Ese día empieza a contar el mes."},
  {"t": "paso", "n": "3", "titulo": "Deja tu cuenta por escrito", "cuerpo": "Manda tu IBAN por email o por mensaje. Así no hay excusa para no pagarte."},
 ],
 "texto": cap("Tres cosas que te ahorran muchos problemas para recuperar la fianza:\n\n1. Graba el piso el día que te vas.\n2. Pide un justificante firmado de la entrega de llaves.\n3. Deja tu IBAN por escrito.\n\nDesde la entrega de llaves, tu casero tiene un mes para devolvértela.", CTA_F, TAGS_F)},

{"id": "c02", "tipo": "carrusel", "fecha": "2026-11-17T13:00:00", "cta": "fianza",
 "titulo_tiktok": "Cómo recuperar tu fianza en 4 pasos",
 "slides": [
  {"t": "portada", "kicker": "Paso a paso", "titulo": "Cómo recuperar tu fianza en [[4 pasos]]"},
  {"t": "paso", "n": "1", "titulo": "Entrega las llaves con justificante", "cuerpo": "Con fecha. Desde ese día, tu casero tiene un mes para devolvértela."},
  {"t": "paso", "n": "2", "titulo": "Espera ese mes", "cuerpo": "Si te la devuelve entera, perfecto. Si no, o te descuenta cosas sin justificar, sigue."},
  {"t": "paso", "n": "3", "titulo": "Envía un burofax", "cuerpo": "Con lo que reclamas, tu IBAN y un plazo para responder. Desde abril de 2025 hay que intentar negociar antes de demandar, y el burofax sirve para demostrarlo."},
  {"t": "paso", "n": "4", "titulo": "Si en 30 días no responde", "cuerpo": "Puedes ir al juzgado con un juicio verbal. Hasta 2.000 €, sin abogado ni procurador."},
  {"t": "numero", "num": "5 años", "sub": "es el plazo que tienes para reclamarla. Aunque haya pasado tiempo, todavía puedes."},
  {"t": "cta", "variante": "burofax"},
 ],
 "texto": cap("Cómo recuperar tu fianza, paso a paso:\n\n1. Entrega las llaves con justificante.\n2. Espera el mes que le da la ley a tu casero.\n3. Envía un burofax con lo que reclamas y tu IBAN.\n4. Si en 30 días no responde, puedes ir al juzgado. Hasta 2.000 €, sin abogado ni procurador.\n\nTienes 5 años para reclamarla.", CTA_F, TAGS_F)},

{"id": "v04", "tipo": "video", "fecha": "2026-11-17T18:00:00", "cta": "agencia", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Noticia", "texto": "[[3,6 millones]] de multa a una inmobiliaria por cobrar a sus inquilinos."},
  {"t": "texto", "titulo": "Quién y por qué", "cuerpo": "Consumo multó a Alquiler Seguro por prácticas abusivas. Entre ellas, cobrar al inquilino servicios que debía pagar el propietario."},
  {"t": "texto", "titulo": "La multa ya es [[firme]]", "cuerpo": "en vía administrativa desde abril de 2026. La empresa todavía puede recurrirla en los tribunales."},
  {"t": "texto", "titulo": "¿Y tú?", "cuerpo": "Si alquilaste tu vivienda desde mayo de 2023 y pagaste honorarios a la agencia, puedes reclamarlos."},
 ],
 "texto": cap("El Ministerio de Consumo multó con 3,6 millones de euros a Alquiler Seguro por prácticas abusivas con sus inquilinos, entre ellas cobrarles servicios que correspondía pagar al propietario. La multa es firme en vía administrativa desde abril de 2026.\n\nSi alquilaste tu vivienda desde mayo de 2023 y pagaste honorarios a una inmobiliaria, puedes reclamarlos.", CTA_A, TAGS_A)},

# ───────────── MIÉRCOLES 18 ─────────────
{"id": "v05", "tipo": "video", "fecha": "2026-11-18T10:00:00", "cta": "agencia", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Inmobiliarias", "texto": "«Gestión», «solvencia», «apertura de expediente»… [[Es lo mismo.]]"},
  {"t": "texto", "titulo": "El truco del nombre", "cuerpo": "Desde 2023, los gastos de gestión inmobiliaria los paga el propietario. Algunas agencias los siguen cobrando con otro nombre."},
  {"t": "texto", "titulo": "Lo que dice [[Consumo]]", "cuerpo": "La prohibición se aplica se llame como se llame, si es un servicio para poner en alquiler el piso del propietario."},
  {"t": "lista", "titulo": "Esto lo paga el propietario:", "items": ["Enseñar el piso", "Anunciarlo", "Preparar el contrato"]},
 ],
 "texto": cap("Si al alquilar te cobraron «gastos de gestión», «estudio de solvencia» o «apertura de expediente», fíjate bien en qué pagaste.\n\nSegún Consumo, la prohibición de cobrar al inquilino los gastos de gestión inmobiliaria se aplica sea cual sea el nombre, si es un servicio para alquilar el piso del propietario.", CTA_A, TAGS_A)},

{"id": "c03", "tipo": "carrusel", "fecha": "2026-11-18T13:00:00", "cta": "fianza",
 "titulo_tiktok": "Qué tiene que llevar tu burofax para reclamar la fianza",
 "slides": [
  {"t": "portada", "kicker": "Guárdalo", "titulo": "Qué tiene que llevar tu burofax para [[reclamar la fianza]]"},
  {"t": "paso", "n": "1", "titulo": "Tus datos y los de tu casero", "cuerpo": "Nombre, DNI y domicilio de los dos. El de tu casero, el que aparece en el contrato."},
  {"t": "paso", "n": "2", "titulo": "La vivienda y las fechas", "cuerpo": "Dirección del piso, fecha del contrato y fecha en que entregaste las llaves."},
  {"t": "paso", "n": "3", "titulo": "Cuánto reclamas", "cuerpo": "La fianza (y la garantía adicional, si pagaste una) más los intereses del artículo 36.4 de la LAU."},
  {"t": "paso", "n": "4", "titulo": "Dónde te tienen que pagar", "cuerpo": "Tu IBAN. Así no hay excusas."},
  {"t": "paso", "n": "5", "titulo": "Un plazo para resolverlo", "cuerpo": "Invítale a solucionarlo. Si en 30 días desde que lo recibe no responde, podrás demandar."},
  {"t": "paso", "n": "6", "titulo": "Cómo enviarlo", "cuerpo": "Burofax con certificación de texto y acuse de recibo. Así puedes probar qué enviaste y cuándo lo recibió."},
  {"t": "cta", "variante": "burofax"},
 ],
 "texto": cap("Un burofax para reclamar la fianza tiene que dejar claro quién reclama, qué, cuánto y dónde te tienen que pagar.\n\nEnvíalo con certificación de texto y acuse de recibo: es tu prueba de que intentaste resolverlo antes de ir al juzgado.", CTA_F, TAGS_F)},

{"id": "v06", "tipo": "video", "fecha": "2026-11-18T18:00:00", "cta": "fianza", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Fianza", "texto": "¿Te vas del piso [[antes de que acabe]] el contrato?"},
  {"t": "texto", "titulo": "Puedes irte", "cuerpo": "si llevas al menos 6 meses y avisas con 30 días de antelación. Lo dice el artículo 11 de la LAU."},
  {"t": "texto", "titulo": "¿Te pueden cobrar algo?", "cuerpo": "Solo si el contrato lo dice: como mucho, un mes de renta por cada año que falte. Si no hay nada pactado, nada."},
  {"t": "mito", "mito": "Si te vas antes, pierdes la fianza.", "real": "La cláusula que te quita la fianza por no cumplir todo el contrato es nula."},
 ],
 "texto": cap("Irte antes de tiempo no significa perder la fianza.\n\nSi llevas al menos 6 meses y avisas con 30 días, puedes irte. Solo te pueden pedir la indemnización que diga el contrato (como mucho, un mes por año que falte). Y una cláusula que te quite la fianza por no cumplir todo el contrato es nula.", CTA_F, TAGS_F)},

# ───────────── JUEVES 19 ─────────────
{"id": "v07", "tipo": "video", "fecha": "2026-11-19T10:00:00", "cta": "fianza", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Antes de firmar", "texto": "¿Cuánto te pueden pedir [[de fianza]]?"},
  {"t": "numero", "num": "1 mes", "sub": "de renta. Es la fianza legal en un alquiler de vivienda."},
  {"t": "numero", "num": "+2 meses", "sub": "como máximo de garantía adicional, en contratos de hasta 5 años (o 7 si el casero es una empresa)."},
  {"t": "texto", "titulo": "¿Te piden más?", "cuerpo": "La garantía adicional no puede pasar de dos meses. Y todo lo que entregues como garantía se devuelve al final, igual que la fianza."},
 ],
 "texto": cap("En un alquiler de vivienda, la fianza legal es de un mes de renta.\n\nAdemás te pueden pedir una garantía adicional, pero con límite: dos meses como máximo en contratos de hasta 5 años (o 7 si el casero es una empresa). Y al final se devuelve todo, igual que la fianza.", CTA_F, TAGS_F)},

{"id": "c04", "tipo": "carrusel", "fecha": "2026-11-19T13:00:00", "cta": "fianza",
 "titulo_tiktok": "5 mitos sobre la fianza que te pueden costar dinero",
 "slides": [
  {"t": "portada", "kicker": "Mitos", "titulo": "5 mitos sobre la fianza que te pueden [[costar dinero]]"},
  {"t": "mito", "mito": "El último mes no lo pago y que se quede la fianza.", "real": "La fianza garantiza todo el contrato: rentas, suministros y daños. Si la «gastas» en el último mes y luego hay algo más, te lo reclamarán aparte."},
  {"t": "mito", "mito": "Sin abogado no puedo reclamar.", "real": "Hasta 2.000 € puedes presentar un juicio verbal sin abogado ni procurador."},
  {"t": "mito", "mito": "Me la tiene que devolver el mismo día.", "real": "Tiene un mes desde la entrega de llaves. A partir de ahí, te debe intereses."},
  {"t": "mito", "mito": "Ya ha pasado mucho tiempo, es tarde.", "real": "Tienes 5 años para reclamarla."},
  {"t": "mito", "mito": "Me puede cobrar la pintura sí o sí.", "real": "Solo si hay daños que van más allá del desgaste normal de vivir en la casa."},
  {"t": "cta"},
 ],
 "texto": cap("5 cosas que mucha gente cree sobre la fianza y no son así. La primera puede salirte cara.\n\n¿Cuál te sorprende más?", CTA_F, TAGS_F)},

{"id": "v08", "tipo": "video", "fecha": "2026-11-19T18:00:00", "cta": "fianza", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Fianza", "texto": "¿Te fuiste del piso hace un año y [[sigues sin tu fianza]]?"},
  {"t": "numero", "num": "5 años", "sub": "es el plazo que tienes para reclamarla."},
  {"t": "texto", "titulo": "El tiempo [[juega a tu favor]]", "cuerpo": "Pasado el mes desde la entrega de llaves, lo que te deben genera intereses."},
  {"t": "lista", "titulo": "Lo que necesitas:", "items": ["El contrato de alquiler", "El justificante de la fianza", "La fecha en que entregaste las llaves"]},
 ],
 "texto": cap("Que haya pasado tiempo no significa que hayas perdido tu fianza: tienes 5 años para reclamarla.\n\nY desde que se cumplió el mes tras entregar las llaves, lo que te deben genera intereses.", CTA_F, TAGS_F)},

# ───────────── VIERNES 20 ─────────────
{"id": "v09", "tipo": "video", "fecha": "2026-11-20T10:00:00", "cta": "fianza", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Frases de casero", "texto": "3 excusas para no devolverte la fianza [[(y qué responder)]]"},
  {"t": "dialogo", "frase": "Hay que pintar el piso.", "respuesta": "El desgaste normal no se descuenta. Si hay daños, que los justifique con factura."},
  {"t": "dialogo", "frase": "Te la devuelvo cuando lo alquile.", "respuesta": "No depende de eso. Tiene un mes desde que entregas las llaves."},
  {"t": "dialogo", "frase": "Como te vas antes, la pierdes.", "respuesta": "La fianza no es una multa. Solo cabe la indemnización pactada, si la hay."},
 ],
 "texto": cap("«Hay que pintar», «te la devuelvo cuando lo alquile», «como te vas antes, la pierdes»…\n\nNinguna de las tres es motivo para quedarse tu fianza. ¿Cuál te han dicho a ti?", CTA_F, TAGS_F)},

{"id": "c05", "tipo": "carrusel", "fecha": "2026-11-20T13:00:00", "cta": "agencia",
 "titulo_tiktok": "Cómo reclamar los honorarios que te cobró la inmobiliaria",
 "slides": [
  {"t": "portada", "kicker": "Inmobiliarias", "titulo": "¿Pagaste honorarios a la inmobiliaria? [[Así puedes reclamarlos]]"},
  {"t": "lista", "etiqueta": "Paso 1", "titulo": "Comprueba si tu caso encaja", "items": ["Alquiler de vivienda habitual (no de temporada)", "Firmado desde el 26 de mayo de 2023", "Pagaste a la agencia por gestionar o formalizar el contrato"]},
  {"t": "ley", "ref": "Art. 20.1 · Ley de Arrendamientos Urbanos", "texto": "Los gastos de gestión inmobiliaria y los de formalización del contrato serán a cargo del arrendador."},
  {"t": "texto", "etiqueta": "Paso 2", "titulo": "Reúne las pruebas", "cuerpo": "Factura, recibo, transferencia o el cargo en tu tarjeta. Y el contrato de alquiler."},
  {"t": "texto", "etiqueta": "Paso 3", "titulo": "Reclama por escrito", "cuerpo": "Envía a la inmobiliaria una reclamación, mejor por burofax, con el importe, tu IBAN y un plazo para devolverlo."},
  {"t": "texto", "etiqueta": "Paso 4", "titulo": "Si no te lo devuelven", "cuerpo": "Puedes denunciarlo ante Consumo de tu comunidad y reclamarlo en el juzgado. Hasta 2.000 €, sin abogado ni procurador."},
  {"t": "cta", "variante": "agencia"},
 ],
 "texto": cap("Si la inmobiliaria te cobró sus honorarios al alquilar tu vivienda habitual, desde el 26 de mayo de 2023 ese dinero lo tenía que pagar el propietario.\n\nComprueba si tu caso encaja, reúne las pruebas y reclámalo por escrito.", CTA_A, TAGS_A)},

{"id": "v10", "tipo": "video", "fecha": "2026-11-20T18:00:00", "cta": "agencia", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Haz la cuenta", "texto": "Alquiler de 1.000 €. Te cobraron [[un mes + IVA]] de agencia."},
  {"t": "numero", "num": "1.210 €", "sub": "que, según la ley, le tocaba pagar al propietario."},
  {"t": "texto", "titulo": "Puedes pedir que [[te los devuelvan]]", "cuerpo": "si es tu vivienda habitual y firmaste desde el 26 de mayo de 2023."},
  {"t": "texto", "titulo": "Guarda la prueba del pago", "cuerpo": "Factura, transferencia o cargo en la tarjeta. Sin ella, reclamar es más difícil."},
 ],
 "texto": cap("Un mes de agencia más IVA, en un alquiler de 1.000 €, son 1.210 €.\n\nSi lo pagaste al alquilar tu vivienda habitual después del 26 de mayo de 2023, ese dinero lo tenía que pagar el propietario. Puedes reclamarlo.", CTA_A, TAGS_A)},

# ───────────── SÁBADO 21 ─────────────
{"id": "v11", "tipo": "video", "fecha": "2026-11-21T10:00:00", "cta": "fianza", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Checklist", "texto": "El día que dejas el piso, [[no te olvides de esto]]."},
  {"t": "lista", "titulo": "Antes de irte:", "items": ["Déjalo limpio, como lo recibiste", "Fotos y vídeo de todo, con fecha", "Foto de los contadores"]},
  {"t": "lista", "titulo": "Al entregar las llaves:", "items": ["Todas las copias", "Justificante firmado con la fecha", "Tu IBAN por escrito"]},
  {"t": "texto", "titulo": "Y después, [[cuenta un mes]].", "cuerpo": "Si para entonces no tienes tu fianza, toca reclamar."},
 ],
 "texto": cap("Checklist para el día que dejas el piso:\n\n✓ Déjalo limpio, como lo recibiste\n✓ Fotos y vídeo de todo, con fecha\n✓ Foto de los contadores\n✓ Entrega todas las llaves con justificante firmado\n✓ Deja tu IBAN por escrito\n\nGuárdalo para cuando te mudes.", CTA_F, TAGS_F)},

{"id": "c06", "tipo": "carrusel", "fecha": "2026-11-21T13:00:00", "cta": "fianza",
 "titulo_tiktok": "Antes de firmar un alquiler, comprueba esto",
 "slides": [
  {"t": "portada", "kicker": "Antes de firmar", "titulo": "Antes de firmar un alquiler, [[comprueba esto]]"},
  {"t": "paso", "n": "1", "titulo": "La fianza: un mes", "cuerpo": "Es la legal en un alquiler de vivienda. Las garantías extra, como mucho dos meses más."},
  {"t": "paso", "n": "2", "titulo": "Nada de honorarios", "cuerpo": "Los gastos de gestión inmobiliaria y de formalización del contrato los paga el propietario."},
  {"t": "paso", "n": "3", "titulo": "La fianza, en el contrato", "cuerpo": "Que aparezca con su importe. Y pide recibo o paga por transferencia."},
  {"t": "paso", "n": "4", "titulo": "Fotos del piso al entrar", "cuerpo": "De todo, con fecha. Y si puedes, firma un inventario. Te servirán el día que te vayas."},
  {"t": "paso", "n": "5", "titulo": "Paga siempre con rastro", "cuerpo": "Transferencia o tarjeta. Si es en efectivo, pide recibo firmado."},
  {"t": "cta", "variante": "guardar"},
 ],
 "texto": cap("Lo que hagas antes de firmar decide cuánto te cuesta recuperar tu dinero al irte.\n\nGuárdalo para tu próximo piso y compártelo con quien esté buscando.", CTA_F, TAGS_F)},

{"id": "v12", "tipo": "video", "fecha": "2026-11-21T18:00:00", "cta": "fianza", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Reclamar", "texto": "Mandaste el burofax y tu casero no contesta. [[¿Y ahora?]]"},
  {"t": "texto", "titulo": "Desde abril de 2025", "cuerpo": "antes de demandar hay que intentar negociar. El burofax sirve para demostrar que lo intentaste."},
  {"t": "numero", "num": "30 días", "sub": "sin respuesta desde que lo recibe, y puedes ir al juzgado."},
  {"t": "texto", "titulo": "Hasta [[2.000 €]]", "cuerpo": "puedes presentar un juicio verbal sin abogado ni procurador. Los juzgados tienen formularios para hacerlo."},
 ],
 "texto": cap("Si tu casero no contesta al burofax, no se acaba ahí.\n\nDesde abril de 2025 hay que intentar negociar antes de demandar. Si pasan 30 días desde que lo recibe sin respuesta, ya puedes ir al juzgado. Hasta 2.000 €, sin abogado ni procurador.", CTA_F, TAGS_F)},

# ───────────── DOMINGO 22 ─────────────
{"id": "v13", "tipo": "video", "fecha": "2026-11-22T10:00:00", "cta": "fianza", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Haz la cuenta", "texto": "Imagina: 900 € de fianza y [[3 meses esperando]]."},
  {"t": "texto", "titulo": "Entregas las llaves el [[1 de julio]].", "cuerpo": "Tu casero tiene hasta el 1 de agosto para devolvértela."},
  {"t": "numero", "num": "92 días", "sub": "de retraso si el 1 de noviembre sigue sin pagarte."},
  {"t": "numero", "num": "907,37 €", "sub": "900 € de fianza + 7,37 € de intereses al 3,25 % anual."},
  {"t": "texto", "titulo": "Lo importante no son los intereses.", "cuerpo": "Es que la ley está de tu parte. Y un burofax bien hecho se lo deja claro."},
 ],
 "texto": cap("Un ejemplo: 900 € de fianza, llaves entregadas el 1 de julio. El 1 de agosto se acaba el plazo de tu casero.\n\nSi el 1 de noviembre sigue sin pagar, te debe 900 € más 7,37 € de intereses.\n\nPrueba con tus datos en la calculadora.", CTA_F, TAGS_F)},

{"id": "c07", "tipo": "carrusel", "fecha": "2026-11-22T13:00:00", "cta": "fianza",
 "titulo_tiktok": "La fianza del alquiler en 6 números",
 "slides": [
  {"t": "portada", "kicker": "Guárdalo", "titulo": "La fianza en [[6 números]]"},
  {"t": "numero", "num": "1 mes", "sub": "de renta: la fianza legal en un alquiler de vivienda."},
  {"t": "numero", "num": "1 mes", "sub": "tiene tu casero para devolvértela desde que entregas las llaves."},
  {"t": "numero", "num": "3,25 %", "sub": "de interés anual si se retrasa: el interés legal del dinero en 2026."},
  {"t": "numero", "num": "30 días", "sub": "sin respuesta a tu burofax, y puedes ir al juzgado."},
  {"t": "numero", "num": "2.000 €", "sub": "Hasta esa cantidad puedes reclamar sin abogado ni procurador."},
  {"t": "numero", "num": "5 años", "sub": "para reclamarla."},
  {"t": "cta", "variante": "guardar"},
 ],
 "texto": cap("Todo lo que necesitas saber de la fianza, en 6 números. Guárdalo y compártelo con quien viva de alquiler.", CTA_F, TAGS_F)},

{"id": "v14", "tipo": "video", "fecha": "2026-11-22T18:00:00", "cta": "agencia", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Inmobiliarias", "texto": "«Si no pagas los honorarios, [[no te damos el piso]].»"},
  {"t": "texto", "titulo": "Lo pagaste para no perderlo.", "cuerpo": "Es lo que pasa casi siempre. Y aun así, puedes reclamarlo."},
  {"t": "texto", "titulo": "Aunque [[lo firmaras]].", "cuerpo": "La ley pone esos gastos a cargo del propietario, y Consumo considera abusivo trasladarlos al inquilino."},
  {"t": "lista", "titulo": "Lo que necesitas:", "items": ["El contrato de alquiler", "La prueba del pago", "Los datos de la agencia"]},
 ],
 "texto": cap("Mucha gente pagó los honorarios de la agencia porque, si no, se quedaba sin piso. Aun así, puedes reclamarlos.\n\nSi alquilaste tu vivienda habitual desde el 26 de mayo de 2023, esos gastos los tenía que pagar el propietario.", CTA_A, TAGS_A)},
]
