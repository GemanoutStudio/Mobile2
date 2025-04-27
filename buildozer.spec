[app]
title = FarmLandDemo
package.name = farmlanddemo
package.domain = gemanout.fld
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3, pygame==2.5.0, sdl2_ttf, sdl2_image, sdl2_mixer
android.permissions = INTERNET
android.api = 33
android.ndk = 25b
android.sdk_version = 34
android.archs = arm64-v8a
android.ndk_path = ~/.buildozer/android/platform/android-ndk
android.sdk_path = ~/.buildozer/android/platform/android-sdk