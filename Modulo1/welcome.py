# programa de bienvenida.
# Created by Lázaro Alonso, modified by Esteban Jiménez Rodríguez.
from time import sleep
def print_words(sentence):
    for word in sentence.split():
        for l in word:
            sleep(.05)
            print(l, end = '')
        print(end = ' ')
sentence1 = 'Hola, bienvenid@ a la asignatura de Portafolios de Inversión.'
print_words(sentence1)
sentence2 = 'Soy Harry Markowitz y me gustaría saber un poco acerca de ti, por ejemplo'
print_words(sentence2)
sentence3 = '¿Cuál es tu nombre?'
print_words(sentence3)
prompt = ' >> '
nombre_usuario = input(prompt)
sentence4 = 'Gusto en conocerte ' + nombre_usuario + ', espero que te guste el curso.'
print_words(sentence4)
sentence5 = 'Acá aprenderemos cómo es que los inversionistas racionales toman decisiones acerca de su inversión.'
print_words(sentence5)
sentence7 = 'Pero bueno, eso luego, ¿Qué edad tienes?'
print_words(sentence7)
edad = input(prompt)
sentence8 = '¿Te ha gustado esta bienvenida?'
print_words(sentence8)
gustar = input(prompt)
sfinal = ' Muy bien %s, dices que %s te gustó la bienvenida.' % (nombre_usuario, gustar)
sfinal3 = 'Y además estas por cumplir %s años. Fue un gusto conocerte, hasta pronto!' %  (int(edad)+ 1 )
print_words(sfinal)
print_words(sfinal3)
