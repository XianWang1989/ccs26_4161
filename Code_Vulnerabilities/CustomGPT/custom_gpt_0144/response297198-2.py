dtype_dict = {
    11: 'bool', 12: str, 13: str, 14: str,
    17: str, 19: str, 20: str, 21: str
}

df = pd.read_csv("leads.csv", dtype=dtype_dict)
