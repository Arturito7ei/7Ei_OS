# Data Residency

> Where data lives and which laws apply.

## 7Ei AG — Swiss Company

7Ei AG is incorporated in Switzerland. Swiss Federal Data Protection Act (nDSG/FADP) applies as the baseline.

## Deployment Options

| Option | Data location | Law | Use case |
|--------|--------------|-----|----------|
| `aws_ch` | AWS Zurich (eu-central-2) | Swiss nDSG | Default for Swiss clients |
| `gcp_ch` | GCP Zurich (europe-west6) | Swiss nDSG | Alternative Swiss |
| `azure` | Azure Switzerland North | Swiss nDSG | Microsoft ecosystem |
| `aws` | AWS Frankfurt (eu-central-1) | EU GDPR | EU clients |
| `gcp` | GCP Belgium (europe-west1) | EU GDPR | EU clients |
| `oracle` | Oracle EU regions | EU GDPR | Oracle ecosystem |
| `local` | Customer's own infrastructure | Customer's law | On-premise |

## Rules

1. **User chooses** data residency at org creation — never override
2. **LLM calls** route through the selected cloud provider's region
3. **Vector data** (Pinecone) must be in the same region as the primary database
4. **Backups** stay in the same jurisdiction as the primary data
5. **Cross-border transfers** require explicit user consent and legal basis

## For Agents

- Check `org.cloudProvider` before making external API calls
- Never send user data to a service outside the designated region
- Log data access for audit trail compliance
