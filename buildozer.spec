[app]

title = Gallery Permission App

package.name = gallerypermission

package.domain = org.example

source.dir = .

source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait

fullscreen = 0

android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO

android.api = 35

android.minapi = 23

android.archs = arm64-v8a

android.accept_sdk_license = True

[buildozer]

log_level = 2

warn_on_root = 
