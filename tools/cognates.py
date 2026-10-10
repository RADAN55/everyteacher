#!/usr/bin/env python3
"""The word lists behind cognate-hunt.html.

    python3 tools/cognates.py        # writes cognates.js

Three lists, in order of trust:

  SURE      English → Spanish pairs a bilingual teacher would vouch for on
            sight. These light up with no question mark. School words first:
            the vocabulary of science, history, math and ELA textbooks.
  FALSE     Words that look Spanish and mean something else. These are the
            ones that embarrass a student, so they are flagged, not lit.
  RULES     Ending patterns that turn an English word into a likely Spanish
            one (-tion → -ción). A word caught only by a rule is marked as a
            guess, and the page says so.

A pair belongs in SURE only if a student could SEE it: the two words have to
look alike on the page, not just mean the same thing. war/guerra is a
translation; battle/batalla is a cognate.

Add to SURE in the plain "english: spanish" form. One pair per line. Keep
the Spanish in its dictionary form (singular, masculine, infinitive).
"""
import json
import pathlib
import re

SURE = """
# --- science ---
animal: animal          plant: planta           cell: célula            organism: organismo
energy: energía         force: fuerza           gravity: gravedad       mass: masa
matter: materia         molecule: molécula      atom: átomo             element: elemento
electron: electrón      proton: protón          neutron: neutrón        nucleus: núcleo
temperature: temperatura   evaporation: evaporación   condensation: condensación
precipitation: precipitación   photosynthesis: fotosíntesis   respiration: respiración
oxygen: oxígeno         hydrogen: hidrógeno     carbon: carbono         nitrogen: nitrógeno
mineral: mineral        rock: roca              volcano: volcán         planet: planeta
solar: solar            system: sistema         orbit: órbita           satellite: satélite
climate: clima          atmosphere: atmósfera   ocean: océano           continent: continente
ecosystem: ecosistema   habitat: hábitat        species: especie        population: población
bacteria: bacteria      virus: virus            infection: infección    vaccine: vacuna
muscle: músculo         skeleton: esqueleto     organ: órgano           circulation: circulación
digestion: digestión    nutrition: nutrición    protein: proteína       vitamin: vitamina
experiment: experimento   hypothesis: hipótesis   observation: observación
conclusion: conclusión  evidence: evidencia     variable: variable      data: datos
laboratory: laboratorio   microscope: microscopio   telescope: telescopio            electricity: electricidad   circuit: circuito   battery: batería
liquid: líquido         solid: sólido           gas: gas                vapor: vapor
density: densidad       volume: volumen         velocity: velocidad     acceleration: aceleración
friction: fricción      reaction: reacción      solution: solución
fossil: fósil           dinosaur: dinosaurio    extinction: extinción   evolution: evolución
adaptation: adaptación  reproduction: reproducción   genetic: genético   mutation: mutación
erosion: erosión        sediment: sedimento     crystal: cristal        magma: magma
# --- math ---
number: número          fraction: fracción      decimal: decimal        percent: porcentaje
equation: ecuación      variable: variable      function: función       expression: expresión
coefficient: coeficiente   exponent: exponente  factor: factor          multiple: múltiplo
sum: suma               difference: diferencia  product: producto       quotient: cociente
divide: dividir         multiply: multiplicar   calculate: calcular     estimate: estimar
total: total            area: área              perimeter: perímetro    volume: volumen
circle: círculo         triangle: triángulo     rectangle: rectángulo   polygon: polígono
angle: ángulo           line: línea             parallel: paralelo      perpendicular: perpendicular
diameter: diámetro      radius: radio           circumference: circunferencia
geometry: geometría     algebra: álgebra        statistics: estadística   probability: probabilidad
graph: gráfica          table: tabla            diagram: diagrama       coordinate: coordenada
positive: positivo      negative: negativo            equivalent: equivalente
proportion: proporción            interval: intervalo     median: mediana
maximum: máximo         minimum: mínimo         approximately: aproximadamente
dozen: docena           double: doble           triple: triple          unit: unidad
meter: metro            kilometer: kilómetro    gram: gramo             liter: litro
second: segundo         minute: minuto          hour: hora
# --- social studies ---
history: historia       government: gobierno    democracy: democracia   republic: república
constitution: constitución   congress: congreso   senate: senado
president: presidente   election: elección      vote: voto
nation: nación          state: estado           territory: territorio   colony: colonia
independence: independencia   revolution: revolución   declaration: declaración
liberty: libertad       justice: justicia
economy: economía       commerce: comercio      industry: industria     agriculture: agricultura
immigrant: inmigrante   migration: migración    population: población   community: comunidad
culture: cultura        tradition: tradición    religion: religión      society: sociedad
civilization: civilización   empire: imperio    monarchy: monarquía     dictator: dictador             battle: batalla          soldier: soldado
treaty: tratado         alliance: alianza       conflict: conflicto     invasion: invasión
map: mapa               region: región          capital: capital        frontier: frontera
continent: continente   river: río              mountain: montaña       desert: desierto          decade: década        modern: moderno
document: documento     primary: primario          evidence: evidencia
cause: causa            effect: efecto          consequence: consecuencia   result: resultado
segregation: segregación   discrimination: discriminación   protest: protesta
movement: movimiento    reform: reforma         progress: progreso      depression: depresión
# --- ELA and school ---
author: autor    narrator: narrador      poem: poema
poetry: poesía          novel: novela           fiction: ficción        drama: drama
theme: tema             conflict: conflicto             dialogue: diálogo
metaphor: metáfora      simile: símil           symbol: símbolo         irony: ironía
paragraph: párrafo       verb: verbo
adjective: adjetivo     adverb: adverbio        pronoun: pronombre      preposition: preposición
vocabulary: vocabulario   definition: definición   dictionary: diccionario   grammar: gramática
analyze: analizar       compare: comparar       contrast: contrastar    describe: describir
explain: explicar       identify: identificar   infer: inferir          interpret: interpretar
argue: argumentar       argument: argumento     opinion: opinión        persuade: persuadir      predict: predecir       evaluate: evaluar       organize: organizar
information: información   idea: idea           detail: detalle         example: ejemplo
introduction: introducción   conclusion: conclusión   text: texto       title: título
class: clase            student: estudiante     professor: profesor     calendar: calendario
cafeteria: cafetería    gymnasium: gimnasio     office: oficina         computer: computadora           paper: papel      page: página
music: música           art: arte               science: ciencia        mathematics: matemáticas
exam: examen            project: proyecto       presentation: presentación
family: familia         doctor: doctor          hospital: hospital      medicine: medicina
# --- added after the first run on real paragraphs ---
chemical: químico       chemistry: química      physics: física         biology: biología
glucose: glucosa        chlorophyll: clorofila  absorb: absorber        combine: combinar
essential: esencial     depend: depender        authority: autoridad    security: seguridad
convention: convención  delegate: delegado      debate: debatir         controversial: controvertido
central: central        individual: individual  opponent: oponente      emerge: emerger
historian: historiador  operation: operación    donation: donación      stable: estable
distribute: distribuir  equally: igualmente     exactly: exactamente    finally: finalmente
# --- academic words that travel everywhere ---
important: importante   different: diferente    similar: similar        possible: posible
necessary: necesario    natural: natural        general: general        special: especial
specific: específico    complete: completo      correct: correcto       exact: exacto
normal: normal          common: común           final: final            original: original
part: parte             form: forma             type: tipo              model: modelo
process: proceso        structure: estructura   section: sección        center: centro
problem: problema       method: método          object: objeto          material: material
condition: condición    situation: situación    action: acción          activity: actividad
direction: dirección    position: posición      distance: distancia     space: espacio        limit: límite           order: orden
plan: plan              list: lista             group: grupo            pair: par
reason: razón           purpose: propósito      relation: relación      connection: conexión
create: crear           produce: producir       prepare: preparar       use: usar
observe: observar       investigate: investigar   discover: descubrir   demonstrate: demostrar
decide: decidir         consider: considerar    continue: continuar     include: incluir
indicate: indicar       permit: permitir        present: presentar      represent: representar
require: requerir       respond: responder      select: seleccionar     separate: separar
"""

