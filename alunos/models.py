from django.db import models
import face_recognition
import os
from django.conf import settings

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    foto = models.ImageField(upload_to='fotos_alunos/')  # Pasta para armazenar as fotos
    features = models.TextField(blank=True, null=True)  # Para armazenar as características faciais

    def __str__(self):
        return self.nome

    def salvar_caracteristicas_facial(self):
        """
        Extrai as características faciais da foto do aluno e as salva no banco de dados.
        """
        # Caminho completo da foto do aluno
        caminho_foto = os.path.join(settings.MEDIA_ROOT, self.foto.name)

        # Carregar a imagem e detectar as faces
        imagem = face_recognition.load_image_file(caminho_foto)
        faces = face_recognition.face_encodings(imagem)

        if faces:
            # Apenas armazenar as características da primeira face detectada
            self.features = str(faces[0].tolist())  # Converte a lista de características para string
            self.save()
        else:
            raise ValueError("Nenhuma face detectada na foto.")
