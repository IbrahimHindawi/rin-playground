# rin-playground

Small rin language playground project.

## Dependencies

- Python 3
- CMake
- Ninja
- LLVM/Clang with `clang-cl`
- `rin.exe` on `PATH`, usually from `C:\devel\rin-windows-x64`
- `std` beside `rin.exe`, copied by the rin compiler build to `C:\devel\rin-windows-x64\std`

## Build And Run

```powershell
python bunyan.py run debug
```

Bunyan runs:

```text
rin.exe compile src/main.rin -> build/rin_gen/main.c + build/rin_gen/main.h
cmake config/build
build/rin-playground.exe
```

The project imports the standard library through:

```i
import "std/print.rin"
```

`rin.exe` resolves that through the `std` folder beside the compiler executable. Use Bunyan `i_import_dirs` only for project-local libraries.

Other configs:

```powershell
python bunyan.py build release
python bunyan.py build reldebug
python bunyan.py clean
```
