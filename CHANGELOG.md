# Changelog

All notable changes to this project will be documented in this file.

## [4.0.0] - 2025-07-03

### 🚀 Features

- [**breaking**] Merge branch 'new-pins-enum' ([36af531](36af53185c6f385b2d024f28c551fe5fa2680c5e))

- [**breaking**] Add Ruff as linter/formatter ([cbe1b0c](cbe1b0c9a5c5ec8ddd708e7c4d2baba848b22eb0))

- Add Touchberry Pi V1 mapping ([5c295e9](5c295e96395c72345bb63cbe6e94ea36faa9f8ba))

- Add old mapping for GateBerry V9 ([ec7ce90](ec7ce90af7b3440ebd2e01e7c1d72ba958d5c0a6))

- Add deprecation warning for RPIPLC, instead use RPIPLC_CPU ([f2d35ae](f2d35ae9715694ab69e39a1dffb3cc52ab46f4fc))

- Add GateBerry V9 click mapping ([3fcd60c](3fcd60c5503562c0e39063ba64e2d8d3c610ef59))


### 🐛 Bug Fixes

- Remove RPIPLC inside the library ([0c13638](0c136387b349f16022474c38ebc3adad63c65c01))

- Show available versions when writting bad PLC version ([6419d87](6419d8720a1c076412ae37b4d9fbca46dfb568e8))

- Don't emit deprecation warning when calling digital_write with bool ([e957bfb](e957bfbd327e94d499550f9fdb5cc23abac56e6a))

- Don't initialize RPIPLCClass if pip is being called ([24b6d50](24b6d50cf3c725b7de06937436d41c370b1cdfe4))

- Add RPIPLC V6 19R model ([ee9a76e](ee9a76e97b550b05b4b628a0014ddbc4e85bd2a9))

- Make an "all" package ([b4f0cfc](b4f0cfca8c1fb438e73d24fe6b956724ccb23c5a))

- Remove initExpandedGPIOV2 ([f4bc045](f4bc045e4ac1073aa961ebde1d58a187f5d0c6ab))

- Add prompt before uninstalling older python3-librpiplc ([484dd66](484dd66f17c227c894b1c90de62a451ac4ec5074))

- Update README with apt package, build instructions and general fixes ([4604340](46043407f965303df81912095a03386dee7e554f))

- Add TouchBerry Pi V1 ADS1015 initialization ([25829d8](25829d8154dc109574a19478372f786237971173))

- Check that librpiplc_path exists before checking if is owned by dpkg ([08c6ed1](08c6ed1a97abb9279538ac591a2ca045e86d0869))

- Ensure that string returned by find_library is not None or an empty string ([b06658a](b06658a58ca2e500db042a10aa0ac9a041c6cc25))

- Fix NoReset argtypes and restype + Do not add the third LTC2309 when using a RPIPLC ([89a1cce](89a1cce8741f1d45e1b79ffd01e595b3183c6112))

- Fix type checking errors ([91017cd](91017cd6bad959e85cb625fec57032a9feda7f8c))


### 💼 Other

- Update clean_debian target ([2f7e7be](2f7e7be31caaf21b1aa53f4a29a4345cb037e109))

- Make python3-librpiplc a Debian package ([48fd426](48fd426cbc5f25311d294cf48e8a7eecf28c191b))

- Revert 389b516: Use the find_library function inside ctypes ([f0e8381](f0e838164fccccc2819dd6b4919fecef29064832))

- Try to load the C library from multiple places

Useful if ldconfig did not (or cannot) run ([389b516](389b516776cfe37e642ac008b6bcebd158d6e061))

- GateBerry V9 mapping ([766aace](766aace5d45e9de71a437971bba6c10fd7f3d595))

- Unpair major library version from the C library

Since the Python library will be retro-compatible with librpiplc 3.0.0, it is no longer necessary to make the major version the same. ([9b32d23](9b32d234ddd167dd36681988638268b005af0a0e))

- Change librpiplc limiting version to 4.0.0

Although the official version of this library will be 4.0.0 (a major bump), it's only to synchronize it with the major versions of librpiplc. These versions should be compatible with the 3.X.X libraries. ([21b750f](21b750fbb241fe92bafa197d9feeb1ed7177b1b1))

- Add support for deinit without restarting peripherals ([ac398cd](ac398cd282b8bf2cb54494ee142dfe194bccb752))

- Add with_init method compatible with the "with" statement ([a5539a4](a5539a495e39026d19a2bc750a9d55b0888497e7))

- Add deprecation warning when passing an int to digital_write + Accept bool as alternative ([f05d5b9](f05d5b984604217647115cf7c522d5f38dbf14f6))

- Keep _c_struct as an attribute class

After initializing, the arrays were being deallocated. ctypes doesn't keep track of them, so they must be referenced by someone to not get yeeted by the garbage collector ([d099b81](d099b81a1f14d029773801dc89120029e912a131))

