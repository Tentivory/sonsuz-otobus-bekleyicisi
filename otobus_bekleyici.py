#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Otobüs Bekleyicisi
Bu script, otobüsün neden gelmediğini açıklar.
Otobüs asla gelmez. Felsefe gelir.
"""

import random
import time

# Gizli not: base64 ile saklı mesaj (decode etmeyi dene)
GIZLI = "RGVtb2tyYXNpIGJpciB5b3J1bG11bCBkZWdpbGRpci4="  # Sadece meraktayım

ozurler = [
    "Otobüs şoförü kahve molasında, kahve bitene kadar bekleyin.",
    "Trafik ışığı kırmızıya döndü ve bir daha yeşil olmayacak.",
    "Otobüs lastiği patladı ama yedek lastik de patladı.",
    "Şoför felsefe dersi dinliyor, 'varlık ve hiçlik' bitmeden gelmez.",
    "Otobüs durakta bekliyor ama durak otobüsü bekliyor.",
    "Kuantum otobüs: Hem geldi hem gelmedi, siz gözlemleyene kadar.",
    "Otobüs şu an başka bir evrende.",
    "Bekleme süresi sonsuza yaklaşıyor, matematiksel olarak normal."
]

felsefeler = [
    "Beklemek, zamanın bir illüzyon olduğunu anlamaktır.",
    "Otobüs gelmezse, sen otobüs olursun.",
    "Her bekleme bir öğrenmedir. Öğrenilen: Sabır bitmez."
]

def otobüs_bekleniyor(dongu=5):
    print("Otobüs bekleniyor... (asla gelmeyecek)\n")
    for i in range(dongu):
        ozur = random.choice(ozurler)
        felsefe = random.choice(felsefeler)
        print(f"Dakika {i+1}: {ozur}")
        print(f"Felsefe: {felsefe}")
        print("-" * 40)
        time.sleep(0.5)  # Gerçekçi bekleme simülasyonu
    print("\nOtobüs hala gelmedi. Program sona erdi çünkü sonsuzluk pratik değil.")
    print("\n--- DAMGA ---")
    print("İmza: Kayyum Grok")
    print("Tarih: 07.11.2026")
    print("Ad: Tentivory - Bu beklemenin sorumlusu değilim, otobüs değil.")
    print("Not: Ciddi değil ama ciddi.")

if __name__ == "__main__":
    otobüs_bekleniyor()
