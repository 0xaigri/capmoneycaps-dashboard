# 📈 CAPS Dashboard

Ce projet permet de suivre l’évolution quotidienne du nombre total de **CAPS** depuis [cap.app](https://cap.app/caps).  

Les données sont collectées automatiquement avec **Playwright** (script `TestCap.py`) puis sauvegardées dans un fichier CSV (`caps_history.csv`).  
Une application **Streamlit** (`app.py`) permet ensuite de visualiser cette évolution dans un graphique interactif.  

---

## 📂 Contenu du projet  

- `TestCap.py` → script Python pour collecter les données (à lancer chaque jour ou via tâche planifiée)  
- `caps_history.csv` → historique des données (rempli par le script)  
- `app.py` → application Streamlit pour afficher la courbe d’évolution  
- `requirements.txt` → dépendances nécessaires (streamlit, pandas, matplotlib)  

---

## ⚙️ Installation locale  

1. Cloner le repo :  
   ```bash
   git clone https://github.com/ton-compte/caps-dashboard.git
   cd caps-dashboard
   ```

2. Installer les dépendances :  
   ```bash
   pip install -r requirements.txt
   ```

3. Lancer le script de collecte (remplit `caps_history.csv`) :  
   ```bash
   python TestCap.py
   ```

4. Lancer l’application Streamlit :  
   ```bash
   streamlit run app.py
   ```

👉 L’app sera accessible sur [http://localhost:8501](http://localhost:8501)  

---

## 🚀 Déploiement en ligne  

1. Pousser le projet sur **GitHub** (inclure `caps_history.csv` et `requirements.txt`).  
2. Aller sur [Streamlit Cloud](https://streamlit.io/cloud) → **New app**.  
3. Sélectionner ton repo et `app.py`.  
4. Streamlit installe automatiquement les dépendances et déploie ton app.  

Ton dashboard sera disponible via une URL du type :  
```
https://ton-projet.streamlit.app
```

---

## ✨ Exemple de rendu  

- 📊 Une courbe montrant l’évolution quotidienne du total de CAPS  
- 🗓️ Chaque point correspond à une exécution de `TestCap.py`  
- 🧾 Les données sont historisées dans `caps_history.csv`  
