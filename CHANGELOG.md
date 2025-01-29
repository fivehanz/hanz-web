# Changelog

## [0.20.0](https://github.com/fivehanz/hanz-web/compare/v0.19.0...v0.20.0) (2024-12-26)


### Features

* docker swarm for prod ([ef36507](https://github.com/fivehanz/hanz-web/commit/ef36507f79bf44d9cefa683a8e9627db0bc3c0f8))
* dockerimage w/ bun for uikit dist ([401a955](https://github.com/fivehanz/hanz-web/commit/401a95514d3e5cb9b11f51e1d9b8be882c4dc396))
* nginx uses proxy protocol ([5d04bcf](https://github.com/fivehanz/hanz-web/commit/5d04bcf117f4990c73ef98edffb4e2c3e9be0883))
* uikit 3.21.13; rm tailwind ([f5efd71](https://github.com/fivehanz/hanz-web/commit/f5efd71199f290683d4f3ac9f55da3ec96ce7d21))
* upgrade django to 5.1, wagtail to 6.3 ([083264e](https://github.com/fivehanz/hanz-web/commit/083264e92d11e0046cac87abc7edd16956dedce4))
* whitenoise for statics, compose refactor ([9dcb80e](https://github.com/fivehanz/hanz-web/commit/9dcb80ebcc0c9480523cf2262000813faf9a6fef))


### Bug Fixes

* alignments with uikit, projects, navbar ([0e070dc](https://github.com/fivehanz/hanz-web/commit/0e070dc7e615e6b76dae5572d790d00f3bbc1bb0))
* dbrestore pg_restore w/ permissions ([054e5c3](https://github.com/fivehanz/hanz-web/commit/054e5c39b45d9b9db6c3906c5dc3b86022ed1ccb))
* projects card w/ margin and padding ([8705536](https://github.com/fivehanz/hanz-web/commit/8705536d98a3e8454eca9dd9ed64963d231ea893))

## [0.19.0](https://github.com/fivehanz/hanz-web/compare/v0.18.0...v0.19.0) (2024-09-14)


### Features

* add plausible analytics & rm GTM ([cb62bc8](https://github.com/fivehanz/hanz-web/commit/cb62bc8586221c56ffc0f0a7e804d9c524a2dfe7))
* init celery worker, beat ([410cf3c](https://github.com/fivehanz/hanz-web/commit/410cf3c1764eff50838b25f30f31e3d5b103c43f))
* schedule dbbackup using celery ([61645ba](https://github.com/fivehanz/hanz-web/commit/61645ba694a54f57046347594a6e9c6fabcac9e2))
* working fonts family ([2d1a8be](https://github.com/fivehanz/hanz-web/commit/2d1a8be348a37dd11a94b95ef2d43ef10b0a6b34))


### Bug Fixes

* **500 IS ERROR:** CF frontend cache invalidator ([c375c66](https://github.com/fivehanz/hanz-web/commit/c375c66cee2e5b03b55ace5590e809c473945a9b))
* default auto field ([b05e449](https://github.com/fivehanz/hanz-web/commit/b05e449f887ff85895fd71f9356dfffd6fb0ec3a))
* plausible analytics load on page ([8e1432f](https://github.com/fivehanz/hanz-web/commit/8e1432f4c9095d9325633d33c9a1ecbfaea6fb32))
* prod dockerfile path ([bca044b](https://github.com/fivehanz/hanz-web/commit/bca044b962bc90634f7f59305ea6810f95a73d41))
* rm db nw, add celery depend on web, rm bridge ([75c53c9](https://github.com/fivehanz/hanz-web/commit/75c53c903badc4a72cac2c473b14b8043b4ec900))
* rm duplicate cf config ([5a757dc](https://github.com/fivehanz/hanz-web/commit/5a757dca8f7b806cbc58a1603db4a8b6ffcaaa37))
* rm duplicate config cloudflare cache ([5f7baeb](https://github.com/fivehanz/hanz-web/commit/5f7baeb3f30ebc26f1ca7d4a2ed2e1fc44347b01))

## [0.18.0](https://github.com/fivehanz/hanz-web/compare/v0.17.0...v0.18.0) (2024-08-04)


### Features

* automatic static collect ([42d8a9a](https://github.com/fivehanz/hanz-web/commit/42d8a9a0983587515a1aa7d5c74da451b2c85750))


### Bug Fixes

* **entrypoint:** conditionals ([37b37ce](https://github.com/fivehanz/hanz-web/commit/37b37ceb33a9becd558648335089c2eaa43861aa))
* static build release ([1e0ad8e](https://github.com/fivehanz/hanz-web/commit/1e0ad8e7a00bb66eb645c4e4ea1cc66c40edc09f))
* static files ([c07da5e](https://github.com/fivehanz/hanz-web/commit/c07da5e79ce03ae9880313a1c543664d6f2f5ff9))
* **statics:** multiple commands ([0211c6d](https://github.com/fivehanz/hanz-web/commit/0211c6d6f31098777233d8b3b6413df138fbe870))

## [0.17.0](https://github.com/fivehanz/hanz-web/compare/v0.16.0...v0.17.0) (2024-08-04)


### Features

* move CI to docker based ([40bbbab](https://github.com/fivehanz/hanz-web/commit/40bbbab7f8393365d80ebdda77d585c6f8c0e544))
* move to granian == 1.5.2 ([242078c](https://github.com/fivehanz/hanz-web/commit/242078ca19f7e7efff9ec9b2150124b820c0a0b1))
* move to poetry from pipenv ([6ebb76b](https://github.com/fivehanz/hanz-web/commit/6ebb76ba923a0c15b645d21f7e14963159f0f4ad))
* s3 default base storage ([1944e01](https://github.com/fivehanz/hanz-web/commit/1944e016d2359cc8643793bed09cb8931844eb65))
* s3 storage for media ([ca3eeb2](https://github.com/fivehanz/hanz-web/commit/ca3eeb2d2df1f70405b4611bd5a03f37cead6395))
* update bun to 1.1.21 ([f3c2b0c](https://github.com/fivehanz/hanz-web/commit/f3c2b0c4b9e714cf66a3c28ea86e9303e5915d22))
* update django version to 5.0.3 ([6f0258f](https://github.com/fivehanz/hanz-web/commit/6f0258f092fb573faaac60f4be680e8942a13c6a))
* update to wagtail 6 ([76a0797](https://github.com/fivehanz/hanz-web/commit/76a079726b1cd250d741ad2ad6a21691c612286d))
* upgrade nginx config ([a688491](https://github.com/fivehanz/hanz-web/commit/a6884915838780bc5097085fb15e77b3230be002))


### Bug Fixes

* docker dev environment ([0ce2490](https://github.com/fivehanz/hanz-web/commit/0ce2490a48128c8dc8189866c817a85bb006bf32))

## [0.16.0](https://github.com/fivehanz/hanz-web/compare/v0.15.0...v0.16.0) (2024-01-22)


### Features

* add email backend in prod ([c906099](https://github.com/fivehanz/hanz-web/commit/c9060990c205d873ced3770bff583d15765b8016))
* projects page ([3fed025](https://github.com/fivehanz/hanz-web/commit/3fed0251e7572600f2b3bed1a0499dfe16c4d515))
* projects pages ([42d50d2](https://github.com/fivehanz/hanz-web/commit/42d50d2862221f782ca93dc905309a6713ea4cd2))
* working wagtail-ai ([a53876c](https://github.com/fivehanz/hanz-web/commit/a53876c2247bb9bf1349a4327a79ab990d298867))

## [0.15.0](https://github.com/fivehanz/hanz-web/compare/v0.14.0...v0.15.0) (2024-01-18)


### Features

* auto gen sitemaps.xml ([e925e55](https://github.com/fivehanz/hanz-web/commit/e925e559ed117fe597956709e0d346664812cad2))


### Bug Fixes

* favicon ([6c15632](https://github.com/fivehanz/hanz-web/commit/6c15632356eaae2cb33085a9db5141bbabcdd306))

## [0.14.0](https://github.com/fivehanz/hanz-web/compare/v0.13.1...v0.14.0) (2024-01-18)


### Features

* dev env with minio ([4fac4c6](https://github.com/fivehanz/hanz-web/commit/4fac4c6a8101a8b55039134b1edfa3b6c25449df))


### Bug Fixes

* s3 dbbackup works ([174cad7](https://github.com/fivehanz/hanz-web/commit/174cad7c5c44d4131315ca4b2ff86493a4faf88e))

## [0.13.1](https://github.com/fivehanz/hanz-web/compare/v0.13.0...v0.13.1) (2024-01-17)


### Bug Fixes

* gtm js not working on prod ([2e4d82c](https://github.com/fivehanz/hanz-web/commit/2e4d82c595371ac897f0212157e06b9350b6ca9e))

## [0.13.0](https://github.com/fivehanz/hanz-web/compare/v0.12.0...v0.13.0) (2024-01-17)


### Features

* google tag manager settings ([f92a06f](https://github.com/fivehanz/hanz-web/commit/f92a06f2c391d9f0079d26ed655e046b76ad92a5))

## [0.12.0](https://github.com/fivehanz/hanz-web/compare/v0.11.0...v0.12.0) (2024-01-14)


### Features

* wagtail-cache extension & menu ([b218469](https://github.com/fivehanz/hanz-web/commit/b2184697e67d793c1da7cf200264418892b42ff6))

## [0.11.0](https://github.com/fivehanz/hanz-web/compare/v0.10.0...v0.11.0) (2024-01-13)


### Features

* setup redis cache ([9bc10d7](https://github.com/fivehanz/hanz-web/commit/9bc10d78d9fbbbf933da8f0627f2318ede2871b8))

## [0.10.0](https://github.com/fivehanz/hanz-web/compare/v0.9.0...v0.10.0) (2024-01-12)


### Features

* hero section on homepage ([6e2183e](https://github.com/fivehanz/hanz-web/commit/6e2183e47b6a72f50223842f7960319bd32618ea))

## [0.9.0](https://github.com/fivehanz/hanz-web/compare/v0.8.0...v0.9.0) (2024-01-10)


### Features

* add alpinejs ([8ee1102](https://github.com/fivehanz/hanz-web/commit/8ee1102d51b5271370b4d2447d616f1c55d26e9d))
* basic working contact form ([0dfa32d](https://github.com/fivehanz/hanz-web/commit/0dfa32d44680f6f77889c4247f9ab52b686a1b02))

## [0.8.0](https://github.com/fivehanz/hanz-web/compare/v0.7.0...v0.8.0) (2024-01-10)


### Features

* nginx deployment init ([0cda156](https://github.com/fivehanz/hanz-web/commit/0cda156dd7d40f42bf2e9ee28559173339ebaf63))
* optimize js w/ defer ([2bbd51c](https://github.com/fivehanz/hanz-web/commit/2bbd51c1b602bca850b94213840a8d30c3aa8a1c))

## [0.7.0](https://github.com/fivehanz/hanz-web/compare/v0.6.0...v0.7.0) (2024-01-09)


### Features

* deployment init w/ docker-compose ([3178c8c](https://github.com/fivehanz/hanz-web/commit/3178c8c93c8626e9b5be2b01e7716544f5b7912d))
* nav links; footer links; optimizations ([830d66c](https://github.com/fivehanz/hanz-web/commit/830d66c3a1a970f46c7db211dd9e252df5078e72))

## [0.6.0](https://github.com/fivehanz/hanz-web/compare/v0.5.0...v0.6.0) (2024-01-07)


### Features

* optimize compress assets ([5f66f7c](https://github.com/fivehanz/hanz-web/commit/5f66f7c7b822ab7ffc23632b3fcf321e6567b03f))


### Bug Fixes

* assets compression to brotli ([e0a8031](https://github.com/fivehanz/hanz-web/commit/e0a80318f1bbff6df385c474c00d9065367fa06b))

## [0.5.0](https://github.com/fivehanz/hanz-web/compare/v0.4.0...v0.5.0) (2024-01-06)


### Features

* optimize dfile, assets compression ([c1dde3f](https://github.com/fivehanz/hanz-web/commit/c1dde3f00f7ca9f1a5e05754060a6f77b8cbbae2))
* refactor + flowbite ([5fdb960](https://github.com/fivehanz/hanz-web/commit/5fdb9601bcb743999408781074bd80d7811dbc22))

## [0.4.0](https://github.com/fivehanz/hanz-web/compare/v0.3.1...v0.4.0) (2023-12-22)


### Features

* add brotli compression ([8047493](https://github.com/fivehanz/hanz-web/commit/80474932804acbc828619a63824a494d9b550d6f))
* integrate htmx ([a1ebed2](https://github.com/fivehanz/hanz-web/commit/a1ebed21b4639c1756d4edcd79d0085a3511e772))

## [0.3.1](https://github.com/fivehanz/hanz-web/compare/v0.3.0...v0.3.1) (2023-12-16)


### Bug Fixes

* csrf ([075797a](https://github.com/fivehanz/hanz-web/commit/075797a7dbb9589784ebec23b5a27d9a58d8a434))
* debug and hosts in prod ([ae58cb1](https://github.com/fivehanz/hanz-web/commit/ae58cb1805a42a99dbb412051fce4b169cc6c6d9))

## [0.3.0](https://github.com/fivehanz/hanz-web/compare/v0.2.0...v0.3.0) (2023-12-16)


### Features

* use whitenoise for static files ([69e44dd](https://github.com/fivehanz/hanz-web/commit/69e44dd66e2c7d1d5861d5a273968bbda05ad4da))


### Bug Fixes

* staticfiles not showing ([1de021a](https://github.com/fivehanz/hanz-web/commit/1de021a8ca8db0de08c6f4df63ffc6a52347e8d3))

## [0.2.0](https://github.com/fivehanz/hanz-web/compare/v0.1.0...v0.2.0) (2023-12-14)


### Features

* tailwindcss ([b18ff15](https://github.com/fivehanz/hanz-web/commit/b18ff158e976e8069f0b2c4c955d145ee5535913))

## 0.1.0 (2023-12-12)


### Features

* postgres init ([1e0fa3b](https://github.com/fivehanz/hanz-web/commit/1e0fa3bd486752a850dad2bc7631d691d5097c75))