# Looks Spanish, isn't. english: what the Spanish look-alike actually means
FALSE = """
actually: actualmente means currently — not "in fact" (en realidad)
assist: asistir means to attend — not "to help" (ayudar)
attend: atender means to pay attention or serve — not "to be present at" (asistir)
carpet: carpeta means folder — not a rug (alfombra)
college: colegio means a K-12 school — not university (universidad)
compromise: compromiso means commitment — not a middle-ground deal (acuerdo)
constipated: constipado means having a cold — not what you think (estreñido)
contest: contestar means to answer — not a competition (concurso)
deception: decepción means disappointment — not a lie (engaño)
embarrassed: embarazada means pregnant — not ashamed (avergonzado)
exit: éxito means success — not the way out (salida)
fabric: fábrica means factory — not cloth (tela)
idiom: idioma means language — not a figure of speech (modismo)
introduce: introducir means to insert — not to present a person (presentar)
large: largo means long — not big (grande)
lecture: lectura means reading — not a talk (conferencia)
library: librería means bookstore — not a library (biblioteca)
molest: molestar means to bother — a much milder word
notice: noticia means news — not to observe (notar)
once: once means eleven — a number, not "one time" (una vez)
parents: parientes means relatives — not mother and father (padres)
pie: pie means foot — not dessert (pastel)
realize: realizar means to carry out — not to become aware (darse cuenta)
record: recordar means to remember — not to write down (grabar, registrar)
rope: ropa means clothes — not a cord (cuerda)
sane: sano means healthy — not of sound mind (cuerdo)
sensible: sensible means sensitive — not practical (sensato)
soap: sopa means soup — not for washing (jabón)
success: suceso means an event — not achievement (éxito)
support: soportar means to put up with — not to back someone (apoyar)
sympathetic: simpático means nice, likeable — not compassionate (comprensivo)
tuna: tuna means prickly pear — not the fish (atún)
""".strip()

