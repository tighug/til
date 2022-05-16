# Starship

## Installation

### macOS

1. バイナリをインストールします

```bash
brew install starship
```

2. シェルの設定ファイルにスクリプトを追記します

`~/.zshrc`に以下を追記します。

```bash
# ~/.zshrc
eval "$(starship init zsh)"
```

### Linux

1. バイナリをインストールします

```bash
curl -fsSL https://starship.rs/install.sh | bash
```

2.  シェルの設定ファイルにスクリプトを追記します

    === "Bash"

`~/.bashrc`に以下を追記します。

```bash
# ~/.bashrc
eval "$(starship init bash)"
```

## Configuration

`~/.config/starship.toml`に記述します。

```toml
# ~/.config/starship.toml

add_newline = true
prompt_order = [
    "username",
    "hostname",
    "kubernetes",
    "directory",
    "git_branch",
    "git_state",
    "git_status",
    "package",
    "dotnet",
    "golang",
    "java",
    "nodejs",
    "python",
    "ruby",
    "rust",
    "nix_shell",
    "memory_usage",
    "aws",
    "env_var",
    "cmd_duration",
    "line_break",
    "jobs",
    "battery",
    "time",
    "character",
]

[aws]
symbol = "☁️ "
style = "bold yellow"
disabled = true

[battery]
full_symbol = "•"
charging_symbol = "⇡"
discharging_symbol = "⇣"
disabled = true

[character]
symbol = "❯"
error_symbol = "❯"
use_symbol_for_status = true
vicmd_symbol = "❮"
style_success = "bold green"
style_failure = "bold red"
disabled = false

[cmd_duration]
min_time = 2
prefix = ""
style = "bold yellow"
disabled = false

[directory]
truncation_length = 0
truncate_to_repo = false
style = "bold cyan"
disabled = false

[env_var]

[git_status]


[line_break]
disabled = false

[memory_usage]
show_percentage = true
show_swap = false
threshold = 75
icon = " "
style = "bold dimmed red"
disabled = true

[nodejs]
symbol = "⬢ "
style = "green"
disabled = true

[package]
symbol = "📦 "
style = "red"
disabled = true
```

## References

- [Starship](https://starship.rs/)
