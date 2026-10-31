from mcp.server.fastmcp import FastMCP
import httpx

# Initialize the server
mcp = FastMCP("CitizenAssistant")

# Define tools for the citizen persona
@mcp.tool()
def check_application_status(mobile_number: str, dob_password: str) -> str:
    """Check the status of an old age pension application."""
    # Example: Make an internal request to the existing Flask portal
    # The portal container is accessible internally via http://app:8000
    response = httpx.post(
        "http://app:8000/api/status", 
        json={"mobile": mobile_number, "password": dob_password}
    )
    return response.text

@mcp.tool()
def submit_application(mobile_number: str, age: int, address: str) -> str:
    """Submit a new pension application. Rule: Age must be >= 60."""
    if age < 60:
        return "Application rejected: Applicant must be 60 or above."
    # Add API call to Flask portal to submit data
    return "Application submitted successfully."

if __name__ == "__main__":
    # Run the server on port 8001 using SSE transport bound to 0.0.0.0
    mcp.run(transport='sse')