<p align="center">
  <img src="https://raw.githubusercontent.com/DroidX-UI-Devices/vendor_droidxOTA/14/assets/banners/latest.png" />
</p>


# Official Devices

This is our repo where stuff related to our OTA config and official devices is stored.

You also need to use this to apply for official maintainership for your device.

### 1. How to apply?

You must fulfill the following requirements before applying:

- [List of official devices](docs/devices.md)

- [Device stability requirements](docs/device_requirements.md)

- [Maintainer requirements](docs/maintainer_requirements.md)

- [Maintainers' code of conduct](docs/maintainers_code_of_conduct.md)

You must be aware that just fulfilling these requirements doesn't necessarily mean that you're going to be accepted. We will also consider some other points if necessary, like experience or how your behavior is towards other people (users or otherwise), and even with some technical stuff.

- If you agree with everything, please fill this [Official maintainership form](https://github.com/DroidX-UI-Devices/vendor_droidxOTA/issues/new/choose)


### JSON structure ###
```
{
  "response": [
                {
                        "maintainer": "''",
                        "oem": "''",
                        "device": "''",
                        "version": "'$version'",
                        "filename": "'$filename'",
                        "download": "https://sourceforge.net/projects/droidxui-releases/files/'$1'/'$3'/download",
                        "timestamp": '$timestamp',
                        "md5": "'$md5'",
                        "sha256": "'$sha256'",
                        "size": '$size',
                        "version": "'$version'",
                        "buildtype": "''",
                        "forum": "''",
                        "telegram": "''"
    }
  ]
}
