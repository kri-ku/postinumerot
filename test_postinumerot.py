import postinumerot

TOIMIPAIKAT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

kaannetty_lista = postinumerot.ryhmittele_toimipaikoittain(TOIMIPAIKAT)


def test_toimipaikka_loytyy_avaimena_kun_avaimet_ja_arvot_kaanetty():
    assert "KIURUVESI" in kaannetty_lista.keys()


def test_toimipaikka_palauttaa_kaksi_arvoa():
    palautusarvot = postinumerot.etsi_toimipaikan_postinumerot(
        "KIURUVESI", kaannetty_lista)
    assert len(palautusarvot) == 2


def test_toimipaikka_palauttaa_yhden_arvon():
    palautusarvot = postinumerot.etsi_toimipaikan_postinumerot(
        "MUURUVESI", kaannetty_lista)
    assert len(palautusarvot) == 1


def test_jos_toimipaikkaa_ei_ole_palautetaan_tyhja_lista():
    palautusarvot = postinumerot.etsi_toimipaikan_postinumerot(
        "KLAUKKALA", kaannetty_lista)
    assert not len(palautusarvot)
