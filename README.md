# bl

Blender tookits

## Development

create virtual env

```sh
conda create -y --name bl python=3.11
pip install -e ".[tests]"
```

start blender

```sh
BLENDER_SYSTEM_PYTHON=$(conda info --base)/envs/bl /Applications/Blender.app/Contents/MacOS/Blender
```
