# PHPicker.

A simple tool, written in Python, to allow selecting between different [Homebrew][brew] versions of PHP on OS X.

## Usage.

### Displaying available versions.

```bash
$ phpicker
5.3.28
5.4.26
5.5.10
5.6.0-alpha.2
5.6.0-alpha.3
```

### Selecting a version.

Switching to PHP 5.4.26.

```bash
$ eval $(phpicker 5.4.26)
```

### Selecting a version using short syntax.

This will select the latest version of PHP 5.6 you have installed.

```bash
$ eval $(phpicker 5.6)
```

[brew]: http://brew.sh
