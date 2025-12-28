# Reusable Prompts

## Create Guided Template from Reference Implementation

**Prompt:**
```
Update [TARGET_FILE] with in-line comments prompting me how to reproduce [REFERENCE_FILE]. The goal here is to guide me towards typing it out from memory by providing hints, not telling me exactly what to do.
```

**Usage Example:**
```
Update challenges/dayX_agent.py with in-line comments prompting me how to reproduce challenges/day3_agent.py. The goal here is to guide me towards typing it out from memory by providing hints, not telling me exactly what to do.
```

**What this prompt does:**
- Creates a template file with hint comments (not exact solutions)
- Uses TODO markers to indicate where code should go
- Includes contextual hints (e.g., "hint: it's a dictionary with 'role' and 'content'")
- Maintains the logical flow of the original code
- Uses questions to prompt thinking rather than giving answers
- Ensures syntax validity with `pass` statements where needed

**Guidelines for the AI:**
- Read both the reference file and target file
- Create comments that guide without revealing exact answers
- Use question-based hints (e.g., "What format does the API expect?")
- Include TODO markers for each code section
- Preserve the docstring from the reference file
- Maintain proper Python syntax with placeholder `pass` statements

