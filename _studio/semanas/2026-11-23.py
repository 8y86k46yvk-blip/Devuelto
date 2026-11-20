# Contenido de Devuelto · semana del 23 al 29 de noviembre de 2026
# [[texto]] = texto en verde. Datos legales comprobados el 20/11/2026:
# Real Decreto-ley 29/2026, de 6 de octubre (BOE núm. 249, 07/10/2026; en vigor el 08/10/2026),
# convalidado por la Diputación Permanente del Congreso el 12/11/2026 (BOE-A-2026-23755, 13/11/2026).
# Nueva redacción de la LAU: art. 2.1 (habitación = vivienda habitual), art. 7.2 y 9 bis (vivienda temporal:
# causa real y acreditable, prueba del arrendador, >31 días y ≤12 meses, más de dos seguidos → habitual),
# art. 18.1 (sin pacto expreso no hay actualización; tope IRAV), art. 20.1 y 20.2 (tributos no imponibles al
# inquilino; comunidad solo por escrito con importe anual; gestión inmobiliaria y formalización «ni directa ni
# indirectamente, bajo ningún concepto o denominación», incluida novación y renovación; servicios no esenciales
# solo si se piden por escrito), art. 21.5 (15 días naturales; descuento de rentas futuras), art. 36.5 (garantía
# adicional máx. 2 meses, 1 en temporales; prohibido exigir seguro de impago), art. 36.7 (documento de
# finalización; presunción de buen estado), art. 37.2 (contrato por escrito a petición del inquilino),
# DF 5.ª (prórroga extraordinaria hasta 2 años; contratos que acaban antes del 31/12/2028; 8 meses al corriente),
# DF 6.ª (hasta el 31/12/2027, sin nuevo pacto, subida máx. 2 %), DT 8.ª LAU (temporales anteriores: régimen
# anterior). LAU sin cambios: art. 9.1 (5/7 años), 21.1, 21.3 y 21.4, 36.1 (1 mes) y 36.4 (1 mes).
# IRAV de octubre de 2026: 2,57 % (INE, 13/11/2026; EFE e idealista). Constitución, art. 18.2.

AVISO = "Información general, no es asesoramiento jurídico."
TAGS_F = "#fianza #alquiler #inquilinos #vivienda #derechosdelinquilino"
TAGS_A = "#alquiler #inmobiliaria #inquilinos #leydevivienda #vivienda"
TAGS_D = "#alquiler #inquilinos #vivienda #derechosdelinquilino #leydevivienda"
CTA_F = "→ Calcula cuánto te deben en devuelto.app (enlace en el perfil)"
CTA_A = "→ Calcula cuánto puedes recuperar en devuelto.app (enlace en el perfil)"
CTA_G = "→ Y si algún día no te devuelven la fianza, calcula cuánto te deben en devuelto.app (enlace en el perfil)"

def cap(body, cta, tags):
    return f"{body}\n\n{cta}\n\n{AVISO}\n{tags}"

POSTS = [
# ───────────── LUNES 23 ─────────────
{"id": "v01", "tipo": "video", "fecha": "2026-11-23T10:00:00", "cta": "agencia", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Noticia", "texto": "¿Vives de alquiler? El decreto de vivienda [[ya está convalidado.]]"},
  {"t": "texto", "titulo": "Qué es", "cuerpo": "El Real Decreto-ley 29/2026. Está en vigor desde el 8 de octubre y el Congreso lo convalidó el 12 de noviembre."},
  {"t": "numero", "num": "2 %", "sub": "como máximo de subida anual de la renta hasta finales de 2027, si no acordáis otra cosa."},
  {"t": "texto", "titulo": "Sin [[seguro de impago]] obligatorio.", "cuerpo": "La ley dice ahora que en ningún caso te lo pueden exigir."},
  {"t": "texto", "titulo": "Ni honorarios [[con otro nombre]].", "cuerpo": "Los gastos de gestión inmobiliaria no se te pueden cobrar, ni directa ni indirectamente."},
 ],
 "texto": cap("El Congreso convalidó el 12 de noviembre el Real Decreto-ley 29/2026, el «decreto de vivienda». Está en vigor desde el 8 de octubre.\n\nTres cambios que te afectan si vives de alquiler:\n• Si no hay un nuevo acuerdo, la subida anual de la renta no puede pasar del 2 % hasta el 31 de diciembre de 2027.\n• No te pueden exigir un seguro de impago.\n• Los gastos de inmobiliaria no se te pueden cobrar, se llamen como se llamen.\n\nOjo: algunos cambios dependen de cuándo firmaste tu contrato.", CTA_A, TAGS_D)},

