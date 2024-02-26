# DroidX-UI OTA repo
In order for a device to be officially supported by droidx, OTA information needs to be added.
Please refer to the following "Readme" to get started

## 1. Introduction ##
In order for a device to be OTA compliant, there are a few things to know.

### 1.1 JSON structure ###
```
{
  "response": [
    {
        "maintainer": "Name (nickname)",
        "oem": "OEM",
        "device": "Device Name",
        "filename": "droidx-2.x-<date>-<device codename>-v<crversion>.zip",
        "download": "https://sourceforge.net/projects/droidxui-releases/files/*.zip/download",
        "timestamp": 0000000000,
        "sha256": "abcdefg123456",
        "size": 123456789,
        "forum": "https://forum link", #(mandatory)
        "gapps": "https://gapps link", #(mandatory)
        "telegram": "https://telegram link",
    }
  ]
}
```

### 1.2 changelog.txt structure ### 
```
Highlights & Device Specific Changes:
Device: Device name (<device codename>)
Device maintainer: Name (nickname)

===== <date> =====
- change 1
- change 2
- change 3
```
