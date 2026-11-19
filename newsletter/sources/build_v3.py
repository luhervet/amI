# -*- coding: utf-8 -*-
"""V3 : V2 + bandeau chiffres clés, frise « Nous sommes ici », encart exposition, bande de vœux."""
import sys
import build_v2 as b
from build_v2 import (T, spacer, p, eyebrow, h2, h3, placeholder, button, section, body_rows, two,
                      card, stat_card, header, sommaire, edito, footer,
                      BLUE, ACCENT, ACCENT_TXT, DARK, INK, GREY, LIGHT, LINE, F, FH, LIGHT_ATTRS)
from content import *

PALE = "#BFE3F7"
def hld(s):  # surlignage lisible sur fond foncé
    return f'<span style="background-color:#fff3a3;color:#1F2933;">{s}</span>'     # texte secondaire sur fond foncé (contraste 8,9:1 sur DARK)
FUTURE = "#B8C7DA"   # étapes à venir de la frise

# ---------- 1. Bandeau chiffres clés ----------

def key_figures():
    def cell(value, label):
        return (f'<td width="118" valign="top" style="width:118px;padding:0 12px 0 0;">'
                f'{T(f"<tr><td height=\"3\" bgcolor=\"{ACCENT}\" style=\"height:3px;background-color:{ACCENT};font-size:0;line-height:0;\" width=\"36\">&nbsp;</td><td style=\"font-size:0;line-height:0;\">&nbsp;</td></tr>")}'
                f'<p style="margin:12px 0 0 0;font-family:{F};font-size:42px;line-height:46px;font-weight:bold;color:#ffffff;">{value}</p>'
                f'<p style="margin:4px 0 0 0;font-family:{F};font-size:13px;line-height:18px;color:{PALE};">{label}</p></td>')
    figs = [("XX", c[0]) for c in CHIFFRES]
    pair = lambda a, c: T("<tr>" + cell(*a) + cell(*c) + "</tr>")
    grid = T(f'''<tr><td class="stack pb-s" width="260" valign="top" style="width:260px;">{pair(figs[0], figs[1])}</td>
<td class="stack" width="260" valign="top" style="width:260px;">{pair(figs[2], figs[3])}</td></tr>''')
    return f'''<tr><td bgcolor="{DARK}" style="background-color:{DARK};padding:34px 40px 30px 40px;" class="px">
{eyebrow("La participation en chiffres", PALE)}
<p style="margin:0 0 24px 0;font-family:{F};font-size:20px;line-height:26px;font-weight:bold;color:#ffffff;">Débat public en France et concertation en Suisse, cumulés</p>
{grid}
<p style="margin:26px 0 0 0;font-family:{F};font-size:13px;line-height:18px;"><a href="#chiffres" style="color:#ffffff;text-decoration:underline;">Voir le détail par pays</a> <span style="color:{PALE};">&darr;</span></p>
</td></tr>{spacer(32)}'''

# ---------- 3. Frise « Nous sommes ici » ----------

STEPS = [
    (hl("Mai – sept. 2026"), "Débat public et concertation", "done", ""),
    (SUP_ER + " déc. 2026", "Publication des comptes rendus et bilans", "current", "Webinaire le " + hl("XX déc.")),
    ("Mars 2027 au plus tard", "Réponse du CERN et engagements", "future", ""),
    ("Dès 2027", "Concertation continue", "future", ""),
    ("2<sup style='font-size:70%;line-height:0;vertical-align:super;text-transform:none;'>d</sup> sem. 2028", "Décision des États membres", "future", ""),
]

def _line(color):
    if not color:
        return '<td width="37" style="width:37px;font-size:0;line-height:0;">&nbsp;</td>'
    return (f'<td width="37" valign="middle" style="width:37px;">'
            f'{T(f"<tr><td height=\"3\" bgcolor=\"{color}\" style=\"height:3px;background-color:{color};font-size:0;line-height:0;\">&nbsp;</td></tr>")}</td>')

