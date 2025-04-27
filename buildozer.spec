name: Build Python/Pygame Android App

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build-android:
    runs-on: ubuntu-latest

    steps:
      # Krok 1: Pobranie kodu repozytorium
      - name: Checkout repository
        uses: actions/checkout@v4

      # Krok 2: Konfiguracja środowiska Python
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10' # Użyj wersji zgodnej z Twoim projektem

      # Krok 3: Konfiguracja Javy (JDK)
      - name: Set up Java Development Kit (JDK)
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '11' # JDK 11 lub 17 są zalecane

      # Krok 4: Instalacja podstawowych zależności systemowych
      # (Usunięto niektóre specyficzne dla SDL2, zakładając, że p4a je dostarczy,
      # ale zostawiono kluczowe jak build-essential, git, zip, etc.)
      - name: Install base system dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y \
            git \
            zip \
            unzip \
            build-essential \
            python3-dev \
            libffi-dev \
            libssl-dev \
            liblzma-dev \
            libbz2-dev \
            libncursesw5-dev \
            libgdbm-compat-dev \
            libsqlite3-dev \
            libreadline-dev \
            uuid-dev \
            autoconf \
            libtool \
            pkg-config \
            ccache

      # ===>>> NOWE KROKI: Instalacja Android SDK <<<===
      - name: Set up Android SDK tools
        uses: android-actions/setup-android@v3.0.0 # Użyj dedykowanej akcji

      - name: Install Android SDK Components
        run: |
          echo "y" | $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager --licenses > /dev/null # Zaakceptuj licencje
          echo "Installing SDK components..."
          # Zainstaluj platform-tools, platformę (API 33) i build-tools (34.0.0)
          # Upewnij się, że wersje zgadzają się z buildozer.spec (android.target=33, android.build_tools_version=34.0.0)
          $ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager "platform-tools" "platforms;android-33" "build-tools;34.0.0"
          echo "SDK components installed."

      # Opcjonalny krok weryfikacji AIDL
      - name: Verify AIDL tool presence
        run: |
          echo "Verifying aidl..."
          AIDL_PATH="$ANDROID_HOME/build-tools/34.0.0/aidl"
          if [ -f "$AIDL_PATH" ]; then
            echo "AIDL found at $AIDL_PATH"
            ls -l "$AIDL_PATH"
            # Sprawdź, czy jest wykonywalny
            if [ -x "$AIDL_PATH" ]; then
              echo "AIDL is executable."
            else
              echo "Warning: AIDL found but may not be executable."
              chmod +x "$AIDL_PATH" # Spróbuj nadać uprawnienia
            fi
          else
            echo "Error: AIDL not found at expected path $AIDL_PATH after installation!"
            echo "Listing contents of $ANDROID_HOME/build-tools/34.0.0/ :"
            ls -la "$ANDROID_HOME/build-tools/34.0.0/" || echo "Could not list build-tools directory."
            # Zgłoś błąd, aby workflow się zatrzymał, jeśli nadal go brakuje
            # exit 1 # Możesz odkomentować, aby zatrzymać workflow tutaj jeśli AIDL brakuje
          fi
          echo "AIDL verification finished."

      # Krok 6: Instalacja Buildozera i zależności Python
      - name: Install Python dependencies (including Buildozer)
        run: |
          python -m pip install --upgrade pip
          pip install --upgrade buildozer cython # Upewnij się, że buildozer jest aktualny
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          echo "Python dependencies installed."

      # Krok 7: Budowanie APK (wersja debug) z większą szczegółowością logów
      - name: Build debug APK with Buildozer (verbose)
        run: |
          echo "Starting Buildozer build process..."
          # Używamy -vv dla jeszcze bardziej szczegółowych logów
          # Przekazujemy też ANDROID_HOME, chociaż Buildozer powinien go wykryć z env
          export ANDROID_HOME=$ANDROID_HOME
          buildozer -vv android debug

      # Krok 8: Przesłanie zbudowanego pliku APK jako artefaktu
      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: android-apk-debug
          path: bin/*.apk
          if-no-files-found: error