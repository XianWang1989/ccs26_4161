var = next((v for v in [foo(), bar(), baz()] if v), None)
if var:
    return var
