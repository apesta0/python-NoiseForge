# NoiseForge

Procedural grayscale noise generation toolkit written entirely in pure Python.

NoiseForge is a lightweight procedural texture and noise generation system focused on deterministic output, portability, and minimal dependencies.


# Overview

NoiseForge generates procedural grayscale noise images using deterministic mathematical noise functions.

The application allows users to:

- Generate seeded noise
- Create repeatable/tileable patterns
- Export directly to PNG
- Control image dimensions
- Control grayscale intensity ranges
- Produce reproducible outputs from identical seeds

The entire project is built using only Python standard library modules.

No external dependencies are required.

---

# Philosophy

NoiseForge was designed around several core principles:

## Minimal Dependencies

The project avoids third-party libraries entirely.

This means:

- No NumPy
- No Pillow
- No OpenCV
- No external PNG libraries

Only Python standard library modules are used.

---

## Deterministic Generation

The same seed always produces the same output.

This is useful for:

- procedural terrain
- texture generation
- reproducible experiments
- game development
- seeded simulations

---

## Portability

NoiseForge runs on nearly any Python installation without setup complexity.

No pip installation is required.

---

## Educational Design

The codebase intentionally exposes the internal structure of:

- PNG encoding
- procedural noise generation
- deterministic hashing
- grayscale image construction

The goal is to remain understandable and hackable.

---

# Features

## Seed-Based Noise Generation

Every image is generated from a user-provided seed value.

Example:

```text
Seed: 1234
```

Using the same seed repeatedly will always produce the same image.

---

## Repeatable / Tileable Patterns

NoiseForge supports repeatable noise generation.

When enabled:

- image edges wrap seamlessly
- patterns tile correctly
- textures can repeat infinitely

Useful for:

- game textures
- procedural materials
- scrolling backgrounds
- terrain systems

---

## Adjustable Resolution

Users can control:

- image width
- image height

Example:

```text
Width: 1024
Height: 1024
```

---

## Grayscale Range Control

Users may control:

- lowest point (white)
- highest point (black)

This allows:

- softer textures
- higher contrast
- washed-out noise
- harsh static effects

---

## PNG Exporting

NoiseForge manually encodes PNG files without external libraries.

The exporter handles:

- PNG signatures
- chunk creation
- CRC validation
- zlib compression
- grayscale formatting

All PNG files produced are standards-compliant.

---

# Project Structure

```text
noiseforge/
│
├── CODE_OF_CONDUCT.md
├── README.md
├── SECURITY.md
│
├── noiseforge/
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── generator.py
│   ├── pngwriter.py
│   ├── preview.py
│   └── ui.py
│
└── run.sh
```

---

# Technical Details

## Noise Algorithm

NoiseForge currently uses deterministic hash-based pseudo-noise.

Advantages:

- extremely lightweight
- deterministic
- fast
- dependency-free

This is not Perlin noise.

Future versions may support:

- Perlin noise
- Simplex noise
- cellular noise
- fractal Brownian motion

---

## Grayscale Format

NoiseForge exports 8-bit grayscale PNG images.

Value mapping:

```text
0   = White
255 = Black
```

This is intentionally inverted from standard grayscale representation.

---

## PNG Construction

PNG files are manually assembled using:

- struct
- zlib

The exporter builds:

- IHDR chunks
- IDAT chunks
- IEND chunks

without relying on external imaging libraries.

---

# Requirements

## Python

Recommended:

```text
Python 3.10+
```

Minimum likely supported:

```text
Python 3.7+
```

---

# Dependencies

None.

NoiseForge only uses Python standard library modules.

---

# Standard Library Modules Used

```text
tkinter
struct
zlib
```

---

# Running NoiseForge

```bash
python -m noiseforge
```

or

```bash
./run.sh
```

---

# Using NoiseForge

## Step 1

Enter a seed value.

Example:

```text
1234
```

---

## Step 2

Select image dimensions.

Example:

```text
Width: 512
Height: 512
```

---

## Step 3

Adjust grayscale range.

Example:

```text
Lowest Point: 0
Highest Point: 255
```

---

## Step 4

Enable or disable repeatable patterns.

Enabled:
- tileable textures

Disabled:
- fully unique noise

---

## Step 5

Click:

```text
Generate PNG
```

Choose export location.

Done.

---

# Future Plans

Planned features include:

- colored gradients
- Perlin noise
- Simplex noise
- animation export
- GIF export
- shader pipelines
- node systems
- GPU acceleration
- texture layering
- procedural terrain generation
- CLI mode
- plugin system

---

# Alpha Notice

This project is currently in:

```text
Alpha 0.0.2
```

Current limitations:

- minimal UI
- grayscale only
- limited export settings

Breaking changes are expected between versions.

---

# License

MIT License

Copyright (c) 2026 Spakerdev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software.

---

# Author

Spakerdev

---

# NoiseForge

Procedural generation through pure Python.
