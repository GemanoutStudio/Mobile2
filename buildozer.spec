[app]
# Podstawowe informacje o aplikacji
title = FarmLandDemo
package.name = farmlanddemo
package.domain = gemanout.fld
source.dir = .
source.include_exts = py,png,jpg,kv,atlas # Dostosuj rozszerzenia do swoich plików

# Wersja aplikacji - MUSI być ustawiona
version = 1.0 # Ustaw swoją wersję

# Wymagania Python i przepisy python-for-android
# Uwaga: pygame==2.5.0 może wymagać nowszego NDK niż r25c, ale na razie zostawmy.
# Jeśli będą problemy z kompilacją Pygame, można spróbować z nowszym NDK (np. r26d) lub starszym Pygame.
requirements = python3,pygame==2.5.0

# Uprawnienia Androida
android.permissions = INTERNET # Dodaj inne, jeśli potrzebujesz

# Ustawienia Androida
android.minapi = 21
android.target = 33             # Musi pasować do ANDROID_PLATFORM w build.yml
android.archs = arm64-v8a
android.ndk_version = r25c      # Musi pasować do ANDROID_NDK w build.yml (zmieniono z 25b)
android.build_tools_version = 34.0.0 # Musi pasować do ANDROID_BUILD_TOOLS w build.yml

# Orientacja ekranu (opcjonalnie)
# orientation = landscape

# Tryb pełnoekranowy (opcjonalnie)
# fullscreen = 0

# Usuń te linie, jeśli istnieją, aby polegać na zmiennych środowiskowych:
# android.sdk_path = ...
# android.ndk_path = ...

[buildozer]
# Poziom logowania (0 = quiet, 1 = basic, 2 = verbose)
log_level = 2
# Ostrzeżenia (0 = wyłączone, 1 = włączone)
warn_on_root = 1
