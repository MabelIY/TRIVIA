import os  
import random
import time

iniciar_trivia = True
intentos = 0 
while iniciar_trivia == True:
  os. system('clear')
  intentos = intentos + 1
  print("\033[34m              JUEGO DE LA TRIVIA\033[39m")
  print("\033[34m              *******************\033[39m")
  puntaje = random.randint(1,5) 
  
  nombre = input("\033[94m ¿Cual es tu nombre?  \033[39m")
  print("\033[94m\nHola " , nombre , ". Bienvenido al juego de la trivia. Por favor responde las siguientes preguntas seleccionando una alternativa y presionando 'Enter' para enviar tu respuesta.\nPor cada respuesta correcta ganas 10 puntos.\033[39m")
  print("\033[94mComenzaras el juego con una bonificacion especial de ",puntaje," puntos\033[39m")
  print("\033[94mBuena Suerte!\n\033[39m")
  
  preguntas =["\033[94m1. ¿Quién descubrio America\033[39m",
              "\033[94m2. ¿Qué escritor español era conocido como 'el manco de Lepanto'?\033[39m",
              "\033[94m3. ¿Quién fue el primer virrey del Perú?\033[39m",
              "\033[94m4. ¿Quién fue el primer presidente del Perú\033[39m"]
  
  alternativas = [["a. Francisco Pizarro","b. Manco capac","c. Hernando de Luque","d. Cristobal colón"],
                ["a. Rubén Dario","b. Miguel de Cervantes","c. Octavio Paz","d. Miguel Angel"],
                ["a. Blasco Núñez Vela","b. Francisco de Toledo","c. Enríquez de Almansa","d. Fernando Torres de Portugal"],
                ["a. José de la Riva Agüero","b. Jose de la Serna","c. Alberto Fujimori","d. Ollanta Humala"]]
  
  claves =     ["d",
                "b",
                "a",
                "a"]
  
  for i in range(4):
    print(preguntas[i])
    for j in range(4):
      print(str(alternativas[i][j]))
    
    print("Por favor ", nombre, ". Elije una respuesta")
    respuesta = input("\nTu Respuesta: ")
    while respuesta not in ("a","b","c","d"):
          respuesta = input("\nDebes responder solo una de las alternativas a, b, c o d. Por favor  ingresa nuevamente tu respuesta: ")
  
    if respuesta == claves[i]:
      puntaje = puntaje + 10
      print("\033[32mMuy bien! ", nombre,". La respuesta es correcta. Ganaste 10 puntos!\033[39m")
      time.sleep(2)
    else:
      print("\033[31mTe equivocaste! ", nombre,". La respuesta es incorrecta\033[39m")
      time.sleep(2)
  
  
    os. system('clear')
  
  print("Gracias ",nombre," por jugar mi trivia. Alcanzaste ", puntaje ," puntos.")
  print("¿Deseas intetar de nuevo?")
  repetir_trivia = input("Ingresa 'S' para repetir y cualquier otra tecla para finalizar\n").lower()
  if repetir_trivia !="s":
    print("Espero ", nombre," que lo hayas pasado bien. Hasta Pronto!")
    iniciar_trivia = False
    