# (English ending, Spanish ending). Order matters: longer first. Only endings
# that are right far more often than wrong; -ly, -al, -or were dropped as noisy.
RULES = [
    ("ization", "ización"), ("ication", "icación"), ("tion", "ción"), ("sion", "sión"),
    ("ity", "idad"), ("ancy", "ancia"), ("ency", "encia"), ("ance", "ancia"),
    ("ence", "encia"), ("ment", "mento"), ("ous", "oso"), ("ical", "ico"), ("ic", "ico"),
    ("ive", "ivo"), ("ary", "ario"), ("ory", "orio"), ("ist", "ista"), ("ism", "ismo"),
    ("ble", "ble"), ("ify", "ificar"), ("ize", "izar"),
]


def parse_sure():
    out = {}
    for line in SURE.splitlines():
        line = line.split("#")[0]
        for m in re.finditer(r"([a-z]+):\s*([^\s:]+(?:\s[^\s:]+)*?)(?=\s{2,}|\s*$)", line):
            out[m.group(1)] = m.group(2).strip()
    return out


def parse_false():
    out = {}
    for line in FALSE.splitlines():
        en, rest = line.split(":", 1)
        out[en.strip()] = rest.strip()
    return out


if __name__ == "__main__":
    sure, false = parse_sure(), parse_false()
    js = ("/* Generated by tools/cognates.py — edit that file, not this one. */\n"
          "window.COGNATES=" + json.dumps(
              {"sure": sure, "false": false, "rules": RULES},
              ensure_ascii=False, separators=(",", ":")) + ";\n")
    pathlib.Path(__file__).resolve().parent.parent.joinpath("cognates.js").write_text(js, encoding="utf-8")
    print(f"{len(sure)} sure pairs, {len(false)} false friends, {len(RULES)} rules -> cognates.js")
