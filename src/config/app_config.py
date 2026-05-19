# src/app_config.py

# Verze aplikace
APP_VERSION = "1.0.6"

# URL k manifestu s nejnovější verzí "https://raw.githubusercontent.com/RysanekDavid/The-Tarnished-Chronicle/main/update_test/latest.json"
MANIFEST_URL = "https://raw.githubusercontent.com/RysanekDavid/The-Tarnished-Chronicle/main/update_test/latest.json"
# TEST_URL = "http://localhost:8000/test_manifest.json"

# Asset Management for large image files
IMAGE_ASSETS_URL = "https://github.com/RysanekDavid/ER_checklist_assets/releases/download/v1.0.0/Bosses_locations.zip"
APP_DATA_DIR = "TheTarnishedChronicle"

# Default overlay styles
DEFAULT_OVERLAY_BG_COLOR_STR = "rgba(100, 100, 100, 220)"
DEFAULT_OVERLAY_TEXT_COLOR_STR = "lightblue"
DEFAULT_OVERLAY_FONT_SIZE_STR = "15pt"

# Monitoring settings
DEFAULT_MONITORING_INTERVAL_SEC = 5

# Rust CLI settings
RUST_CLI_TOOL_PATH_PLACEHOLDER = "RUST_CLI_TOOL_PATH_PLACEHOLDER"
DEFAULT_BOSS_REFERENCE_FILENAME = "boss_ids_reference.json"
DLC_BOSS_REFERENCE_FILENAME = "boss_ids_reference_DLC.json" 


# Lokace, které v tomto seznamu nebudou, se automaticky zařadí na konec.
LOCATION_PROGRESSION_ORDER = [
    # Início de Jogo (Níveis 1-40)
    "Limgrave",
    "Península do Pranto",
    "Castelo Tempesvéu",

    # Meio de Jogo (Níveis 40-90)
    "Liurnia dos Lagos",
    "Academia de Raya Lucaria",
    "Rio Siofra",
    "Rio Ainsel",
    "Caelid",
    "Planalto Altus",
    "Dragonbarrow",
    "Monte Gelmir",
    "Arredores da Capital",
    "Nokron, Cidade Eterna",
    "Profundezas das Raízes",
    "Lago da Podridão",
    "Leyndell, Capital Real",

    # Fim de Jogo (Níveis 100+)
    "Terras Proibidas",
    "Cumes dos Gigantes",
    "Campo Nevado Consagrado",
    "Altar da Luz da Lua",
    "Mausoléu da Dinastia Mohgwyn",
    "Farum Azula em Ruínas",
    "Árvore Sagrada de Miquella",
    "Leyndell, Capital das Cinzas",
    "Trono Éldico",

    # DLC
    "Planície Tumular",
    "Scadu Altus",
    "Base de Rauh",
    "Costa Cerúlea",
    "Túmulo Oculto de Charo",
    "Pico Dentilhado",
    "Bosques Abissais",
    "Vista de Scadu",
    "Ruínas Antigas de Rauh",
    "Enir-Ilim",
]
GAME_PHASE_HEADINGS = {
    "Limgrave": {
        "text": "Início de Jogo: (Níveis 1-40)",
        "property": "early"
    },
    "Liurnia dos Lagos": {
        "text": "Meio de Jogo: (Níveis 40-90)",
        "property": "mid"
    },
    "Terras Proibidas": {
        "text": "Fim de Jogo: (Níveis 100+)",
        "property": "late"
    },
    "dlc_header": {
        "text": "DLC: Sombra da Árvore do Érdtree",
        "property": "dlc"
    }
}