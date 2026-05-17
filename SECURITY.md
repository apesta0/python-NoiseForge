# Security Policy

## NoiseForge

Version:

```text
Alpha 0.0.2
```

Author:

```text
Spakerdev
```

License:

```text
MIT License
```

---

# Overview

NoiseForge is a local-only procedural noise generation toolkit written entirely in pure Python.

The project currently:

- does not use networking
- does not collect telemetry
- does not transmit user data
- does not require internet access
- does not use external APIs
- does not execute remote code

All generation and exporting occurs locally on the user's machine.

---

# Supported Versions

Because NoiseForge is currently in alpha development, only the latest version is officially supported.

| Version | Supported |
|---|---|
| Alpha 0.0.2 | Yes |
| Alpha 0.0.1 | Yes |

Older versions may contain unresolved bugs or vulnerabilities.

---

# Reporting a Vulnerability

If you discover a security issue, vulnerability, or unintended behavior, please report it responsibly.

Recommended report contents:

- vulnerability description
- reproduction steps
- affected version
- operating system
- screenshots or logs if applicable
- suggested mitigation if known

---

# What To Report

Please report issues involving:

- arbitrary file access
- unsafe file writing
- memory exhaustion
- application crashes
- malformed PNG generation
- denial-of-service vectors
- code execution vulnerabilities
- malicious input handling
- GUI injection vulnerabilities

---

# What Not To Report

The following are generally not considered security vulnerabilities in the current alpha versions:

- crashes caused by absurd image dimensions
- freezing caused by extremely large exports
- malformed user input causing exceptions
- visual artifacts in generated noise
- invalid manual modifications to source code

These may still be reported as bugs.

---

# Security Design

NoiseForge was intentionally designed with a minimal attack surface.

## No Networking

NoiseForge contains:

- no HTTP requests
- no sockets
- no cloud connectivity
- no telemetry systems

This significantly reduces remote attack vectors.

---

## No External Dependencies

NoiseForge uses only Python standard library modules.

Advantages:

- reduced supply-chain risk
- fewer dependency vulnerabilities
- easier auditing
- predictable runtime behavior

---

## Local File Operations Only

NoiseForge only writes files explicitly selected by the user.

The application does not:

- scan directories
- modify unrelated files
- perform automatic uploads
- access protected system resources

---

## Deterministic Generation

Noise generation is mathematical and deterministic.

No executable content is generated.

PNG outputs contain only grayscale image data.

---

# Known Security Limitations

As an alpha-stage project, NoiseForge currently has limited protection against resource exhaustion.

Examples:

- extremely large image dimensions
- excessive memory allocation
- intentionally malformed user input

Future versions may include:

- dimension limits
- safer validation
- memory guards
- export protection systems

---

# Secure Usage Recommendations

Users are encouraged to:

- avoid running unknown modified builds
- verify source code before execution
- avoid exporting absurdly large images
- keep Python updated
- use trusted environments

---

# Third-Party Code

NoiseForge currently includes no third-party runtime dependencies.

If future versions introduce external libraries, they will be documented here.

---

# Disclosure Policy

Please avoid publicly disclosing vulnerabilities until a fix or mitigation is available.

Responsible disclosure helps protect users and contributors.

---

# Future Security Goals

Planned improvements include:

- stronger input validation
- export safety checks
- sandboxed generation systems
- safer GUI handling
- automated testing
- fuzz testing for PNG generation
- memory usage protection
- structured error handling

---

# Contact

Project Maintainer:

```text
Spakerdev
```

---

# Final Notes

NoiseForge is currently an experimental alpha-stage project.

Security hardening is ongoing and will improve significantly in future releases.
