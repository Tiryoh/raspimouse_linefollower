# ラズパイマウスのデバイスドライバインストーラ

ラズパイマウスのデバイスドライバ( [rt-net/RaspberryPiMouse](https://github.com/rt-net/RaspberryPiMouse) )をセットアップするためのインストーラです。

## 使い方

### デバイスドライバのビルド

次のように端末で`build_driver.sh`を実行し、デバイスドライバをビルドします。

```
./build_driver.sh
```

カーネルのバージョンが変わらない限り、このスクリプトの実行は1回のみで問題ありません。

### デバイスドライバのインストール

次のように端末で`install_driver.sh`を実行し、デバイスドライバをインストールします。

```
./install_driver.sh
```

デバイスドライバは起動するたびにカーネルに組み込む必要があります。  
`install_auto_loader.sh`を実行してデバイスドライバをOS起動時にカーネルへ自動で組み込まれるようにするか、この`install_driver.sh`をOS起動後に毎回手動で実行する必要があります。

### デバイスドライバのインストールを自動化

次のように端末で`install_auto_loader.sh`を実行します。

```
./install_auto_loader.sh
```

RaspberryPiMouseのデバイスドライバをOS起動時に自動でカーネルに組み込むように設定します。

## スクリプトの内容

### build_driver.sh
`~/RaspberryPiMouse/src/drivers/rtmouse.c`をビルドするためのスクリプトです。  
`/usr/src`にカーネルのヘッダがなければapt-getで`raspberrypi-kernel-headers`をインストールします。
ホームディレクトリに[rt-net/RaspberryPiMouse](https://github.com/rt-net/RaspberryPiMouse)がなければ、gitでGitHubからダウンロードしてきます。

### install_driver.sh
`rtmouse.ko`をカーネルに組み込むためのスクリプトです。  
insmodでカーネルにデバイスドライバを組み込みます。
`~/RaspberryPiMouse/src/drivers`に`rtmouse.ko`があればそちらを、なければ
`~/RaspberryPiMouse/lib/Pi2B+`ディレクトリにある適切なバージョンのデバイスドライバをインストールします。

### install_auto_loader.sh
`install_driver.sh`をOS起動時に自動で呼び出すように設定するためのスクリプトです。  
crontabで呼び出します。

## ライセンス

MITライセンスで公開しています。