{"id": "c01", "tipo": "carrusel", "fecha": "2026-11-23T13:00:00", "cta": "agencia",
 "titulo_tiktok": "Decreto de vivienda: 7 cambios si vives de alquiler",
 "slides": [
  {"t": "portada", "kicker": "Noticia", "titulo": "Decreto de vivienda: [[7 cambios]] si vives de alquiler"},
  {"t": "numero", "num": "2 %", "sub": "como máximo de subida anual de la renta hasta el 31/12/2027, si no hay un nuevo acuerdo."},
  {"t": "texto", "etiqueta": "Renta", "titulo": "Sin pacto, no hay subida", "cuerpo": "Si tu contrato no prevé actualizar la renta, no se actualiza. Y si lo prevé, nunca por encima del índice del INE."},
  {"t": "texto", "etiqueta": "Garantías", "titulo": "Seguro de impago: no te lo pueden exigir", "cuerpo": "Y la garantía adicional, como mucho dos meses de renta (uno si el alquiler es temporal)."},
  {"t": "texto", "etiqueta": "Inmobiliaria", "titulo": "Honorarios: tampoco con otro nombre", "cuerpo": "Ni directa ni indirectamente. Incluye preparar, gestionar o renovar el contrato."},
  {"t": "texto", "etiqueta": "Gastos", "titulo": "Los impuestos del piso no son tuyos", "cuerpo": "Los tributos de la vivienda, como el IBI, no se te pueden imponer. La comunidad, solo con pacto escrito e importe anual."},
  {"t": "texto", "etiqueta": "Reparaciones", "titulo": "15 días para responder", "cuerpo": "Si un desperfecto afecta a la habitabilidad, la seguridad o la salubridad, el casero tiene 15 días desde tu aviso por escrito."},
  {"t": "texto", "etiqueta": "Al irte", "titulo": "Un documento del estado del piso", "cuerpo": "Firmado por los dos. Si no se firma o no recoge desperfectos, se presume, salvo prueba en contrario, que lo devolviste bien."},
  {"t": "cta", "variante": "agencia"},
 ],
 "texto": cap("El Real Decreto-ley 29/2026 está en vigor desde el 8 de octubre y el Congreso lo convalidó el 12 de noviembre. Estos son 7 cambios que te conviene conocer si vives de alquiler.\n\nGuárdalo y compártelo con quien viva de alquiler. Algunos cambios dependen de cuándo firmaste tu contrato.", CTA_A, TAGS_D)},

{"id": "v02", "tipo": "video", "fecha": "2026-11-23T18:00:00", "cta": "agencia", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Inmobiliarias", "texto": "¿Te cobran por [[renovar el contrato?]]"},
  {"t": "ley", "ref": "Art. 20.2 · Ley de Arrendamientos Urbanos", "texto": "Los gastos de gestión inmobiliaria y de formalización del contrato no podrán ser repercutidos al arrendatario, ni directa ni indirectamente, bajo ningún concepto o denominación."},
  {"t": "texto", "titulo": "Renovar [[también cuenta]].", "cuerpo": "Desde el 8 de octubre de 2026, la ley incluye expresamente la preparación, la gestión, la novación y la renovación del contrato."},
  {"t": "texto", "titulo": "¿Y los «servicios extra»?", "cuerpo": "Solo te los pueden cobrar si los pediste tú por escrito, sabiendo antes que eran opcionales y cuánto costaban."},
 ],
 "texto": cap("Si la inmobiliaria te pide dinero por renovar tu contrato de alquiler, fíjate en la fecha.\n\nDesde el 8 de octubre de 2026, el artículo 20.2 de la Ley de Arrendamientos Urbanos dice que los gastos de gestión y de formalización del contrato, incluida su renovación, no se le pueden repercutir al inquilino bajo ningún concepto o denominación.", CTA_A, TAGS_A)},

