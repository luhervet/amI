# -*- coding: utf-8 -*-
"""V2 : proposition modernisée, même charte (bleu CERN #155EA9, accent #009FE3)."""
import sys
from content import *

BLUE = "#155EA9"
ACCENT = "#009FE3"      # décoratif uniquement (contraste insuffisant pour du texte)
ACCENT_TXT = "#0072BC"  # bleu clair accessible pour le texte
DARK = "#0E3D6E"
INK = "#1F2933"
GREY = "#5B6B7C"
LIGHT = "#F2F6FB"
LINE = "#D9E3EF"
F = "Helvetica, Arial, sans-serif"
FH = F
LIGHT_ATTRS = f'bgcolor="{LIGHT}" style="background-color:{LIGHT};border-radius:8px;"'

def T(inner, width="100%", attrs=""):
    w = f' width="{width}"' if width else ""
    return f'<table role="presentation"{w} cellpadding="0" cellspacing="0" border="0" {attrs}>{inner}</table>'

def spacer(h):
    return f'<tr><td height="{h}" style="height:{h}px;font-size:0;line-height:0;">&nbsp;</td></tr>'

def p(text, size=15, lh=24, color=INK, extra=""):
    return f'<p style="margin:0 0 14px 0;mso-line-height-rule:exactly;font-family:{F};font-size:{size}px;line-height:{lh}px;color:{color};{extra}">{text}</p>'

def eyebrow(text, color=ACCENT_TXT):
    return f'<p style="margin:0 0 6px 0;font-family:{F};font-size:12px;line-height:16px;letter-spacing:1.5px;font-weight:bold;color:{color};text-transform:uppercase;">{text}</p>'

def h2(text, anchor):
    return f'<h2 class="h2" style="margin:0;font-family:{FH};font-size:26px;line-height:32px;font-weight:700;color:{BLUE};"><a name="{anchor}" id="{anchor}"></a>{text}</h2>'

def h3(text, anchor=None, size=19, color=INK):
    a = f'<a name="{anchor}" id="{anchor}"></a>' if anchor else ""
    return f'<h3 style="margin:0 0 8px 0;font-family:{FH};font-size:{size}px;line-height:{size+6}px;font-weight:700;color:{color};">{a}{text}</h3>'

def placeholder(label, w, h, radius=6):
    return T(f'<tr><td height="{h}" align="center" valign="middle" bgcolor="#DCE7F3" style="height:{h}px;background-color:#DCE7F3;border-radius:{radius}px;font-family:{F};font-size:13px;line-height:18px;color:{BLUE};">[ {label}<br>{w} × {h} px ]</td></tr>', width=str(w), attrs='class="full"')

def more(text="Lire la suite", href="#"):
    return f'<a href="{href}" style="font-family:{F};font-size:14px;line-height:20px;font-weight:bold;color:{BLUE};text-decoration:none;">{text}&nbsp;&rarr;</a>'

def button(text, href, bg=BLUE, fg="#ffffff", nowrap=True):
    nw = "white-space:nowrap;" if nowrap else ""
    return T(f'<tr><td bgcolor="{bg}" align="center" style="background-color:{bg};border-radius:22px;padding:10px 18px;{nw}"><a href="{href}" target="_blank" style="font-family:{F};font-size:14px;line-height:20px;font-weight:bold;color:{fg};text-decoration:none;display:inline-block;{nw}">{text}</a></td></tr>', width="")

def section(num, label, title, anchor, body_rows):
    head = f'''<tr><td style="padding:0 40px;" class="px">{T(f'<tr><td style="border-top:3px solid {BLUE};font-size:0;line-height:0;" width="48">&nbsp;</td><td style="font-size:0;line-height:0;">&nbsp;</td></tr>')}</td></tr>
{spacer(18)}
<tr><td style="padding:0 40px;" class="px">{eyebrow(f"{num} — {label}")}{h2(title, anchor)}</td></tr>
{spacer(20)}'''
    return head + body_rows + spacer(44)

# ---------- Blocs ----------

