import flet as ft
import webbrowser
import os

def main(page: ft.Page):
    # --- CONFIGURATION DE LA PAGE ---
    page.title = "MED-AUDIO PRO"
    page.window_width = 400
    page.window_height = 850
    page.bgcolor = "#F8FAFC"
    
    # --- GESTION DES FICHIERS AUDIO LOCAUX ---
    base_path = os.path.dirname(__file__)

    def play_sound(filename):
        file_path = os.path.join(base_path, "assets", filename)
        if os.path.exists(file_path):
            webbrowser.open(f"file://{file_path}")
        else:
            print(f"Erreur : Le fichier {filename} est introuvable dans le dossier assets.")

    # --- BASE DE DONNÉES CLINIQUE COMPLÈTE (FRANÇAIS) ---
    SOUNDS_DB = [
        # --- CARDIAQUE : NORMAL ---
        {"cat": "C", "type": "✅ Normal", "name": "B1 (Boum)", "file": "b1.mp3", "desc": "Fermeture des valves auriculo-ventriculaires (mitrale et tricuspide). Marque le début de la systole. Maximum à l'apex."},
        {"cat": "C", "type": "✅ Normal", "name": "B2 (Taque)", "file": "b2.mp3", "desc": "Fermeture des valves sigmoïdes (aortique et pulmonaire). Marque le début de la diastole. Maximum à la base (2ème espace intercostal)."},
        
        # --- CARDIAQUE : ADDITIONNEL ---
        {"cat": "C", "type": "⚠️ Additionnel", "name": "B3 (Galop ventriculaire)", "file": "b3.mp3", "desc": "Bruit protodiastolique de remplissage ventriculaire rapide. Normal chez l'enfant/sportif ; indique une insuffisance cardiaque ou une surcharge volumique chez l'adulte."},
        {"cat": "C", "type": "⚠️ Additionnel", "name": "B4 (Galop auriculaire)", "file": "b4.mp3", "desc": "Bruit télédiastolique. Dû à la contraction de l'oreillette contre un ventricule rigide et peu compliant (ex: hypertension sévère, hypertrophie)."},
        
        # --- CARDIAQUE : PATHOLOGIQUE ---
        {"cat": "C", "type": "❌ Pathologique", "name": "Souffle de rétrécissement aortique", "file": "retrecissement_aortique.mp3", "desc": "Souffle systolique éjectionnel, rude, losangique (crescendo-decrescendo). Foyer aortique (2ème EIC droit), irradiant vers les vaisseaux du cou."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Souffle d'insuffisance aortique", "file": "insuffisance_aortique.mp3", "desc": "Souffle diastolique doux, humé, decrescendo. Maximum au foyer aortique ou bord sternal gauche, patient penché en avant."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Roulement de rétrécissement mitral", "file": "retrecissement_mitral.mp3", "desc": "Roulement diastolique de basse fréquence, souvent précédé d'un claquement d'ouverture. Maximum à l'apex en décubitus latéral gauche."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Souffle d'insuffisance mitrale", "file": "insuffisance_mitrale.mp3", "desc": "Souffle holosystolique en jet de vapeur, de haute fréquence. Maximum à l'apex, irradiant vers l'aisselle gauche."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Souffle d'insuffisance tricuspidienne", "file": "insuffisance_tricuspidienne.mp3", "desc": "Souffle holosystolique au bord inférieur gauche du sternum. L'intensité augmente à l'inspiration (Signe de Carvallo)."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Souffle de rétrécissement pulmonaire", "file": "retrecissement_pulmonaire.mp3", "desc": "Souffle systolique éjectionnel au 2ème EIC gauche. Irradie souvent vers l'épaule gauche et le cou."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Frottement péricardique", "file": "frottement_pericardique.mp3", "desc": "Bruit superficiel, rude, de va-et-vient (comme du cuir froissé). Signe classique de la péricardite aiguë."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Claquement d'ouverture", "file": "claquement_ouverture.mp3", "desc": "Bruit sec et claquant en début de diastole, causé par l'ouverture forcée d'une valve mitrale sténosée et épaissie."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Clic d'éjection", "file": "clic_ejection.mp3", "desc": "Bruit sec protosystolique. Souvent associé à une bicuspidie aortique ou une sténose valvulaire pulmonaire."},
        {"cat": "C", "type": "❌ Pathologique", "name": "Clic mésosystolique", "file": "clic_mesosystolique.mp3", "desc": "Bruit sec en milieu de systole, souvent suivi d'un souffle télésystolique. Signe classique du prolapsus de la valve mitrale (PVM)."},

        # --- PULMONAIRE : NORMAL ---
        {"cat": "P", "type": "✅ Normal", "name": "Murmure vésiculaire", "file": "murmure vésiculaire.mp3", "desc": "Bruit doux et humé, de basse fréquence. L'inspiration est plus longue que l'expiration. Entendu sur la majeure partie des champs pulmonaires périphériques."},
        {"cat": "P", "type": "✅ Normal", "name": "Bruit trachéo-bronchique (Souffle tubaire)", "file": "souffle_tubaire.mp3", "desc": "Fort, de haute tonalité, tubulaire. L'expiration est plus longue que l'inspiration. Normal sur la trachée ; pathologique si entendu en périphérie (syndrome de condensation)."},
        {"cat": "P", "type": "✅ Normal", "name": "Bruit broncho-vésiculaire", "file": "broncho_vesiculaire.mp3", "desc": "Tonalité et intensité intermédiaires. Inspiration égale à l'expiration. Normalement entendu entre les omoplates et aux 1er/2ème EIC en antérieur."},
        {"cat": "P", "type": "✅ Normal", "name": "Bruit trachéal", "file": "bruit_tracheal.mp3", "desc": "Très fort, rude et de haute fréquence. Entendu directement sur la trachée dans le cou."},

        # --- PULMONAIRE : SURAJOUTÉS (PATHOLOGIQUES) ---
        {"cat": "P", "type": "❌ Pathologique", "name": "Râles crépitants", "file": "crepitants.mp3", "desc": "Bruits discontinus, fins et secs (comme du Velcro ou des cheveux frottés près de l'oreille). Suggère du liquide dans les alvéoles (Pneumonie, Insuffisance cardiaque, Fibrose)."},
        {"cat": "P", "type": "❌ Pathologique", "name": "Sibilants (Wheezing)", "file": "sibilants.mp3", "desc": "Bruits continus, sifflements musicaux aigus. Causés par le passage de l'air dans des bronches rétrécies (Asthme, BPCO)."},
        {"cat": "P", "type": "❌ Pathologique", "name": "Ronflants (Rhonchi)", "file": "rhonchi.mp3", "desc": "Bruits continus, de basse fréquence, ressemblant à des ronflements. Indique des sécrétions épaisses dans les grosses voies (Bronchite). Disparaissent souvent après la toux."},
        {"cat": "P", "type": "❌ Pathologique", "name": "Stridor", "file": "stridor.mp3", "desc": "Bruit aigu, fort et strident, principalement à l'inspiration. Signe d'URGENCE d'une obstruction des voies aériennes supérieures (Épiglottite, Corps étranger)."},
        {"cat": "P", "type": "❌ Pathologique", "name": "Frottement pleural", "file": "frottement_pleural.mp3", "desc": "Bruit rude, grinçant, audible aux deux temps respiratoires. Se produit lorsque les feuillets pleuraux enflammés frottent l'un contre l'autre (Pleurésie)."},
        {"cat": "P", "type": "❌ Pathologique", "name": "Diminution du murmure vésiculaire", "file": "diminution_murmure.mp3", "desc": "Moins audible que la normale. Se produit lors d'un faible effort respiratoire, d'une hyperinflation (BPCO sévère/Emphysème) ou chez les patients obèses."},
        {"cat": "P", "type": "❌ Pathologique", "name": "Abolition du murmure vésiculaire", "file": "abolition_murmure.mp3", "desc": "Aucun passage d'air entendu. Signe d'URGENCE indiquant une obstruction sévère, un épanchement pleural massif ou un pneumothorax (poumon collabé)."}
    ]

    # --- ATTRIBUTION DES COULEURS DES BADGES ---
    def get_badge_color(stype):
        if "✅" in stype: return ft.Colors.GREEN_600
        if "⚠️" in stype: return ft.Colors.ORANGE_600
        return ft.Colors.RED_600

    # --- CONSTRUCTEUR DE CARTES UI ---
    # Modifié pour accepter l'objet entier (item) et ajouter le bouton audio
    def EntryCard(item):
        return ft.Container(
            padding=15, bgcolor=ft.Colors.WHITE, border_radius=15,
            border=ft.border.all(1, "#E2E8F0"),
            content=ft.Column([
                ft.Row([
                    ft.Text(item["name"], size=16, weight="bold", color=ft.Colors.BLUE_900, expand=True),
                    ft.Container(
                        ft.Text(item["type"], size=10, color="white", weight="bold"), 
                        bgcolor=get_badge_color(item["type"]), 
                        padding=ft.padding.only(left=8, right=8, top=4, bottom=4), 
                        border_radius=5
                    )
                ]),
                ft.Divider(height=1, color="#EDF2F7"),
                ft.Text(item["desc"], size=13, color=ft.Colors.GREY_800),
                
                # NOUVEAU : Bouton pour lire le fichier audio local
                ft.ElevatedButton(
                    "ÉCOUTER",
                    icon=ft.Icons.PLAY_ARROW_ROUNDED,
                    on_click=lambda _: play_sound(item["file"]),
                    bgcolor=ft.Colors.BLUE_100,
                    color=ft.Colors.BLUE_900,
                    elevation=0
                )
            ], spacing=8)
        )

    # --- LOGIQUE DE NAVIGATION ---
    def switch_to_home(e=None):
        view_container.controls = [
            ft.Container(height=40),
            ft.Icon(ft.Icons.LOCAL_HOSPITAL, color=ft.Colors.BLUE_700, size=50),
            ft.Text("ATLAS CLINIQUE", size=24, weight="bold", color=ft.Colors.BLUE_900),
            ft.Text("SÉLECTIONNER LE SYSTÈME D'EXAMEN", size=14, color=ft.Colors.GREY_600),
            ft.Container(height=30),
            
            # Bouton Cardiaque
            ft.Container(
                on_click=lambda _: switch_to_list("C"),
                padding=20, bgcolor="white", border_radius=20, border=ft.border.all(1, "#EDF2F7"),
                content=ft.Row([
                    ft.Icon(ft.Icons.FAVORITE, color="red", size=30), 
                    ft.Column([ft.Text("EXAMEN CARDIAQUE", color='black', weight="bold", size=16), ft.Text("Valves & Souffles", size=12, color='grey')])
                ])
            ),
            ft.Container(height=10),
            
            # Bouton Pulmonaire
            ft.Container(
                on_click=lambda _: switch_to_list("P"),
                padding=20, bgcolor="white", border_radius=20, border=ft.border.all(1, "#EDF2F7"),
                content=ft.Row([
                    ft.Icon(ft.Icons.AIR, color="blue", size=30), 
                    ft.Column([ft.Text("EXAMEN PULMONAIRE", color='black', weight="bold", size=16), ft.Text("Bruits respiratoires & surajoutés", size=12, color="grey")])
                ])
            )
        ]
        page.update()

    def switch_to_list(cat):
        title = "BRUITS CARDIAQUES" if cat == "C" else "BRUITS PULMONAIRES"
        items = [s for s in SOUNDS_DB if s["cat"] == cat]
        
        view_container.controls = [
            ft.Container(height=20),
            ft.Row([
                ft.IconButton(ft.Icons.ARROW_BACK, on_click=switch_to_home, icon_color=ft.Colors.BLUE_900),
                ft.Text(title, size=20, weight="bold", color=ft.Colors.BLUE_900)
            ]),
            # Modifié pour passer l'objet entier (i) à EntryCard
            ft.ListView(controls=[EntryCard(i) for i in items], spacing=10, expand=True, padding=10)
        ]
        page.update()

    # --- INITIALISATION DE L'APPLICATION ---
    view_container = ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
    page.add(view_container)
    switch_to_home()

# Indispensable : On lie le dossier "assets" à l'application Flet
ft.app(target=main, assets_dir="assets")
