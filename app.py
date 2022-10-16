import cv2
import mediapipe as mp

# Inicializar o opencv e o mediapipa

webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto  = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
  # Ler as informações da webcam
  verificador, frame = webcam.read()
  
  if not verificador:
    break

  # reconhecer os rosts que tem ali dentro
  lista_rostos = reconhecedor_rostos.process(frame)

  if lista_rostos.detections:
    for rosto in lista_rostos.detections:
      # desenhar os rostos na imagem
      desenho.draw_detection(frame, rosto)

  cv2.imshow("Teste de Deteccao de Rostos",frame)
  
  # quanto apertar ESC, para o loop
  if cv2.waitKey(5) == 27:
    break

webcam.release()