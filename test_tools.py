import json
import sys
import os
from freshservice_mcp.server import mcp

# Set env vars
os.environ['FRESHSERVICE_DOMAIN'] = 'helpdesk.sanahealthgroup.com'
os.environ['FRESHSERVICE_APIKEY'] = 'LBREgyjQ5twU5TQGviF8'

# List all tools
tools = mcp.list_tools()
project_tools = [t for t in tools if 'project' in t.name.lower()]

print(f"Found {len(project_tools)} project management tools:")
for tool in project_tools:
    print(f"  - {tool.name}: {tool.description}")
