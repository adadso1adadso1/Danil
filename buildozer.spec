[app]
title = Lada XRAY
package.name = ladaapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 1

# Отключаем лишние архитектуры для стабильности
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

# Настройки для предотвращения ошибок с памятью
android.ndk_api = 21
android.api = 30
android.minapi = 21

# Включаем логи, если что-то пойдет не так
log_level = 2