def header():
    return f'''<tr><td align="center" style="padding:10px 20px;font-family:{F};font-size:12px;line-height:16px;color:{GREY};">
<!-- Remplacer les href par les liens Spotler (désinscription / version web) -->
<a href="#" style="color:{GREY};text-decoration:underline;">Version web</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="#" style="color:{GREY};text-decoration:underline;">Désinscription</a></td></tr>
{brand_header()}
<tr><td bgcolor="{BLUE}" style="background-color:{BLUE};padding:6px 40px 30px 40px;" class="px">
<p style="margin:0 0 10px 0;font-family:{F};font-size:12px;line-height:16px;letter-spacing:2px;font-weight:bold;color:#BFE3F7;">LETTRE DES TERRITOIRES&nbsp;&nbsp;·&nbsp;&nbsp;{NUMERO}</p>
<h1 class="h1" style="margin:0;font-family:{FH};font-size:36px;line-height:42px;font-weight:700;color:#ffffff;">L’actualité de l’étude FCC</h1>
<p style="margin:12px 0 0 0;font-family:{F};font-size:16px;line-height:24px;color:#E3F1FB;">Débat public en France, concertation en Suisse : retour sur la participation et prochaines étapes</p>
</td></tr>
<tr><td bgcolor="{ACCENT}" height="5" style="background-color:{ACCENT};height:5px;font-size:0;line-height:0;">&nbsp;</td></tr>
{spacer(32)}'''

def sommaire():
    rows = ""
    entries = [("", "edito", "Édito de Michael Benedikt, chef de l’étude FCC", [])] + [
        (f"0{i+1}", sid, title, subs) for i, (sid, title, subs) in enumerate(SECTIONS)]
    for n, sid, title, subs in entries:
        num = n or "00"
        sub = "".join(f'<br><a href="#{a}" style="font-family:{F};font-size:13px;line-height:20px;color:{GREY};text-decoration:none;">–&nbsp;{t}</a>' for a, t in subs)
        rows += f'''<tr><td width="44" valign="top" style="padding:10px 0;border-bottom:1px solid {LINE};font-family:{FH};font-size:20px;line-height:22px;font-weight:700;color:{ACCENT_TXT};">{num}</td>
<td valign="top" style="padding:10px 0;border-bottom:1px solid {LINE};"><a href="#{sid}" style="font-family:{F};font-size:15px;line-height:22px;font-weight:bold;color:{INK};text-decoration:none;">{title}</a>{sub}</td></tr>'''
    inner = f'<tr><td style="padding:24px 28px 14px 28px;">{eyebrow("Au sommaire", BLUE)}{T(rows)}</td></tr>'
    return f'<tr><td style="padding:0 40px;" class="px">{T(inner, attrs=LIGHT_ATTRS)}</td></tr>{spacer(44)}'

def edito():
    quote = "Le CERN tient à vous remercier sincèrement pour votre participation, vos questions, vos propositions et l’attention portée au projet."
    top = f'''<tr><td style="padding:0 40px;" class="px"><img src="{IMG_EDITO}" width="520" class="full" alt="Michael Benedikt, chef de l’étude FCC" style="display:block;width:520px;max-width:100%;height:auto;border:0;border-radius:8px;"></td></tr>{spacer(20)}
<tr><td style="padding:0 40px;" class="px">{T(f"""<tr>
<td valign="top">
<a name="edito" id="edito"></a>
<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr><td bgcolor="{BLUE}" style="background-color:{BLUE};border-radius:14px;padding:5px 14px;font-family:{F};font-size:13px;line-height:16px;font-weight:bold;letter-spacing:1px;color:#ffffff;">ÉDITO</td></tr></table>
<p style="margin:14px 0 0 0;font-family:{FH};font-size:20px;line-height:28px;font-style:italic;font-weight:600;color:{BLUE};">« {quote} »</p>
</td></tr>""")}</td></tr>{spacer(20)}'''
    body = "".join(p(x) for x in EDITO)
    sign = f'''{T(f'<tr><td style="border-left:3px solid {ACCENT};padding:2px 0 2px 14px;font-family:{F};font-size:15px;line-height:22px;color:{INK};"><strong>{EDITO_SIGN[0]}</strong><br><span style="color:{GREY};">{EDITO_SIGN[1]}</span></td></tr>', width="")}'''
    return top + f'<tr><td style="padding:0 40px;" class="px">{body}{p(EDITO_CLOSING)}{sign}</td></tr>{spacer(44)}'

def stat_card(country, sub, idx, color):
    cells = ""
    for i in range(0, 4, 2):
        cells += "<tr>" + "".join(
            f'<td width="50%" valign="top" style="padding:12px 10px;"><p style="margin:0;font-family:{FH};font-size:30px;line-height:34px;font-weight:700;color:{color};">{c[idx]}</p><p style="margin:2px 0 0 0;font-family:{F};font-size:13px;line-height:18px;color:{GREY};">{c[0]}</p></td>'
            for c in CHIFFRES[i:i+2]) + "</tr>"
    return T(f'''<tr><td bgcolor="{color}" style="background-color:{color};border-radius:8px 8px 0 0;padding:12px 16px;font-family:{F};font-size:15px;line-height:20px;font-weight:bold;color:#ffffff;">{country}<br><span style="font-weight:normal;font-size:13px;">{sub}</span></td></tr>
<tr><td style="border:1px solid {LINE};border-top:0;border-radius:0 0 8px 8px;padding:6px;">{T(cells)}</td></tr>''')

