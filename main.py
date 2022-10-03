from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # oculta a janela principal do tkinter
img = askopenfilename() # abre uma janela para selecionar a imagem

imagem = Image.open(img) # carrega a imagem
imagem = img.convert('L') # coverte a imagem para preto e branco
imagem.save(img) # salva a imagem em preto e branco