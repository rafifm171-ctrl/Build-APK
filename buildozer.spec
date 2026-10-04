[app]

title = Kalkulator Serbaguna
package.name = kalkulatorserbaguna
package.domain = org.kalkulator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = hostpython3==3.12.9,python3==3.12.9,kivy==2.3.1,certifi
orientation = portrait
fullscreen = 0

android.permissions = android.permission.INTERNET

android.archs = arm64-v8a

android.accept_sdk_license = True

android.debug_artifact = apk

p4a.branch = master

[buildozer]

log_level = 2
warn_on_root = 1
