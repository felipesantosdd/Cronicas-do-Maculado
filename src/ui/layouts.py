# src/ui/layouts.py

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QFrame, QCheckBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from .widgets.icon_header import IconHeader
from ..utils import get_resource_path

def create_file_slot_layout(parent_widget):
    main_v_layout = QVBoxLayout()
    main_v_layout.setSpacing(8)
    
    # --- Save File Section ---
    main_v_layout.addWidget(IconHeader(get_resource_path("assets/icons/file-text.svg"), "Arquivo de Save"))

    # Create horizontal layout for path and success indicator
    path_layout = QHBoxLayout()
    path_layout.setSpacing(8)

    # Success indicator icon (initially hidden)
    parent_widget.save_file_success_icon = QLabel()
    success_pixmap = QPixmap(get_resource_path("assets/icons/check-circle.svg"))
    parent_widget.save_file_success_icon.setPixmap(success_pixmap.scaled(20, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    parent_widget.save_file_success_icon.setFixedSize(20, 20)
    parent_widget.save_file_success_icon.setVisible(False)
    path_layout.addWidget(parent_widget.save_file_success_icon)

    # File path label
    parent_widget.save_file_path_label = QLabel("Nenhum arquivo de save selecionado...")
    parent_widget.save_file_path_label.setObjectName("filePathLabel")
    parent_widget.save_file_path_label.setWordWrap(True)
    path_layout.addWidget(parent_widget.save_file_path_label, 1)  # Stretch factor 1

    main_v_layout.addLayout(path_layout)

    parent_widget.browse_button = QPushButton("Procurar Arquivo de Save")
    parent_widget.browse_button.setObjectName("browseButton")
    main_v_layout.addWidget(parent_widget.browse_button)
    main_v_layout.addSpacing(15)

    # --- Character Section ---
    main_v_layout.addWidget(IconHeader(get_resource_path("assets/icons/user.svg"), "Personagem:"))
    parent_widget.character_slot_combobox = QComboBox(parent_widget)
    parent_widget.character_slot_combobox.setPlaceholderText("Selecione um personagem")
    parent_widget.character_slot_combobox.setEnabled(False)
    main_v_layout.addWidget(parent_widget.character_slot_combobox)

    # Add a label for character mismatch warnings
    parent_widget.character_warning_label = QLabel("")
    parent_widget.character_warning_label.setObjectName("warningLabel")
    parent_widget.character_warning_label.setWordWrap(True)
    parent_widget.character_warning_label.setVisible(False) # Hidden by default
    main_v_layout.addWidget(parent_widget.character_warning_label)
    
    main_v_layout.addSpacing(15)
    
    # --- Filter Section ---
    separator = QFrame()
    separator.setFrameShape(QFrame.Shape.HLine)
    separator.setFrameShadow(QFrame.Shadow.Plain)
    separator.setObjectName("separatorLine")
    main_v_layout.addWidget(separator)
    main_v_layout.addSpacing(10)
    
    # Content Filter (Base/DLC/All)
    main_v_layout.addWidget(IconHeader(get_resource_path("assets/icons/filter.svg"), "Filtro de Conteúdo"))
    parent_widget.content_filter_combobox = QComboBox()
    parent_widget.content_filter_combobox.addItem("Mostrar Tudo", userData="all")
    parent_widget.content_filter_combobox.addItem("Apenas Jogo Base", userData="base")
    parent_widget.content_filter_combobox.addItem("Apenas DLC", userData="dlc")
    main_v_layout.addWidget(parent_widget.content_filter_combobox)
    main_v_layout.addSpacing(10)

    # Display Filter (Hide Defeated)
    parent_widget.hide_defeated_checkbox = QCheckBox("Ocultar Chefes Derrotados")
    parent_widget.hide_defeated_checkbox.setObjectName("hideDefeatedCheckbox")
    main_v_layout.addWidget(parent_widget.hide_defeated_checkbox)
    main_v_layout.addSpacing(10)

    return main_v_layout

from PySide6.QtWidgets import QScrollArea, QWidget, QGroupBox, QLineEdit
from PySide6.QtGui import QIcon
from .widgets.toggle_switch import ToggleSwitch

def create_main_boss_area(parent_widget):
    scroll_area = QScrollArea(parent_widget)
    scroll_area.setWidgetResizable(True)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    scroll_area.setObjectName("mainBossScrollArea")
    main_container_widget = QWidget()
    main_container_widget.setObjectName("locationsContainer")
    parent_widget.locations_layout = QVBoxLayout(main_container_widget)
    parent_widget.locations_layout.setContentsMargins(10, 10, 10, 10)
    parent_widget.locations_layout.setSpacing(0)
    parent_widget.locations_layout.addStretch()
    scroll_area.setWidget(main_container_widget)
    return scroll_area

def create_overlay_settings_panel_layout(parent_widget):
    settings_panel_widget = QFrame()
    settings_panel_widget.setObjectName("settingsPanel")
    settings_layout = QVBoxLayout(settings_panel_widget)
    settings_layout.setSpacing(10)

    content_groupbox = QGroupBox("Informações Exibidas")
    content_layout = QVBoxLayout()
    parent_widget.overlay_show_bosses = QCheckBox("Mostrar Contador de Chefes")
    parent_widget.overlay_show_bosses.setChecked(True)
    content_layout.addWidget(parent_widget.overlay_show_bosses)
    parent_widget.overlay_show_deaths = QCheckBox("Mostrar Contador de Mortes")
    content_layout.addWidget(parent_widget.overlay_show_deaths)
    parent_widget.overlay_show_time = QCheckBox("Mostrar Tempo de Jogo")
    content_layout.addWidget(parent_widget.overlay_show_time)
    parent_widget.overlay_show_seconds = QCheckBox("Mostrar Segundos no Tempo")
    parent_widget.overlay_show_seconds.setStyleSheet("margin-left: 20px;")
    content_layout.addWidget(parent_widget.overlay_show_seconds)

    parent_widget.overlay_show_last_boss = QCheckBox("Mostrar Último Chefe Morto")
    parent_widget.overlay_show_last_boss.setToolTip("Exibe o nome e horário do último chefe derrotado.")
    content_layout.addWidget(parent_widget.overlay_show_last_boss)
    content_groupbox.setLayout(content_layout)
    settings_layout.addWidget(content_groupbox)

    appearance_groupbox = QGroupBox("Aparência")
    appearance_layout = QVBoxLayout(appearance_groupbox)
    text_color_layout = QHBoxLayout()
    text_color_layout.addWidget(QLabel("Cor do Texto:"))
    parent_widget.overlay_text_color_button = QPushButton("lightblue")
    parent_widget.overlay_text_color_button.setToolTip("Clique para escolher a cor do texto")
    text_color_layout.addWidget(parent_widget.overlay_text_color_button)
    appearance_layout.addLayout(text_color_layout)

    font_size_layout = QHBoxLayout()
    font_size_layout.addWidget(QLabel("Tamanho da Fonte:"))
    parent_widget.overlay_font_size_combobox = QComboBox()
    for size in range(10, 31, 2):
        parent_widget.overlay_font_size_combobox.addItem(f"{size}pt")
    font_size_layout.addWidget(parent_widget.overlay_font_size_combobox)
    appearance_layout.addLayout(font_size_layout)

    settings_layout.addWidget(appearance_groupbox)
    
    return settings_panel_widget

def create_obs_panel_layout(parent_widget):
    # Create main container frame
    obs_settings_panel = QFrame()
    obs_settings_panel.setObjectName("settingsPanel")
    main_layout = QVBoxLayout(obs_settings_panel)
    main_layout.setContentsMargins(0, 0, 0, 0)
    
    # Create scroll area for the content
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    scroll_area.setMaximumHeight(400)  # Limit height to prevent app stretching
    scroll_area.setObjectName("obsScrollArea")
    
    # Create content widget for the scroll area
    content_widget = QWidget()
    layout = QVBoxLayout(content_widget)
    layout.setSpacing(10)

    top_layout = QHBoxLayout()
    top_layout.addWidget(QLabel("<b>Habilitar Saída de Arquivos OBS</b>"))
    top_layout.addStretch()
    parent_widget.obs_enable_toggle = ToggleSwitch()
    top_layout.addWidget(parent_widget.obs_enable_toggle)
    layout.addLayout(top_layout)

    instructions_layout = QHBoxLayout()
    parent_widget.obs_instructions_button = QPushButton(" Mostrar Instruções de Configuração")
    parent_widget.obs_instructions_button.setIcon(QIcon(get_resource_path("assets/icons/info-circle-solid.svg")))
    parent_widget.obs_instructions_button.setObjectName("infoButton")
    instructions_layout.addWidget(parent_widget.obs_instructions_button)
    instructions_layout.addStretch()
    layout.addLayout(instructions_layout)

    separator = QFrame()
    separator.setFrameShape(QFrame.Shape.HLine)
    separator.setFrameShadow(QFrame.Shadow.Sunken)
    separator.setObjectName("separatorLine")
    layout.addWidget(separator)
    layout.addSpacing(5)
    
    layout.addWidget(QLabel("Pasta de Saída:"))
    parent_widget.obs_folder_path_label = QLabel("Não definida.")
    parent_widget.obs_folder_path_label.setObjectName("filePathLabel")
    layout.addWidget(parent_widget.obs_folder_path_label)
    parent_widget.obs_browse_button = QPushButton("Definir Pasta de Saída")
    parent_widget.obs_browse_button.setObjectName("obsBrowseButton") # Add object name
    layout.addWidget(parent_widget.obs_browse_button)

    files_groupbox = QGroupBox("Configurar Arquivos de Saída")
    files_groupbox.setObjectName("files_groupbox")
    files_layout = QVBoxLayout(files_groupbox)
    files_layout.setSpacing(15)

    boss_layout = QVBoxLayout()
    parent_widget.obs_bosses_enabled = QCheckBox("Habilitar bosses.txt")
    parent_widget.obs_bosses_enabled.setChecked(True)
    boss_layout.addWidget(parent_widget.obs_bosses_enabled)
    parent_widget.obs_bosses_format = QLineEdit("Chefes: {defeated}/{total}")
    boss_layout.addWidget(parent_widget.obs_bosses_format)
    files_layout.addLayout(boss_layout)

    death_layout = QVBoxLayout()
    parent_widget.obs_deaths_enabled = QCheckBox("Habilitar deaths.txt")
    parent_widget.obs_deaths_enabled.setChecked(True)
    death_layout.addWidget(parent_widget.obs_deaths_enabled)
    parent_widget.obs_deaths_format = QLineEdit("Mortes: {deaths}")
    death_layout.addWidget(parent_widget.obs_deaths_format)
    files_layout.addLayout(death_layout)

    death_management_groupbox = QGroupBox("Gerenciamento do Contador de Mortes OBS")
    death_management_layout = QVBoxLayout(death_management_groupbox)

    parent_widget.obs_reset_deaths_button = QPushButton("Zerar Contador de Mortes OBS")
    parent_widget.obs_reset_deaths_button.setToolTip("Define o contador de mortes do OBS como 0 via offset. A contagem real de mortes não é afetada.")
    death_management_layout.addWidget(parent_widget.obs_reset_deaths_button)

    parent_widget.obs_undo_reset_button = QPushButton("Desfazer Reset")
    parent_widget.obs_undo_reset_button.setToolTip("Remove o offset do contador de mortes.")
    parent_widget.obs_undo_reset_button.setEnabled(False)
    death_management_layout.addWidget(parent_widget.obs_undo_reset_button)
    
    files_layout.addWidget(death_management_groupbox)

    time_layout = QVBoxLayout()
    parent_widget.obs_time_enabled = QCheckBox("Habilitar time.txt")
    parent_widget.obs_time_enabled.setChecked(True)
    time_layout.addWidget(parent_widget.obs_time_enabled)
    parent_widget.obs_time_format = QLineEdit("Tempo: {time}")
    time_layout.addWidget(parent_widget.obs_time_format)
    files_layout.addLayout(time_layout)

    last_boss_layout = QVBoxLayout()
    parent_widget.obs_last_boss_enabled = QCheckBox("Habilitar last_boss.txt")
    parent_widget.obs_last_boss_enabled.setChecked(True)
    last_boss_layout.addWidget(parent_widget.obs_last_boss_enabled)
    parent_widget.obs_last_boss_format = QLineEdit("Última Morte: {boss_name} ({kill_time})")
    last_boss_layout.addWidget(parent_widget.obs_last_boss_format)
    files_layout.addLayout(last_boss_layout)
    
    files_groupbox.setLayout(files_layout)
    layout.addWidget(files_groupbox)
    
    # --- Add Apply Button ---
    layout.addSpacing(5)
    parent_widget.obs_apply_button = QPushButton("Aplicar Alterações")
    parent_widget.obs_apply_button.setObjectName("applyButton") # Optional for styling
    layout.addWidget(parent_widget.obs_apply_button)
    
    # Set the content widget to the scroll area and add scroll area to main layout
    scroll_area.setWidget(content_widget)
    main_layout.addWidget(scroll_area)
    
    return obs_settings_panel