def _dot(state, size=28):
    if state == "current":
        size -= 8
    elif state == "future":
        size -= 4
    if state == "done":
        st, inner = f"background-color:{BLUE};", f'<span style="font-family:{F};font-size:14px;line-height:{size}px;color:#ffffff;font-weight:bold;">&#10003;</span>'
        bg = BLUE
    elif state == "current":
        st, inner, bg = f"background-color:{ACCENT_TXT};border:4px solid #CFE6F6;", "&nbsp;", ACCENT_TXT
    else:
        st, inner, bg = f"background-color:#ffffff;border:2px solid {FUTURE};", "&nbsp;", "#ffffff"
    return (f'<td width="{size}" height="{size}" align="center" valign="middle" bgcolor="{bg}" '
            f'style="width:{size}px;height:{size}px;{st}border-radius:50%;font-size:0;line-height:{size}px;">{inner}</td>')

def frise_desktop():
    n = len(STEPS)
    pins, track, labels = "", "", ""
    for i, (date, title, state, note) in enumerate(STEPS):
        pin = (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td bgcolor="{ACCENT_TXT}" style="background-color:{ACCENT_TXT};border-radius:10px;padding:4px 7px;font-family:{F};font-size:10px;line-height:12px;font-weight:bold;color:#ffffff;white-space:nowrap;">Nous sommes ici</td></tr></table>'
               f'<p style="margin:0;font-family:{F};font-size:10px;line-height:12px;color:{ACCENT_TXT};text-align:center;">&#9660;</p>') if state == "current" else "&nbsp;"
        pins += f'<td width="104" valign="bottom" align="center" style="width:104px;height:34px;padding-bottom:4px;">{pin}</td>'
        nxt = STEPS[i + 1][2] if i < n - 1 else None
        left = None if i == 0 else (BLUE if state in ("done", "current") else FUTURE)
        right = None if i == n - 1 else (BLUE if nxt in ("done", "current") else FUTURE)
        track += f'<td width="104" style="width:104px;">{T("<tr>" + _line(left) + _dot(state) + _line(right) + "</tr>", width="104", attrs='style="border-collapse:separate;"')}</td>'
        tcol = INK if state != "future" else GREY
        nt = f'<p style="margin:6px 0 0 0;font-family:{F};font-size:11px;line-height:15px;color:{GREY};">{note}</p>' if note else ""
        labels += (f'<td width="104" valign="top" align="center" style="width:104px;padding:12px 4px 0 4px;">'
                   f'<p style="margin:0;font-family:{F};font-size:11px;line-height:15px;font-weight:bold;color:{BLUE};text-transform:uppercase;letter-spacing:.3px;">{date}</p>'
                   f'<p style="margin:4px 0 0 0;font-family:{F};font-size:13px;line-height:17px;font-weight:bold;color:{tcol};">{title}</p>{nt}</td>')
    return T(f"<tr>{pins}</tr><tr>{track}</tr><tr>{labels}</tr>", width="520", attrs='class="dsk-only"')

def frise_mobile():
    rows = ""
    for i, (date, title, state, note) in enumerate(STEPS):
        last = i == len(STEPS) - 1
        line = "" if last else f"border-left:3px solid {BLUE if STEPS[i+1][2] in ('done','current') else FUTURE};"
        pin = f'<span style="display:inline-block;background-color:{ACCENT_TXT};border-radius:10px;padding:3px 8px;font-size:11px;line-height:13px;font-weight:bold;color:#ffffff;margin-bottom:4px;text-transform:none;">Nous sommes ici</span><br>' if state == "current" else ""
        nt = f'<br><span style="font-size:12px;color:{GREY};font-weight:normal;">{note}</span>' if note else ""
        rows += (f'<tr><td width="28" valign="top" style="width:28px;">{T("<tr>" + _dot(state, 22) + "</tr>", attrs='style="border-collapse:separate;"')}</td>'
                 f'<td valign="top">'
                 f'<p style="margin:0;font-family:{F};font-size:12px;line-height:16px;font-weight:bold;color:{BLUE};text-transform:uppercase;">{pin}{date}</p>'
                 f'<p style="margin:2px 0 {0 if last else 18}px 0;font-family:{F};font-size:15px;line-height:20px;font-weight:bold;color:{INK if state != "future" else GREY};">{title}{nt}</p></td></tr>')
    return (f'<!--[if !mso]><!--><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="mob-only" '
            f'style="display:none;max-height:0;overflow:hidden;">{rows}</table><!--<![endif]-->')

