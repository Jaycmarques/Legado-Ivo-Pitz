from django.shortcuts import render
from .models import FamilyMember, Relationship
from django.db.models import Q, Prefetch, Func, Value
from django.views.decorators.cache import cache_page
from django.db.models.functions import Lower


class Unaccent(Func):
    function = 'unaccent'

@cache_page(60*15)
def familytree(request):
    # Carregando apenas os membros de primeiro nível
    family_members = FamilyMember.objects.filter(parents__isnull=True).prefetch_related(
        'children'
    ).order_by('id')
    
    return render(request, 'familytree/index.html', {'family_members': family_members})

def detail(request):
    member_id = request.GET.get('id')
    try:
        member = FamilyMember.objects.prefetch_related(
            Prefetch('children', queryset=Relationship.objects.select_related('child'))
        ).get(id=member_id)

        children = member.children.all()  # Aqui você já pré-carregou os filhos
        return render(request, 'familytree/familymember.html', {'member': member, 'children': children})
    except FamilyMember.DoesNotExist:
        return render(request, 'familytree/familymember.html', {'error': 'Membro não encontrado.'})


def search_family_member(request):
    search_value = request.GET.get('search', '').strip()

    family_members = FamilyMember.objects.annotate(
        name_unaccent=Unaccent(Lower('name')),
        info_unaccent=Unaccent(Lower('info')),
        id_unaccent=Unaccent('id')
    ).filter(
        Q(id_unaccent__icontains=Unaccent(Value(search_value))) |
        Q(name_unaccent__icontains=Unaccent(Value(search_value))) |
        Q(info_unaccent__icontains=Unaccent(Value(search_value)))
    ).prefetch_related(
        Prefetch('children', queryset=Relationship.objects.select_related('child'))
    ).distinct()

    return render(
        request,
        'familytree/index.html',
        {
            'family_members': family_members,
            'search_value': search_value,
        }
    )

