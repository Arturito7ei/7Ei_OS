# Glossary

Complete decoder ring for 7Ei shorthand, acronyms, and internal language.

## Acronyms

| Term | Meaning | Context |
|------|---------|--------|
| WO | Work Order | Self-contained Claude Code instruction block |
| PRD | Product Requirements Document | PRD.md in project repos |
| TRD | Technical Requirements Document | Part of CLAUDE.md |
| RAG | Retrieval-Augmented Generation | Pinecone vector search in agent chat |
| BYOK | Bring Your Own Key | Per-org API key override |
| CI | Continuous Integration | GitHub Actions |
| TOR | Terms of Reference | Agent instruction document |
| nDSG | Swiss data protection law | Cloud provider choices |
| ADR | Architecture Decision Record | Technical decision docs |

## Internal Terms

| Term | Meaning |
|------|--------|
| Mission Control | 7Ei's main product — AI virtual office app |
| Silver Board | Virtual advisory board with persona-based advisors |
| Arturito (agent) | Chief of Staff AI agent in Mission Control |
| Dispatch | Claude Cowork's phone-first interface |
| Sprint cycle | Plan → execute → merge → deploy → test |
| Execution plan | Markdown file with work orders pushed to repo |
| Hot cache | CLAUDE.md working memory for quick lookups |
| Knowledge promotion | Pattern: session → agent → project → org → OS |

## People

| Name | Person |
|------|--------|
| Arturito | Arturito R2D2, Founder of 7Ei AG |

## Cloud Providers

| Value | Provider | Data Residency |
|-------|----------|----------------|
| aws | AWS Bedrock Frankfurt | EU/GDPR |
| aws_ch | AWS Bedrock Zurich | Swiss nDSG |
| gcp | Google Vertex AI europe-west1 | EU/GDPR |
| gcp_ch | Google Vertex AI Zurich | Swiss nDSG |
| azure | Azure OpenAI Switzerland North | Swiss nDSG |
| oracle | Oracle Cloud EU | EU/GDPR |