# ───────────── MARTES 24 ─────────────
{"id": "v03", "tipo": "video", "fecha": "2026-11-24T10:00:00", "cta": "fianza", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Garantías", "texto": "¿Te obligan a contratar [[un seguro de impago?]]"},
  {"t": "mito", "mito": "Sin seguro de impago, no hay piso.", "real": "Desde el 8 de octubre de 2026, la ley prohíbe exigírtelo."},
  {"t": "ley", "ref": "Art. 36.5 · Ley de Arrendamientos Urbanos", "texto": "En ningún caso podrá exigirse al arrendatario la contratación de seguros de impago de renta."},
  {"t": "numero", "num": "2 meses", "sub": "es lo máximo de garantía adicional, además de la fianza, en contratos de hasta 5 años (7 si el casero es una empresa)."},
 ],
 "texto": cap("Si te dicen que sin seguro de impago no hay piso, no es así.\n\nDesde el 8 de octubre de 2026, el artículo 36.5 de la Ley de Arrendamientos Urbanos dice que en ningún caso se le puede exigir al inquilino un seguro de impago.\n\nY la garantía adicional a la fianza tiene límite: dos meses de renta como máximo en contratos de hasta 5 años (7 si el casero es una empresa).", CTA_F, TAGS_F)},

{"id": "c02", "tipo": "carrusel", "fecha": "2026-11-24T13:00:00", "cta": "fianza",
 "titulo_tiktok": "Fianza, garantía y seguro: cuánto te pueden pedir al alquilar",
 "slides": [
  {"t": "portada", "kicker": "Antes de firmar", "titulo": "Fianza, garantía y seguro: [[cuánto te pueden pedir]]"},
  {"t": "numero", "num": "1 mes", "sub": "de renta: la fianza en metálico de un alquiler de vivienda."},
  {"t": "numero", "num": "2 meses", "sub": "como máximo de garantía adicional en contratos de hasta 5 años (7 si el casero es una empresa)."},
  {"t": "numero", "num": "1 mes", "sub": "como máximo de garantía adicional si el alquiler es temporal."},
  {"t": "texto", "etiqueta": "No pueden", "titulo": "Obligarte a un seguro de impago", "cuerpo": "Desde el 8 de octubre de 2026, la ley lo dice claro: en ningún caso te lo pueden exigir."},
  {"t": "texto", "etiqueta": "Al final", "titulo": "Se devuelve todo", "cuerpo": "Si no hay rentas pendientes ni daños, la fianza y la garantía vuelven a ti. Tu casero tiene un mes desde que entregas las llaves."},
  {"t": "cta", "variante": "guardar"},
 ],
 "texto": cap("Antes de firmar un alquiler, comprueba lo que te piden:\n\n• Fianza: un mes de renta.\n• Garantía adicional: como máximo dos meses (uno si el alquiler es temporal).\n• Seguro de impago: no te lo pueden exigir.\n\nGuárdalo para tu próximo piso.", CTA_F, TAGS_F)},

{"id": "v04", "tipo": "video", "fecha": "2026-11-24T18:00:00", "cta": "guardar", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Tus derechos", "texto": "Se rompe algo importante y [[tu casero no responde.]] ¿Y ahora?"},
  {"t": "paso", "n": "1", "titulo": "Avísale por escrito", "cuerpo": "Con fotos y un presupuesto razonable de la reparación."},
  {"t": "paso", "n": "2", "titulo": "Espera 15 días", "cuerpo": "Desde que recibe tu aviso. Es su plazo para aceptar el presupuesto, proponer otra reparación o hacerla él."},
  {"t": "paso", "n": "3", "titulo": "Si no responde", "cuerpo": "Puedes hacer la obra y descontar su importe de las próximas rentas. Guarda todas las facturas."},
  {"t": "texto", "titulo": "Eso sí: [[no vale para todo]].", "cuerpo": "Solo para daños que afecten a la habitabilidad, la seguridad o la salubridad de la vivienda."},
 ],
 "texto": cap("Desde el 8 de octubre de 2026, si hay un daño que afecta a la habitabilidad, la seguridad o la salubridad de tu vivienda, puedes pedir la reparación por escrito con un presupuesto razonable.\n\nTu casero tiene 15 días naturales para responder. Si no lo hace o se niega sin motivo, puedes hacer la reparación y descontarla de las rentas, con las facturas como prueba.\n\nEn los alquileres temporales, el plazo es de 5 días hábiles.", CTA_G, TAGS_D)},

