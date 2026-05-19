# -*- mode: python ; coding: utf-8 -*-
# build.spec — Crônicas do Maculado

import os

block_cipher = None

# Paths
project_root = os.path.abspath('.')
cli_exe = os.path.join(project_root, 'flag_extractor_cli', 'target', 'release', 'flag_extractor_cli.exe')
icon_path = os.path.join(project_root, 'assets', 'images', 'app_logo.ico')

a = Analysis(
    [os.path.join(project_root, 'src', 'main.py')],
    pathex=[project_root],
    binaries=[
        # Bundle the Rust CLI so rust_cli_handler finds it via sys._MEIPASS
        (cli_exe, '.'),
    ],
    datas=[
        # PT-BR boss JSONs — filesystem-first fallback in boss_data_manager reads these
        (os.path.join(project_root, 'data', 'Bosses'), os.path.join('data', 'Bosses')),
    ],
    hiddenimports=[
        'resources_rc',
        'PySide6.QtSvg',
        'PySide6.QtSvgWidgets',
        'PySide6.QtXml',
        'PySide6.QtNetwork',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Cronicas_do_Maculado',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,       # sem janela de console
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Cronicas_do_Maculado',
)
