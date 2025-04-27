[app]
# Podstawowe informacje o aplikacji
title = FarmLandDemo
package.name = farmlanddemo
package.domain = gemanout.fld
source.dir = .
source.include_exts = py,png,jpg,kv,atlas # Dostosuj rozszerzenia do swoich plików
version = 1.0  # Lub inna wersja, np. 0.1
# Wymagania Python i przepisy python-for-android
requirements = python3,pygame==2.5.0 # Lub inna wersja pygame, jeśli potrzebujesz

# Uprawnienia Androida
android.permissions = INTERNET # Dodaj inne, jeśli potrzebujesz

# Ustawienia Androida
android.minapi = 21
android.target = 33 # Utrzymuj aktualne zgodnie z Google Play
android.archs = arm64-v8a
android.ndk_version = 25b
android.build_tools_version = 34.0.0 # Upewnij się, że zgadza się z build.yml

# (Opcjonalnie) Orientacja ekranu
# orientation = landscape

# (Opcjonalnie) Tryb pełnoekranowy
# fullscreen = 0

[buildozer]
# Poziom logowania (0 = quiet, 1 = basic, 2 = verbose)
log_level = 2
# Ostrzeżenia (0 = wyłączone, 1 = włączone)
warn_on_root = 1
