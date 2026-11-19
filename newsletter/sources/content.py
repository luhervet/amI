# -*- coding: utf-8 -*-
"""Contenu partagé par les deux versions de la Lettre des territoires (décembre 2026)."""

IMG = "https://content.mailplus.nl/m20/images/mailing504046367/"
IMG_BANNER = IMG + "cern_logo_test.png"
IMG_EDITO = IMG + "202508_192_00691.jpg"
IMG_CERN = IMG + "cern_logo_seul.png"
IMG_LINKTREE = IMG + "linktree_circle_logo_icon_linktree_app_editable_transparent_background_premium_social_media_design_for_digital_download_free_png.png"
IMG_FCC = IMG + "fcc_circle_main_rgb_white__1_0.png"
IMG_EU = "https://content.mailplus.nl/m20/images/user503105558/drapeau_europe.jpeg?noCache=1752764588000"

URL_LINKTREE = "https://linktr.ee/FCC_study"
URL_CONTACT = "https://www.fcc-faisabilite.eu/contact/"
URL_PRIVACY = "https://home.cern/fr/data-privacy-protection-policy"
URL_FCC = "https://www.fcc-faisabilite.eu/"

NUMERO = "DÉCEMBRE 2026"
PREHEADER = "La participation en chiffres, les prochaines étapes et l’actualité de l’étude FCC"

EU_TEXT = ("Le présent projet a bénéficié d’un financement au titre du programme-cadre de "
           "l’Union européenne pour la recherche et l’innovation « Horizon 2020 » dans le "
           "cadre de la convention de subvention n° 9517545.")

# Surligné jaune = point à vérifier avant envoi
def hl(s):
    return f'<span style="background-color:#fff3a3;">{s}</span>'

EDITO = [
    "Chers lecteurs,",
    "Ces quatre derniers mois ont été marqués par de nombreux échanges autour du projet FCC, dans le cadre du débat public organisé en France sous l’égide de la Commission nationale du débat public (CNDP) et de la concertation conduite en Suisse, en coordination avec le Canton de Genève. Ces deux démarches, qui ont permis de multiplier les occasions de dialogue, de rencontre et d’expression, viennent désormais de s’achever formellement. Elles ont constitué des temps particulièrement riches et constructifs, auxquels élus, associations, habitants, acteurs économiques et membres de la communauté scientifique ont largement contribué. Le CERN tient à vous remercier sincèrement pour votre participation, vos questions, vos propositions et l’attention portée au projet.",
    "La clôture de ces dispositifs marque également le moment de reprendre notre rendez-vous régulier avec vous à travers cette Lettre des territoires. C’est l’occasion de revenir sur les principaux temps forts de cette séquence, mais aussi de partager les premières observations qui en ressortent et les prochaines étapes du projet.",
    "Au-delà des échanges directs, des observations et des interpellations recueillies au fil des rencontres, les bilans formels du débat public en France et de la concertation en Suisse ont désormais été publiés, à compter du 1<sup style='font-size:70%;line-height:0;vertical-align:super;'>er</sup> décembre. Le bilan du débat public français " + hl("fera (ou à fait)") + " également l’objet d’un webinaire dans les jours qui suivent sa publication. Ces documents viennent compléter les nombreux échanges qui ont jalonné cette période et constituent des éléments importants pour la suite.",
    "Le CERN engage à présent un travail d’analyse et de réflexion approfondi sur l’ensemble de ces contributions, tant sur le fond que sur la manière dont le projet et le dialogue avec les territoires peuvent continuer à évoluer. Cette étape doit permettre de formuler une réponse à ces démarches de participation, accompagnée d’engagements précis et concrets, qui seront rendus publics au plus tard en mars 2027.",
    "Ce jalon ouvrira ensuite une nouvelle étape, celle de la concertation continue, qui accompagnera le projet dans la durée. La première phase de cette démarche s’inscrira notamment dans la perspective de la décision des États membres de l’Organisation, attendue au cours du second semestre 2028. Le dialogue avec les territoires continuera ainsi à accompagner les différentes étapes de développement du projet.",
    "Vous trouverez dans cette lettre un retour sur les temps forts de ces derniers mois, sur les démarches de participation qui viennent de s’achever, ainsi que sur les actualités et les prochaines étapes du projet FCC.",
    "Fidèle à sa volonté de transparence et de dialogue, le CERN continuera à vous tenir informés de l’avancée du projet et des échanges avec les territoires. D’ici là, toute l’équipe FCC se joint à moi pour vous souhaiter de belles fêtes de fin d’année.",
]
EDITO_SIGN = ("Michael Benedikt", "Chef de l’étude FCC")
EDITO_CLOSING = "Bien cordialement,"

LOREM = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante venenatis dapibus, posuere velit aliquet. Cras mattis consectetur purus sit amet fermentum. Donec ullamcorper nulla non metus auctor fringilla, vestibulum id ligula porta felis euismod semper.",
    "Maecenas sed diam eget risus varius blandit sit amet non magna. Nullam quis risus eget urna mollis ornare vel eu leo. Aenean lacinia bibendum nulla sed consectetur. Etiam porta sem malesuada magna mollis euismod.",
    "Curabitur blandit tempus porttitor. Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Praesent commodo cursus magna, vel scelerisque nisl consectetur et.",
]
LOREM_SHORT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante venenatis dapibus, posuere velit aliquet. Donec ullamcorper nulla non metus auctor fringilla."

