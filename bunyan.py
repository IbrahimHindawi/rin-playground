from __future__ import annotations

from scripts.bunyan import main


if __name__ == "__main__":
    main(
        project_name="rin-playground",
        mode="rin",
        rin_entry="src/main.rin",
    )
