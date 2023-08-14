<div align="center">
    <h1>🔃 Awakatime</h1>
    <p>Uma API wrapper assíncrona para o Wakatime</p>
    <a href="https://wakatime.com/badge/github/controlado/awakatime">
        <img src="https://wakatime.com/badge/github/controlado/awakatime.svg" alt="wakatime">
    </a>
    <a href="https://discordapp.com/users/854886148455399436">
        <img src="https://dcbadge.vercel.app/api/shield/854886148455399436?style=flat" alt="discord">
    </a>
    <br>
    <a href="https://github.com/controlado/awakatime/issues/new">
        <img src="https://img.shields.io/badge/Report%20a%20bug-gray" alt="report">
    </a>
    <a href="https://awakatime.readthedocs.io/en/latest/?badge=latest">
        <img src="https://readthedocs.org/projects/awakatime/badge/?version=latest" alt="documentation">
    </a>
    <a href="README.md">
        <img src="https://img.shields.io/badge/English-bright" alt="english">
    </a>
    <a href="README.br.md">
        <img src="https://img.shields.io/badge/Português-bright" alt="português">
    </a>
    <br>
    <a href="https://codecov.io/gh/controlado/awakatime">
        <img src="https://codecov.io/gh/controlado/awakatime/branch/main/graph/badge.svg?token=86DTBWW41H">
    </a>
    <a href="https://pypi.org/project/awakatime/">
        <img src="https://img.shields.io/pypi/v/awakatime?color=green" alt="pypi">
    </a>
    <img src="https://img.shields.io/github/license/controlado/awakatime" alt="license">
</div>

## Instalação

```bash
pip install awakatime
```

## Uso

O ideal é usar o gerenciador de contexto para criar uma instância do cliente.

```python
import asyncio

from awakatime import Awakatime


async def main():
    async with Awakatime("sua_chave_da_api") as awakatime:
        tasks = [awakatime.get_all_time(), awakatime.get_projects()]
        all_time, projects = await asyncio.gather(*tasks)
        print(all_time)
        print(projects)


if __name__ == "__main__":
    coro = main()
    asyncio.run(coro)
```

## Desenvolvimento

Não esqueça de instalar o [Poetry](https://python-poetry.org/) em seu ambiente.

```bash
git clone https://github.com/controlado/awakatime.git
cd awakatime
poetry install --with dev
```