# Chiffres de participation : XX = à compléter
CHIFFRES = [
    ("questions et avis en ligne", "XX", "XX"),
    ("cahiers d’acteurs", "XX", "XX"),
    ("réunions publiques", "XX", "XX"),
    ("débats mobiles", "XX", "XX"),
]

FOCUS = [
    ("Le Groupe citoyen jeune", "<em>Dispositif mis en place par " + hl("[organisateur]") + ".</em> " + LOREM[0]),
    ("L’Atelier de la relève", "<em>Dispositif mis en place par " + hl("[organisateur]") + ".</em> " + LOREM[1]),
]

SUP_ER = "1<sup style='font-size:70%;line-height:0;vertical-align:super;text-transform:none;'>er</sup>"

SOURCES_CHIFFRES = ("Sources : CNDP – Commission particulière du débat public ; " + hl("[organisateur de la concertation suisse]")
                    + ". Chiffres arrêtés au " + hl("XX") + ".")

# Calendrier (déduit de l'édito) : (date, texte, réalisé ?)
JALONS = [
    (hl("XX 2026"), "Clôture du débat public en France et de la concertation en Suisse", True),
    (SUP_ER + " décembre 2026", "Publication par la CNDP du compte rendu et du bilan du débat public, et du rapport de la concertation suisse", True),
    (hl("XX décembre 2026"), "Webinaire de présentation du compte rendu et du bilan du débat public", False),
    ("Au plus tard en mars 2027", "Publication de la réponse du CERN : décision sur les suites données au débat public et à la concertation, et engagements", False),
    ("À partir de 2027", "Concertation continue avec les territoires", False),
    ("Second semestre 2028", "Décision des États membres du CERN sur l’avenir du projet (attendue)", False),
]

# Liens vers les documents publiés (à compléter)
DOCS = [
    ("Compte rendu et bilan du débat public (CNDP)", "#"),
    ("Rapport de la concertation suisse", "#"),
    ("Webinaire : inscription / replay", "#"),
]

ACTUS = [
    ("gouvernance", "Une nouvelle gouvernance territoriale", "Des groupes de travail avec les élus, de part et d’autre de la frontière"),
    ("evenements", "L’équipe FCC aux rendez-vous du territoire", "Retour sur les événements locaux auxquels l’équipe a participé"),
    ("geotechnique", "Campagne de reconnaissance géotechnique", "Point d’étape sur les forages et sondages, des investigations menées dans le cadre de l’étude, qui ne préjugent pas de la décision"),
    ("faisceau", "Essais sous faisceau : de premiers résultats", "De mai à août 2026, des essais ont permis de " + hl("[à compléter]")),
    ("expo", "Exposition « Why? »", hl("[Lieu], jusqu’au [date], entrée libre")),
]

SECTIONS = [
    ("retour", "Débat public en France, concertation en Suisse : retour sur la participation",
     [("chiffres", "La participation en chiffres"),
      ("focus", "Focus : le Groupe citoyen jeune et l’Atelier de la relève")]),
    ("compte-rendu", "Des comptes rendus à la réponse du CERN : les prochaines étapes", []),
    ("actualite", "L’actualité du projet", [(a[0], a[1]) for a in ACTUS]),
]

# Typographie française : espaces insécables dans le texte (hors <head>/<style>)
import re as _re
def fr_typo(html):
    head_end = html.index("</head>")
    head, body = html[:head_end], html[head_end:]
    head = _re.sub(r"(<title>)([^<]*)", lambda m: m.group(1) + _nb(m.group(2)), head)
    body = _re.sub(r">([^<]+)<", lambda m: ">" + _nb(m.group(1)) + "<", body)
    return head + body
def _nb(t):
    t = _re.sub(r" +([:;?!»])", r"&nbsp;\1", t)
    t = _re.sub(r"« +", "«&nbsp;", t)
    t = t.replace("«Why?»", "«&nbsp;Why?&nbsp;»")
    return t

# Bandeau de marque en HTML (remplace l'image cern_logo_test.png pour pouvoir modifier le texte)
BRAND_SUBTITLE = ""  # sous-titre sous le logo FCC (vide = aucun)
def brand_header(pad="22px 40px 16px 40px", cls="px"):
    f = "Helvetica, Arial, sans-serif"
    alt = "font-family:Arial,sans-serif;font-size:12px;color:#ffffff;"
    return f'''<tr><td bgcolor="#155EA9" style="background-color:#155EA9;padding:{pad};" class="{cls}">
<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
<td valign="middle" style="padding:0 14px 0 0;"><img src="{IMG_CERN}" width="64" alt="CERN" style="{alt}display:block;width:64px;height:auto;border:0;"></td>
<td valign="middle" width="1" bgcolor="#ffffff" style="width:1px;background-color:#ffffff;font-size:0;line-height:0;">&nbsp;</td>
<td valign="middle" style="padding:0 12px 0 14px;"><img src="{IMG_FCC}" width="56" alt="FCC" style="{alt}display:block;width:56px;height:auto;border:0;"></td>
<td valign="middle" style="font-family:{f};color:#ffffff;">
<p style="margin:0;mso-line-height-rule:exactly;font-family:{f};font-size:15px;line-height:17px;color:#ffffff;letter-spacing:.5px;">FUTUR<br>COLLISIONNEUR<br>CIRCULAIRE</p>
{f'<p style="margin:3px 0 0 0;mso-line-height-rule:exactly;font-family:{f};font-size:13px;line-height:16px;color:#ffffff;font-style:italic;font-weight:bold;">{BRAND_SUBTITLE}</p>' if BRAND_SUBTITLE else ""}
</td></tr></table>
</td></tr>'''
