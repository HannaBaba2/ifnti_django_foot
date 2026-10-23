import pytest
from tournoi.models import Match
from tournoi.models import Equipe

   
@pytest.fixture
def equipe1(db):
    return Equipe.objects.create(nom="Equipe A", promo="L1")

@pytest.fixture
def equipe2(db):
    return Equipe.objects.create(nom="Equipe B", promo="L2")


@pytest.fixture
def match_non_joue(db,equipe1,equipe2):
    return Match.objects.create(equipe_visiteuse=equipe2, equipe_domicile=equipe1,date="2020-01-01", status="EN_ATTENTE")
@pytest.fixture
def match_joue(db,equipe1,equipe2):
    return Match.objects.create(equipe_visiteuse=equipe2, equipe_domicile=equipe1,date="2020-01-01", status="JOUE")


@pytest.fixture
def match(db,equipe1,equipe2):
    return Match.objects.create(equipe_visiteuse=equipe2, equipe_domicile=equipe1,date="2020-01-01")

def test_equipe_un_nom_promo(equipe1):
    assert equipe1.nom
    assert equipe1.promo 
    
def test_pas_equipe_avec_meme_nom( equipe1):
    with pytest.raises(Exception):
        Equipe.objects.create(nom="Equipe A", promo="L2")
        
def test_afficher_equipe(equipe1):
    assert str(equipe1) == "Equipe A"   
    
    
def test_match_equipe_visiteuse_domicile(match):
 
    assert match.equipe_visiteuse == equipe2
    assert match.equipe_domicile == equipe1
    assert match.date

def test_score_match_non_joue(match_non_joue):
    assert match_non_joue.score is None
    

def test_afficher_match_non_joue(match_non_joue):
    assert str(match_non_joue) == "Equipe A - Equipe B : à jouer" 
    
def test_afficher_match_joue(match_joue):
    assert str(match_joue) == "Equipe A : 3-1"
    
    
    
    