def two(left, right, gap=20):
    return f'''<tr><td style="padding:0 40px;" class="px">{T(f"""<tr>
<td class="stack pb" width="250" valign="top" style="width:250px;">{left}</td>
<td class="hide" width="{gap}" style="width:{gap}px;font-size:0;line-height:0;">&nbsp;</td>
<td class="stack" width="250" valign="top" style="width:250px;">{right}</td></tr>""")}</td></tr>'''

def card(img_label, title, text, anchor=None, badge=None):
    b = f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" style="margin:0 0 8px 0;"><tr><td bgcolor="#FFF1D6" style="background-color:#FFF1D6;border-radius:10px;padding:3px 10px;font-family:{F};font-size:11px;line-height:14px;font-weight:bold;color:#8A5A00;">{badge}</td></tr></table>' if badge else ""
    return T(f'''<tr><td>{placeholder(img_label, 250, 150)}</td></tr>
<tr><td style="padding:16px 0 0 0;">{b}{h3(title, anchor, 18)}<p style="margin:0 0 10px 0;font-family:{F};font-size:14px;line-height:21px;color:{INK};">{text}</p></td></tr>''')

def body_rows(html):
    return f'<tr><td style="padding:0 40px;" class="px">{html}</td></tr>'

def retour():
    rows = body_rows(p(LOREM[0]))
    rows += body_rows(f'<a name="chiffres" id="chiffres"></a>' + h3("La participation en chiffres", size=19, color=INK)) + spacer(6)
    rows += two(stat_card("En France", "Débat public (CNDP)", 1, BLUE), stat_card("En Suisse", "Concertation", 2, ACCENT_TXT))
    rows += spacer(14) + body_rows(p(SOURCES_CHIFFRES, size=13, lh=20, color=GREY, extra="font-style:italic;"))
    rows += spacer(14) + body_rows(f'<a name="focus" id="focus"></a>' + h3("Focus : le Groupe citoyen jeune et l’Atelier de la relève", size=19) + p(LOREM[2]))
    rows += spacer(6) + two(*[card(f"Photo – {t}", t, x) for t, x in FOCUS])
    return section("01", "Participation", SECTIONS[0][1], "retour", rows)

def process():
    items = ""
    for i, (d, t, done) in enumerate(JALONS):
        dot = BLUE if done else ACCENT
        t = t + f'<br><span style="font-size:12px;line-height:16px;color:{GREY};">{"Réalisé" if done else "À venir"}</span>'
        bb = f"border-bottom:1px solid {LINE};" if i < len(JALONS) - 1 else ""
        items += f'''<tr>
<td class="tl-dot" width="22" valign="top" style="width:22px;padding:13px 0 0 0;{bb}">{T(f'<tr><td width="12" height="12" bgcolor="{dot}" style="width:12px;height:12px;background-color:{dot};border-radius:6px;font-size:0;line-height:0;">&nbsp;</td></tr>', width="12")}</td>
<td class="tl-date" width="170" valign="top" style="width:170px;padding:10px 10px 10px 0;{bb}font-family:{F};font-size:13px;line-height:18px;font-weight:bold;color:{BLUE};text-transform:uppercase;letter-spacing:.5px;">{d}</td>
<td class="stack" valign="top" style="padding:10px 0;{bb}font-family:{F};font-size:15px;line-height:20px;color:{INK};">{t}</td></tr>'''
    rows = body_rows(p(LOREM[0]) + p(LOREM[1]))
    box = f'<tr><td style="padding:22px 24px 12px 24px;">{eyebrow("Le calendrier", BLUE)}{T(items)}</td></tr>'
    rows += spacer(4) + body_rows(T(box, attrs=LIGHT_ATTRS))
    docs = "".join(f'<tr><td style="padding:0 0 10px 0;">{button(t + "&nbsp;&rarr;", u, nowrap=False)}</td></tr>' for t, u in DOCS)
    rows += spacer(24) + body_rows(eyebrow("Les documents", BLUE) + T(spacer(6)) + T(docs, width=""))
    return section("02", "Les suites de la participation", SECTIONS[1][1], "compte-rendu", rows)

