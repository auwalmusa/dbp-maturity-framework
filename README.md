# DBP Maturity Framework

## Mind the Specification Gap: A Data Architecture Maturity Framework for Digital Battery Passport Implementation Under EU Regulation 2023/1542

This repository contains the technical artefacts associated with the research paper by **Auwal Musa (Batteric Ltd)**. It provides a standardised approach to assessing organisational readiness for the 2027 EU Digital Battery Passport (DBP) mandate.

### Overview

EU Regulation 2023/1542 introduces complex data requirements that current "static" digital systems cannot support. This project provides:
1.  **Maturity Scoring Logic:** A Python-based diagnostic tool to assess DBP readiness.
2.  **Reference Data Schema:** A JSON-LD structure designed for decentralised data exchange (EDC) and interoperability.

### 📁 Project Structure

*   `maturity_scoring.py`: The core algorithm for calculating maturity levels (0-4) across Technical, Semantic, and Governance dimensions.
*   `dbp_reference_schema.json`: A machine-readable schema for battery data attributes mandated by Annex XIII.

### 🛠️ Getting Started

#### Maturity Assessment
To run a maturity assessment for your organisation, execute the Python script:

```bash
python maturity_scoring.py
```

#### Data Implementation
Use the `dbp_reference_schema.json` as a blueprint for your data architecture. It is designed to be compatible with decentralised identifiers (DIDs) and the Catena-X data space.

### 📄 Documentation
For the full theoretical background and methodology, please refer to the associated paper: 
**"Mind the Specification Gap" by Auwal Musa.**

### 🤝 Contributing
Contributions that extend the semantic ontologies or scoring criteria are welcome. Please open an issue or submit a pull request.

---
**Maintained by:** Auwal Musa, [Batteric Ltd](https://batteric.com)
**Contact:** auwal@batteric.com


