# bl

Blender tookits

## Development

create virtual env

```sh
uv venv --python 3.13

source .venv/bin/activate
uv pip install -ve "."
```

start blender

```sh
PYTHONPATH=$VIRTUAL_ENV/lib/python3.13/site-packages:$PYTHONPATH /Applications/Blender.app/Contents/MacOS/Blender --python-use-system-env --env-system-python $(uv python find 3.13) --python-expr "import site; site.addsitedir('$VIRTUAL_ENV/lib/python3.13/site-packages')"
```