def actualite():
    byid = {a[0]: a for a in ACTUS}
    fa = byid["gouvernance"]
    featured = body_rows(placeholder(f"Photo – {fa[1]}", 520, 240) +
        T(spacer(18)) +
        h3(fa[1], fa[0], 22, BLUE) + p(f"<strong>{fa[2]}.</strong> {LOREM[0]}"))
    grid_ids = ["evenements", "geotechnique", "faisceau", "expo"]
    cards = [card(f"Photo – {byid[g][1]}", byid[g][1], f"<strong>{byid[g][2]}.</strong> {LOREM_SHORT}", g) for g in grid_ids]
    rows = featured + spacer(36) + two(cards[0], cards[1]) + spacer(32) + two(cards[2], cards[3])
    return section("03", "Actualités", SECTIONS[2][1], "actualite", rows)

def footer():
    alt = "font-family:Arial,sans-serif;font-size:14px;color:#ffffff;"
    col = lambda inner, w: f'<td class="stack" width="{w}" valign="middle" align="center" style="width:{w}px;padding:8px 0;">{inner}</td>'
    mid = (f'<p style="margin:0 0 10px 0;font-family:{F};font-size:14px;line-height:20px;color:#ffffff;font-weight:bold;text-align:center;">Restons en contact</p>'
           + T(f'<tr><td align="center" style="padding:0 0 8px 0;">{button("Nous suivre", URL_LINKTREE, "#ffffff", BLUE)}</td></tr>'
               f'<tr><td align="center">{button("Nous contacter", URL_CONTACT, "#ffffff", BLUE)}</td></tr>', width=""))
    return f'''<tr><td bgcolor="{BLUE}" style="background-color:{BLUE};padding:28px 40px 24px 40px;" class="px">
{T("<tr>" + col(f'<img src="{IMG_CERN}" width="110" alt="CERN" style="{alt}display:block;width:110px;height:auto;border:0;margin:0 auto;">', 173)
   + col(mid, 174)
   + col(f'<img src="{IMG_FCC}" width="100" alt="FCC" style="{alt}display:block;width:100px;height:auto;border:0;margin:0 auto;">', 173) + "</tr>")}
{T(f'<tr><td height="20" style="height:20px;font-size:0;line-height:0;border-bottom:1px solid #4F86C2;">&nbsp;</td></tr>{spacer(16)}')}
<p style="margin:0;font-family:{F};font-size:13px;line-height:20px;color:#E3F1FB;text-align:center;">Plus d’informations sur <a href="{URL_FCC}" target="_blank" style="color:#ffffff;text-decoration:underline;">fcc-faisabilite.eu</a></p>
</td></tr>
<tr><td align="center" style="padding:14px 40px 0 40px;font-family:{F};font-size:13px;line-height:20px;" class="px"><a href="{URL_PRIVACY}" target="_blank" style="color:{BLUE};text-decoration:underline;">Informations sur la protection des données</a></td></tr>
<tr><td style="padding:16px 40px 30px 40px;" class="px">{T(f"""<tr>
<td width="70" valign="top" style="width:70px;padding-right:14px;"><img src="{IMG_EU}" width="60" alt="Drapeau de l’Union européenne" style="display:block;width:60px;height:auto;border:0;"></td>
<td valign="top" style="font-family:{F};font-size:12px;line-height:18px;color:{GREY};">{EU_TEXT}</td></tr>""")}</td></tr>'''

def build():
    rows = header() + sommaire() + edito() + retour() + process() + actualite() + footer()
    return fr_typo(TEMPLATE.replace("{{ROWS}}", rows))

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
  h1,h2,h3,p {{ margin:0; }}
  @media only screen and (max-width:600px) {{
    .container, .full {{ width:100% !important; }}
    .px {{ padding-left:20px !important; padding-right:20px !important; }}
    .stack {{ display:block !important; width:100% !important; }}
    .pb {{ padding-bottom:28px !important; }}
    .ph {{ padding-right:0 !important; }}
    .hide {{ display:none !important; }}
    .center {{ text-align:left !important; }}
    .center-t {{ float:none !important; }}
    .h1 {{ font-size:28px !important; line-height:34px !important; }}
    .h2 {{ font-size:22px !important; line-height:28px !important; }}
    .tl-date {{ display:block !important; width:auto !important; padding-bottom:0 !important; border:0 !important; }}
    .tl-dot {{ display:none !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background-color:#E9EEF4;">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;">{PREHEADER}{"&nbsp;&zwnj;" * 90}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#E9EEF4" style="background-color:#E9EEF4;">
<tr><td align="center" style="padding:0 0 30px 0;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="width:600px;max-width:600px;background-color:#ffffff;">
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
