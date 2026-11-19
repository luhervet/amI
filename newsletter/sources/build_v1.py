# -*- coding: utf-8 -*-
"""V1 : même design que la Lettre des territoires d'avril 2026."""
import sys
from content import *

BLUE = "#155EA9"
LINK = "#0000EE"
FONT = "Helvetica, Arial, sans-serif"

def sep(px=2, pad="10px"):
    return f'''<tr><td style="padding:{pad};"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="font-size:0;line-height:0;border-bottom:{px}px solid {BLUE};">&nbsp;</td></tr></table></td></tr>'''

def p(text, align="justify", size=14, lh=17, color="#000000", extra=""):
    return f'<p style="margin:0;mso-line-height-rule:exactly;font-family:{FONT};font-size:{size}px;line-height:{lh}px;color:{color};text-align:{align};{extra}">{text}</p>'

def gap():
    return f'<p style="margin:0;font-size:14px;line-height:17px;">&nbsp;</p>'

def paras(lst):
    return gap().join(p(x) for x in lst)

def h3(text, anchor=None):
    a = f'<a name="{anchor}" id="{anchor}"></a>' if anchor else ""
    return f'''<tr><td style="padding:10px;"><h3 class="h3" style="margin:0;mso-line-height-rule:exactly;font-family:{FONT};font-size:28px;line-height:34px;color:#000000;font-weight:bold;">{a}{text}</h3></td></tr>'''

def h4(text, anchor=None):
    a = f'<a name="{anchor}" id="{anchor}"></a>' if anchor else ""
    return f'''<tr><td style="padding:10px;"><h4 style="margin:0;mso-line-height-rule:exactly;font-family:{FONT};font-size:20px;line-height:24px;color:#000000;font-weight:normal;">{a}{text}</h4></td></tr>'''

def text_row(html, pad="10px"):
    return f'<tr><td style="padding:{pad};">{html}</td></tr>'

def image_ph(label, h=300, caption=None):
    cap = f'<tr><td style="padding:10px;"><p style="margin:0;font-family:{FONT};font-size:12px;line-height:15px;color:#000000;"><em>{caption}</em></p></td></tr>' if caption else ""
    return f'''<tr><td align="center"><table role="presentation" width="600" class="full" cellpadding="0" cellspacing="0" border="0"><tr><td height="{h}" align="center" valign="middle" bgcolor="#E8EEF6" style="height:{h}px;background-color:#E8EEF6;border-radius:3px;font-family:{FONT};font-size:14px;color:{BLUE};">[ {label} – 600 × {h} px ]</td></tr></table></td></tr>{cap}'''

def sommaire():
    items = []
    for sid, title, subs in SECTIONS:
        sub = ""
        if subs:
            sub = '<ul style="margin:4px 0 0 0;padding-left:20px;">' + "".join(
                f'<li style="margin:0 0 2px 0;"><a href="#{a}" style="color:{LINK};text-decoration:underline;">{t}</a></li>' for a, t in subs) + "</ul>"
        items.append(f'<li style="margin:0 0 4px 0;"><a href="#{sid}" style="color:{LINK};text-decoration:underline;">{title}</a>{sub}</li>')
    return f'<ul style="margin:0;padding-left:40px;font-family:{FONT};font-size:14px;line-height:17px;color:#000000;">{"".join(items)}</ul>'

def two_cols(left, right, lw=300, rw=300):
    return f'''<tr><td><table role="presentation" width="600" class="full" cellpadding="0" cellspacing="0" border="0"><tr>
<td class="stack" width="{lw}" valign="top" style="width:{lw}px;">{left}</td>
<td class="stack" width="{rw}" valign="top" style="width:{rw}px;">{right}</td>
</tr></table></td></tr>'''

def h6(text):
    return f'<h6 style="margin:0;mso-line-height-rule:exactly;font-family:{FONT};font-size:16px;line-height:19px;color:{BLUE};font-weight:bold;">{text}</h6>'

def chiffres_col(country, idx):
    rows = "".join(
        f'<tr><td style="padding:4px 0;font-family:{FONT};font-size:14px;line-height:17px;color:#000000;"><strong style="color:{BLUE};font-size:18px;">{c[idx]}</strong>&nbsp; {c[0]}</td></tr>'
        for c in CHIFFRES)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:10px;">{h6(country)}<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:8px;">{rows}</table></td></tr></table>'

def block(inner_rows):
    return f'<tr><td><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{inner_rows}</table></td></tr>'

