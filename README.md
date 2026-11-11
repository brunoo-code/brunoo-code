<p align="center">
  <img src="./assets/bnqq-system-engineering.svg" width="920" alt="Bruno Novais · BNQQ System Engineering · Engenharia reversa de jogos e ferramentas Windows">
</p>

<p align="center">
  <a href="#projetos-em-destaque">Projetos</a> · <a href="#tecnologias">Tecnologias</a> · <a href="#contribuições">Contribuições</a>
</p>

Desenvolvo ferramentas de engenharia reversa para jogos e Windows. Trabalho com **formatos binários**, **memória de processos** e **automação**. Nos projetos abaixo, mostro o que consegui inspecionar, medir ou reproduzir.

| Análise binária | Depuração de kernel | Desempenho em jogos |
| :---: | :---: | :---: |
| **339 entradas** verificadas no PAK original do Quake | **2.002 consultas aceitas** na bancada Hyper‑V | **6 frentes** de otimização e medição para CS2 e VALORANT |
| [Quake PAK Inspector](https://github.com/brunoo-code/quake-pak-inspector) | [BNQQ Driver Lab](https://github.com/brunoo-code/win-kernel-telemetry/blob/main/docs/hyperv-validation.md) | [BNQQ Toolkit](https://github.com/brunoo-code/bnqq-toolkit) |

## Projetos em destaque

<table>
  <tr>
    <td valign="top">
      <a href="https://github.com/brunoo-code/quake-pak-inspector#interface-para-windows"><img src="./assets/quake-pak-gui.png" width="820" alt="Interface do Quake PAK Inspector com arquivos alterados e comparação hexadecimal lado a lado"></a>
      <h3>Quake PAK Inspector</h3>
      <p>Inspetor de arquivos binários em <strong>C++20 e Win32</strong>. Navegue pelos recursos do Quake, compare dois pacotes em hexadecimal e confira qual mod sobrescreve cada arquivo pela CLI. Validado com 339 entradas do Quake 1.06 shareware.</p>
      <a href="https://github.com/brunoo-code/quake-pak-inspector/releases/latest">Baixar demo</a> · <a href="https://github.com/brunoo-code/quake-pak-inspector#hub-de-mods-em-c-e-lua">Hub de mods em Lua</a> · <a href="https://github.com/brunoo-code/quake-pak-inspector">Código</a>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td valign="top">
      <a href="https://github.com/brunoo-code/win-kernel-telemetry/blob/main/docs/hyperv-validation.md#teste-de-carga-concorrente"><img src="./assets/bnqq-hyperv-lab.svg" width="820" alt="BNQQ Driver Lab no Hyper-V com oito conexões, duas mil consultas de carga e zero rejeições"></a>
      <h3>BNQQ Driver Lab · Hyper‑V</h3>
      <p>VM Windows Server 2025 x64 usada para validar o <strong>BNQQ Kernel Telemetry</strong>, um driver WDM em C++ com cliente Win32. A bancada reúne uma sessão de depuração de kernel com KD do pacote WinDbg e um teste de carga com oito conexões simultâneas.</p>
      <a href="https://github.com/brunoo-code/win-kernel-telemetry/blob/main/docs/hyperv-validation.md#teste-de-carga-concorrente">Ver teste de carga</a> · <a href="https://github.com/brunoo-code/win-kernel-telemetry/blob/main/docs/hyperv-validation.md#depurador">Ver depuração</a> · <a href="https://github.com/brunoo-code/win-kernel-telemetry">Código</a>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Game Memory Lab</h3>
      <p>Busca diferencial de valores e leitura e escrita de memória de um processo de demonstração pelas APIs Win32.</p>
      <a href="https://github.com/brunoo-code/game-memory-lab">Ver projeto</a>
    </td>
    <td width="50%" valign="top">
      <h3>Aim Overlay Lab</h3>
      <p>Protótipo em C++20 que projeta coordenadas 3D na tela e visualiza a seleção de alvos em uma arena offline.</p>
      <a href="https://github.com/brunoo-code/aim-overlay-lab">Ver projeto</a>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td valign="top">
      <a href="https://github.com/brunoo-code/bnqq-toolkit"><img src="./assets/bnqq-competitive-six.svg" width="820" alt="BNQQ Toolkit, otimização competitiva em seis frentes para CS2 e VALORANT"></a>
      <h3>BNQQ Toolkit</h3>
      <p><strong>Otimizador avançado para quem leva CS2 e VALORANT competitivo a sério.</strong> O BNQQ atua em seis frentes do PC para reduzir a interferência de tarefas em segundo plano e buscar quadros mais consistentes. Foi feito para jogadores que querem investigar stutter e input lag e medir o efeito dos ajustes no próprio setup.</p>
      <ul>
        <li><strong>CPU e aplicativos.</strong> O Start Competitivo prepara a sessão, preserva os apps escolhidos e ajusta a prioridade dos processos selecionados conforme a atividade.</li>
        <li><strong>Rede e gráficos.</strong> Limite o upload de apps de sincronização, configure limites de FPS para menu e partida no CS2 e ajuste preferências gráficas locais do VALORANT.</li>
        <li><strong>Diagnóstico e medição.</strong> Consulte hardware e drivers e compare rodadas com o FrameBench e o PresentMon usando 1% e 0,1% lows e p99 de tempo de quadro. Para confirmar input lag de ponta a ponta, use uma medição específica de mouse até tela.</li>
      </ul>
      <a href="https://github.com/brunoo-code/bnqq-toolkit">Conhecer o BNQQ Toolkit</a> · <a href="https://github.com/brunoo-code/bnqq-toolkit/blob/main/docs/COMPETITIVE-START.md#menu-29-start-competitivo">Ver Start Competitivo</a> · <a href="https://github.com/brunoo-code/bnqq-toolkit#medir-antes-de-concluir">Como medir</a>
    </td>
  </tr>
</table>

### Mais projetos

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/brunoo-code/EchoLive#demo"><img src="./assets/echolive-preview.png" width="410" alt="Sala do EchoLive com duas pessoas trocando mensagens"></a>
      <h3>EchoLive</h3>
      <p>Salas privadas com voz, vídeo e chat em tempo real.</p>
      <a href="https://github.com/brunoo-code/EchoLive#demo">Ver demo</a> · <a href="https://github.com/brunoo-code/EchoLive">Código</a>
    </td>
    <td width="50%" valign="top">
      <a href="https://brunoo-code.github.io/cs2-replay-lab/example/?v=21565ca"><img src="./assets/mirage-cs2-preview.png" width="410" alt="Radar de Mirage com pontos de eventos e filtros por round"></a>
      <h3>CS2 Replay Lab</h3>
      <p>Radar interativo de Mirage gerado a partir de um replay real.</p>
      <a href="https://brunoo-code.github.io/cs2-replay-lab/example/?v=21565ca">Abrir radar</a> · <a href="https://github.com/brunoo-code/cs2-replay-lab">Código</a>
    </td>
  </tr>
</table>

- [Save File Lab](https://github.com/brunoo-code/save-file-lab) · Comparação e edição de saves binários com validação CRC.

## Tecnologias

| Área | Ferramentas |
| --- | --- |
| **Sistemas e diagnóstico** | ![C++](https://img.shields.io/badge/C%2B%2B-1c4050?style=flat-square&logo=cplusplus&logoColor=a6f3e7) ![Win32](https://img.shields.io/badge/Win32-1c4050?style=flat-square) ![WDK](https://img.shields.io/badge/WDK-1c4050?style=flat-square) ![WinDbg](https://img.shields.io/badge/WinDbg-1c4050?style=flat-square) ![Hyper-V](https://img.shields.io/badge/Hyper--V-1c4050?style=flat-square) |
| **Scripts e formatos** | ![Lua](https://img.shields.io/badge/Lua-33285e?style=flat-square&logo=lua&logoColor=d4bcff) ![PowerShell](https://img.shields.io/badge/PowerShell-33285e?style=flat-square) ![Python](https://img.shields.io/badge/Python-33285e?style=flat-square&logo=python&logoColor=d4bcff) ![C Sharp](https://img.shields.io/badge/C%23-33285e?style=flat-square) |
| **Web em tempo real** | ![JavaScript](https://img.shields.io/badge/JavaScript-20314d?style=flat-square&logo=javascript&logoColor=9ad8ff) ![React](https://img.shields.io/badge/React-20314d?style=flat-square&logo=react&logoColor=9ad8ff) ![Node.js](https://img.shields.io/badge/Node.js-20314d?style=flat-square&logo=nodedotjs&logoColor=9ad8ff) |

## Contribuições

<p align="center">
  <a href="https://github.com/brunoo-code?tab=repositories"><img src="./assets/github-stats.svg" width="920" alt="Estatísticas públicas do GitHub: repositórios, estrelas recebidas e contribuições no último ano"></a>
  <a href="https://github.com/brunoo-code#js-contribution-activity"><img src="./assets/github-activity.svg" width="920" alt="Gráfico das contribuições públicas semanais nas últimas 16 semanas"></a>
</p>

[Ver histórico de contribuições no GitHub](https://github.com/brunoo-code#js-contribution-activity)

<!-- Atualize os cards e o gráfico com python tools/update-profile-stats.py. -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/contributions-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/contributions.svg">
  <img alt="Cobrinha animada percorrendo meu gráfico de contribuições no GitHub" src="./assets/contributions.svg">
</picture>
