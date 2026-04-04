# Self-Contained-Growing-Unit
## AI-Driven Closed-Loop Biosystem (Stage 1)

This repository contains the software infrastructure for an autonomous, AI-managed environmental control system. It utilizes a distributed edge-server architecture to offload heavy API processing from microcontrollers, allowing an integrated Large Language Model to make real-time resource management decisions based on biological telemetry. 

## System Architecture
* **The Edge (C++):** ESP32 code handling analog/digital sensor polling (I2C, 1-Wire) and physical actuation (5V relays for water/lighting).
* **The Server (Python):** Local Flask routing infrastructure that ingests edge telemetry, formats the data payload, and interfaces with the Anthropic API (Claude).
* **The Brain:** Prompt logic that parses raw botanical data (VPD, soil moisture, pH) to execute closed-loop control commands.

**Current Build Stage:** MVP Integration (Testing biological autonomy).
