# Bug/Error Reproduction Repository

## Introduction
This repository is created to help reproduce the error encountered on Linux when setting up with devenv and poetry.
The purpose of this README is to guide users/developers on how to set up and run the provided sample code to observe the error or bug.

## Error/Bug Description
The system seems not to be able to locate the libstdc++,`raise ValueError(
ValueError: the greenlet library is required to use this function. libstdc++.so.6: cannot open shared object file: No such file or directory` 
a similar issue is found [here](https://discourse.nixos.org/t/sqlalchemy-python-fails-to-find-libstdc-so-6-in-virtualenv/38153), but as [nix-ld](https://github.com/Mic92/nix-ld) works only on NixOS, this soution can be replicated for us who use devenv

## Steps to Reproduce
The following steps can be followed to reproduce the error

1. **Clone the Repository**:
```
git clone <repository-url>
```

2. **Install Dependencies**:
   We assume that whoever is testing this already has devenv installed and working
```
cd devenv-sqlalchemy-asyncpg
```

3. **Run the Sample Code**:

```
devenv up
```

4. **Write Migrations to the test db**:

```
alembic upgrade head
```

Then go to http://localhost:8000/ on your browser and try adding and fetching some users