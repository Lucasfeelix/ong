from django.shortcuts import render


def alunos(request):
    return render(request, 'people/listagem.html')
