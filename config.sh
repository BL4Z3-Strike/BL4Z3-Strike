#!/bin/bash

SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"
BIN_DIR="$HOME/bin"

if [ ! -d "$BIN_DIR" ]; then
  echo "Creating $BIN_DIR directory..."
  mkdir "$BIN_DIR"
fi

echo "Copying Python scripts and other files to $BIN_DIR..."
cp "$SCRIPT_DIR/bl4z3" "$BIN_DIR/"
cp "$SCRIPT_DIR/AnyDesk_RCE_exploit.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/hash_cracker.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/script.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/Bash_Shell.sh" "$BIN_DIR/"
cp "$SCRIPT_DIR/listener.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/ssh_bruteforce_with_proxy.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/mac_changer.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/sudo_exploit.sh" "$BIN_DIR/"
cp "$SCRIPT_DIR/config.sh" "$BIN_DIR/"
cp "$SCRIPT_DIR/malicious_example.pdf" "$BIN_DIR/"
cp "$SCRIPT_DIR/torservice.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/directory_trevarsal.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/network_sniffer.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/unreal_engine_remote_exploit.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/directory_trevarsal.sh" "$BIN_DIR/"
cp "$SCRIPT_DIR/port_scanner.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/vulnerability_scanner.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/discord_nuke_bot.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/ftp_bruteforce_with_proxy.py" "$BIN_DIR/"
cp "$SCRIPT_DIR/script.ps1" "$BIN_DIR/"

chmod +x "$BIN_DIR/bl4z3"
chmod +x "$BIN_DIR/Bash_Shell.sh"
chmod +x "$BIN_DIR/sudo_exploit.sh"
chmod +x "$BIN_DIR/directory_trevarsal.sh"

SHELL_RC="$HOME/.bashrc"
if [ -n "$ZSH_VERSION" ]; then
  SHELL_RC="$HOME/.zshrc"
fi

if ! grep -q "$BIN_DIR" "$SHELL_RC"; then
  echo "Updating PATH in $SHELL_RC..."
  echo "export PATH=\"$BIN_DIR:\$PATH\"" >> "$SHELL_RC"
fi

echo "Reloading shell configuration..."
source "$SHELL_RC"

echo "Installation complete. You can now run your scripts from anywhere."
