# 🖥️ IT Helpdesk Toolkit

> Outil Python de support IT pour la gestion d'incidents, le diagnostic système et le scan réseau — conçu pour les environnements Helpdesk N1/N2/N3.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## ✨ Fonctionnalités

| Module | Description |
|--------|-------------|
| 🔍 **Scanner réseau** | Ping sweep + scan des ports courants (RDP, SSH, LDAP, SMB…) |
| 💻 **Informations système** | OS, CPU, RAM, disques, interfaces réseau en temps réel |
| 🎫 **Gestionnaire d'incidents** | Création, suivi et clôture de tickets (style GLPI) |
| 📊 **Rapport HTML** | Génération d'un rapport complet système + incidents |

---

## 📸 Aperçu

```
 ██╗████████╗    ██╗  ██╗███████╗██╗     ██████╗ ██████╗ ███████╗███████╗██╗  ██╗
 ██║╚══██╔══╝    ██║  ██║██╔════╝██║     ██╔══██╗██╔══██╗██╔════╝██╔════╝██║ ██╔╝
 ...

  [1]  🔍  Scanner réseau
  [2]  💻  Informations système
  [3]  🎫  Gestionnaire d'incidents
  [4]  📊  Générer un rapport
  [5]  📋  Voir les incidents ouverts
  [0]  ❌  Quitter
```

---

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/justindoglo/it-helpdesk-toolkit.git
cd it-helpdesk-toolkit

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'outil
python main.py
```

> **Windows** : Lancer en tant qu'administrateur pour le scan réseau complet.  
> **Linux/macOS** : `sudo python main.py` recommandé pour les pings ICMP.

---

## 📁 Structure du projet

```
it-helpdesk-toolkit/
│
├── main.py                    # Point d'entrée principal
├── requirements.txt           # Dépendances Python
├── README.md
│
├── modules/
│   ├── network_scanner.py     # Scan réseau (ping + ports)
│   ├── system_info.py         # Informations système
│   ├── incident_logger.py     # Gestion des tickets
│   └── reporter.py            # Génération de rapport HTML
│
├── logs/
│   └── incidents.json         # Base de données des tickets (auto-créée)
│
└── reports/
    └── rapport_YYYYMMDD.html  # Rapports générés
```

---

## 🎫 Gestionnaire d'incidents

L'outil intègre un système de ticketing simplifié compatible avec les workflows GLPI :

- **Catégories** : HW (matériel), SW (logiciel), NET (réseau), AD (Active Directory), M365 (Microsoft 365)
- **Priorités** : Basse / Moyenne / Haute
- **Statuts** : OUVERT → CLÔTURÉ
- **Stockage** : fichier JSON local (`logs/incidents.json`)

---

## 🔍 Scanner réseau

Ports détectés automatiquement :

| Port | Service |
|------|---------|
| 22 | SSH |
| 80 / 443 | HTTP / HTTPS |
| 135 | RPC |
| 389 / 636 | LDAP / LDAPS (Active Directory) |
| 445 | SMB |
| 3389 | RDP (Bureau à distance) |
| 5985 | WinRM |
| + 10 autres | … |

---

## 📊 Rapport HTML

Le rapport généré contient :
- Résumé des incidents (total, ouverts, clôturés)
- Statistiques par catégorie
- Tableau complet des tickets
- Informations OS, CPU, RAM, disques, réseau

---

## 🛠️ Technologies

- **Python 3** — langage principal
- **psutil** — collecte des métriques système
- **socket / subprocess** — scan réseau
- **concurrent.futures** — scan multi-threadé
- **JSON** — stockage des incidents
- **HTML/CSS** — rapport visuel

---

## 👤 Auteur

**DOGLO Koami Justin**  
Technicien Support IT — Helpdesk N1/N2/N3  
📍 Meknès, Maroc  
📧 doglojustin5@gmail.com  
🔗 [linkedin.com/in/justindoglo](https://linkedin.com/in/justindoglo)  
🌐 [justindoglo.github.io](https://justindoglo.github.io)

---

## 📄 Licence

MIT License — libre d'utilisation et de modification.
