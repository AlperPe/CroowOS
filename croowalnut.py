import time

class CroowalnutTabs:
    def __init__(self, psize=256):
        self.Psize = psize
        self.roots = {chr(65 + i): 65 + i for i in range(26)}
        self.havuz = [None] * psize

    def open_tab(self, root_char, tab_delta, payload):
        """Sekmeyi ara ağaçlar kurmadan doğrudan delta koordinatına mühürler."""
        root_char = root_char.upper()
        root_val = self.roots.get(root_char)
        if not root_val:
            return

        slot = (root_val + tab_delta) % self.Psize
        
        # Canlılık ve zaman değişkenleri (T_live analizi)
        birth_time = time.time()
        
        self.havuz[slot] = {
            "root": root_char,
            "delta": tab_delta,
            "content": payload,
            "birth_time": birth_time,
            "last_access": birth_time
        }
        print(f"[TAB OPEN] Kök: '{root_char}' Sekme Delta: +{tab_delta} (Slot: {slot}) mühürlendi. Boyut: Minimal.")

    def access_tab(self, root_char, tab_delta):
        """O(1) hızında sekçeye zıplar ve canlılık süresini günceller."""
        root_char = root_char.upper()
        root_val = self.roots.get(root_char)
        slot = (root_val + tab_delta) % self.Psize
        
        tab = self.havuz[slot]
        if tab and tab["delta"] == tab_delta and tab["root"] == root_char:
            tab["last_access"] = time.time()
            alive_duration = time.time() - tab["birth_time"]
            print(f"\n[JUMBER -> TAB] Sekme Açıldı: {tab['content']}")
            print(f"⏱️ Canlı Kalma Süresi: {alive_duration:.2f} saniye | Slot: {slot}")
        else:
            print("[SAPMA] Sekme bulunamadı! return eleman -> Sönümlendi.")
