# Release Python Project as PyInstaller Executable on Multiple OSs

This repository provides you with an example of how to deploy a Python project as a PyInstaller
executable to multiple OSs. PyInstaller allows to create an executable out of the Python project. To
build the executable for a specific OS, the build command has to be run on this OS.
On every pushed `v*` tag, the [Release](.github/workflows/release.yaml) workflow does exactly this
and publishes a release for the OSs `ubuntu-lates`, `macos-latest` and `windows-latest`.

## Release Workflow

The [Release](.github/workflows/release.yaml) workflow executes the following steps.

1. Create GitHub release
2. Store URL of release to attach further artifacts
3. Set up Python environment on different machines
4. Install project dependencies (incl. PyInstaller)
5. Create executable with PyInstaller
6. Package executable in .zip
7. Publish .zip with built executable to previous release via URL

## Release Tags

The [Release](.github/workflows/release.yaml) workflow is triggered by every tag which starts
with `v*`, e.g. `v0.3.2`. It then creates a release for this tag with the name of the tag. To tag a
current state of the repo, create a tag with `git tag v1.4.3` and push the tag
with `git push --tags`.

## Create Executable With PyInstaller

The example application greats either the person specified as an argument or the world if no one is
specified. The following steps create an executable for your machine.

1. Install PyInstaller with `pip install pyinstaller`
2. Execute `pyinstaller src/cli.py --name hello-world --onefile`
3. Test single executable `dist/hello-world`
    1. With arg: `./dist/hello-world Carla`
    2. Without arg: `./dist/hello-world`