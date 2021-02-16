import postinumerot

TOIMIPAIKAT = {
    "74701": "SMARTPOST",
    "35540": "SMART POST",
    "74700": "SMARTPSOT",
    "73460": "SMARTPSOT",
    "00980": "SMARTPOST",
    "88879": "SMART POST",
    "88888": "SMART POST"
}

kaannetty_lista = postinumerot.ryhmittele_toimipaikoittain(TOIMIPAIKAT)


def test_SMARTPOST_hakusanana_palauttaa_oikean_maaran_postinumeroita():
    lista_postinro = postinumerot.etsi_toimipaikan_postinumerot(
        "SMARTPOST", kaannetty_lista)
    assert len(lista_postinro) == len(TOIMIPAIKAT)


def test_SMART_POST_hakusanana_palauttaa_oikean_maaran_postinumeroita():
    lista_postinro = postinumerot.etsi_toimipaikan_postinumerot(
        "SMART POST", kaannetty_lista)
    assert len(lista_postinro) == len(TOIMIPAIKAT)


def test_SMARTPSOT_hakusanana_palauttaa_oikean_maaran_postinumeroita():
    lista_postinro = postinumerot.etsi_toimipaikan_postinumerot(
        "SMARTPSOT", kaannetty_lista)
    assert len(lista_postinro) == len(TOIMIPAIKAT)


def test_SMARTPOST_JA_SMART_POST_hakusananat_palauttavat_saman_maaran_postinumeroita():
    lista_smartpost = postinumerot.etsi_toimipaikan_postinumerot(
        "SMARTPOST", kaannetty_lista)
    lista_smart_post = postinumerot.etsi_toimipaikan_postinumerot(
        "SMART POST", kaannetty_lista)
    assert len(lista_smartpost) == len(lista_smart_post)
