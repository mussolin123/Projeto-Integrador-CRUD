from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Aluno
from .serializers import AlunoSerializer
import face_recognition
from django.http import JsonResponse, HttpResponse

# View para a página inicial
def home(request):
    return HttpResponse("Bem-vindo ao sistema de reconhecimento facial!")

# ViewSet para o Aluno
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
   # permission_classes = [AllowAny]

    # Listar alunos com filtragem
    def list(self, request):
        nome = request.GET.get('nome', None)
        matricula = request.GET.get('matricula', None)
        
        # Filtra os alunos de acordo com os parâmetros fornecidos
        alunos = Aluno.objects.all()

        # Aponta filtros específicos
        if nome and matricula:
            # Busca por nome e matrícula ao mesmo tempo
            alunos = alunos.filter(nome__icontains=nome, matricula=matricula)
        elif nome:
            alunos = alunos.filter(nome__icontains=nome)
        elif matricula:
            alunos = alunos.filter(matricula=matricula)

        serializer = self.get_serializer(alunos, many=True)
        return Response(serializer.data)

    # Adicione o método DELETE para remover o aluno
    #Método DELETE para deletar um aluno pelo ID (ou matrícula)
    def destroy(self, request, *args, **kwargs):
        matricula = kwargs.get('pk')  # 'pk' é o identificador padrão do Django
        try:
            aluno = Aluno.objects.get(matricula=matricula)
            aluno.delete()
            return Response({'message': 'Aluno deletado com sucesso'}, status=204)
        except Aluno.DoesNotExist:
            return Response({'message': 'Aluno não encontrado'}, status=404)
        
    # Criar um aluno via API
def create(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()

            aluno = serializer.instance

            # Adicione tratamento seguro ao chamar a função facial
            try:
                aluno.salvar_caracteristicas_facial()  # Extrai e salva a face enviada.
            except Exception as e:
                return Response(
                    {"message": "Aluno salvo, mas erro ao processar a face: " + str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"message": "Erro ao salvar aluno: " + str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def reconhecer_aluno(request):
    if 'foto' in request.FILES:
        foto_enviada = request.FILES['foto']
        foto_enviada_imagem = face_recognition.load_image_file(foto_enviada)
        encodings_foto_enviada = face_recognition.face_encodings(foto_enviada_imagem)

        if not encodings_foto_enviada:
            return JsonResponse({'erro': 'Nenhuma face detectada'}, status=400)

        for aluno in Aluno.objects.all():
            if aluno.features:
                features_aluno = eval(aluno.features)
                matches = face_recognition.compare_faces([features_aluno], encodings_foto_enviada[0])

                if matches[0]:
                    return JsonResponse({'matricula': aluno.matricula, 'nome': aluno.nome})

        return JsonResponse({'erro': 'Aluno não reconhecido'}, status=404)
    else:
        return JsonResponse({'erro': 'Nenhuma foto foi enviada'}, status=400)
    
# Gera o token logo após o cadastro do usuário #
class UserRegisterAPIView(APIView):
    permission_classes = [AllowAny]  # Acesso público ao endpoint