# ───────────── MIÉRCOLES 25 ─────────────
{"id": "v05", "tipo": "video", "fecha": "2026-11-25T10:00:00", "cta": "fianza", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Fianza", "texto": "¿Al irte del piso [[no firmasteis nada?]] La ley juega a tu favor."},
  {"t": "texto", "titulo": "El documento de finalización", "cuerpo": "Desde el 8 de octubre de 2026, la ley pide dejar por escrito el estado del piso al terminar el contrato, firmado por los dos."},
  {"t": "ley", "ref": "Art. 36.7 · Ley de Arrendamientos Urbanos", "texto": "…se presumirá, salvo prueba en contrario, que la vivienda fue entregada en estado adecuado de conservación."},
  {"t": "texto", "titulo": "Si no se firma [[o no recoge daños]]", "cuerpo": "se presume que la devolviste en buen estado. Si tu casero quiere descontarte algo, tendrá que probarlo."},
  {"t": "texto", "titulo": "Aun así, [[graba el piso]].", "cuerpo": "Fotos y vídeo con fecha el día que te vas. Cuantas más pruebas, mejor."},
 ],
 "texto": cap("Desde el 8 de octubre de 2026, al terminar el contrato hay que dejar por escrito el estado de la vivienda en un documento firmado por los dos.\n\nSi ese documento no se firma, o no recoge ningún desperfecto, la ley presume, salvo prueba en contrario, que la vivienda se entregó en buen estado.\n\nAun así, graba el piso el día que te vas.", CTA_F, TAGS_F)},

{"id": "c03", "tipo": "carrusel", "fecha": "2026-11-25T13:00:00", "cta": "fianza",
 "titulo_tiktok": "Reparaciones del piso de alquiler: quién paga qué",
 "slides": [
  {"t": "portada", "kicker": "Guárdalo", "titulo": "Reparaciones del piso: [[quién paga qué]]"},
  {"t": "texto", "etiqueta": "Casero", "titulo": "Lo necesario para vivir en condiciones", "cuerpo": "Tiene que hacer las reparaciones necesarias para conservar la vivienda habitable, sin subirte la renta por ello."},
  {"t": "texto", "etiqueta": "Tú", "titulo": "Las pequeñas del día a día", "cuerpo": "Las pequeñas reparaciones que exige el desgaste por el uso ordinario de la vivienda."},
  {"t": "texto", "etiqueta": "Tú", "titulo": "Lo que rompas tú", "cuerpo": "Si el deterioro es culpa tuya, la reparación también te toca."},
  {"t": "texto", "etiqueta": "Urgente", "titulo": "Si no puede esperar", "cuerpo": "Avisando antes al casero, puedes hacer las reparaciones urgentes para evitar un daño inminente o una incomodidad grave, y pedirle el importe."},
  {"t": "texto", "etiqueta": "Desde octubre", "titulo": "15 días para responder", "cuerpo": "Si el daño afecta a la habitabilidad, la seguridad o la salubridad, pídela por escrito con presupuesto. Si en 15 días no responde, puedes hacerla y descontarla de la renta."},
  {"t": "cta", "variante": "guardar"},
 ],
 "texto": cap("¿Se ha roto algo en tu piso de alquiler? Depende de qué sea:\n\n• Lo necesario para que la vivienda sea habitable lo paga el casero.\n• Las pequeñas reparaciones del uso diario, tú.\n• Lo que rompas tú, también tú.\n\nY desde el 8 de octubre de 2026, si el casero no responde en 15 días a una reparación de habitabilidad, puedes hacerla y descontarla de la renta.", CTA_G, TAGS_D)},

{"id": "v06", "tipo": "video", "fecha": "2026-11-25T18:00:00", "cta": "agencia", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Frases de inmobiliaria", "texto": "3 cosas que te dirá una inmobiliaria [[(y qué responder)]]"},
  {"t": "dialogo", "frase": "Los honorarios los paga siempre el inquilino.", "respuesta": "En el alquiler de vivienda, desde mayo de 2023 los paga el propietario."},
  {"t": "dialogo", "frase": "No son honorarios, es el estudio de solvencia.", "respuesta": "Da igual el nombre: no se te pueden cobrar bajo ningún concepto o denominación."},
  {"t": "dialogo", "frase": "El seguro de impago es obligatorio.", "respuesta": "Desde octubre de 2026, la ley prohíbe exigírtelo."},
 ],
 "texto": cap("«Lo paga siempre el inquilino», «es el estudio de solvencia», «el seguro de impago es obligatorio»…\n\nNinguna de las tres es cierta en un alquiler de vivienda. ¿Cuál te han dicho a ti?", CTA_A, TAGS_A)},