def process():
    rows = body_rows(p(LOREM[0]))
    box = (f'<tr><td style="padding:24px 0 22px 0;" class="frise-pad">'
           f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:0 24px;">{eyebrow("Le calendrier", BLUE)}</td></tr></table>'
           f'{frise_desktop()}'
           f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:0 24px;">{frise_mobile()}</td></tr></table>'
           f'</td></tr>')
    rows += spacer(6) + f'<tr><td style="padding:0 40px;" class="px">{T(box, attrs=LIGHT_ATTRS)}</td></tr>'
    docs = "".join(f'<tr><td style="padding:0 0 10px 0;">{button(t + "&nbsp;&rarr;", u, nowrap=False)}</td></tr>' for t, u in DOCS)
    rows += spacer(24) + body_rows(eyebrow("Les documents", BLUE) + T(spacer(6)) + T(docs, width=""))
    return section("02", "Les suites de la participation", SECTIONS[1][1], "compte-rendu", rows)

# ---------- Section 01 avec bandeau chiffres ----------

def retour():
    head = f'''<tr><td style="padding:0 40px;" class="px">{T(f'<tr><td style="border-top:3px solid {BLUE};font-size:0;line-height:0;" width="48">&nbsp;</td><td style="font-size:0;line-height:0;">&nbsp;</td></tr>')}</td></tr>
{spacer(18)}
<tr><td style="padding:0 40px;" class="px">{eyebrow("01 — Participation")}{h2(SECTIONS[0][1], "retour")}</td></tr>
{spacer(20)}'''
    rows = body_rows(p(LOREM[0])) + spacer(8)
    rows += key_figures()
    rows += body_rows('<a name="chiffres" id="chiffres"></a>' + h3("Le détail par pays", size=19)) + spacer(6)
    rows += two(stat_card("En France", "Débat public (CNDP)", 1, BLUE), stat_card("En Suisse", "Concertation", 2, ACCENT_TXT))
    rows += spacer(14) + body_rows(p(SOURCES_CHIFFRES, size=13, lh=20, color=GREY, extra="font-style:italic;"))
    rows += spacer(14) + body_rows('<a name="focus" id="focus"></a>' + h3("Focus : le Groupe citoyen jeune et l’Atelier de la relève", size=19) + p(LOREM[2]))
    rows += spacer(6) + two(*[card(f"Photo – {t}", t, x) for t, x in FOCUS])
    return head + rows + spacer(44)

# ---------- 6. Encart exposition ----------

def expo():
    aid, title, chapo = next(a for a in ACTUS if a[0] == "expo")
    info = lambda lab, val: (f'<td class="stack" width="155" valign="top" style="width:155px;padding:0 10px 14px 0;">'
                             f'<p style="margin:0;font-family:{F};font-size:11px;line-height:14px;font-weight:bold;letter-spacing:1px;color:{PALE};">{lab}</p>'
                             f'<p style="margin:4px 0 0 0;font-family:{F};font-size:15px;line-height:20px;font-weight:bold;color:#ffffff;">{val}</p></td>')
    infos = T("<tr>" + info("OÙ", hld("[Lieu]")) + info("QUAND", hld("[Dates]")) + info("ACCÈS", "Entrée libre") + "</tr>")
    panel = f'''<tr><td>{placeholder("Visuel de l’exposition « Why? »", 520, 240, 0)}</td></tr>
<tr><td bgcolor="{DARK}" style="background-color:{DARK};border-top:4px solid {ACCENT};padding:28px 28px 26px 28px;">
{eyebrow("Exposition", PALE)}
<h3 style="margin:0;font-family:{FH};font-size:46px;line-height:50px;font-weight:bold;color:#ffffff;"><a name="{aid}" id="{aid}"></a>« Why? »</h3>
<p style="margin:12px 0 22px 0;font-family:{F};font-size:16px;line-height:24px;color:#E3F1FB;">{hld("[Accroche : une exposition pour … – à compléter]")} {LOREM_SHORT}</p>
{infos}
<div style="height:8px;line-height:8px;font-size:8px;">&nbsp;</div>
{btn_full("Préparer ma visite&nbsp;&rarr;", "#", "#ffffff", DARK)}
</td></tr>'''
    return body_rows(T(panel))