def edito():
    body = gap().join(p(x) for x in EDITO)
    body += gap() + p(EDITO_CLOSING) + gap() + p(f'<strong>{EDITO_SIGN[0]}</strong><br>{EDITO_SIGN[1]}')
    btn = f'''<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:14px;"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{BLUE}" align="center" style="background-color:{BLUE};border-radius:16px;padding:10px 20px;font-family:{FONT};font-size:20px;line-height:24px;color:#ffffff;">ÉDITO</td></tr></table></td></tr></table>'''
    txt = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td class="edito-txt" style="padding:10px 10px 10px 30px;">{body}</td></tr></table>'
    return (f'<tr><td align="center" style="padding-top:12px;"><img src="{IMG_EDITO}" width="600" class="full" alt="Michael Benedikt, chef de l’étude FCC" style="display:block;width:600px;max-width:100%;height:auto;border:0;"></td></tr>'
            + two_cols(btn, txt, 220, 380))

def jalons():
    rows = "".join(
        f'<tr><td width="170" valign="top" style="padding:6px 10px 6px 0;font-family:{FONT};font-size:14px;line-height:17px;color:{BLUE};font-weight:bold;border-bottom:1px solid #DCE4EF;">{d}</td>'
        f'<td valign="top" style="padding:6px 0;font-family:{FONT};font-size:14px;line-height:17px;color:#000000;border-bottom:1px solid #DCE4EF;">{t}</td></tr>'
        for d, t, done in JALONS)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>'

def docs_links():
    btns = "".join(f'<tr><td style="padding:0 0 10px 0;"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{BLUE}" style="background-color:{BLUE};border-radius:16px;padding:8px 18px;"><a href="{u}" target="_blank" style="font-family:{FONT};font-size:14px;line-height:18px;color:#ffffff;text-decoration:none;display:block;">{t}&nbsp;&rarr;</a></td></tr></table></td></tr>' for t, u in DOCS)
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0">{btns}</table>'

