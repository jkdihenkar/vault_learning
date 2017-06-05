# Steps for Building vault-api

step 1 - `sdist`

```
[jd@jaypc pyconsumables]$ python3.6 setup.py sdist
running sdist
running egg_info
writing vault_api.egg-info/PKG-INFO
writing dependency_links to vault_api.egg-info/dependency_links.txt
writing requirements to vault_api.egg-info/requires.txt
writing top-level names to vault_api.egg-info/top_level.txt
reading manifest file 'vault_api.egg-info/SOURCES.txt'
writing manifest file 'vault_api.egg-info/SOURCES.txt'
warning: sdist: standard file not found: should have one of README, README.rst, README.txt

running check
creating vault-api-1.0.0
creating vault-api-1.0.0/vault-api
creating vault-api-1.0.0/vault_api.egg-info
copying files to vault-api-1.0.0...
copying setup.cfg -> vault-api-1.0.0
copying setup.py -> vault-api-1.0.0
copying vault-api/__init__.py -> vault-api-1.0.0/vault-api
copying vault-api/vault_api.py -> vault-api-1.0.0/vault-api
copying vault-api/vault_confs.py -> vault-api-1.0.0/vault-api
copying vault_api.egg-info/PKG-INFO -> vault-api-1.0.0/vault_api.egg-info
copying vault_api.egg-info/SOURCES.txt -> vault-api-1.0.0/vault_api.egg-info
copying vault_api.egg-info/dependency_links.txt -> vault-api-1.0.0/vault_api.egg-info
copying vault_api.egg-info/requires.txt -> vault-api-1.0.0/vault_api.egg-info
copying vault_api.egg-info/top_level.txt -> vault-api-1.0.0/vault_api.egg-info
Writing vault-api-1.0.0/setup.cfg
Creating tar archive
removing 'vault-api-1.0.0' (and everything under it)
```

step 2 - `install`

```
[jd@jaypc pyconsumables]$ sudo `which python3.6` -m pip install dist/vault-api-1.0.0.tar.gz  --upgrade
Processing ./dist/vault-api-1.0.0.tar.gz
Installing collected packages: vault-api
  Found existing installation: vault-api 1.0.0
    Can't uninstall 'vault-api'. No files were found to uninstall.
  Running setup.py install for vault-api ... done
Successfully installed vault-api-1.0.0
```