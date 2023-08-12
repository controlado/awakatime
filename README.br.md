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
    <a href="https://pypi.org/project/awakatime/">
        <img src="https://img.shields.io/pypi/v/awakatime" alt="pypi">
    </a>
    <img src="https://img.shields.io/github/license/controlado/awakatime" alt="license">
    <br>
    <img src="https://img.shields.io/badge/Documentation-gray" alt="documentation">
    <a href="README.md">
        <img src="https://img.shields.io/badge/English-blue" alt="english">
    </a>
    <a href="README.br.md">
        <img src="https://img.shields.io/badge/Português%20Brasileiro-blue" alt="português">
    </a>
</div>

## Instalação

```bash
pip install awakatime
```

## Uso

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