# ───────────── JUEVES 26 ─────────────
{"id": "v07", "tipo": "video", "fecha": "2026-11-26T10:00:00", "cta": "guardar", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Haz la cuenta", "texto": "¿Cuánto te pueden subir [[el alquiler]] este año?"},
  {"t": "numero", "num": "2 %", "sub": "como máximo hasta el 31 de diciembre de 2027, si no acordáis algo nuevo."},
  {"t": "texto", "titulo": "Imagina: [[900 €]] al mes.", "cuerpo": "Con una subida del 2 %, como mucho pasarías a pagar 918 € al mes."},
  {"t": "texto", "titulo": "¿Tu contrato [[no dice nada]]?", "cuerpo": "Entonces no hay subida: sin un pacto expreso, la renta no se actualiza."},
  {"t": "numero", "num": "2,57 %", "sub": "es el índice del INE de octubre. Aunque sea más alto, el tope del decreto es el 2 %."},
 ],
 "texto": cap("Hasta el 31 de diciembre de 2027, la subida anual del alquiler no puede pasar del 2 % si no hay un nuevo acuerdo con tu casero. Lo dice el Real Decreto-ley 29/2026.\n\nEjemplo: con 900 € al mes, como mucho pasarías a 918 €.\n\nSi tu contrato no prevé ninguna actualización, la renta no se sube. Y si tu renta supera el límite del índice de referencia de precios, tampoco.", CTA_G, TAGS_D)},

{"id": "c04", "tipo": "carrusel", "fecha": "2026-11-26T13:00:00", "cta": "fianza",
 "titulo_tiktok": "El decreto de vivienda en 6 números",
 "slides": [
  {"t": "portada", "kicker": "Guárdalo", "titulo": "El decreto de vivienda en [[6 números]]"},
  {"t": "numero", "num": "2 %", "sub": "como máximo de subida anual de la renta hasta finales de 2027, sin un nuevo acuerdo."},
  {"t": "numero", "num": "15 días", "sub": "tiene tu casero para responder si le pides por escrito una reparación de habitabilidad."},
  {"t": "numero", "num": "1 mes", "sub": "como máximo de garantía adicional, además de la fianza, en un alquiler temporal."},
  {"t": "numero", "num": "12 meses", "sub": "es, como regla general, lo máximo que puede durar un alquiler temporal."},
  {"t": "numero", "num": "2 años", "sub": "de prórroga extraordinaria que puedes pedir si tu contrato acaba antes del 31/12/2028 y cumples los requisitos."},
  {"t": "numero", "num": "8 meses", "sub": "seguidos al corriente de pago: es uno de esos requisitos."},
  {"t": "cta", "variante": "guardar"},
 ],
 "texto": cap("Lo que cambia con el Real Decreto-ley 29/2026, en 6 números. Guárdalo y compártelo con quien viva de alquiler.", CTA_G, TAGS_D)},

{"id": "v08", "tipo": "video", "fecha": "2026-11-26T18:00:00", "cta": "fianza", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Paso a paso", "texto": "Te vas del piso: [[luz, agua y gas]] en 3 pasos."},
  {"t": "paso", "n": "1", "titulo": "Foto de los contadores", "cuerpo": "El último día, con fecha. Es la lectura final de lo que te toca pagar."},
  {"t": "paso", "n": "2", "titulo": "Pide la factura final", "cuerpo": "A cada compañía, si los contratos están a tu nombre. Así sabes exactamente cuánto debes."},
  {"t": "paso", "n": "3", "titulo": "Si te lo descuentan", "cuerpo": "De la fianza solo pueden restarte los suministros pendientes que te tocaban a ti. Pide el detalle por escrito."},
 ],
 "texto": cap("Los suministros son una de las excusas más habituales para no devolver la fianza entera.\n\n1. Haz foto de los contadores el último día.\n2. Pide la factura final de cada suministro a tu nombre.\n3. Si te descuentan algo, pide el detalle por escrito.\n\nSolo te pueden descontar lo que te correspondía pagar a ti.", CTA_F, TAGS_F)},

