
[app]

title = البقاء للأقوى YAMEN
package.name = yamen
package.domain = org.yamen.app

source.dir = .
source.include_exts = py,txt,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 35
android.minapi = 23
android.ndk = 28c
android.archs = armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 0
