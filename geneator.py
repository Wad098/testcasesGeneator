from jinja2 import Environment, FileSystemLoader

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader('./'))

# Load the template
template = env.get_template('test_case_template.j2')

# Test case data
test_cases = [
    {
        "case_id": "case_001",
        "test_name": "api_endpoint_case_001",
        "description": "接口测试用例 001",
        "hex_string": "7AE5-3CEF-E06F-FC7A",
        "expected_result": "expected_result_001"
    },
    {
        "case_id": "case_002",
        "test_name": "api_endpoint_case_002",
        "description": "接口测试用例 002",
        "hex_string": "8B12-4DFA-C09E-ABCD",
        "expected_result": "expected_result_002"
    }
]

# Render the template with all test cases
output = template.render(test_cases=test_cases)

# Write all test cases to a single file
with open("test_api.py", "w", encoding="utf-8") as f:
    f.write(output)