def horizontal_card(aid):
    a = next(x for x in ACTUS if x[0] == aid)
    return f'''<tr><td style="padding:0 40px;" class="px">{T(f"""<tr>
<td class="stack pb" width="200" valign="top" style="width:200px;">{placeholder(f"Photo – {a[1]}", 200, 150)}</td>
<td class="hide" width="20" style="width:20px;font-size:0;line-height:0;">&nbsp;</td>
<td class="stack" valign="top">{h3(a[1], a[0], 18)}<p style="margin:0;font-family:{F};font-size:14px;line-height:21px;color:{INK};"><strong>{a[2]}.</strong> {LOREM_SHORT}</p></td></tr>""")}</td></tr>'''

def actualite():
    byid = {a[0]: a for a in ACTUS}
    g = byid["gouvernance"]
    featured = body_rows(placeholder(f"Photo – {g[1]}", 520, 240) + T(spacer(18)) +
                         h3(g[1], g[0], 22, BLUE) + p(f"<strong>{g[2]}.</strong> {LOREM[0]}"))
    grid = [card(f"Photo – {byid[k][1]}", byid[k][1], f"<strong>{byid[k][2]}.</strong> {LOREM_SHORT}", k) for k in ("geotechnique", "faisceau")]
    rows = (featured + spacer(32) + horizontal_card("evenements") + spacer(36)
            + two(*grid) + spacer(40) + expo())
    return section("03", "Actualités", SECTIONS[2][1], "actualite", rows)

# ---------- Bande de vœux ----------

def voeux():
    return f'''<tr><td style="padding:0 40px;" class="px">{T(f"""<tr><td align="center" style="padding:30px 24px;border-top:1px solid {LINE};border-bottom:1px solid {LINE};">
<p style="margin:0;font-family:{F};font-size:14px;line-height:14px;color:{ACCENT};letter-spacing:6px;">&#10022; &#10022; &#10022;</p>
<p style="margin:12px 0 6px 0;font-family:{FH};font-size:24px;line-height:30px;font-weight:bold;color:{BLUE};">Belles fêtes de fin d’année</p>
<p style="margin:0;font-family:{F};font-size:15px;line-height:22px;color:{GREY};">Toute l’équipe FCC vous donne rendez-vous en 2027.</p>
</td></tr>""")}</td></tr>{spacer(36)}'''

EXTRA_CSS = """    .dsk-only {{ display:none !important; }}
    .mob-only {{ display:table !important; max-height:none !important; overflow:visible !important; }}
    .pb-s {{ padding-bottom:22px !important; }}
  }}
</style>"""

def build():
    rows = header() + sommaire() + edito() + retour() + process() + actualite() + voeux() + footer()
    tpl = b.TEMPLATE.replace("  }}\n</style>", EXTRA_CSS) if "  }}\n</style>" in b.TEMPLATE else b.TEMPLATE.replace("  }\n</style>", EXTRA_CSS.replace("{{", "{").replace("}}", "}"))
    return fr_typo(tpl.replace("{{ROWS}}", rows))

# =====================  Passe UX / mobile  =====================

def btn_full(text, href, bg=BLUE, fg="#ffffff"):
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" class="mob-full"><tr>'
            f'<td bgcolor="{bg}" align="center" style="background-color:{bg};border-radius:22px;padding:12px 22px;">'
            f'<a href="{href}" target="_blank" style="font-family:{F};font-size:15px;line-height:20px;font-weight:bold;color:{fg};text-decoration:none;display:inline-block;">{text}</a></td></tr></table>')

