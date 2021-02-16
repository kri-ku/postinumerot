import http_pyynto
import re


def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat


def sisaltaako_sana_valeja(sana):
    # käytetään toimipaikan postinumeroiden hakemisessa
    sanalista = sana.split()
    if len(sanalista) > 1:
        return True

    return False


def tarkasta_anagrammit(eka, toka):
    # käytetään toimipaikan postinumeroiden hakemisessa
    # tarkastetaan sisältävätkö sanat samat kirjaimet

    eka_lista = sorted(eka)
    toka_lista = sorted(toka)
    e_string = "".join(eka_lista)
    t_string = "".join(toka_lista)

    if e_string == t_string:
        return True

    return False


def etsi_toimipaikan_postinumerot(etsittava, lista_toimipaikoittain):
    kaikki_postinumerot = []
    etsittava_ilman_valeja = etsittava
    tmp_ilman_valeja = ""

    for tmp in lista_toimipaikoittain:
        tmp_ilman_valeja = tmp

        if tmp == etsittava:
            kaikki_postinumerot.extend(lista_toimipaikoittain[tmp])
        elif sisaltaako_sana_valeja(etsittava):  # jos hakusanassa välejä
            etsittava_ilman_valeja = etsittava.replace(" ", "").strip()
            if etsittava_ilman_valeja == tmp:
                kaikki_postinumerot.extend(lista_toimipaikoittain[tmp])
            elif tarkasta_anagrammit(etsittava_ilman_valeja, tmp):
                kaikki_postinumerot.extend(lista_toimipaikoittain[tmp])

        # jos listalla olevassa sanassa väleja
        elif sisaltaako_sana_valeja(tmp):
            tmp_ilman_valeja = tmp.replace(" ", "").strip()
            if etsittava == tmp_ilman_valeja:
                kaikki_postinumerot.extend(lista_toimipaikoittain[tmp])
            elif tarkasta_anagrammit(tmp_ilman_valeja, etsittava):
                kaikki_postinumerot.extend(lista_toimipaikoittain[tmp])

        elif tarkasta_anagrammit(etsittava, tmp):
            kaikki_postinumerot.extend(lista_toimipaikoittain[tmp])

    return kaikki_postinumerot


def etsi_ja_tulosta_toimipaikan_postinumerot(toimipaikka, lista_toimipaikoittain):
    loytyiko = etsi_toimipaikan_postinumerot(
        toimipaikka, lista_toimipaikoittain)
    if loytyiko:
        loydetyt_str = ', '.join(loytyiko)
        # print(
        #   f'LISTAN PITUUS: {len(loytyiko)}')
        print(loydetyt_str)
    else:
        print('Toimipaikkaa ei löytynyt')


def kysy_etsittava_toimipaikka():
    toimipaikka = input('Kirjoita postitoimipaikka: ').strip().upper()
    return toimipaikka


def main():
    postinumerot_avaimina = http_pyynto.hae_postinumerot()
    toimipaikat_avaimina = ryhmittele_toimipaikoittain(postinumerot_avaimina)
    toimipaikka = kysy_etsittava_toimipaikka()
    etsi_ja_tulosta_toimipaikan_postinumerot(toimipaikka, toimipaikat_avaimina)


if __name__ == '__main__':
    main()
