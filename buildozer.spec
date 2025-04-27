[app]
# Podstawowe informacje o aplikacji
title = FarmLandDemo
package.name = farmlanddemo
package.domain = gemanout.fld
source.dir = .
source.include_exts = py,png,jpg,kv,atlas # Zostaw kv/atlas jeśli ich używasz, inaczej możesz usunąć
version = 1.0

# Wymagania Python i przepisy python-for-android
# Usuwamy sdl2_*, ponieważ przepis pygame sam nimi zarządza.
# hostpython3 jest ważny dla procesu budowania.
requirements = python3,pygame==2.5.0

# Uprawnienia Androida
android.permissions = INTERNET

# ===>>> ZMIENIONE/DODANE USTAWIENIA ANDROIDA <<<===

# Minimalny poziom API Androida, na którym aplikacja będzie działać
android.minapi = 21 # Popularny wybór zapewniający szeroką kompatybilność

# Docelowy poziom API Androida (ważne dla Google Play, musi być aktualny)
# Używamy wartości z Twojego android.api, zakładając, że to był cel
android.target = 33 # Użyj 33 lub nowszego zgodnie z wymaganiami Google Play

# Architektury do zbudowania (arm64-v8a jest standardem dla nowych urządzeń)
android.archs = arm64-v8a

# Wersja Android NDK (Native Development Kit) - 25b jest dobrym wyborem
android.ndk_version = 25b

# Wersja Android Build Tools - KLUCZOWE DLA NAPRAWY BŁĘDU AIDL
android.build_tools_version = 34.0.0 # Użyj stabilnej, nowszej wersji

# ===>>> USUNIĘTE USTAWIENIA <<<===
# android.api = 33 # Zastąpione przez android.minapi i android.target
# android.sdk_version = 34 # Nie jest to standardowe ustawienie, używamy build_tools_version
# android.ndk_path = ~/.buildozer/android/platform/android-ndk # Niepotrzebne, Buildozer zarządza tym
# android.sdk_path = ~/.buildozer/android/platform/android-sdk # Niepotrzebne, Buildozer zarządza tym

# (Opcjonalnie) Orientacja ekranu (np. landscape, portrait, sensorLandscape)
orientation = landscape

# (Opcjonalnie) Czy aplikacja ma działać w trybie pełnoekranowym (0 = nie, 1 = tak)
fullscreen = 0

# (Opcjonalnie, jeśli są problemy) Możesz spróbować wskazać konkretny branch p4a
# p4a.branch = master # lub develop