def back_to_top():
    return (f'<tr><td align="right" style="padding:14px 40px 0 40px;" class="px">'
            f'<a href="#sommaire" style="font-family:{F};font-size:13px;line-height:18px;color:{GREY};text-decoration:underline;">&uarr;&nbsp;Retour au sommaire</a></td></tr>')

def header_v3():
    return f'''<tr><td align="center" style="padding:10px 20px;font-family:{F};font-size:12px;line-height:16px;color:{GREY};">
<!-- Remplacer les href par les liens Spotler (désinscription / version web) -->
<a href="#" style="color:{GREY};text-decoration:underline;">Version web</a>&nbsp;&nbsp;·&nbsp;&nbsp;<a href="#" style="color:{GREY};text-decoration:underline;">Désinscription</a></td></tr>
{brand_header()}
<tr><td bgcolor="{BLUE}" style="background-color:{BLUE};padding:6px 40px 30px 40px;" class="px">
<p style="margin:0 0 10px 0;font-family:{F};font-size:12px;line-height:18px;letter-spacing:2px;font-weight:bold;color:#BFE3F7;">LETTRE DES TERRITOIRES<span class="mob-hide">&nbsp;&nbsp;·&nbsp;&nbsp;</span><span class="mob-block">{NUMERO}</span></p>
<h1 class="h1" style="margin:0;font-family:{FH};font-size:36px;line-height:42px;font-weight:700;color:#ffffff;">L’actualité de l’étude&nbsp;FCC</h1>
<p style="margin:12px 0 0 0;font-family:{F};font-size:16px;line-height:24px;color:#E3F1FB;">Débat public en France, concertation en Suisse : retour sur la participation et prochaines étapes</p>
</td></tr>
<tr><td bgcolor="{ACCENT}" height="5" style="background-color:{ACCENT};height:5px;font-size:0;line-height:0;">&nbsp;</td></tr>
{spacer(28)}'''

ESSENTIEL = [
    ("Les comptes rendus et bilans sont publiés", "Débat public en France et concertation en Suisse, depuis le " + SUP_ER + " décembre", "#compte-rendu"),
    ("Le CERN répondra au plus tard en mars 2027", "Avec des engagements précis et concrets, rendus publics", "#compte-rendu"),
    ("Exposition « Why? »", hl("[Lieu et dates]") + " – entrée libre", "#expo"),
]

def essentiel():
    rows = ""
    for i, (t, sub, href) in enumerate(ESSENTIEL):
        bb = f"border-bottom:1px solid {LINE};" if i < len(ESSENTIEL) - 1 else ""
        rows += (f'<tr><td width="30" valign="top" style="width:30px;padding:12px 0;{bb}font-family:{F};font-size:18px;line-height:22px;font-weight:bold;color:{ACCENT_TXT};">{i+1}</td>'
                 f'<td valign="top" style="padding:12px 0;{bb}"><a href="{href}" style="font-family:{F};font-size:16px;line-height:22px;font-weight:bold;color:{INK};text-decoration:none;">{t}&nbsp;<span style="color:{ACCENT_TXT};">&rarr;</span></a>'
                 f'<br><span style="font-family:{F};font-size:14px;line-height:20px;color:{GREY};">{sub}</span></td></tr>')
    inner = f'<tr><td style="border-left:4px solid {ACCENT};padding:18px 22px 8px 22px;">{eyebrow("L’essentiel en 30 secondes", BLUE)}{T(rows)}</td></tr>'
    return f'<tr><td style="padding:0 40px;" class="px">{T(inner, attrs=f"style=\"border:1px solid {LINE};border-left:0;\"")}</td></tr>{spacer(28)}'

