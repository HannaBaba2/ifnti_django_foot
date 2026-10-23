import pytest
#from tournoi.models import Match
from tournoi.models import Equipe

   
@pytest.fixture
def equipe1(db):
    return Equipe.objects.create(nom="Equipe A", promo="L1")

@pytest.fixture
def equipe2(db):
    return Equipe.objects.create(nom="Equipe B", promo="L2")

def test_equipe_un_nom_promo(equipe1):
    assert equipe1.nom
    assert equipe1.promo 
