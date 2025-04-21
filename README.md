# bl

Blender tookits

## Development

create virtual env

```sh
pyenv virtualenv 3.11.11 bl
pip install -e ".[tests]"
```

start blender

```sh
BLENDER_SYSTEM_PYTHON=$(pyenv prefix 3.11.11) PYTHONPATH=$(pyenv prefix bl)/lib/python3.11/site-packages /Applications/Blender.app/Contents/MacOS/Blender --python-use-system-env
```