# ───────────── VIERNES 27 ─────────────
{"id": "v09", "tipo": "video", "fecha": "2026-11-27T10:00:00", "cta": "guardar", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Frases de casero", "texto": "3 frases de casero [[que no tienes por qué aceptar]]"},
  {"t": "dialogo", "frase": "El IBI lo pagas tú.", "respuesta": "Desde octubre de 2026, la ley dice que los impuestos de la vivienda no se le pueden imponer al inquilino."},
  {"t": "dialogo", "frase": "La comunidad va aparte.", "respuesta": "Solo si está pactado por escrito en el contrato, con su importe anual."},
  {"t": "dialogo", "frase": "La caldera, arréglala tú.", "respuesta": "Si afecta a la habitabilidad, la reparación es del casero. Pídesela por escrito."},
 ],
 "texto": cap("«El IBI lo pagas tú», «la comunidad va aparte», «la caldera, arréglala tú»…\n\nDesde el 8 de octubre de 2026, los tributos de la vivienda no se pueden imponer al inquilino. Los gastos de comunidad, solo si están pactados por escrito con su importe anual. Y las reparaciones necesarias para que la vivienda sea habitable son del casero.\n\n¿Cuál te han dicho a ti?", CTA_G, TAGS_D)},

{"id": "c05", "tipo": "carrusel", "fecha": "2026-11-27T13:00:00", "cta": "agencia",
 "titulo_tiktok": "5 mitos sobre los honorarios de la inmobiliaria",
 "slides": [
  {"t": "portada", "kicker": "Mitos", "titulo": "5 mitos sobre los honorarios de [[la inmobiliaria]]"},
  {"t": "mito", "mito": "Los honorarios los paga siempre el inquilino.", "real": "En el alquiler de vivienda, desde el 26 de mayo de 2023 los paga el propietario."},
  {"t": "mito", "mito": "Si lo llaman «estudio de solvencia», sí me lo pueden cobrar.", "real": "No se te pueden repercutir bajo ningún concepto o denominación."},
  {"t": "mito", "mito": "Renovar el contrato sí se paga.", "real": "Desde octubre de 2026, la ley incluye también la novación y la renovación del contrato."},
  {"t": "mito", "mito": "Los «servicios extra» los pago sí o sí.", "real": "Solo si los pediste tú por escrito, sabiendo antes que eran opcionales y su coste."},
  {"t": "mito", "mito": "Si ya lo pagué, no hay nada que hacer.", "real": "Puedes reclamarlo. Guarda la factura o el justificante del pago."},
  {"t": "cta", "variante": "agencia"},
 ],
 "texto": cap("5 cosas que mucha gente cree sobre los honorarios de la inmobiliaria y no son así.\n\nEn el alquiler de vivienda, los gastos de gestión inmobiliaria y de formalización del contrato los paga el propietario. Y desde el 8 de octubre de 2026 la ley lo detalla aún más: tampoco con otro nombre ni al renovar.", CTA_A, TAGS_A)},

{"id": "v10", "tipo": "video", "fecha": "2026-11-27T18:00:00", "cta": "guardar", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Alquiler temporal", "texto": "¿Contrato «temporal» para vivir ahí [[todo el año?]]"},
  {"t": "texto", "titulo": "Tiene que haber [[una causa real]].", "cuerpo": "Escrita en el contrato y demostrable. Si hay dudas, la tiene que probar el casero."},
  {"t": "texto", "titulo": "Si no la hay, [[es vivienda habitual]].", "cuerpo": "Y se aplican sus reglas: entre ellas, una duración mínima de 5 años (7 si el casero es una empresa)."},
  {"t": "numero", "num": "12 meses", "sub": "es, como regla general, lo máximo que puede durar. Y si encadenan más de dos contratos seguidos, el primero cuenta como vivienda habitual."},
 ],
 "texto": cap("Un alquiler temporal necesita una causa real y demostrable, escrita en el contrato. Si falta, se trata como un alquiler de vivienda habitual, con sus reglas: entre ellas, una duración mínima de 5 años (7 si el casero es una empresa).\n\nOjo: estas reglas del Real Decreto-ley 29/2026 son para los contratos firmados desde el 8 de octubre de 2026. Los anteriores siguen con el régimen antiguo hasta que terminen.", CTA_G, TAGS_D)},