def sommaire_v3():
    rows = ""
    entries = [("", "edito", "Édito de Michael Benedikt, chef de l’étude FCC", [])] + [
        (f"0{i+1}", sid, title, subs) for i, (sid, title, subs) in enumerate(SECTIONS)]
    for n, sid, title, subs in entries:
        sub = "".join(f'<br><a href="#{a}" style="font-family:{F};font-size:13px;line-height:20px;color:{GREY};text-decoration:none;">–&nbsp;{t}</a>' for a, t in subs)
        sub = f'<span class="mob-hide">{sub}</span>' if sub else ""
        rows += (f'<tr><td width="44" valign="top" style="padding:12px 0;border-bottom:1px solid {LINE};font-family:{F};font-size:20px;line-height:22px;font-weight:700;color:{ACCENT_TXT};">{n or "00"}</td>'
                 f'<td valign="top" style="padding:12px 0;border-bottom:1px solid {LINE};"><a href="#{sid}" style="font-family:{F};font-size:15px;line-height:22px;font-weight:bold;color:{INK};text-decoration:none;">{title}</a>{sub}</td></tr>')
    inner = f'<tr><td style="padding:22px 26px 12px 26px;" class="som-pad"><a name="sommaire" id="sommaire"></a>{eyebrow("Au sommaire", BLUE)}{T(rows)}</td></tr>'
    return f'<tr><td style="padding:0 40px;" class="px">{T(inner, attrs=LIGHT_ATTRS)}</td></tr>{spacer(44)}'

def frise_mobile():
    rows = ""
    for i, (date, title, state, note) in enumerate(STEPS):
        last = i == len(STEPS) - 1
        total = 24
        pin = f'<span style="display:inline-block;background-color:{ACCENT_TXT};border-radius:10px;padding:3px 9px;font-size:11px;line-height:13px;font-weight:bold;color:#ffffff;text-transform:none;">Nous sommes ici</span><br>' if state == "current" else ""
        nt = f'<br><span style="font-size:13px;line-height:18px;color:{GREY};font-weight:normal;">{note}</span>' if note else ""
        dot = T("<tr>" + _dot(state, total) + "</tr>", width=str(total), attrs='style="border-collapse:separate;"')
        rows += (f'<tr><td width="36" valign="top" style="width:36px;padding:{18 if state == "current" else 0}px 0 0 0;">{dot}</td>'
                 f'<td valign="top" style="padding:0 0 {0 if last else 20}px 0;">'
                 f'<p style="margin:0 0 2px 0;font-family:{F};font-size:12px;line-height:16px;font-weight:bold;color:{BLUE};text-transform:uppercase;">{pin}{date}</p>'
                 f'<p style="margin:0;font-family:{F};font-size:16px;line-height:22px;font-weight:bold;color:{INK if state != "future" else GREY};">{title}{nt}</p></td></tr>')
    return (f'<!--[if !mso]><!--><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="mob-only" '
            f'style="display:none;max-height:0;overflow:hidden;">{rows}</table><!--<![endif]-->')

def process_v3():
    rows = body_rows(p(LOREM[0]))
    box = (f'<tr><td style="padding:24px 0 22px 0;">'
           f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:0 24px;">{eyebrow("Le calendrier", BLUE)}</td></tr></table>'
           f'{frise_desktop()}'
           f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding:6px 22px 0 22px;">{frise_mobile()}</td></tr></table>'
           f'</td></tr>')
    rows += spacer(6) + f'<tr><td style="padding:0 40px;" class="px">{T(box, attrs=LIGHT_ATTRS)}</td></tr>'
    docs = "".join(f'<tr><td style="padding:0 0 10px 0;">{btn_full(t + "&nbsp;&rarr;", u)}</td></tr>' for t, u in DOCS)
    rows += spacer(24) + body_rows(eyebrow("Les documents", BLUE) + T(spacer(6)) + T(docs, attrs='class="mob-full"'))
    return section("02", "Les suites de la participation", SECTIONS[1][1], "compte-rendu", rows)

