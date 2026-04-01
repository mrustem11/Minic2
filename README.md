# 🚩 Red Team Ops: HTTP C2 & OpSec Monitor

Bu layihə sadə bir **C2 (Command & Control)** infrastrukturu və hücumçunun öz serverini qoruması üçün **OpSec** monitorinq alətindən ibarətdir.

---

## 🛠️ Alətlər

### 1. ⚡ Mini C2 Framework
* **agent.py**: Hədəf sistemdə işləyir, hər 5 saniyədən bir serverdən əmr soruşur.
* **server.py**: Flask üzərində qurulub, hücumçuya interaktiv əmr vermək imkanı yaradır.

### 2. 🛡️ OpSec: Brute-Force Detector
* **dedektor.py**: Serverin giriş loglarını analiz edir.
* **Məntiq**: 3+ uğursuz cəhddən sonra gələn uğurlu girişi ("Pattern") aşkar edir.

---

## 🚀 İşə Salma Qaydası

1. Serveri aktivləşdirin:
   `python server.py`
2. Agenti hədəf maşında başladın:
   `python agent.py`
3. Log monitorinqi işə salın:
   `python dedektor.py`

---

## ⚠️ Disclaimer
Yalnız təhsil məqsədlidir.