# ───────────── SÁBADO 28 ─────────────
{"id": "v11", "tipo": "video", "fecha": "2026-11-28T10:00:00", "cta": "guardar", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Checklist", "texto": "El día que entras al piso, [[haz esto.]]"},
  {"t": "lista", "titulo": "Antes de meter tus cosas:", "items": ["Fotos y vídeo de cada habitación, con fecha", "Anota cada desperfecto que veas", "Foto de los contadores"]},
  {"t": "lista", "titulo": "Y por escrito:", "items": ["El contrato, firmado por los dos", "El recibo de la fianza", "La lista de desperfectos, enviada al casero"]},
  {"t": "texto", "titulo": "El día que te vayas, [[te lo agradecerás]].", "cuerpo": "Es tu prueba de cómo estaba el piso cuando llegaste."},
 ],
 "texto": cap("Checklist para el día que entras en un piso de alquiler:\n\n✓ Fotos y vídeo de cada habitación, con fecha\n✓ Anota cada desperfecto\n✓ Foto de los contadores\n✓ Contrato firmado por los dos\n✓ Recibo de la fianza\n✓ Envía al casero la lista de desperfectos\n\nSi tu casero no quiere hacer el contrato por escrito, puedes exigirlo.", CTA_G, TAGS_F)},

{"id": "c06", "tipo": "carrusel", "fecha": "2026-11-28T13:00:00", "cta": "fianza",
 "titulo_tiktok": "Al devolver las llaves: el documento que protege tu fianza",
 "slides": [
  {"t": "portada", "kicker": "Fianza", "titulo": "Al devolver las llaves: [[el documento que te protege]]"},
  {"t": "texto", "etiqueta": "Qué es", "titulo": "El documento de finalización", "cuerpo": "Desde el 8 de octubre de 2026, la ley pide dejar por escrito el estado del piso al terminar el contrato, firmado por los dos."},
  {"t": "lista", "etiqueta": "Consejo", "titulo": "Lo que te conviene que recoja", "items": ["La fecha en que entregas las llaves", "El estado de cada habitación", "Los desperfectos, o «ninguno»", "La lectura de los contadores"]},
  {"t": "texto", "etiqueta": "A tu favor", "titulo": "Si no recoge desperfectos", "cuerpo": "o si no llega a firmarse, se presume, salvo prueba en contrario, que devolviste la vivienda en buen estado."},
  {"t": "texto", "etiqueta": "Consejo", "titulo": "Guarda tus propias pruebas", "cuerpo": "Fotos y vídeo con fecha del día que te vas. Y una copia del documento firmado."},
  {"t": "numero", "num": "1 mes", "sub": "tiene tu casero para devolverte la fianza desde que entregas las llaves."},
  {"t": "cta", "variante": "burofax"},
 ],
 "texto": cap("Desde el 8 de octubre de 2026, al terminar el contrato hay que dejar por escrito el estado de la vivienda, en un documento firmado por los dos.\n\nSi no se firma o no recoge desperfectos, se presume, salvo prueba en contrario, que la vivienda se entregó en buen estado. Guárdalo para el día que te mudes.", CTA_F, TAGS_F)},

{"id": "v12", "tipo": "video", "fecha": "2026-11-28T18:00:00", "cta": "guardar", "musica": 2,
 "escenas": [
  {"t": "hook", "kicker": "Tus derechos", "texto": "¿Puede entrar tu casero [[con su llave]] cuando quiera?"},
  {"t": "texto", "titulo": "No sin tu permiso.", "cuerpo": "Mientras vives ahí, es tu domicilio. Y la Constitución dice que el domicilio es inviolable."},
  {"t": "ley", "ref": "Art. 18.2 · Constitución Española", "texto": "El domicilio es inviolable. Ninguna entrada o registro podrá hacerse en él sin consentimiento del titular o resolución judicial, salvo en caso de flagrante delito."},
  {"t": "texto", "titulo": "¿Visitas o reparaciones?", "cuerpo": "Se acuerdan contigo: día y hora. Tener una llave no le da derecho a entrar."},
 ],
 "texto": cap("Que tu casero tenga una copia de la llave no significa que pueda entrar cuando quiera.\n\nMientras vives ahí, es tu domicilio, y el artículo 18.2 de la Constitución dice que el domicilio es inviolable: nadie puede entrar sin tu consentimiento o una resolución judicial, salvo flagrante delito.\n\nLas visitas y las reparaciones se acuerdan contigo.", CTA_G, TAGS_D)},

