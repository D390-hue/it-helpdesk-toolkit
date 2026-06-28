#!/usr/bin/env python3
"""
IT Helpdesk Toolkit
===================
Outil de support IT pour la gestion d'incidents, le scan réseau
et le diagnostic système.

Auteur : DOGLO Koami Justin
GitHub : https://github.com/justindoglo
"""

import os
import sys
from modules.network_scanner import NetworkScanner
from modules.system_info import SystemInfo
from modules.incident_logger import IncidentLogger
from modules.reporter import Reporter

# ── Couleurs ANSI ──────────────────────────────────────────────
CYAN   = "\033[96m"
BLUE   = "\033[94m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
BOLD   = "\033[1m"
RESET  = "\033[0m"
DIM    = "\033[2m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(f"""
{CYAN}{BOLD}
 ██╗████████╗    ██╗  ██╗███████╗██╗     ██████╗ ██████╗ ███████╗███████╗██╗  ██╗
 ██║╚══██╔══╝    ██║  ██║██╔════╝██║     ██╔══██╗██╔══██╗██╔════╝██╔════╝██║ ██╔╝
 ██║   ██║       ███████║█████╗  ██║     ██████╔╝██║  ██║█████╗  ███████╗█████╔╝
 ██║   ██║       ██╔══██║██╔══╝  ██║     ██╔═══╝ ██║  ██║██╔══╝  ╚════██║██╔═██╗
 ██║   ██║       ██║  ██║███████╗███████╗██║     ██████╔╝███████╗███████║██║  ██╗
 ╚═╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
{RESET}
{DIM}          IT Helpdesk Toolkit v1.0  ·  by DOGLO Koami Justin{RESET}
{DIM}          github.com/justindoglo{RESET}
""")


def menu():
    print(f"{BOLD}{'─'*50}{RESET}")
    print(f"  {CYAN}[1]{RESET}  🔍  Scanner réseau")
    print(f"  {CYAN}[2]{RESET}  💻  Informations système")
    print(f"  {CYAN}[3]{RESET}  🎫  Gestionnaire d'incidents")
    print(f"  {CYAN}[4]{RESET}  📊  Générer un rapport")
    print(f"  {CYAN}[5]{RESET}  📋  Voir les incidents ouverts")
    print(f"  {RED}[0]{RESET}  ❌  Quitter")
    print(f"{BOLD}{'─'*50}{RESET}")


def main():
    scanner  = NetworkScanner()
    sysinfo  = SystemInfo()
    incidents = IncidentLogger()
    reporter  = Reporter(incidents, sysinfo)

    while True:
        clear()
        banner()
        menu()

        choice = input(f"\n{BOLD}  Votre choix : {RESET}").strip()

        if choice == "1":
            clear()
            print(f"\n{CYAN}{BOLD}=== SCANNER RÉSEAU ==={RESET}\n")
            target = input("  Adresse IP ou plage (ex: 192.168.1.1 ou 192.168.1.0/24) : ").strip()
            if target:
                scanner.run(target)
            input(f"\n{DIM}  Appuyez sur Entrée pour continuer...{RESET}")

        elif choice == "2":
            clear()
            print(f"\n{CYAN}{BOLD}=== INFORMATIONS SYSTÈME ==={RESET}\n")
            sysinfo.display()
            input(f"\n{DIM}  Appuyez sur Entrée pour continuer...{RESET}")

        elif choice == "3":
            clear()
            incident_menu(incidents)

        elif choice == "4":
            clear()
            print(f"\n{CYAN}{BOLD}=== GÉNÉRATION DE RAPPORT ==={RESET}\n")
            path = reporter.generate()
            print(f"\n{GREEN}  ✔ Rapport généré : {path}{RESET}")
            input(f"\n{DIM}  Appuyez sur Entrée pour continuer...{RESET}")

        elif choice == "5":
            clear()
            print(f"\n{CYAN}{BOLD}=== INCIDENTS OUVERTS ==={RESET}\n")
            incidents.list_open()
            input(f"\n{DIM}  Appuyez sur Entrée pour continuer...{RESET}")

        elif choice == "0":
            print(f"\n{GREEN}  Bye ! 👋{RESET}\n")
            sys.exit(0)

        else:
            print(f"\n{RED}  Choix invalide.{RESET}")


def incident_menu(incidents):
    print(f"\n{CYAN}{BOLD}=== GESTIONNAIRE D'INCIDENTS ==={RESET}\n")
    print(f"  {CYAN}[1]{RESET}  Créer un incident")
    print(f"  {CYAN}[2]{RESET}  Voir tous les incidents")
    print(f"  {CYAN}[3]{RESET}  Clôturer un incident")
    print(f"  {CYAN}[0]{RESET}  Retour\n")

    choice = input(f"{BOLD}  Votre choix : {RESET}").strip()

    if choice == "1":
        print(f"\n{BOLD}  Nouveau ticket{RESET}")
        titre      = input("  Titre           : ").strip()
        categorie  = input("  Catégorie (HW/SW/NET/AD/M365) : ").strip().upper()
        priorite   = input("  Priorité (1=Basse 2=Moyenne 3=Haute) : ").strip()
        desc       = input("  Description     : ").strip()
        utilisateur = input("  Utilisateur concerné : ").strip()
        if titre:
            ticket_id = incidents.create(titre, categorie, priorite, desc, utilisateur)
            print(f"\n{GREEN}  ✔ Ticket #{ticket_id} créé avec succès.{RESET}")

    elif choice == "2":
        incidents.list_all()

    elif choice == "3":
        incidents.list_open()
        tid = input(f"\n  ID du ticket à clôturer : ").strip()
        resolution = input("  Note de résolution : ").strip()
        if tid:
            incidents.close(tid, resolution)

    input(f"\n{DIM}  Appuyez sur Entrée pour continuer...{RESET}")


if __name__ == "__main__":
    main()
