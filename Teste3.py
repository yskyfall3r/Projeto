import RPi.GPIO as GPIO
import time

# Configura os pinos
#LM358 = 17  # Entrada do comparador (HIGH = travado)
M1_IN1 = 27     # Motor 1 - Sentido horário
M1_IN2 = 22     # Motor 1 - Sentido anti-horário

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Configura GPIOs
#GPIO.setup(LM358, GPIO.IN)
GPIO.setup(LM358, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(M1_IN1, GPIO.OUT)
GPIO.setup(M1_IN2, GPIO.OUT)

def motor1_horario():
    GPIO.output(M1_IN1, GPIO.HIGH)
    GPIO.output(M1_IN2, GPIO.LOW)

def motor1_antihorario():
    GPIO.output(M1_IN1, GPIO.LOW)
    GPIO.output(M1_IN2, GPIO.HIGH)

def motor1_parar():
    GPIO.output(M1_IN1, GPIO.LOW)
    GPIO.output(M1_IN2, GPIO.LOW)


try:
    motor1_ativo = True

    while motor1_ativo:
        motor1_horario()
        time.sleep(0.1)
        motor1_antihorario()
        time.sleep(0.1)
        motor1_horario()
        time.sleep(0.1)
        motor1_antihorario()
        time.sleep(0.1)
        motor1_horario()
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário.")

finally:
    motor1_parar()
    GPIO.cleanup()
