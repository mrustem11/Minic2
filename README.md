
#  MiniC2: HTTP Command & Control Framework

Bu layihə, Flask bazasında qurulmuş sadə bir **C2 (Command & Control)** infrastrukturudur. Hücumçu (Server) və hədəf sistem (Agent) arasında HTTP protokolu üzərindən interaktiv əmr icrasını təmin edir.

---

##  Komponentlər

### 1.  Server (server.py)
Flask serveri rolunu oynayır. Terminal vasitəsilə istifadəçidən əmrlər qəbul edir və hədəf sistemdən gələn nəticələri çap edir.
* **Port:** 5000
* **Endpoints:** `/get_command` (GET), `/send_result` (POST)

### 2.  Agent (agent.py)
Hədəf maşında arxa planda işləyən skriptdir. 
* **İşləmə mexanizmi:** Hər 5 saniyədən bir serverə sorğu ataraq yeni əmr olub-olmadığını yoxlayır.
* **İcra:** `subprocess` kitabxanası vasitəsilə sistem əmrlərini icra edir və nəticəni serverə geri göndərir.

---

##  Quraşdırılma və İstifadə

### 1. Tələblər
Sisteminizdə Python-un quraşdırıldığından və lazımi kitabxanaların olduğundan əmin olun:
```bash
pip install flask requests
```

### 2. İşə salma qaydası

1. **Serveri başladın:**
   ```bash
   python server.py
   ```
   *Server işə düşdükdən sonra sizdən terminalda əmr gözləyəcək.*

2. **Agenti başladın (Hədəf sistemdə):**
   ```bash
   python agent.py
   ```

3. **İdarəetmə:**
   * Server terminalında `whoami`, `dir` və ya `ls` kimi əmrlər daxil edin.
   * Agent həmin əmri götürüb icra edəcək və nəticəni serverin ekranına qaytaracaq.

---

##  Texniki Axın (Workflow)
1. **Agent** -> HTTP GET sorğusu göndərir.
2. **Server** -> Terminalda input gözləyir və əmri Agentə ötürür.
3. **Agent** -> Əmri Shell üzərində işlədir.
4. **Agent** -> Nəticəni HTTP POST vasitəsilə geri qaytarır.
5. **Server** -> Nəticəni terminalda vizuallaşdırır.

---

##  Xəbərdarlıq (Disclaimer)
Bu layihə yalnız **təhsil və kibertəhlükəsizlik araşdırmaları** üçün hazırlanmışdır. İcazəsiz sistemlərdə istifadə edilməsi qanunsuz ola bilər. Müəllif məsuliyyət daşımır.
```
