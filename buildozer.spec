[app]
title = SARA
package.name = saraassistant
package.domain = org.sara
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy==2.2.1,urllib3,requests,certifi
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.allow_backup = True
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