def build():
    rows = []
    # En-tête
    rows.append(f'''<tr><td align="center" style="padding:10px;font-family:{FONT};font-size:14px;line-height:17px;color:#000000;">
<!-- Remplacer les href par les liens Spotler (désinscription / version web) -->
<a href="#" style="color:{LINK};text-decoration:underline;">Désinscription</a> |&nbsp;<a href="#" style="color:{LINK};text-decoration:underline;">Version web</a></td></tr>''')
    rows.append(brand_header("20px 30px 10px 30px", "brand"))
    rows.append(f'<tr><td bgcolor="{BLUE}" style="background-color:{BLUE};padding:10px 10px 0 10px;"><h1 class="h1" style="margin:0;font-family:{FONT};font-size:40px;line-height:48px;color:#f6f6f6;font-weight:normal;">L’actualité de l’étude FCC</h1></td></tr>')
    rows.append(sep())
    rows.append(f'<tr><td bgcolor="{BLUE}" style="background-color:{BLUE};padding:15px;font-family:{FONT};font-size:14px;line-height:17px;color:#fcfcfc;">LETTRE DES TERRITOIRES<br>{NUMERO}</td></tr>')
    # Sommaire
    rows.append(h3("<strong>Sommaire</strong>"))
    rows.append(text_row(sommaire()))
    rows.append(sep())
    # Édito
    rows.append(edito())
    # Section 1
    rows.append(sep(9, "30px 10px"))
    rows.append(h3(SECTIONS[0][1], "retour"))
    rows.append(image_ph("Photo réunion publique / débat mobile", 300, "Légende de la photo – lorem ipsum dolor sit amet."))
    rows.append(text_row(p(LOREM[0])))
    rows.append(h4("La participation en chiffres", "chiffres"))
    rows.append(two_cols(chiffres_col("En France – débat public", 1), chiffres_col("En Suisse – concertation", 2)))
    rows.append(text_row(p(SOURCES_CHIFFRES, size=12, lh=16, extra="font-style:italic;")))
    rows.append(h4("Focus : le Groupe citoyen jeune et l’Atelier de la relève", "focus"))
    rows.append(text_row(p(LOREM[2])))
    focus_cols = [f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:10px;">{h6(t)}<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td height="8" style="height:8px;font-size:0;line-height:0;">&nbsp;</td></tr></table>{p(x)}</td></tr></table>' for t, x in FOCUS]
    rows.append(two_cols(*focus_cols))
    # Section 2
    rows.append(sep(9, "30px 10px"))
    rows.append(h3(SECTIONS[1][1], "compte-rendu"))
    rows.append(text_row(paras(LOREM[:2])))
    rows.append(h4("Le calendrier"))
    rows.append(text_row(jalons()))
    rows.append(text_row(docs_links()))
    # Section 3
    rows.append(sep(9, "30px 10px"))
    rows.append(h3("L’actualité du projet", "actualite"))
    for i, (aid, title, chapo) in enumerate(ACTUS):
        if i:
            rows.append(sep(2))
        rows.append(h4(title, aid))
        rows.append(image_ph(f"Photo – {title}", 250))
        rows.append(text_row(p(f"<strong>{chapo}.</strong> " + LOREM[i % 3]) + gap() + p(LOREM[(i + 1) % 3])))
    rows.append(f'<tr><td height="30" style="height:30px;font-size:0;line-height:0;">&nbsp;</td></tr>')
    # Pied de page
    col_cern = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="padding:28px 16px 16px 16px;"><img src="{IMG_CERN}" width="168" alt="CERN" style="font-family:Arial,sans-serif;font-size:14px;color:#ffffff;display:block;width:168px;max-width:100%;height:auto;border:0;"></td></tr></table>'
    col_mid = f'''<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
<tr><td height="25" style="height:25px;font-size:0;line-height:0;">&nbsp;</td></tr>
<tr><td align="center" style="padding:8px;font-family:{FONT};font-size:14px;line-height:17px;color:#ffffff;"><strong>Nous suivre</strong></td></tr>
<tr><td align="center"><a href="{URL_LINKTREE}" target="_blank"><img src="{IMG_LINKTREE}" width="60" alt="Nos réseaux (Linktree)" style="font-family:Arial,sans-serif;font-size:14px;color:#ffffff;display:inline-block;width:60px;height:auto;border:0;"></a></td></tr>
<tr><td align="center" style="padding:8px;font-family:{FONT};font-size:14px;line-height:17px;color:#ffffff;"><strong>Nous contacter</strong></td></tr>
<tr><td align="center" style="padding:5px;"><table role="presentation" width="66%" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="#ffffff" align="center" style="background-color:#ffffff;border-radius:16px;padding:10px 20px;"><a href="{URL_CONTACT}" target="_blank" style="font-family:Arial, Helvetica, sans-serif;font-size:15px;line-height:18px;color:#009FE3;text-decoration:none;display:block;"><strong>cliquez ici</strong></a></td></tr></table></td></tr>
</table>'''
    col_fcc = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="padding:51px 8px 8px 8px;"><img src="{IMG_FCC}" width="134" alt="FCC – logo" style="font-family:Arial,sans-serif;font-size:14px;color:#ffffff;display:block;width:134px;max-width:100%;height:auto;border:0;"></td></tr></table>'
    rows.append(f'''<tr><td bgcolor="{BLUE}" style="background-color:{BLUE};"><table role="presentation" width="600" class="full" cellpadding="0" cellspacing="0" border="0"><tr>
<td class="stack" width="200" valign="top" style="width:200px;">{col_cern}</td>
<td class="stack" width="200" valign="top" style="width:200px;">{col_mid}</td>
<td class="stack" width="200" valign="top" style="width:200px;">{col_fcc}</td>
</tr>
<tr><td colspan="3" style="padding:20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="font-size:0;line-height:0;border-bottom:2px solid #ffffff;">&nbsp;</td></tr></table></td></tr>
</table></td></tr>''')
    rows.append(f'<tr><td align="center" style="padding:10px;font-family:{FONT};font-size:14px;line-height:17px;"><a href="{URL_PRIVACY}" target="_blank" style="color:{LINK};text-decoration:underline;">Informations sur la protection des données</a></td></tr>')
    eu_l = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="padding:15px 0 10px 41px;" class="eu-img"><img src="{IMG_EU}" width="109" alt="Drapeau de l’Union européenne" style="display:block;width:109px;height:auto;border:0;"></td></tr></table>'
    eu_r = f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:12px 10px 10px 10px;">{p(EU_TEXT, lh=20)}</td></tr></table>'
    rows.append(two_cols(eu_l, eu_r, 150, 450))

    return fr_typo(TEMPLATE.replace("{{ROWS}}", "\n".join(rows)))

TEMPLATE = f'''<!DOCTYPE html>
<html lang="fr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>Lettre des territoires – {NUMERO.capitalize()}</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
  body {{ margin:0; padding:0; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; }}
  table {{ border-collapse:collapse; mso-table-lspace:0; mso-table-rspace:0; }}
  img {{ border:0; outline:none; text-decoration:none; -ms-interpolation-mode:bicubic; }}
  a[x-apple-data-detectors] {{ color:inherit !important; text-decoration:none !important; }}
  h1,h2,h3,h4,h5,h6,p {{ margin:0; }}
  @media only screen and (max-width:600px) {{
    .container, .full {{ width:100% !important; }}
    .stack {{ display:block !important; width:100% !important; }}
    .h1 {{ font-size:32px !important; line-height:38px !important; }}
    .h3 {{ font-size:24px !important; line-height:29px !important; }}
    .edito-txt {{ padding:10px !important; }}
    .eu-img {{ padding:15px 0 0 0 !important; }}
    .brand {{ padding:16px 10px 8px 10px !important; }}
    p {{ text-align:left !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background-color:#ffffff;">
<!-- Pré-en-tête (texte d'aperçu dans la boîte de réception) -->
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">{PREHEADER}{"&nbsp;&zwnj;" * 90}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="background-color:#ffffff;">
<tr><td align="center">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">
{{{{ROWS}}}}
</table>
<!--[if mso]></td></tr></table><![endif]-->
</td></tr>
</table>
</body>
</html>
'''

if __name__ == "__main__":
    open(sys.argv[1], "w", encoding="utf-8").write(build())
