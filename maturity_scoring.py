"""
Maturity Scoring Logic for Digital Battery Passport (DBP) Implementation.
This script calculates the DBP maturity level based on technical, semantic, and governance dimensions.
"""

def calculate_maturity_score(capabilities):
    """
    Calculates maturity score (0-4) based on a dictionary of capabilities.
    """
    dimensions = {
        "technical": 0,
        "semantic": 0,
        "governance": 0
    }
    
    # Technical Dimension Logic
    if capabilities.get("use_dids_vcs"):
        dimensions["technical"] = 4
    elif capabilities.get("use_edc_connectors"):
        dimensions["technical"] = 3
    elif capabilities.get("standard_ids_gs1_iso"):
        dimensions["technical"] = 2
    elif capabilities.get("internal_erp_digitized"):
        dimensions["technical"] = 1
        
    # Semantic Dimension Logic
    if capabilities.get("automated_ontology_mapping"):
        dimensions["semantic"] = 4
    elif capabilities.get("cross_sector_data_models"):
        dimensions["semantic"] = 3
    elif capabilities.get("industry_standard_schemas"):
        dimensions["semantic"] = 2
    elif capabilities.get("structured_data"):
        dimensions["semantic"] = 1
        
    # Governance Dimension Logic
    if capabilities.get("verifiable_audit_trails"):
        dimensions["governance"] = 4
    elif capabilities.get("policy_based_access"):
        dimensions["governance"] = 3
    elif capabilities.get("bilateral_data_agreements"):
        dimensions["governance"] = 2
    elif capabilities.get("internal_iam"):
        dimensions["governance"] = 1

    # Overall score is the average across dimensions
    overall_score = sum(dimensions.values()) / len(dimensions)
    return round(overall_score, 2), dimensions

# Example usage (Current "Best Practice" Firm)
firm_capabilities = {
    "standard_ids_gs1_iso": True,
    "internal_erp_digitized": True,
    "industry_standard_schemas": True,
    "structured_data": True,
    "bilateral_data_agreements": True,
    "internal_iam": True,
    # Firm is missing EDC Connectors and DIDs (Level 3/4)
}

score, breakdown = calculate_maturity_score(firm_capabilities)

if __name__ == "__main__":
    print(f"--- DBP Maturity Assessment: Batteric Framework ---")
    print(f"Overall Maturity Score: {score} / 4.0")
    print(f"Breakdown: {breakdown}")
    
    if score < 3.0:
        print("
[WARNING] 'Specification Gap' Detected: Firm cannot support dynamic SoH reporting.")
    else:
        print("
[SUCCESS] Firm meets requirements for 2027 Circular Economy compliance.")
