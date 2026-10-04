[app]

title = Kalkulator Serbaguna
package.name = kalkulatorserbaguna
package.domain = org.kalkulator

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

requirements = hostpython3==3.12.9,python3==3.12.9,kivy==2.3.1,certifi,charset-normalizer==3.4.9
orientation = portrait
fullscreen = 0

android.permissions = android.permission.INTERNET

android.archs = arm64-v8a

android.accept_sdk_license = True

android.debug_artifact = apk

p4a.branch = develop
p4a.commit = d2ee8c5
[buildozer]

log_level = 2
warn_on_root = 1
