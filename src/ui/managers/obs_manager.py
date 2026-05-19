# src/obs_manager.py

import os
from PySide6.QtWidgets import QFileDialog, QMessageBox, QGroupBox, QPushButton
from PySide6.QtCore import QSettings, Qt
from ...utils import format_seconds_to_hms

class ObsManager:
    def __init__(self, main_app_ref, obs_panel_ref, settings_button_ref,
                 enable_toggle_ref, folder_label_ref,
                 instructions_button_ref, bosses_enabled_ref, bosses_format_ref,
                 deaths_enabled_ref, deaths_format_ref, time_enabled_ref, time_format_ref,
                 last_boss_enabled_ref, last_boss_format_ref,
                 obs_reset_deaths_button_ref, obs_undo_reset_button_ref,
                 character_slot_combobox_ref):
       
        
        self.app = main_app_ref
        self.panel = obs_panel_ref
        
        # UI References
        self.settings_button = settings_button_ref
        self.enable_toggle = enable_toggle_ref
        self.folder_label = folder_label_ref
        # Find the browse button within the panel, making this class self-contained
        self.browse_button = self.panel.findChild(QPushButton, "obsBrowseButton")
        self.instructions_button = instructions_button_ref
        self.bosses_enabled = bosses_enabled_ref
        self.bosses_format = bosses_format_ref
        self.deaths_enabled = deaths_enabled_ref
        self.deaths_format = deaths_format_ref
        self.time_enabled = time_enabled_ref
        self.time_format = time_format_ref
        self.last_boss_enabled = last_boss_enabled_ref
        self.last_boss_format = last_boss_format_ref
        self.obs_reset_deaths_button = obs_reset_deaths_button_ref
        self.obs_undo_reset_button = obs_undo_reset_button_ref
        self.character_combobox = character_slot_combobox_ref
        self.apply_button = self.panel.findChild(QPushButton, "applyButton")

        # UI Grouping for enabling/disabling
        self.child_widgets = [
            self.folder_label, self.browse_button,
            self.bosses_enabled, self.bosses_format, self.deaths_enabled,
            self.deaths_format, self.time_enabled, self.time_format,
            self.last_boss_enabled, self.last_boss_format,
            self.panel.findChild(QGroupBox, "files_groupbox")
        ]

        self.settings = QSettings("TheTarnishedChronicle", "App")
        self.death_offset = 0 # This will hold the offset for the CURRENT character
        self._load_settings()
        self.connect_signals()
        self.handle_state_change() # Apply initial enabled/disabled state
        self.on_character_changed() # Load initial offset and set button state

    def connect_signals(self):
        """Connect all UI signals to their respective handlers."""
        self.enable_toggle.toggled.connect(self.handle_state_change)
        if self.browse_button:
            self.browse_button.clicked.connect(self.set_folder_path)
        self.instructions_button.clicked.connect(self.show_instructions)
        
        # Connect all settings changes to the save method
        self.enable_toggle.toggled.connect(self._save_settings)
        self.bosses_enabled.stateChanged.connect(self._save_settings)
        self.deaths_enabled.stateChanged.connect(self._save_settings)
        self.time_enabled.stateChanged.connect(self._save_settings)
        # Connect checkboxes to save settings immediately
        self.bosses_enabled.stateChanged.connect(self._save_settings)
        self.deaths_enabled.stateChanged.connect(self._save_settings)
        self.time_enabled.stateChanged.connect(self._save_settings)
        self.last_boss_enabled.stateChanged.connect(self._save_settings)

        # Connect format edits and the new apply button to the new handler
        if self.apply_button:
            self.apply_button.clicked.connect(self.apply_and_save_formats)
        self.bosses_format.editingFinished.connect(self.apply_and_save_formats)
        self.deaths_format.editingFinished.connect(self.apply_and_save_formats)
        self.time_format.editingFinished.connect(self.apply_and_save_formats)
        self.last_boss_format.editingFinished.connect(self.apply_and_save_formats)
        
        self.obs_reset_deaths_button.clicked.connect(self.reset_obs_deaths)
        self.obs_undo_reset_button.clicked.connect(self.undo_obs_deaths_reset)

    def _load_settings(self):
        """Load all OBS settings from QSettings and apply them to the UI."""
        self.enable_toggle.setChecked(self.settings.value("obs/enabled", False, type=bool))
        self.folder_label.setText(self.settings.value("obs/folder", "Não definida."))

        self.bosses_enabled.setChecked(self.settings.value("obs/bossesEnabled", True, type=bool))
        self.bosses_format.setText(self.settings.value("obs/bossesFormat", "Chefes: {defeated}/{total}"))

        self.deaths_enabled.setChecked(self.settings.value("obs/deathsEnabled", True, type=bool))
        self.deaths_format.setText(self.settings.value("obs/deathsFormat", "Mortes: {deaths}"))

        self.time_enabled.setChecked(self.settings.value("obs/timeEnabled", True, type=bool))
        self.time_format.setText(self.settings.value("obs/timeFormat", "Tempo: {time}"))

        self.last_boss_enabled.setChecked(self.settings.value("obs/lastBossEnabled", True, type=bool))
        self.last_boss_format.setText(self.settings.value("obs/lastBossFormat", "Última Morte: {boss_name} ({kill_time})"))

        # Note: Character-specific death offset is loaded in on_character_changed, not here.

    def _save_settings(self):
        """Save all current UI settings to QSettings."""
        self.settings.setValue("obs/enabled", self.enable_toggle.isChecked())
        self.settings.setValue("obs/folder", self.folder_label.text())

        self.settings.setValue("obs/bossesEnabled", self.bosses_enabled.isChecked())
        self.settings.setValue("obs/bossesFormat", self.bosses_format.text())

        self.settings.setValue("obs/deathsEnabled", self.deaths_enabled.isChecked())
        self.settings.setValue("obs/deathsFormat", self.deaths_format.text())

        self.settings.setValue("obs/timeEnabled", self.time_enabled.isChecked())
        self.settings.setValue("obs/timeFormat", self.time_format.text())

        self.settings.setValue("obs/lastBossEnabled", self.last_boss_enabled.isChecked())
        self.settings.setValue("obs/lastBossFormat", self.last_boss_format.text())

        # Note: Character-specific death offset is saved in its own methods.

    def apply_and_save_formats(self):
        """Saves the format strings and immediately refreshes the OBS files."""
        print("Applying and saving OBS format changes...")
        self._save_settings()
        self.app.app_logic.force_stats_update_for_obs()

    def handle_state_change(self):
        """Enable or disable child widgets based on the main toggle."""
        is_enabled = self.enable_toggle.isChecked()
        for widget in self.child_widgets:
            if widget: # Check if widget exists
                widget.setEnabled(is_enabled)
    

    def set_folder_path(self):
        """Open a dialog to select an output folder."""
        current_path = self.folder_label.text()
        start_dir = current_path if os.path.isdir(current_path) else ""
        folder = QFileDialog.getExistingDirectory(self.app, "Selecionar Pasta de Saída", start_dir)
        if folder:
            self.folder_label.setText(folder)
            self._save_settings() # Save immediately after selection
            self.app.app_logic.force_stats_update_for_obs()
    
    def show_instructions(self):
        """Zobrazí detailní a přehledné instrukce pro nastavení OBS."""
        msg_box = QMessageBox(self.app)
        msg_box.setWindowTitle("Instruções de Saída de Arquivos OBS")
        msg_box.setIcon(QMessageBox.Icon.Information)

        # Použijeme HTML pro bohaté formátování
        title_app = "<h3>Passo 1: Configurar na Crônica do Manchado</h3>"
        steps_app = """
        <ol>
            <li><b>Ativar o Recurso:</b> Clique no botão principal no topo deste painel para ativar a escrita de arquivos.</li>
            <li>
                <b>Definir a Pasta de Saída:</b> Clique em 'Definir Pasta de Saída' e escolha uma pasta dedicada no seu computador (ex.: uma pasta 'TTC-OBS' na Área de Trabalho).
                <br><em>É aqui que todos os arquivos de texto serão salvos.</em>
            </li>
            <li>
                <b>Configurar Arquivos:</b> Para cada estatística (Chefes, Mortes, Tempo), você pode:
                <ul>
                    <li>Marcar a caixa 'Habilitar' para criar/atualizar o arquivo (ex.: <code>bosses.txt</code>).</li>
                    <li>Personalizar o formato do texto usando marcadores:
                        <ul>
                            <li><code>{defeated}</code> - Número de chefes derrotados.</li>
                            <li><code>{total}</code> - Total de chefes.</li>
                            <li><code>{deaths}</code> - Contagem de mortes atual.</li>
                            <li><code>{time}</code> - Tempo total de jogo (HH:MM:SS).</li>
                            <li><code>{boss_name}</code> - Nome do último chefe morto.</li>
                            <li><code>{kill_time}</code> - Tempo de jogo quando o último chefe foi morto.</li>
                        </ul>
                    </li>
                </ul>
            </li>
        </ol>
        <p>O aplicativo irá manter esses arquivos atualizados automaticamente.</p>
        """

        title_obs = "<h3>Passo 2: Adicionar Fontes no OBS</h3>"
        steps_obs = """
        <ol>
            <li>
                <b>Adicionar uma Fonte de Texto:</b> Na sua cena do OBS, clique no '+' em 'Fontes' e adicione uma nova fonte <b>Texto (GDI+)</b>. Dê um nome como "Contador de Chefes".
            </li>
            <li>
                <b>Vincular o Arquivo:</b> Nas propriedades da nova fonte de texto, marque a caixa <b>'Ler do arquivo'</b>.
            </li>
            <li>
                <b>Localizar o Arquivo:</b> Clique em 'Procurar' e navegue até a pasta de saída que você selecionou. Escolha o arquivo correspondente (ex.: <code>bosses.txt</code>).
            </li>
            <li>
                <b>Estilizar no OBS:</b> Agora você pode personalizar a fonte, cor e tamanho diretamente no OBS para combinar com o layout da sua stream.
            </li>
            <li>
                <b>Repetir:</b> Para exibir outras estatísticas, repita esses passos. Adicione uma nova fonte 'Texto (GDI+)' para <code>deaths.txt</code>, outra para <code>time.txt</code>, etc.
            </li>
        </ol>
        """
        
        msg_box.setTextFormat(Qt.RichText)
        msg_box.setText(title_app + steps_app + title_obs + steps_obs)
        msg_box.addButton(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def _get_current_character_key(self):
        """Gets the QSettings key for the current character, or None if not selected."""
        if self.character_combobox.currentIndex() > 0:
            char_data = self.character_combobox.currentData()
            if char_data and 'character_name' in char_data:
                # Sanitize character name to be a valid settings key
                return f"char_offsets/{char_data['character_name'].replace(' ', '_')}"
        return None

    def on_character_changed(self):
        """Loads the death offset for the newly selected character and updates UI."""
        char_key = self._get_current_character_key()
        if char_key:
            # Load the offset for this character, defaulting to 0
            self.death_offset = self.settings.value(f"{char_key}/deathOffset", 0, type=int)
            print(f"Loaded death offset {self.death_offset} for {char_key}")
        else:
            # No character selected, reset to 0
            self.death_offset = 0

        # Update the 'Undo' button state based on whether there's an active offset
        self.obs_undo_reset_button.setEnabled(self.death_offset != 0)
        # Force an update of the OBS files with the new offset
        self.app.app_logic.force_stats_update_for_obs()


    def reset_obs_deaths(self):
        """Resets the OBS death counter to zero by calculating and saving an offset for the current character."""
        char_key = self._get_current_character_key()
        if not char_key:
            QMessageBox.warning(self.app, "Aviso", "Por favor, selecione um personagem antes de zerar as mortes.")
            return

        current_deaths = self.app.last_known_stats.get("stats", {}).get("deaths", 0)
        self.death_offset = -current_deaths
        
        # Save the new offset to settings for the specific character
        self.settings.setValue(f"{char_key}/deathOffset", self.death_offset)
        
        self.obs_undo_reset_button.setEnabled(True)
        self.update_obs_files(self.app.last_known_stats) # Force update
        print(f"Saved death offset {self.death_offset} for {char_key}")


    def undo_obs_deaths_reset(self):
        """Removes the death counter offset for the current character."""
        char_key = self._get_current_character_key()
        if not char_key:
            return # Should not happen if button is disabled, but good practice

        self.death_offset = 0
        # Remove the specific setting for this character
        self.settings.remove(f"{char_key}/deathOffset")

        self.obs_undo_reset_button.setEnabled(False)
        self.update_obs_files(self.app.last_known_stats) # Force update
        print(f"Removed death offset for {char_key}")

    def update_obs_files(self, data: dict):
        """Zapíše data do všech povolených souborů."""
        if not self.enable_toggle.isChecked(): return
        folder = self.folder_label.text()
        if not folder or folder == "Not set.": return

        stats = data.get("stats", {})
        last_kill = data.get("last_kill")

        # Formátování času
        s = stats.get('seconds_played', -1)
        time_str = format_seconds_to_hms(s) if s >= 0 else "--:--:--"
        
        # Zápis do bosses.txt
        if self.bosses_enabled.isChecked():
            path = os.path.join(folder, "bosses.txt")
            text = self.bosses_format.text().format(defeated=stats.get('defeated', '--'), total=stats.get('total', '--'))
            self._write_file(path, text)

        # Zápis do deaths.txt
        if self.deaths_enabled.isChecked():
            path = os.path.join(folder, "deaths.txt")
            obs_deaths = stats.get('deaths', 0) + self.death_offset
            text = self.deaths_format.text().format(deaths=obs_deaths)
            self._write_file(path, text)
            
        # Zápis do time.txt
        if self.time_enabled.isChecked():
            path = os.path.join(folder, "time.txt")
            text = self.time_format.text().format(time=time_str)
            self._write_file(path, text)

        # Zápis do last_boss.txt
        if self.last_boss_enabled.isChecked():
            path = os.path.join(folder, "last_boss.txt")
            if last_kill:
                kill_time_str = format_seconds_to_hms(last_kill.get("time", 0))
                text = self.last_boss_format.text().format(
                    boss_name=last_kill.get("name", "N/A"),
                    kill_time=kill_time_str
                )
            else:
                text = "" # Clear the file if no boss has been killed
            self._write_file(path, text)

    def _write_file(self, path, content):
        """Pomocná metoda pro bezpečný zápis do souboru."""
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        except IOError as e:
            print(f"Error writing to OBS file '{path}': {e}")