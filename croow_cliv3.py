#!/usr/bin/env python3
import sys

class CroowRuntime:
    def __init__(self, psize=256, max_roots=26):
        self.Psize = psize
        self.MAX_ROOTS = max_roots
        self.roots = {chr(65 + i): 65 + i for i in range(max_roots)}
        self.havuz = [None] * psize
        print(f"[CROOW KERNEL v0.4] Delta-Kök Saf Matris Aktif | Psize: {self.Psize}")

    def seal(self, delta_jumber, root_char, payload):
        root_char = root_char.upper()
        root_val = self.roots.get(root_char)
        if root_val is None:
            print(f"[HATA] Geçersiz Kök: '{root_char}' (A-Z arası olmalı)")
            return
        
        # Doğrudan delta_jumber ve kök koordinatı ile hedef slot
        target_slot = (root_val + delta_jumber) % self.Psize
        self.havuz[target_slot] = {
            "root": root_char,
            "delta_jumber": delta_jumber,
            "frekans": payload
        }
        print(f"[SEAL OK] Delta: {delta_jumber} | Kök: '{root_char}' -> Fiziksel Slot: {target_slot}")

    def jumber_execute(self, delta_jumber, uf_char):
        uf_char = uf_char.upper()
        selected_root = self.roots.get(uf_char)
        if not selected_root:
            print(f"[GÜVENLİK] Tanımsız Uf Sinyali: '{uf_char}'. Sönümlendi.")
            return

        target_slot = (selected_root + delta_jumber) % self.Psize
        hucre = self.havuz[target_slot]

        print(f"\n[JUMBER VEKTÖRÜ] Delta: {delta_jumber} | Uf (Kök): '{uf_char}' | Slot: {target_slot}")
        
        # Kapalı devre güvenlik ve eşleşme kontrolü
        if hucre and hucre["delta_jumber"] == delta_jumber and hucre["root"] == uf_char:
            print("Cevap Alınıyor...")
            print(f">> [PUSH -> USER] Veri Özü: {hucre['frekans']}")
        else:
            print("[SAPMA TESPİT EDİLDİ] Vektör uyuşmazlığı! return eleman -> Sönümlendi.")

def interactive_shell():
    runtime = CroowRuntime()
    print("\n--- CROOWLANG SAF DELTA-KÖK KABUĞU ---")
    print("Komutlar:")
    print("  SEAL <Delta> <Kök> <Veri>  -> Örn: SEAL 15 K \"Kuantum Paketi\"")
    print("  JUMBER <Delta> <Kök>       -> Örn: JUMBER 15 K")
    print("  EXIT                       -> Çıkış\n")

    while True:
        try:
            cmd = input("croow> ").strip().split()
            if not cmd:
                continue
            
            action = cmd[0].upper()
            if action == "EXIT":
                print("Çekirdek kapatılıyor...")
                break
            elif action == "SEAL" and len(cmd) >= 4:
                delta = int(cmd[1])
                root = cmd[2]
                payload = " ".join(cmd[3:])
                runtime.seal(delta, root, payload)
            elif action == "JUMBER" and len(cmd) == 3:
                delta = int(cmd[1])
                uf = cmd[2]
                runtime.jumber_execute(delta, uf)
            else:
                print("[HATA] Geçersiz format. Kullanım: SEAL <Delta> <Kök> <Veri> veya JUMBER <Delta> <Kök>")
        except Exception as e:
            print(f"[ÇEKİRDEK İSTİSNASI]: {e}")

if __name__ == "__main__":
    interactive_shell()