def footer_v3():
    alt = "font-family:Arial,sans-serif;font-size:14px;color:#ffffff;"
    cern = lambda w: f'<img src="{IMG_CERN}" width="{w}" alt="CERN" style="{alt}display:block;width:{w}px;height:auto;border:0;margin:0 auto;">'
    fcc = lambda w: f'<img src="{IMG_FCC}" width="{w}" alt="FCC" style="{alt}display:block;width:{w}px;height:auto;border:0;margin:0 auto;">'
    mid = (f'<p style="margin:0 0 12px 0;font-family:{F};font-size:15px;line-height:20px;color:#ffffff;font-weight:bold;text-align:center;">Restons en contact</p>'
           + T(f'<tr><td align="center" style="padding:0 0 10px 0;">{btn_full("Nous suivre", URL_LINKTREE, "#ffffff", BLUE)}</td></tr>'
               f'<tr><td align="center">{btn_full("Nous contacter", URL_CONTACT, "#ffffff", BLUE)}</td></tr>', attrs='class="mob-full"'))
    mob_logos = (f'<!--[if !mso]><!--><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" class="mob-only" style="display:none;max-height:0;overflow:hidden;">'
                 f'<tr><td align="right" width="50%" style="padding:0 18px 22px 0;">{cern(90)}</td><td align="left" width="50%" style="padding:0 0 22px 18px;">{fcc(80)}</td></tr></table><!--<![endif]-->')
    return f'''<tr><td bgcolor="{BLUE}" style="background-color:{BLUE};padding:28px 40px 24px 40px;" class="px">
{mob_logos}
{T(f"""<tr>
<td class="stack dsk-only" width="173" valign="middle" align="center" style="width:173px;padding:8px 0;">{cern(110)}</td>
<td class="stack" width="174" valign="middle" align="center" style="width:174px;padding:8px 0;">{mid}</td>
<td class="stack dsk-only" width="173" valign="middle" align="center" style="width:173px;padding:8px 0;">{fcc(100)}</td></tr>""")}
{T(f'<tr><td height="20" style="height:20px;font-size:0;line-height:0;border-bottom:1px solid #4F86C2;">&nbsp;</td></tr>{spacer(16)}')}
<p style="margin:0;font-family:{F};font-size:14px;line-height:20px;color:#E3F1FB;text-align:center;">Plus d’informations sur <a href="{URL_FCC}" target="_blank" style="color:#ffffff;text-decoration:underline;">fcc-faisabilite.eu</a></p>
</td></tr>
<tr><td align="center" style="padding:16px 40px 0 40px;font-family:{F};font-size:14px;line-height:20px;" class="px"><a href="{URL_PRIVACY}" target="_blank" style="color:{BLUE};text-decoration:underline;">Informations sur la protection des données</a></td></tr>
<tr><td style="padding:16px 40px 30px 40px;" class="px">{T(f"""<tr>
<td width="70" valign="top" style="width:70px;padding-right:14px;"><img src="{IMG_EU}" width="60" alt="Drapeau de l’Union européenne" style="font-family:Arial,sans-serif;font-size:11px;color:{GREY};display:block;width:60px;height:auto;border:0;"></td>
<td valign="top" style="font-family:{F};font-size:12px;line-height:18px;color:{GREY};">{EU_TEXT}</td></tr>""")}</td></tr>'''

EXTRA_CSS = """    .dsk-only { display:none !important; }
    .mob-only { display:table !important; max-height:none !important; overflow:visible !important; }
    .mob-hide { display:none !important; }
    .mob-block { display:block !important; }
    .mob-full { width:100% !important; }
    .pb-s { padding-bottom:22px !important; }
    .som-pad { padding:18px 18px 8px 18px !important; }
    .h1 { font-size:30px !important; line-height:36px !important; }
  }
</style>"""

def build():
    rows = (header_v3() + essentiel() + sommaire_v3() + edito() + back_to_top() + spacer(30)
            + retour() + back_to_top() + spacer(30)
            + process_v3() + back_to_top() + spacer(30)
            + actualite() + back_to_top() + spacer(30)
            + voeux() + footer_v3())
    tpl = b.TEMPLATE
    assert "  }\n</style>" in tpl
    tpl = tpl.replace("  }\n</style>", EXTRA_CSS)
    return fr_typo(tpl.replace("{{ROWS}}", rows))

if __name__ == "__main__":
    open(sys.argv[1], "w", encoding="utf-8").write(build())
