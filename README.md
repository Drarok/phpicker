# PHPicker.

A simple tool, written in Python, to allow selecting between the system-installed, and different [Homebrew][brew] versions of PHP on OS X.

## Requirements.

* Python >= 2.7.
* OS X
* [Homebrew][brew]

## Installation.

tl;dr: Clone this repo, create `config.json`, and symlink the binary into your path.

    git clone https://github.com/Drarok/phpicker.git ~/phpicker
    $EDITOR phpicker/config.json # see config.json.sample to guide you
    ln -s ~/phpicker/phpicker /usr/local/bin/phpicker

## Usage.

### Displaying available / current version(s).

```bash
$ phpicker
* 5.3.28
  5.4.26
  5.5.10
  5.6.0-alpha.2
  5.6.0-alpha.3
  system
```

### Selecting a version.

Switching to PHP 5.4.26.

```bash
$ phpicker 5.4.26
  5.3.28
* 5.4.26
  5.5.10
  5.6.0-alpha.2
  5.6.0-alpha.3
  system
```

### Selecting a version using short syntax.

This will select the latest version of PHP 5.6 you have installed.

```bash
$ phpicker 5.6
  5.3.28
  5.4.26
  5.5.10
  5.6.0-alpha.2
* 5.6.0-alpha.3
  system
```

### Selecting a version silently (useful in .bashrc, .zshrc, etc).

```bash
$ phpicker -q 5.4
```

[brew]: http://brew.sh