- Count as deinitialized if deinitExpandedGPIO returns 2 (already deinitialized) ([d5b671b](d5b671bbc483706b2e43cc1afa17942d6dddf2d9))

- Add compatibility with librpiplc versions older than 3.1.0 ([cb499b5](cb499b5fe269fc120df3788d174eb098e08bd970))

- Update README + Linting + Remove types file ([df00e36](df00e36a19aa5187bd46c2b7f9a660c3f241e011))

- Thin dict wrapper to use a custom exception when using an invalid pin + Change types module name (circular import) ([84d20f6](84d20f65a721df53dcf6602bc0f7b27d9b13424d))

- Rename and separate into modules + Type hints ([8872b32](8872b32af0f54a03b972ee3f30f213be1726acd4))

- Refactor code to make it more maintainable ([53df035](53df035a12a4cb3b96a1e9719e2efe34e2564d68))

- Revert "Add stub to enable dynamic linking with the new librpiplc versions"

This reverts commit 5a8bced6faacb9704da34e045d4f5250d5b5df8b. ([7f3f062](7f3f062b54679696629c1eca43ad5626b784f3d1))

- Add stub to enable dynamic linking with the new librpiplc versions ([5a8bced](5a8bced6faacb9704da34e045d4f5250d5b5df8b))


### 🚜 Refactor

- Use __about__.py to save library version ([d4441fd](d4441fd34fc7796c227037e4b2e4147afc1acd7f))


### ⚙️ Miscellaneous Tasks

- Add CHANGELOG ([5c2cf6b](5c2cf6b6110daa4a7dd8cadebcc7911c5e339d0c))

- Bump library version ([a577412](a5774121215fe96c258a817bbda6e1470d4b4c3d))


## [3.0.2] - 2024-05-27

### 💼 Other

- Add RPIPLC model ([30d54c2](30d54c2b9a7fdf1a6e2ed34dafd14ae7cc8c2ce8))


## [3.0.1] - 2024-05-20

### 💼 Other

- Add INT31 pin to Raspberry PLC V6 ([ae60050](ae60050ed2e836cbe2960602ee3da994e1b0020b))

- Return code for init + Add UPSafePi support + Bump library version ([4cec84d](4cec84dda8d569704be64ff2d4430e59f136fc78))

- Remove PWM pins (they are not present in V6) ([62c27b3](62c27b37cb2a13d4fe83a06527e2df6ab2ca2536))

- Add argument to init to forcefully restart ICs ([7a33aac](7a33aac3a0f13a1923847c5ff87886fc696f4603))

- Update README ([6881dd9](6881dd9668194edd004cd422d2ee42fa9bf7ce78))


## [3.0.0] - 2024-04-24

### 🐛 Bug Fixes

- Fix tab/space indentation in examples ([537a851](537a851b9186a9015713c840df6eb1507ec48638))


## [2.0.0] - 2022-08-16

### 💼 Other

- Models.py rpi plc v4 ([b0e1d6c](b0e1d6c7bd009070aa39a2253bbed219acde2434))


## [1.0.0] - 2022-08-16

### 💼 Other

- Models.py rpi plc v3 ([53a8172](53a8172807cbdfc6093442bdce094a33f58f9fd6))

- Models.py rpi plc v4 ([d733475](d733475e5630bbbbe2b4e7cd635a1f98edfd088d))

- Models.py rpi plc v3 ([2286fee](2286fee47eb6ca0dbd01e9ea35fb1adbe53be851))

- Update models.py ([7819601](7819601466089f9a88d8b2d66b11e5f15f6d3f29))

- Update models.py

Models.py updated with the new i2c adresses of the RPI PLC v4 version. ([3f7d6dd](3f7d6dd5fc7bb7ce3b8c369689e505e017313553))

- Update README.md

Functions examples updated. ([76313d7](76313d74e8338f599f14cd781e1c8f32e6bea590))

- Update README.md ([960f83c](960f83c7590b991d8fa3953d14ef74c77645e7fe))

- Update README.md ([b2d2f58](b2d2f5852e89ede60cefafb96fe4129c1f637096))

- Update README.md ([7bcaf2c](7bcaf2ca9e403b0a68902af061a023a041df5251))

- Update README.md ([75a49c6](75a49c6026ed30d5c832ddbeb875d0a8f9c99882))

- Update README.md ([c91559a](c91559af06aba3293ac2eddd009cc5d0949ef9b3))

- Update models.py ([9aea84f](9aea84fc29af5a24cbac0cc6e322da87e14786d4))

- Update README.md ([fd93ef8](fd93ef8ec5d68cfb06b2bb4030fd4b6b2403558c))

- First commit ([f9e6f99](f9e6f999b95964ea86bf75384b8d1ceb88e3d5bb))


<!-- generated by git-cliff -->
