
import cv2


def capturar_e_salvar():

    webcam = cv2.VideoCapture(0)

    if not webcam.isOpened():
        print("Erro ao abrir a webcam.")
        webcam.release()
        return  # early return (retorna antes do fim da def)

    fonte = cv2.FONT_HERSHEY_SIMPLEX
    escala = 0.6
    cor texto = (255, 255, 255)
    espessura = 1

    print("[ESPAÇO] Capturar imagem")
    print("[ESCAPE] Sair")

    while True:  # DO-WHILE será executado pelo menos uma vez
        status, frame = webcam.read()  # captura o frame da webcam
        # desempacota o retorno da função read() em duas variáveis.

        if not status:
            print("Erro ao capturar o frame.")
            break

        frame limpo = frame.copy()

        cv2.rectangle(frame, (10,10), (320, 75), (0,0,0), -1)
        cv2.putText(frame, "[ESPAÇO] Salvar foto", (20, 35), fonte, escala, cor_texto, )

        cv2.imshow("Captura da Webcam local", frame)

        tecla = cv2.waitKey(1) & 0xFF

        if tecla == 32:
            cv2.imwrite("foto.jpg", frame)
            print("Foto salva como foto.jpg")

            foto.cinza = cv2.Color(frame, cv2.COLOR_BGR2)

        elif tecla == 27:
            print("Encerrando câmera...")
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capturar_e_salvar()