# ───────────── DOMINGO 29 ─────────────
{"id": "v13", "tipo": "video", "fecha": "2026-11-29T10:00:00", "cta": "fianza", "musica": 0,
 "escenas": [
  {"t": "hook", "kicker": "Haz la cuenta", "texto": "Imagina: alquiler de 800 € y te piden [[fianza + 3 meses]] de garantía."},
  {"t": "numero", "num": "800 €", "sub": "de fianza: un mes de renta."},
  {"t": "numero", "num": "1.600 €", "sub": "como máximo de garantía adicional: dos meses, en contratos de hasta 5 años (7 si el casero es una empresa)."},
  {"t": "texto", "titulo": "Ese [[tercer mes]] no te lo pueden exigir.", "cuerpo": "Ni que contrates un seguro de impago. Y si el alquiler es temporal, la garantía adicional es de un mes como máximo."},
 ],
 "texto": cap("Un ejemplo: alquiler de 800 € al mes.\n\nFianza: 800 €. Garantía adicional: como máximo 1.600 € (dos meses) en contratos de hasta 5 años, o 7 si el casero es una empresa. Un tercer mes de garantía no te lo pueden exigir, y tampoco un seguro de impago.\n\nAl final del contrato, todo eso se devuelve si no hay deudas ni daños.", CTA_F, TAGS_F)},

{"id": "c07", "tipo": "carrusel", "fecha": "2026-11-29T13:00:00", "cta": "fianza",
 "titulo_tiktok": "¿Se acaba tu contrato de alquiler? Puedes pedir hasta 2 años más",
 "slides": [
  {"t": "portada", "kicker": "Tus derechos", "titulo": "¿Se acaba tu contrato? Puedes pedir [[hasta 2 años más]]"},
  {"t": "lista", "etiqueta": "Requisitos", "titulo": "Si se cumple todo esto:", "items": ["Es tu vivienda habitual y el contrato estaba vigente el 8/10/2026", "Su prórroga obligatoria o tácita acaba antes del 31/12/2028", "Estás al corriente de pago, y lo has estado los 8 meses anteriores"]},
  {"t": "texto", "etiqueta": "Cómo", "titulo": "Lo tienes que pedir tú", "cuerpo": "Es una prórroga «previa solicitud del arrendatario». Mejor por escrito y con fecha."},
  {"t": "numero", "num": "2 años", "sub": "como máximo, en plazos anuales, con las mismas condiciones de tu contrato."},
  {"t": "texto", "etiqueta": "No procede", "titulo": "Cuándo no se aplica", "cuerpo": "Si pactáis otra cosa, firmáis un contrato nuevo, el casero comunica que necesita la vivienda o renováis con una renta al menos un 5 % más baja."},
  {"t": "texto", "etiqueta": "Zona tensionada", "titulo": "Hay otra prórroga", "cuerpo": "En zonas de mercado residencial tensionado, la ley prevé una prórroga de hasta 3 años, también a petición tuya."},
  {"t": "cta", "variante": "guardar"},
 ],
 "texto": cap("Si tu contrato de alquiler de vivienda habitual estaba vigente el 8 de octubre de 2026 y su prórroga acaba antes del 31 de diciembre de 2028, puedes pedir una prórroga extraordinaria de hasta 2 años, en plazos anuales y con las mismas condiciones.\n\nRequisito: estar al corriente de pago y haberlo estado los 8 meses anteriores. Lo dice la disposición final quinta del Real Decreto-ley 29/2026.", CTA_G, TAGS_D)},

{"id": "v14", "tipo": "video", "fecha": "2026-11-29T18:00:00", "cta": "fianza", "musica": 1,
 "escenas": [
  {"t": "hook", "kicker": "Pisos compartidos", "texto": "¿Alquilas [[una habitación?]] La ley también va contigo."},
  {"t": "ley", "ref": "Art. 2.1 · Ley de Arrendamientos Urbanos", "texto": "…cuyo destino primordial sea satisfacer la necesidad de vivienda del arrendatario, incluido el arrendamiento parcial de una habitación o estancia de la vivienda."},
  {"t": "texto", "titulo": "La suma [[tiene un límite]].", "cuerpo": "Lo que se pague entre todas las habitaciones no puede superar la renta del piso completo."},
  {"t": "texto", "titulo": "Pide el contrato [[por escrito]].", "cuerpo": "Puedes exigirlo. Y guarda el recibo de lo que pagues de fianza."},
 ],
 "texto": cap("Desde el 8 de octubre de 2026, la Ley de Arrendamientos Urbanos incluye expresamente el alquiler de una habitación como arrendamiento de vivienda habitual.\n\nY la suma de las rentas de todas las habitaciones alquiladas a la vez no puede superar la renta del piso completo.\n\nSi vives en un piso compartido, pide tu contrato por escrito y guarda el recibo de la fianza.", CTA_F, TAGS_D)},
]
